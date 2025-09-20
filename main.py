from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
import models.models as models, services.crud as crud, schemas.schemas as schemas
from routes import user

import redis

app = FastAPI()

app.include_router(user.router, prefix="/api")


# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"success":"health Check"}