import os
from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Defina a OPENAI_API_KEY no arquivo .env")

client = OpenAI(api_key=api_key)

audio_file = open("audio.wav", "rb")

transcription = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1"
)

texto_usuario = transcription.text
print("Texto transcrito:", texto_usuario)

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"Responda de forma clara: {texto_usuario}"
)

resposta_texto = response.output_text
print("Resposta:", resposta_texto)

tts = gTTS(resposta_texto, lang="pt")
tts.save("resposta.mp3")

print("Áudio gerado: resposta.mp3")
