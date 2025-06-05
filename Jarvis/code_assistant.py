from llm_chat import ask_llm

def handle_code_task(command):
    return ask_llm(f"You are a code assistant. {command}", model="codellama")
