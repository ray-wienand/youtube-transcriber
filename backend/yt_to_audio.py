import os

# YouTube
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Create folder if not exist
os.makedirs("backend/audio", exist_ok=True)

def yt_to_audio(youtube_url):
    # pytube download video part
    yt = YouTube(youtube_url)
    # Capture the video
    audio = yt.streams.filter(only_audio=True).first() # 1st part
    safe_title = yt.title.replace(' ', '_')
    filename = f"backend/audio/{safe_title}.mp4"

    audio.download(filename=filename)
    
    return filename 