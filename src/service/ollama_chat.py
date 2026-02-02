# from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama

llm = ChatOllama(model="medllama2", baseurl="http://localhost:11434")

def chat(user_messages):
    messages = [
        (
            "system",
            "You are a helpful assistant that answer the user questions about medical.",
        ),
        ("human", user_messages),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content