from datetime import datetime
from datetime import datetime
import webbrowser
import subprocess
import pyautogui


def execute_command(command):



    command = command.lower()

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

    elif command.startswith("open "):
        site = command.replace("open ", "").strip()

        webbrowser.open(f"https://www.{site}.com")

        return f"Opening {site}"

    return None