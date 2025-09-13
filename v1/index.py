import pyttsx3

def text_to_speech():
    # Initialize the engine
    engine = pyttsx3.init()

    # Get input from user
    text = input("Enter the text you want to convert to speech: ")

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Run the function
text_to_speech()
