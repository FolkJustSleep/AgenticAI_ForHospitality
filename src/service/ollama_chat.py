# from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama

llm = ChatOllama(model="medllama2", baseurl="http://localhost:11434")

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)