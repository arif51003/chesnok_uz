from passlib.context import CryptContext


def generate_slug(title):
    return title.lower().replace(" ", "_")


pwd_contex=CryptContext(schemes=["argon2"],deprecated="auto")

def hash_password(password:str):
    return pwd_contex.hash(password)


def verify_password(input_password:str,hashed_password:str):
    return pwd_contex.verify(input_password,hashed_password)

