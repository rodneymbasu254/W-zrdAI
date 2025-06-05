import ollama

def ask_llm(prompt, model="llama3"):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
