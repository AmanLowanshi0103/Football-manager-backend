from fastapi import FastAPI, Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext




# Secret key to encode and decode JWT
SECRET_KEY = "your-secret-key"  # Use a strong secret in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifyPassword(Plain_password,Hash_password):
    return pwd_context.verify(Plain_password,Hash_password)


def create_access_token(data):
    user=data.copy()
    return jwt.encode(user, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")