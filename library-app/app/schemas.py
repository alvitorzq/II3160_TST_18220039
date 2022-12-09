from pydantic import BaseModel
from typing import Optional, List


class Users(BaseModel):
    name : str
    email : str
    password : str

class ShowUsers(BaseModel):
    name : str
    email : str
    password : str
    class Config():
        orm_mode = True

class BooksBase(BaseModel):
    title : str
    genre : str
    description : str
    author : str
    isbn : int
    available : Optional[bool]
    class Config():
        orm_mode = True

class Books(BooksBase):
    class Config():
        orm_mode = True

class Authors(BaseModel):
    name : str
    genre: str
    description : str

class ShowAuthors(BaseModel):
    id : int
    name : str
    genre: str
    description : str
    book : List
    class Config():
        orm_mode = True
    
class ShowBooks(BaseModel):
    title : str
    genre : str
    description : str
    author : str
    isbn : int
    class Config():
        orm_mode = True

class SearchBooks(BaseModel):
    title : str
    author : str
    genre : str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str]