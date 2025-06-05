from wake_word import wait_for_wake_word
from voice_interface import listen, speak
from llm_chat import ask_llm
from system_control import handle_system_command
from code_assistant import handle_code_task

def handle_command(command):
    if "code" in command or "explain" in command:
        result = handle_code_task(command)
    elif "open" in command or "shutdown" in command:
        result = handle_system_command(command)
    else:
        result = ask_llm(command)
    speak(result)

if __name__ == "__main__":
    speak("Jarvis is online and awaiting your command.")
    while True:
        wait_for_wake_word()
        speak("Yes, I'm listening...")
        command = listen()
        if command:
            handle_command(command)
