from fastapi import FastAPI
from sqlalchemy.orm import Session
from app import models
from app.database import engine
from app.routers import book, user, author, auth, book_pictures

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(book.router)
app.include_router(author.router)
app.include_router(book_pictures.router)