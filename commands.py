from volume_control import (
    set_volume,
    mute_volume,
    unmute_volume
)
from memory import save_memory, load_memory
from datetime import datetime
import webbrowser
import subprocess
import pyautogui


def execute_command(command):



    command = command.lower()
    # Dynamic Memory System

    if command.startswith("remember my"):

        data = command.replace("remember my", "").strip()

        if " is " in data:
            key, value = data.split(" is ", 1)

            save_memory(key.strip(), value.strip())

            return f"I will remember your {key}"

    elif command.startswith("what is my"):

        key = command.replace("what is my", "").strip()

        memory = load_memory()

        if key in memory:
            return f"Your {key} is {memory[key]}"

        return f"I do not know your {key} yet"

    if command == "open notepad":
        subprocess.Popen("notepad")
        return "Opening Notepad"
    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The time is {current_time}"

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}"

    elif "screenshot" in command:

        filename = datetime.now().strftime(
            "screenshots/screenshot_%Y%m%d_%H%M%S.png"
        )

        screenshot = pyautogui.screenshot()

        screenshot.save(filename)

        return "Screenshot saved successfully"

    elif command == "open calculator":
        subprocess.Popen("calc")
        return "Opening Calculator"


    elif (

            command == "open vscode"

            or command == "open vs code"

            or command == "open visual studio code"
            or command == "open v s code"
            or command == "open v scode"
            or command == "open vs"

    ):

        subprocess.Popen(

            r"C:\Users\Ravikant Jha\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        )

        return "Opening VS Code"
    elif "set volume to" in command:

        try:

            percent = int(
                command.split("set volume to")[1]
                .replace("%", "")
                .replace("percent", "")
                .strip()
            )

            percent = max(0, min(100, percent))

            set_volume(percent)

            return f"Volume set to {percent} percent"

        except Exception as e:

            return f"Volume error: {e}"

    elif "mute volume" in command:

        mute_volume()

        return "Volume muted"

    elif "unmute volume" in command:

        unmute_volume()

        return "Volume unmuted"

    elif command.startswith("open "):
        site = command.replace("open ", "").strip()

        webbrowser.open(f"https://www.{site}.com")

        return f"Opening {site}"

    return None