from fastapi import FastAPI
from db.schemas import Chat


app = FastAPI()


@app.get('/')
def read_root():
    return { 'title': 'hello world' }


@app.post('/chats')
async def create_chat(chat: Chat):
    print(f'{chat = }')
    return chat
