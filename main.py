import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp

load_dotenv("config.env")

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

FFMPEG_PATH = os.getenv("FFMPEG_PATH")
os.environ["PATH"] += os.pathsep + FFMPEG_PATH

YTDLP_PATH = os.getenv("YTDLP_PATH")

if not YTDLP_PATH or not os.path.exists(YTDLP_PATH):
    print("Warning: yt-dlp.exe not found! Please check your installation.")

def get_playlist_tracks(playlist_url):
    """Extract all track names from a Spotify playlist."""
    playlist_id = playlist_url.split("playlist/")[1].split("?")[0]
    tracks = []
    offset = 0

    while True:
        results = sp.playlist_tracks(playlist_id, offset=offset)
        for track in results["items"]:
            song = track["track"]
            track_name = song["name"]
            artist_name = song["artists"][0]["name"]
            tracks.append(f"{track_name} {artist_name}")

        offset += len(results["items"])
        if not results["next"]:
            break

    return tracks

def download_song(song_name):
    """Download a song from YouTube using yt-dlp."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': FFMPEG_PATH,
        'outtmpl': os.path.join(os.path.expanduser("~"), "Music", f"{song_name}.%(ext)s"),
        'quiet': True,
        'default_search': 'ytsearch5',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song_name}"])
        print(f"✅ Downloaded: {song_name}")
    except Exception as e:
        print(f"❌ Failed to download {song_name}: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the playlist: ")
    songs = get_playlist_tracks(playlist_url)
    
    for song in songs:
        print(f"🎵 Downloading: {song}")
        download_song(song)
    
    print("🎉 Download complete!")
