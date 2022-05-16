from sqlalchemy.orm import Session
from .. import models , schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(db: Session, request: schemas.User ):
    new_user = models.User(name=request.name,
                           email=request.email,
                           password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(db : Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {id} is not available")
    return user