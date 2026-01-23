from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Post
from app.schemas import (
    PostCreateRequest,
    PostListResponse,
    PostUpdateRequest)
from app.utils import generate_slug

app=FastAPI(
    title="Chesnokdek sassiq yangiliklar",
    description="Chesnokuz - news website inspired from Qalampir.uz, built in FastAPI",
)


@app.get("/post/",response_model=list[PostListResponse])
async def get_posts(is_active: bool = None, session:Session=Depends(get_db)):
    stmt=select(Post)
    
    if is_active is not None:
        stmt=stmt.where(Post.is_active==is_active)
        
    stmt=stmt.order_by(Post.created_at.desc())
    res=session.execute(stmt)
    return res.scalars().all()

@app.get("/post/{slug}",response_model=PostListResponse)
async def get_post(slug:str,session:Session=Depends(get_db)):
    stmt=select(Post).where(Post.slug.like(f"%{slug}%"))
    res=session.execute(stmt)
    post=res.scalars().first()
    
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
        
    return post

@app.post("/post/create/")
async def post_create(create_date:PostCreateRequest,session:Session=Depends(get_db)):
    post=Post(
        title=create_date.title,
        body=create_date.body,
        slug=generate_slug(create_date.title)
    )
    
    session.add(post)
    session.commit()
    session.refresh(post)
    
    return post

@app.put("/post/{post_id}")
async def post_update(post_id:int,update_data:PostUpdateRequest,session:Session=Depends(get_db)):
    stmt=select(Post).where(Post.id==post_id)
    res=session.execute(stmt)
    post=res.scalars().first()
    
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
        
    post.title=update_data.title
    post.body=update_data.body
    post.slug=generate_slug(update_data.title)
    post.is_active=update_data.is_active
    
    session.commit()
    session.refresh(post)
    
    return post

@app.delete("/post/{post_id}")
async def delet_post(post_id:int,session:Session=Depends(get_db)):
    stmt=select(Post).where(post_id==Post.id)
    res=session.execute(stmt)
    post=res.scalars().first()
    
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
        
    del post
    session.commit()
    session.refresh(post)

@app.put("/post/{post_id}")
async def deactive(post_id:int,session:Session=Depends(get_db)):
    stmt=select(Post).where(Post.id==post_id)
    res=session.execute(stmt)
    post=res.scalars().first()
    
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
        
    