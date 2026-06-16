from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize the hosted endpoint
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)

def generate(msg : str = "Hello"):
    response = model.invoke(f"You're a funny chatbot answer user's question under two sentence and you are going to be used in discord bot, message={msg}")

    return response.content

if __name__ == "__main__":
    out = generate("Hello")
    print(out)