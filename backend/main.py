from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
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


last_questions = {}


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
    
    prev_question = last_questions.get(db_user.uuid)
    if prev_question is None:
        prev_question = ''
    
    new_question = chatbot.get_chat_response(chat.answer)
    last_questions[db_user.uuid] = new_question
    kakao.send_message(db_user.uuid, new_question)
    
    return crud.create_user_chat(db=db,
                                 user_id=db_user.id,
                                 question=prev_question,
                                 chat=chat)
