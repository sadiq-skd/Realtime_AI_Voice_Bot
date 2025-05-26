# Real-Time AI Voice Bot (Offline)

A terminal-based real-time AI voice assistant that:

- Converts speech to text using [Vosk](https://alphacephei.com/vosk/) (offline speech recognition)
- Generates responses using GPT-2 from HuggingFace Transformers
- Speaks responses aloud using `pyttsx3` (offline TTS)

---

## Project Structure

```
Realtime_AI_Voice_Bot/
│
├── voice_bot.py          # Main Python script
├── README.md             # This file
```

> **Note:** The Vosk model folder `vosk-model-small-en-us-0.15/` is **not included** and must be downloaded separately.

---

##  Installation

1. **Install Python packages:**

```bash
pip install sounddevice pyttsx3 vosk transformers torch
```

2. **Download the Vosk English speech recognition model:**

- Download from [Vosk Model page](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip)
- Extract the ZIP file
- Place the extracted folder `vosk-model-small-en-us-0.15` in the **same directory** as `realtime_ai_voice_bot.py`

Your folder structure should look like this:

```
Realtime_AI_Voice_Bot/
├── realtime_ai_voice_bot.py
├── README.md
└── vosk-model-small-en-us-0.15/
```

---

## How to Run

Run the voice bot with:

```bash
python realtime_ai_voice_bot.py
```

Speak into your microphone. The bot will listen, transcribe your voice, generate a response, and speak it back.

To stop the program, press `Ctrl+C`.

---

## Sample Interaction

```
 Speak into the microphone. Press Ctrl+C to stop.

You: hello
Bot: Hello, how can I help you today?
```

---

## Customization

- Replace `distilgpt2` with larger or custom GPT-2 models.
- Add conversation history to improve context.
- Add command or action triggers.
- Create a GUI using frameworks like Gradio or Tkinter.

---

## License

This project is open source under the MIT License.

---

## Author

**Your Name**  
Muhammad Sadiq
