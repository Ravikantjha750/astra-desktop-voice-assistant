from logger import log_command
from speech import speak, listen
from commands import execute_command

speak("Hello Ravi, I am Astra")

while True:

    command = listen()

    if not command:
        continue

    command = command.lower()

    # Remove wake word if present
    command = command.replace("astra", "").strip()

    if command == "stop":
        speak("Goodbye")
        break

    log_command(command)

    result = execute_command(command)

    if result:
        speak(result)

    else:
        speak("I do not know that command yet")