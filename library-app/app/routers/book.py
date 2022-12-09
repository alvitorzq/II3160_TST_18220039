from fastapi import APIRouter, Depends, Response, status, HTTPException
from .. import schemas, database, models, oauth2
from typing import Optional, List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['books']
)

@router.get("/books", response_model = List[schemas.ShowBooks])
def all(db : Session = Depends(database.get_db)):
    books = db.query(models.Book).all()
    return books

@router.get("/books/{title}", status_code=200, response_model = schemas.ShowBooks)
def show_book(title, response : Response, db : Session = Depends(database.get_db)):
    books = db.query(models.Book).filter(models.Book.title == title).first()
    if not books:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with the title {title} is not registered')
    return books

@router.post("/books", status_code = status.HTTP_201_CREATED)
def add_book(book: schemas.Books, db: Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    new_book = models.Book(title=book.title, genre=book.genre, description=book.description, author=book.author, isbn=book.isbn, author_id=3)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.delete("/books/{title}", status_code = status.HTTP_204_NO_CONTENT)
def delete_book(title, book: schemas.Books, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    books = db.query(models.Book).filter(models.Book.title == title)
    if not books.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with the title {title} is not registered')
    
    books.delete(synchronize_session = False)
    db.commit()
    return { 
        "Book has been deleted"
    }

@router.put("/books/{title}", status_code = status.HTTP_202_ACCEPTED)
def update_book(title, book: schemas.Books, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    books = db.query(models.Book).filter(models.Book.title == title)
    if not books.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with the title {title} is not registered')

    books.update({'title': book.title, 'genre': book.genre, 'description': book.description, 'author': book.author, 'isbn': book.isbn})
    db.commit()
    return {
        "Books has been updated"
    }