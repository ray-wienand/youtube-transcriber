# Youtube Transcriber

---
YouTube transcriber extracts the transcription from a given YouTube video. 

## System Requirements
- Python

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

### Get the transcript directly from YouTube
This module downloads the YouTube transcript and removes the timestamps.
It then concatenates the te text into one paragraph.

```shell
python3 backend/yt_transcript.py 
```
