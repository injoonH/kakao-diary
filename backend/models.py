from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(255), unique=True, index=True)
    uuid = Column(String(63), unique=True)
    
    chats = relationship('Chat', back_populates='user')
    diaries = relationship('Diary', back_populates='user')


class Chat(Base):
    __tablename__ = 'chats'
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(1023))
    answer = Column(String(1023))
    post_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='chats')


class Diary(Base):
    __tablename__ = 'diaries'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1023))
    content = Column(String(1023))
    post_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='diaries')
