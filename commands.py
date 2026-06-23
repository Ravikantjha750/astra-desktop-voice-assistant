import webbrowser

def execute_command(command):

    if command.startswith("open "):

        site = command.replace("open ", "").strip().lower()

        url = f"https://www.{site}.com"

        webbrowser.open(url)

        return f"Opening {site}"

    return None