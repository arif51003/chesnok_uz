from fastapi import APIRouter, HTTPException, Path, Query, Response, Cookie
from sqlalchemy import select,or_
from datetime import datetime, timedelta

from app.database import db_dep
from app.models import Post, Category, PostTag, Tag, UserSearch
from app.schemas import (
    PostCreateRequest,
    PostListResponse,
    PostUpdateRequest,
    Categories,
    CookieData,
)
from app.utils import generate_slug

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/list/", response_model=list[PostListResponse])
async def get_posts(session: db_dep, item: Categories, is_active: bool = None):
    stmt = (
        select(Post)
        .join(Category, Post.category_id == Category.id)
        .where(Category.slug == item)
    )

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
        category_id=create_date.category_id,
        user_id=create_date.user_id
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
    if update_data.title is not None:
        post.title = update_data.title
        post.slug = generate_slug(update_data.title)
    if update_data.body is not None:
        post.body = update_data.body
    if update_data.category_id is not None:
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
    response.set_cookie(key=data.key, value=data.value, httponly=True, max_age=60)
    return {"message": "Cookie saqlandi"}


@router.get("/get-cookie/")
def get_cookie(user_token: str | None = Cookie(default=None)):
    if not user_token:
        return {"message": "Cookie topilmadi"}
    return {"user_token": user_token}


@router.get("/trending/", response_model=list[PostListResponse])
async def trend_post(session: db_dep):
    stmt = (
        select(Post)
        .where(Post.created_at >= (datetime.now() - timedelta(days=7)))
        .order_by(Post.likes_count.desc())
        .limit(5)
    )
    res = session.execute(stmt).scalars().all()

    return res


@router.get("/search/", response_model=list[PostListResponse])
async def search_user(session: db_dep, word: str):
    stmt = (
        select(Post)
        .join(Category, Category.id == Post.category_id)
        .join(PostTag, PostTag.post_id == Post.id)
        .join(Tag, Tag.id == PostTag.tag_id)
        .where (
            or_(
            (Post.title.like(f"%{word}%")),
            (Tag.name.like(f"%{word}%")),
            (Category.name.like(f"%{word}%"))
            )))

    res = session.execute(stmt)
    post = res.scalars().all()


    search=select(UserSearch).where(UserSearch.term==word)
    serc=session.execute(search).scalars().first()
    
    if serc:
        serc.count+=1
    else:
        serc=UserSearch(
            term=word.lower()
        )
        session.add(serc)
        
    session.commit()
    session.refresh(serc)
    
    return post
