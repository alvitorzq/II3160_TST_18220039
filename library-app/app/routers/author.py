from fastapi import APIRouter, Depends, Response, status, HTTPException
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['authors']
)

@router.post("/authors", status_code = status.HTTP_201_CREATED)
def add_authors(author: schemas.Authors, db: Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    new_author = models.Author(name=author.name, genre=author.genre, description=author.description)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.delete("/authors/{name}", status_code = status.HTTP_204_NO_CONTENT)
def delete_author(name, author: schemas.Authors, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    authors = db.query(models.Author).filter(models.Author.name == name)
    if not authors.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Author with the name {name} is not found')
    
    authors.delete(synchronize_session = False)
    db.commit()
    return { 
        "Author has been deleted"
    }


@router.put("/authors/{name}", status_code = status.HTTP_202_ACCEPTED)
def update_author(name, author: schemas.Authors, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    authors = db.query(models.Author).filter(models.Author.name == name)
    if not authors.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Author with the name {name} is not found')

    authors.update({'name': author.name, 'genre': author.genre, 'description': author.description})
    db.commit()
    return {
        "Author has been updated"
    }


@router.get("/authors", response_model = List[schemas.ShowAuthors])
def all(db : Session = Depends(database.get_db)):
    authors = db.query(models.Author).all()
    return authors


@router.get("/authors/{name}", status_code=200, response_model = schemas.ShowAuthors)
def show_author(name, response : Response, db : Session = Depends(database.get_db)):
    authors = db.query(models.Author).filter(models.Author.name == name).first()
    if not authors:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Author with the name {name} is not found')
    return authors
