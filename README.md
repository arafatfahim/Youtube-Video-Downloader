# Flask YouTube Downloader

A Flask-powered web application for downloading YouTube videos and audio, with metadata extraction and optional format conversion. This project leverages `yt-dlp` for downloading and `FFmpeg` for format conversion, providing a seamless user experience for downloading YouTube content.

---

## Key Features
- **Metadata Extraction**: Fetch video details such as title, thumbnail, duration, and upload date.
- **Audio & Video Downloads**: Supports downloading videos in formats like MP4 or MKV and extracting audio in MP3 or AAC.
- **Format Conversion**: Converts downloaded media into desired formats using `FFmpeg`.
- **User-Friendly Web Interface**: Built with Flask to offer an intuitive user experience.
- **Dockerized Deployment**: Run the app easily using Docker for a hassle-free setup.

---

## Getting Started

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **FFmpeg**: Required for media conversion. [Install FFmpeg](https://ffmpeg.org/download.html) if not already available.

### Installation Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/arafatfahim/Youtube-Video-Downloader.git
   cd youtube-downloader
   ```
2. **Set up a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```
   
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   flask run
   ```

   **Access the application at http://127.0.0.1:5000.**

### Using Docker
### Steps to Deploy with Docker
1. **Build the Docker Image**
   ```bash
   docker build -t arafatfahim001/youtube-downloader .
   ```
2. **Run the Docker Container**
   ```bash
   docker run -p 5000:5000 arafatfahim001/youtube-downloader
   ```

### Project Structure
   ```bash
   youtube-downloader/
   ├── app.py             # Main Flask application
   ├── requirements.txt   # Python dependencies
   ├── Dockerfile         # Docker configuration
   ├── downloads/         # Directory for downloaded files
   └── templates/         # HTML templates for the frontend
   ```