import os
import yt_video as yv
import text_to_pdf as pdf
from youtube_transcript_api import YouTubeTranscriptApi
from text_to_pdf import create_pdf_from_txt

video_id = yv.video_id

def yt_transcript(video_id):
    """
    Fetches the transcript for the given YouTube video ID, saves it to a file,
    and returns it as a single string.

    Args:
    video_id (str): The ID of the YouTube video.

    Returns:
    str: The transcript of the video concatenated into a single paragraph.
    """
    try:
        print(f"Fetching transcript for video ID: {video_id}")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_paragraph = " ".join([i["text"] for i in transcript])
        
        # Safe title for filename
        safe_title = yv.safe_title
        filename = f"backend/transcriptions/yt_{safe_title}.txt"
        
        # Debug print statements
        print(f"Saving transcript to: {filename}")
        print(f"Transcript content: {transcript_paragraph[:100]}...")  # Print the first 100 characters
        
        # Save transcript to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(transcript_paragraph)
        
        # Check if the file has been written correctly
        if os.path.isfile(filename):
            print(f"File saved successfully: {filename}")
        else:
            print(f"Failed to save the file: {filename}")

        # Create PDF from the saved transcript file
        create_pdf_from_txt(filename)

        return transcript_paragraph
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# print(f"Video ID: {video_id}")
transcript = yt_transcript(video_id)
# print(transcript)

