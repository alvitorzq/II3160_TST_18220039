from fastapi import APIRouter, Depends, Response, status, HTTPException
from .. import schemas, database, models, oauth2
from typing import Optional, List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['search book by pictures']
)

@router.get("/search_books/{pic_id}", status_code=200, response_model = schemas.ShowBooks)
def search_book(pic_id, response : Response, db : Session = Depends(database.get_db)):
    books = db.query(models.Book).filter(models.Book.id == id).first()
    if not books:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with the picture is not registered')
    return books

# @router.post("/search_books", status_code = status.HTTP_201_CREATED)
# def add_book_pictures(book: schemas.SearchBooks, db: Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
#     new_pic = models.BookPic(pic = book.pic, title=book.title, author = book.author, genre=book.genre)
#     db.add(new_pic)
#     db.commit()
#     db.refresh(new_pic)
#     return new_pic