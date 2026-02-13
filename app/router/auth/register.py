from fastapi import APIRouter,HTTPException
from app.schemas.auth_schema import UserRegisterRequest,UserRegisterResponse
from app.database import db_dep
from app.utils import hash_password
from sqlalchemy import select
from app.models import User

router=APIRouter(
)

@router.post("/register",status_code=201,response_model=UserRegisterResponse)
async def register_user(session:db_dep,data:UserRegisterRequest):
    
    a=select(User)
    b=session.execute(a)
    res=b.scalars().all()
    
    superuser=False
    if not res:
        superuser=True
    
    
    stmt=select(User).where(User.email==data.email)
    user=(session.execute(stmt)).scalars().first()
    
    if user:
        raise HTTPException(
            status_code=409,
            detail="Email alredy exists"
        )
    
    
    user=User(
        email=data.email,
        password_hash=hash_password(data.password),
        is_superuser=superuser
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user