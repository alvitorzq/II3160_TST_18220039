from fastapi import APIRouter, Depends, Response, status, HTTPException
from .. import schemas, database, models, oauth2
from typing import Optional, List
from sqlalchemy.orm import Session
from ..hashing import HashPassword


router = APIRouter(
    tags = ['users']
)

@router.post("/user", response_model = schemas.ShowUsers)
def create_user(user : schemas.Users, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    new_user = models.User(name=user.name, email=user.email, password=HashPassword.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/user", response_model = List[schemas.ShowUsers])
def all(db : Session = Depends(database.get_db),current_user : schemas.Users = Depends(oauth2.get_current_user)):
    users = db.query(models.User).all()
    return users


@router.get("/user/{name}", response_model = schemas.ShowUsers)
def show_user(name : str, db : Session = Depends(database.get_db), current_user : schemas.Users = Depends(oauth2.get_current_user)):
    users = db.query(models.User).filter(models.User.name == name).first()
    if not users:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'User with the name {name} is not found')
    return users