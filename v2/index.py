import pyttsx3


def text_to_speech():
    # Initialize the engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty("voices")
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")

    # Choose voice
    try:
        voice_choice = int(input("Choose a voice (number): "))
        engine.setProperty("voice", voices[voice_choice].id)
    except:
        print("Invalid choice, using default voice.")

    # Set speech rate
    try:
        rate = int(input("Enter speech rate (100 = slow, 200 = normal, 300 = fast): "))
        engine.setProperty("rate", rate)
    except:
        print("Invalid input, using default speed.")

    # Get user input
    text = input("\nEnter the text you want to convert to speech: ")

    # Speak text
    engine.say(text)
    engine.runAndWait()

    # Save as audio file (optional)
    save = input("Do you want to save the speech as an MP3 file? (y/n): ").lower()
    if save == "y":
        filename = input("Enter filename (example: output.mp3): ")
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print(f"✅ Audio saved as {filename}")


# Run program
if __name__ == "__main__":
    text_to_speech()
