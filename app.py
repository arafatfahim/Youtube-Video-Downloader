from flask import Flask, render_template, request, jsonify, send_file
from yt_dlp import YoutubeDL
import os
import random
import time
import subprocess

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metadata', methods=['POST'])
def metadata():
    data = request.json
    url = data.get('url')

    try:
        # Use yt_dlp to fetch metadata
        ydl_opts = {'quiet': True, 'extract_flat': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            thumbnail = info.get('thumbnail', '')  # Video thumbnail URL
            duration = info.get('duration_string', '')  # Video duration
            upload_date = info.get('upload_date', '')  # Video upload date
            formatted_date = (
                f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}" if upload_date else ""
            )

            return jsonify({
                'status': 'success',
                'title': title,
                'thumbnail': thumbnail,
                'duration': duration,
                'upload_date': formatted_date
            })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/process', methods=['POST'])
def process():
    try:
        # Get user input
        url = request.json.get('url')
        output_type = request.json.get('output_type')
        file_format = request.json.get('file_format')

        if not url or not output_type or not file_format:
            return jsonify({'status': 'error', 'message': 'Invalid input'})

        # Generate unique file name
        file_base = f"yt_{random.randint(100000, 1000000)}_{int(time.time())}"
        output_file = os.path.join(DOWNLOAD_DIR, f"{file_base}.{file_format}")
        
        if output_type == 'audio':

            # Set yt_dlp options
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': file_format,
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(DOWNLOAD_DIR, f"{file_base}.%(ext)s"),
            }
        elif output_type == 'video':
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_DIR, f"{file_base}.%(ext)s"),
            }

        # Download content and extract title
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown Title')
            thumbnail = info.get('thumbnail', '')  # Video thumbnail URL
            duration = info.get('duration_string', '')  # Video duration
            upload_date = info.get('upload_date', '')  # Video upload date
            formatted_date = (
                f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}" if upload_date else ""
            )

        # Identify downloaded file
        downloaded_file = next(
            (f for f in os.listdir(DOWNLOAD_DIR) if f.startswith(file_base)),
            None
        )
        if not downloaded_file:
            return jsonify({'status': 'error', 'message': 'Download failed'})

        downloaded_path = os.path.join(DOWNLOAD_DIR, downloaded_file)
        
        print(downloaded_file)
        
        print(file_format)    
        # Convert if necessary
        if file_format not in downloaded_file:
            ffmpeg_command = [
                "ffmpeg",
                "-i", downloaded_path,
                "-c:v", "copy",
                "-c:a", "aac",
                "-strict", "experimental",
                "-y",
                output_file
            ]
            subprocess.run(ffmpeg_command, check=True)
            os.remove(downloaded_path)
        elif file_format in ["mp3", "aac"]:
            output_file = downloaded_path
            
        else:
            output_file = downloaded_path

        return jsonify({
            'status': 'success',
            'file': output_file,
            'title': title,
            'thumbnail': thumbnail,
            'duration': duration,
            'upload_date': formatted_date
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
