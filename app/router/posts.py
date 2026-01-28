from fastapi import APIRouter, HTTPException, Path, Query,Response,Cookie
from sqlalchemy import select

from app.database import db_dep
from app.models import Post, Category
from app.schemas import (
    PostCreateRequest,
    PostListResponse,
    PostUpdateRequest,
    Categories,
    CookieData
)
from app.utils import generate_slug

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/list/", response_model=list[PostListResponse])
async def get_posts(session: db_dep, item: Categories, is_active: bool = None):
    stmt = select(Post).join(Category).where(Category.name == item)

    if is_active is not None:
        stmt = stmt.where(Post.is_active == is_active)

    stmt = stmt.order_by(Post.created_at.desc())
    res = session.execute(stmt)
    return res.scalars().all()


@router.get("/{slug}", response_model=PostListResponse)
async def get_post(session: db_dep, slug: str):
    stmt = select(Post).where(Post.slug.like(f"%{slug}%"))
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/create/")
async def post_create(session: db_dep, create_date: PostCreateRequest):
    post = Post(
        title=create_date.title,
        body=create_date.body,
        slug=generate_slug(create_date.title),
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post


@router.patch("/{post_id}")
async def post_update(session: db_dep, post_id: int, update_data: PostUpdateRequest):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Not found")
    if update_data.title:
        post.title = update_data.title
    if update_data.body:
        post.body = update_data.body
    post.slug = generate_slug(update_data.title)
    if update_data.category_id:
        post.category_id = update_data.category_id

    session.commit()
    session.refresh(post)

    return post


@router.delete("/{post_id}", status_code=204)
async def delet_post(session: db_dep, post_id: int):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(post)
    session.refresh(post)
    session.commit()


@router.put("/deactivate")
async def deactive(session: db_dep, post_id: int, is_active: bool = None):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.is_active = is_active
    session.commit()
    session.refresh(post)

    return post

@router.post("/set-cookie/")
def set_cookie(data: CookieData, response: Response):
    response.set_cookie(
        key=data.key,
        value=data.value,
        httponly=True,   
        max_age=60 * 60 
    )
    return {"message": "Cookie saqlandi"}


@router.get("/get-cookie/")
def get_cookie(user_token: str | None = Cookie(default=None)):
    """
    Get cookie by user token

    Args:
        user_token (str | None): User token. Defaults to None.

    Returns:
        dict: Response with user token or message that cookie is not set
    """
    if not user_token:
        return {"message": "Cookie topilmadi"}
    return {"user_token": user_token}

@router.delete("/delete-cookie/")
def delete_cookie(response: Response):
    response.delete_cookie("user_token")
    return {"message": "Cookie o‘chirildi"}