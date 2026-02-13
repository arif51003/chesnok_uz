from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import db_dep
from app.models import User,UserSearch
from app.schemas.schemas import UserSearchResponse

router=APIRouter(
    prefix="/usersearch",
    tags=["User interest"]
)

@router.get("/user_interest/",response_model=list[UserSearchResponse])
async def usersearch(session:db_dep):
    stmt=select(UserSearch).order_by(UserSearch.count.desc())
    res=session.execute(stmt)
    interests=res.scalars().all()
    
    if not interests:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
        
    session.commit()
    # session.refresh(interests)
    
    return interests