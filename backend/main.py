from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
import kakao
import chatbot


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/{nickname}/chats', response_model=schemas.Chat)
def create_chat_for_user(
    nickname: str, chat: schemas.ChatCreate, db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_nickname(db=db, nickname=nickname)
    if db_user is None:
        print('user not found')
        uuid = kakao.get_friend_uuid_by_nickname(nickname)
        if uuid is None:
            print('user not in friends list')
            return
        print('uuid', uuid)
        db_user = crud.create_user(
            db=db,
            user=schemas.UserCreate(nickname=nickname, uuid=uuid)
        )
    else:
        print('user found in DB', db_user)
    
    # chats = crud.get_user_chats(db=db, user_id=db_user.id)
    # print('chats', chats)
    
    response = chatbot.get_chat_response(chat.content)
    kakao.send_message(db_user.uuid, response)
    
    return crud.create_user_chat(db=db, chat=chat, user_id=db_user.id)
