from pypdf import PdfReader
import requests

key = ''
id = ''

reader = PdfReader('data/Command Prompt Cheatsheet.pdf')
pages_number = len(reader.pages)
page = reader.pages
for i in page:
    text = i.extract_text()

    url = "https://api.play.ht/api/v2/tts"
    payload = {
        'text': f'{i}',
        'voice': 's3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json',
        'output_format': 'mp3',
        'voice_engine': 'PlayHT2.0',
    }
    headers = {
        'accept': 'text/event-stream',
        'content-type': 'application/json',
        'AUTHORIZATION': f'{key}',
        'X-USER-ID': f'{id}',
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    print(response.text)