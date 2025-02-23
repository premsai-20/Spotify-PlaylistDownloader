Spotify Playlist Downloader 🎵

A Python-based music downloader that fetches songs from a Spotify playlist and downloads them from YouTube. This project is perfect for music lovers who want an easy way to store their favorite tracks offline.

Features 🚀

Fetch Spotify Playlists – Extracts track details from any public or private Spotify playlist.

Download from YouTube – Matches and downloads high-quality audio from YouTube.

Automatic File Naming – Saves songs with proper titles and metadata.

Cross-Platform – Works on Windows, macOS, and Linux.

Installation ⚙️

Prerequisites

Make sure you have the following installed:

Python 3.7+

pip (Python package manager)

FFmpeg (for processing audio files)

Clone the Repository

git clone https://github.com/premsai-20/SpotifyAPI-PlaylistDownloader.git
cd SpotifyAPI-PlaylistDownloader

Install Dependencies

pip install -r requirements.txt

Set Up Spotify API Credentials

Go to the Spotify Developer Dashboard.

Create a new app and get your Client ID and Client Secret.

Add http://localhost:8888/callback as a redirect URI.

Create a .env file in the project directory and add:

SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback

Usage 📌

Run the script and enter a Spotify playlist URL:

python main.py

The script will fetch the playlist, find matching YouTube videos, and download them.

Notes 📝

This project uses YouTube for audio downloads, so ensure your connection is stable.

If a song isn’t found, you may need to refine the search logic.

Contributing 🤝

Contributions are welcome! Feel free to fork this repo, make improvements, and submit a pull request.

License 📜

This project is open-source under the MIT License.

Author 👨‍💻:
Prem Sai📧 
sakamurisai252@gmail.com🌍
