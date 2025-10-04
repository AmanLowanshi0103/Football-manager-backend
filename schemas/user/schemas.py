from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password:str

class UserRead(UserCreate):
    id: int


class LoginData(BaseModel):
    email:str
    password:str
    
    class Config:
        orm_mode = True  # Tells Pydantic to read data from ORM objects
