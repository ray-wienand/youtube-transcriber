import os
import re
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

youtube_url = "https://www.youtube.com/watch?v=iVkoNcHNR9g"

# Create folder if it doesn't exist
os.makedirs("backend/transcriptions", exist_ok=True)

def yt_transcribe(youtube_url):
    # pytube download video part
    yt = YouTube(youtube_url)
    
    # Get the video id
    video_id = yt.video_id
    
    print('')
    print('********************************************************************************************************************')
    print('')
    print(f"Starting the process for {youtube_url}")
    print('')
    print('********************************************************************************************************************')
    print('')
    
    print(f"Fetching transcript for video ID: {video_id}")
    print('')
    
    # Get the transcript from YT
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Generate a safe title for the transcription file
        # Replace any sequence of invalid filename characters with an underscore

        '''
        Special note: This was a pain in the freaking ass to get right. 
        Even ChatGpt struggled to get it right :-)
        It would keep on saving it with ..txt instead of .txt
        '''
        safe_title = re.sub(r'[\\/*?:"<>|]+', '_', yt.title)
        # Replace multiple spaces with a single underscore
        safe_title = re.sub(r'\s+', '_', safe_title)
        # Ensure no leading or trailing underscores or periods
        safe_title = safe_title.strip('_').strip('.')
        
        # Create the full file path
        output_directory = f"backend/transcriptions/yt_{safe_title}.txt"
        
        # Remove timestamps and concatenate the text
        transcript_paragraph = " ".join([i["text"] for i in transcript])
        
        # Commented out the print statements
        # print(transcript_paragraph) 
        # print('')
        
        print(f"Saving the transcript to: {output_directory}")
        # Save the transcription paragraph to a text file
        with open(output_directory, 'w', encoding='utf-8') as f:
            f.write(transcript_paragraph)
        
        # Check if the file has been written correctly
        if os.path.isfile(output_directory):
            print(f"File saved successfully")
        else:
            print(f"Failed to save the file to: {output_directory}")
        
        print('')
        print('********************************************************************************************************************')
        print('')
        print('Task completed')
        print('')
        print('********************************************************************************************************************')
        print('')
    except Exception as e:
        print(f'There was an error: {e}')

if __name__ == '__main__':
    yt_transcribe(youtube_url)
