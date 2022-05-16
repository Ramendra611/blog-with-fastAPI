from fastapi import APIRouter, Depends ,status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from .. repository import blog

router = APIRouter(
    prefix = "/blog",
    tags =["blogs"]
    )

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session =Depends(database.get_db) ):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,
           db: Session =Depends(database.get_db) ):
     blog.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED  )
def update(id, request: schemas.Blog, db: Session =Depends(database.get_db)):
     blog.update(id ,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session =Depends(database.get_db)  ):
     blog.destroy(db, id)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id : int,  db: Session =Depends(database.get_db) , status_code = 200):

    blog.show(db, id)
