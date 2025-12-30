import speech_recognition as sr

def main():
    """
    Main function to initialize the recognizer and convert 
    microphone input into text.
    """
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Access the microphone
    with sr.Microphone() as source:
        print("\n--- CODTECH SPEECH RECOGNITION SYSTEM ---")
        print("Status: Calibrating for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Status: Listening... (Speak now)")
        
        try:
            # Capture audio with a 5-second limit
            audio = recognizer.listen(source, timeout=5)
            print("Status: Transcribing...")

            # Convert audio to text using Google's pre-trained model
            text = recognizer.recognize_google(audio)
            
            print(f"\nRESULT: {text}")
            
            # Save the result to a file as required for the deliverable
            with open("transcription.txt", "w") as f:
                f.write(text)
            print("\nSuccess: Transcription saved to transcription.txt")

        except sr.UnknownValueError:
            print("Error: Could not understand audio.")
        except sr.RequestError:
            print("Error: Could not reach the recognition service.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()