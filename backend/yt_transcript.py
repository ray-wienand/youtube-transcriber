import os

# YouTube
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

youtube_url = "https://www.youtube.com/watch?v=iVkoNcHNR9g&t=286s&pp=ygUHdHVibGlhbg%3D%3D"

# Create folder if not exist
os.makedirs("backend/transcriptions", exist_ok=True)

def yt_transcribe(youtube_url):

  # pytube download video part
  yt = YouTube(youtube_url)

  # Get the video id
  video_id = yt.video_id
  
  # Get the transcript
  transcript = YouTubeTranscriptApi.get_transcript(video_id)  
  print(f"Downloaded the transcription for {youtube_url}")

  # print(transcript) # This will print the transcript with the time stamps
  
  # Generate safe title for the transcription file
  safe_title = yt.title.replace(' ', '_')
  output_directory = f"backend/transcriptions/yt_{safe_title}.txt"

  # Remove timestamps and concatenate the text
  transcript_paragraph = ""
  for i in transcript:
    transcript_paragraph += " " + i["text"]
  
  print(transcript_paragraph) # This will print the transcription without timestamps in one paragraph

  # Save the transcription paragraph to a text file
  with open(output_directory, 'w', encoding='utf-8') as f:
      f.write(transcript_paragraph)

  print(f"Transcription saved to {output_directory}")


if __name__ == '__main__':
    yt_transcribe(youtube_url)
