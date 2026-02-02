# from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
from src.service.ollama_chat import chat
from model.chat_test import ChatTestRequest, ChatTestResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat", response_model=ChatTestResponse)
def chat_endpoint(user_message: ChatTestRequest):
    chat_response = chat(user_message.message)
    if chat_response is None:
        return JSONResponse(content={"error": "Chat service failed"}, status_code=500)
    return ChatTestResponse(response=chat_response)