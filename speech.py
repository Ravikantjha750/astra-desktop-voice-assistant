import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)  # Zira
engine.setProperty('rate', 180)

def speak(text):
    print(f"Astra: {text}")
    engine.say(text)
    engine.runAndWait()