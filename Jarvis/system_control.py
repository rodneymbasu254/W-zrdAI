import os
import subprocess

def handle_system_command(command):
    if "open chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome."
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the computer."
    else:
        return "Sorry, I couldn't find that command yet."
