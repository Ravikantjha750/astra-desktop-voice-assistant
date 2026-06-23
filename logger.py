from datetime import datetime

def log_command(command):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/commands.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{timestamp} -> {command}\n"
        )