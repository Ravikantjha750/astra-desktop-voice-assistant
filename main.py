from speech import speak, listen

speak("Hello Ravi, I am Astra")

while True:

    command = listen()

    if command:

        speak("You said " + command)

        if command == "stop":
            speak("Goodbye")
            break