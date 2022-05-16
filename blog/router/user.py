from fastapi import APIRouter, Depends ,status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from .. repository import user


router = APIRouter(
    prefix = "/user",
    tags= ["users"]
)

@router.post('/', response_model = schemas.ShowUser)
def create(request: schemas.User, db: Session =Depends(database.get_db) ):
     return user.create(db, request)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session =Depends(database.get_db)):
     return user.show(db , id)
