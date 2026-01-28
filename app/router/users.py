from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import db_dep
from app.models import User
from app.schemas import UserCreateRequest, UserListResponse, UserUpdateRequest

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create/", response_model=UserListResponse)
async def user_create(session: db_dep, data: UserCreateRequest):
    user = User(
        email=data.email,
        password_hash=data.password,
        first_name=data.first_name,
        last_name=data.last_name,
        bio=data.bio,
        profession_id=data.profession_id,
        is_staff=data.is_staff,
        is_superuser=data.is_superuser,
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


@router.get("/list/", response_model=list[UserListResponse])
async def user_list(session: db_dep, is_activ: bool):
    stmt = select(User)

    if is_activ is not None:
        stmt = select(User).where(User.is_active == is_activ)

    res = session.execute(stmt)
    list = res.scalars().all()

    return list


@router.put("/update/", response_model=UserListResponse)
async def update_user(
    session: db_dep,
    user_id: int,
    is_active: bool,
    is_staff: bool,
    is_superuser: bool,
    data: UserUpdateRequest,
):
    stmt = select(User).where(User.id == user_id)
    res = session.execute(stmt)
    user = res.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="Not Found")

    user.first_name = data.first_name
    user.last_name = data.last_name
    user.email = data.email
    user.password_hash = data.password
    user.bio = data.bio
    user.profession_id = data.profession_id
    user.is_active = is_active
    user.is_staff = is_staff
    user.is_superuser = is_superuser

    session.commit()
    session.refresh(user)

    return user


@router.delete("/delete/{user_id}", status_code=204)
async def del_user(session: db_dep, user_id):
    stmt = select(User).where(User.id == user_id)
    res = session.execute(stmt)
    user = res.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="NOT FONUD")

    session.delete(user)
    session.refresh(user)
    session.commit()
