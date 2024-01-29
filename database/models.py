from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    birthday = Column(Date)
    password = Column(String)
    profile_photo = Column(String)
    reg_date = Column(DateTime)


# Таблица публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))  # 2
    post_text = Column(Text)
    likes = Column(Integer, default=0)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')  # user_fk.


# Таблица фотографий к определенному посту
class PostPhoto(Base):
    __tablename__ = 'post_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')

# Дз сделать таблицу для комментарий ДЗ! 10 отжиманий
# class PostComment(Base)