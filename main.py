from speech import speak, listen
from commands import execute_command

speak("Hello Ravi, I am Astra")

while True:

    command = listen()

    if command:

        result = execute_command(command)

        if result:
            speak(result)

        elif command == "stop":
            speak("Goodbye")
            break

        else:
            speak("I do not know that command yet")