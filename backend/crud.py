import datetime
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_nickname(db: Session, nickname: str):
    return db \
        .query(models.User) \
        .filter(models.User.nickname == nickname) \
        .first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_chats(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db \
        .query(models.Chat) \
        .filter(models.Chat.user_id == user_id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_user_chats_on_date(
        db: Session,
        user_id: int,
        date: datetime.date,
        skip: int = 0,
        limit: int = 100):
    return db \
        .query(models.Chat) \
        .filter(models.Chat.user_id == user_id and models.Chat.post_date == date) \
        .offset(skip) \
        .limit(limit) \
        .all()


def create_user_chat(
        db: Session,
        user_id: int,
        question: str,
        chat: schemas.ChatCreate):
    db_chat = models.Chat(**chat.dict(), user_id=user_id, question=question)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def create_user_diary(db: Session, user_id: int, diary: schemas.DiaryCreate):
    db_diary = models.Diary(**diary.dict(), user_id=user_id)
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary


def get_diaries(db: Session, skip: int = 0, limit: int = 100):
    return db \
        .query(models.Diary) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_diaries_on_date(db: Session, date: datetime.date):
    return db \
        .query(models.Diary) \
        .filter(models.Diary.post_date == date) \
        .all()


def update_diary(db: Session, diary_id: int, title: str, content: str):
    return db.query(models.Diary) \
        .filter(models.Diary.id == diary_id) \
        .update({'title': title, 'content': content})
