import webbrowser
import subprocess

def execute_command(command):



    command = command.lower()

    if command == "open notepad":
        subprocess.Popen("notepad")
        return "Opening Notepad"

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