# 🎙️ AI SPEECH RECOGNITION SYSTEM

## 📋 Project Overview
This project is part of my **CODTECH IT SOLUTIONS** internship. It is a functional Speech-to-Text (STT) system capable of transcribing real-time audio from a microphone into text using pre-trained models.

The system features an interactive web-based UI for a user-friendly experience, allowing users to record, transcribe, and download their speech as text files.

---

## 🚀 Features
- **Real-time Transcription:** Uses Google's pre-trained Speech Recognition models.
- **Interactive UI:** Built with **Streamlit** for a seamless web experience.
- **Ambient Noise Adjustment:** Automatically calibrates for background noise to improve accuracy.
- **File Export:** Option to download the transcribed text as a `.txt` file.
- **Multi-language Support:** Configurable to recognize different languages/accents.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** - `SpeechRecognition`: For handling the speech-to-text logic.
  - `PyAudio`: For microphone access and audio stream processing.
  - `Streamlit`: For creating the web-based user interface.

---

## 📂 Project Structure
```text
CODTECH-SPEECH-RECOGNITION/
├── app.py                # Main Streamlit Web Application
├── main.py               # CLI version of the speech system
├── requirements.txt      # List of dependencies
├── transcription.txt     # Saved output of the transcription
└── README.md             # Project documentation