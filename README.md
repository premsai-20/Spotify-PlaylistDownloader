# Spotify Playlist Downloader 🎵

A Python-based music downloader that fetches songs from a Spotify playlist and downloads them from YouTube.

## Features 🚀

- **Fetch Spotify Playlists** – Extracts track details from any public or private Spotify playlist.
- **Download from YouTube** – Matches and downloads high-quality audio from YouTube.
- **Automatic File Naming** – Saves songs with proper titles and metadata.
- **Cross-Platform** – Works on Windows, macOS, and Linux.

## Installation ⚙️

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- FFmpeg (for processing audio files)

### Clone the Repository

```bash
git clone https://github.com/premsai-20/SpotifyAPI-PlaylistDownloader.git
```

### Install Dependencies

Run the following command to install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

## Set Up Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Create a new app and get your **Client ID** and **Client Secret**.
3. Add `http://localhost:8888/callback` as a redirect URI.

## Usage 📌

Run the script and enter a Spotify playlist URL:

```bash
python main.py
```

The script will process the playlist and download the tracks from YouTube.

## Contributing 🤝

Contributions are welcome! Fork the repo and submit a pull request with your improvements or bug fixes.

## Author & Contact

**Prem Sai**  
Email: [sakamurisai252@gmail.com](mailto:sakamurisai252@gmail.com)  
GitHub: [premsai-20](https://github.com/premsai-20)
