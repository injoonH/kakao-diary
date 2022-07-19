import datetime
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import kakao
import chatbot
import papago


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
    # Get user
    db_user = crud.get_user_by_nickname(db=db, nickname=nickname)
    if db_user is None:
        print('User not found')
        uuid = kakao.get_friend_uuid_by_nickname(nickname)
        if uuid is None:
            print('User not in friends list')
            return
        print(f'{uuid = }')
        db_user = crud.create_user(
            db=db,
            user=schemas.UserCreate(nickname=nickname, uuid=uuid)
        )
    else:
        print('==== USER ====')
        print(f'{nickname} found in DB')
    
    # Get previous question
    prev_question = last_questions.get(db_user.uuid)
    if prev_question is None:
        prev_question = ''
    
    # Translate Korean to English
    chat.answer = papago.get_translate(chat.answer, toEnglish=True)
    print('==== Ko-En ====')
    print(chat.answer)
    
    # Save chat in DB
    db_chat = crud.create_user_chat(db=db,
                                    user_id=db_user.id,
                                    question=prev_question,
                                    chat=chat)
    
    # Get previous chats
    print('==== DATE ====')
    print(chat.post_date)
    prev_chats = crud.get_user_chats_on_date(db=db,
                                             user_id=db_user.id,
                                             date=chat.post_date)
    
    # Check if user wants to end a conversation
    if '!!!' in chat.answer.lower():
        last_questions.pop(db_user.uuid, None)
        diary_title, diary_content = chatbot.get_diary(prev_chats=prev_chats)
        
        diary_title = papago.get_translate(diary_title, toEnglish=False)
        diary_content = papago.get_translate(diary_content, toEnglish=False)
        
        crud.create_user_diary(db=db,
                               user_id=db_user.id,
                               diary=schemas.DiaryCreate(
                                   title=diary_title,
                                   content=diary_content,
                                   post_date=chat.post_date))
        return db_chat
    
    # Use last three chats to create next question
    if len(prev_chats) > 3:
        prev_chats = prev_chats[-3:]
    
    # Create next question & send it to user
    print('==== USER CHAT ====')
    print(chat.answer)
    new_question = chatbot.get_chat_response(prev_chats=prev_chats)
    last_questions[db_user.uuid] = new_question

    ko_new_question = papago.get_translate(new_question, toEnglish=False)
    print('==== En-Ko ====')
    print(ko_new_question)
    kakao.send_message(db_user.uuid, ko_new_question)
    
    return db_chat


@app.get('/diaries', response_model=list[schemas.Diary])
def read_diaries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diaries = crud.get_diaries(db, skip=skip, limit=limit)
    return diaries


@app.get('/diaries/{date}', response_model=list[schemas.Diary])
def read_diaries(date: datetime.date, db: Session = Depends(get_db)):
    diaries = crud.get_diaries_on_date(db=db, date=date)
    return diaries


@app.put('/diaries/{diary_id}')
def update_diary(diary_id: int, title: str, content: str, db: Session = Depends(get_db)):
    crud.update_diary(db=db, diary_id=diary_id, title=title, content=content)
