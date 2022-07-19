import datetime
from pydantic import BaseModel


class ChatBase(BaseModel):
    answer: str
    post_date: datetime.date


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    id: int
    user_id: int
    question: str

    class Config:
        orm_mode = True


class DiaryBase(BaseModel):
    title: str | None
    content: str | None
    post_date: datetime.date


class DiaryCreate(DiaryBase):
    pass 


class Diary(DiaryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    nickname: str
    uuid: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    chats: list[Chat] = []
    diaries: list[Diary] = []

    class Config:
        orm_mode = True
