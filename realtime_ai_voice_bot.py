import os
import sys
import json
import queue
import sounddevice as sd
import pyttsx3
from vosk import Model, KaldiRecognizer
from transformers import pipeline

# Path to Vosk model
model_path = os.path.join(os.path.dirname(__file__), "vosk-model-small-en-us-0.15")

if not os.path.exists(model_path):
    print("Model not found at:", model_path)
    sys.exit(1)

# Load Vosk model for speech recognition
print("[INFO] Loading Vosk model...")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Queue for storing audio chunks
q = queue.Queue()

# Callback function for live audio input
def audio_callback(indata, frames, time, status):
    if status:
        print(f"[Audio status]: {status}", file=sys.stderr)
    q.put(bytes(indata))

# Load GPT-2 text generation model
print("[INFO] Loading GPT-2 language model...")
generator = pipeline("text-generation", model="distilgpt2")
print("[INFO] Language model ready.")

# Initialize TTS engine
engine = pyttsx3.init()

# Start real-time voice bot
print("🎤 Speak into the microphone. Press Ctrl+C to stop.")

try:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                user_text = result.get("text", "")

                if user_text:
                    print(f"\nYou: {user_text}")

                    # Generate response
                    #response = generator(user_text, max_length=50, do_sample=True)[0]["generated_text"]
                    response = generator(user_text, max_new_tokens=50, do_sample=True, truncation=True, pad_token_id=50256)[0]['generated_text']
                    print(f"Bot: {response}")

                    # Speak response
                    engine.say(response)
                    engine.runAndWait()

except KeyboardInterrupt:
    print("\n[INFO] Voice bot stopped.")
except Exception as e:
    print(f"[ERROR] {e}")
