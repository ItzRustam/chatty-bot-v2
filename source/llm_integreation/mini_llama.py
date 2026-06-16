from langchain_ollama import ChatOllama

model = ChatOllama(model="tinyllama:1.1b", temperature=0.8)

def generate(msg : str = "Hello"):
    response = model.invoke(f"You're a funny chatbot answer user's question under two sentence and you are going to be used in discord bot, message={msg}")

    return response.content

if __name__ == "__main__":
    output = generate("yoo bud! what's going on!")
    print(output)