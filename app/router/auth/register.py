from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from app.schemas.auth_schema import UserRegisterRequest,UserRegisterResponse
from app.database import db_dep
from app.utils import hash_password
from sqlalchemy import select
from app.models import User
import secrets
from app.utils import redis_client,send_email

router=APIRouter(
)

# @router.post("/register",status_code=201,response_model=UserRegisterResponse)
# async def register_user(session:db_dep,data:UserRegisterRequest):
    
#     a=select(User)
#     b=session.execute(a)
#     res=b.scalars().all()
    
#     superuser=False
#     if not res:
#         superuser=True
    
    
#     stmt=select(User).where(User.email==data.email)
#     user=(session.execute(stmt)).scalars().first()
    
#     if user:
#         raise HTTPException(
#             status_code=409,
#             detail="Email alredy exists"
#         )
    
    
#     user=User(
#         email=data.email,
#         password_hash=hash_password(data.password),
#         is_superuser=superuser
#     )
#     session.add(user)
#     session.commit()
#     session.refresh(user)
    
#     return user

@router.post("/", response_model=UserRegisterResponse)
async def register_user(db: db_dep, data: UserRegisterRequest):
    stmt = select(User).where(User.email == data.email)
    res = (db.execute(stmt)).scalars().first()

    if res:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        email=data.email, password_hash=hash_password(data.password), is_active=False
    )

    secret_code = secrets.token_hex(16)
    send_email(
        data.email, "Email confirmation", f"Your confirmation code is {secret_code}"
    )
    redis_client.setex(secret_code, 120, user.email)  # 5678 : email

    stmt = select(User)
    existing_user = db.execute(stmt).scalars().first()

    if not existing_user:
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

    db.add(user)
    db.commit()

    return JSONResponse(
        status_code=201, content={"message": "Email confirmation sent to your email."}
    )


@router.post("/verify/{secret_code}/", response_model=UserRegisterResponse)
async def verify_register(db: db_dep, secret_code: str):
    email = redis_client.get(secret_code)
    print(email.decode("utf-8"))

    if not email:
        raise HTTPException(status_code=400, detail="Invalid code")

    stmt = select(User).where(User.email == email.decode("utf-8"))
    user = db.execute(stmt).scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = True
    db.commit()

    return JSONResponse(
        status_code=200, content={"message": "User registered successfully"}
    )