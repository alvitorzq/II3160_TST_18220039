from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    genre = Column(String)
    description = Column(String)
    author = Column(String)
    isbn = Column(Integer)
    available = Column(Boolean, unique = False, default = True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    writter = relationship("Author", back_populates="book")


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    genre = Column(String)
    description = Column(String)

    book = relationship("Book", back_populates="writter")

class BookPic(Base):
    __tablename__ = 'books_pictures'

    pic = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
   
