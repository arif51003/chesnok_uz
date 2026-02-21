from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from app.config import settings
from jose import jwt,JWTError
from fastapi import HTTPException


def generate_slug(title):
    return title.lower().replace(" ", "_")


pwd_contex=CryptContext(schemes=["argon2"],deprecated="auto")

def hash_password(password:str):
    return pwd_contex.hash(password)


def verify_password(input_password:str,hashed_password:str):
    return pwd_contex.verify(input_password,hashed_password)


def generate_jwt_tokens(user_id: int, is_access_only: bool = False):
    access_token = jwt.encode(
        algorithm=settings.ALGORITHM,
        key=settings.SECRET_KEY,
        claims={
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        },
    )

    if is_access_only:
        return access_token

    refresh_token = jwt.encode(
        algorithm=settings.ALGORITHM,
        key=settings.SECRET_KEY,
        claims={
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        },
    )

    return access_token, refresh_token


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")