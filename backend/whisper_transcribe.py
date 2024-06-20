import os
import whisper
from yt_to_audio import yt_to_audio  

# Create folder if not exist
os.makedirs("backend/transcriptions", exist_ok=True)

# Whisper
model = whisper.load_model("base")

# Audio URL
youtube_url = "https://www.youtube.com/watch?v=iVkoNcHNR9g&t=286s&pp=ygUHdHVibGlhbg%3D%3D"

def whisper_transcribe(youtube_url):
    
    # Use the yt_to_audio function from yt_to_audio module
    audio_file = yt_to_audio(youtube_url)
    print(f"Extracted audio from {youtube_url}")

    # Transcribe the audio file
    result = model.transcribe(audio_file)

    # Generate safe title for the transcription file
    safe_title = os.path.basename(audio_file).replace('.mp4', '')
    output_directory = f"backend/transcriptions/{safe_title}.txt"

    # Save the transcription result to a text file
    with open(output_directory, 'w', encoding='utf-8') as f:
        f.write(result["text"])

    print(f"Transcription saved to {output_directory}")

    os.remove(f"backend/audio/{safe_title}.mp4")

if __name__ == '__main__':
    whisper_transcribe(youtube_url)
