# YouTube Downloader
A lightweight and powerful Flask-based web application to download YouTube videos and audio. This application uses yt-dlp for high-speed downloading and metadata extraction, with optional format conversion via FFmpeg.

Features:
Fetch video metadata (title, thumbnail, duration, and upload date).
Download YouTube videos in various formats (MP4, MKV, etc.).
Extract and convert audio (MP3, AAC, etc.).
Fully dockerized for easy deployment.
Simple web-based interface for seamless usage.

Requirements:
Docker installed (for containerized deployment).
Optional: FFmpeg installed within the container for format conversions.


How to Use:(DOCKER)
1. Clone the repository.
2. Build the Docker image:
   docker build -t yourusername/youtube-downloader .
3. Run the container:
   docker run -p 5000:5000 yourusername/youtube-downloader
4. Access the web application at
   http://localhost:5000.
