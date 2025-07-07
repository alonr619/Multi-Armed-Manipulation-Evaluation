import ollama

def call_agent(messages, model="llama3.2:latest"): # Modify this for different APIs
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']