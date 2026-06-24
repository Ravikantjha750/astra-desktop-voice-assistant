import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def speak(text):
    print(f"Astra: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():



    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print(f"You: {text}")

        return text.lower()

    except sr.WaitTimeoutError:

        print("No speech detected")

        return ""

    except sr.UnknownValueError:

        print("Could not understand audio")

        return ""

    except Exception as e:

        print("Error:", e)

        return ""