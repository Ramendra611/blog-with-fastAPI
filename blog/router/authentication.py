from fastapi  import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import  Hash
from ..token import create_access_token


router = APIRouter(
    tags = ["authentication"]
)

@router.post('/login')
# def login(request: schemas.Login, db: Session =Depends(database.get_db)):
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session =Depends(database.get_db)): #use this for authentication
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'INVALID Credentials ')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'INVALID Password ')
    #generate a JWT token and return
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
