# Youtube Transcriber

---
YouTube transcriber is an AI app that extracts the audio from a given YouTube video.
It then uses the extracted audio file to transcribe it into a readable text format. 

## Tech Stack

- Python
- OpenAi Whisper
---

## System Requirements
- Python
- ffmpeg (Used by Whisper to work with media files)
  - Install ffmpeg directly on your system. Don't use the pip install package.

## Setup Instructions
- No 3rd party APIs are required
- No .env environments are required


### Setup a virtual environment

```shell
python3 -m venv .venv
```

### Load virtual environment

```shell
source .env/bin/activate
```

### Install dependencies

```shell
pip install -r requirements.txt
```

### Run the transcriber

```shell
python3 backend/whisper_transcribe.py 
```
### Workflow

The yt_to_audio.py module will extract the audio from a given YouTube link. The extracted audio will be saved to the audio folder with the same name as the YouTube video.

The whisper_transcribe.py module will retrieve the saved audio file and transcribe it. The transcription will be saved to the backend/transcriptions folder with the same name as the audio file.

After saving the transcription the audio file will be removed to save space.

## Currently Excluded

In the current repo the following functionality was omitted.
- Download YouTube video and save to file.
- Summarize the transcription.
- Create PDF from transcription.