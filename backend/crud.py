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
