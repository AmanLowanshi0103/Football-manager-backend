from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models, services.crud as crud, schemas.schemas as schemas
from routes import user
from database.database import SessionLocal

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router=APIRouter()

@router.get("/dash")
def testUser():
    return {"find":"Ist working"}

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user=crud.create_user(db, user)
    if user:
        return {"sucess":"user create successfully"}
    else:
        raise HTTPException(status_code=404, detail="error while adding the user")


@router.post("/login")
def login_User(user:schemas.LoginData, db:Session=Depends(get_db)):
    token=crud.login_user(db,user)
    if token :
        return {"token":token}
    else:
        raise HTTPException(status_code=404, detail="Incorrect Username and passowrd")

@router.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}",response_model=schemas.UserRead)
def update_user(user_id: int, user:schemas.UserCreate, db: Session = Depends(get_db)):
    db_user= crud.update_user(db,user_id,user)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=schemas.UserCreate)
def delete_user(user_id: int, db:Session= Depends(get_db)):
    db_user= crud.delete_user(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user
