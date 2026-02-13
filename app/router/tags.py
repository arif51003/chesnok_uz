from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import db_dep
from app.models import Tag
from app.schemas.tag_schema import *
from app.utils import generate_slug

router = APIRouter(prefix="/tag", tags=["Tags"])


@router.post("/create")
async def create_tag(session: db_dep, data: TagCreateRequest):
    tag = Tag(name=data.name, slug=generate_slug(data.name))
    session.add(tag)
    session.commit()
    session.refresh(tag)

    return tag


@router.get("/list", response_model=list[TagsResponse])
async def get_list(session: db_dep):
    stmt = select(Tag)
    res = session.execute(stmt)
    tags = res.scalars().all()
    if not tags:
        raise HTTPException(status_code=404, detail="EMPTY")
    return tags


@router.put("/")
async def update(session: db_dep, tag_id, update: TagCreateRequest):
    stmt = select(Tag).where(Tag.id == tag_id)
    res = session.execute(stmt)
    tag = res.scalars().first()

    if not tag:
        raise HTTPException(status_code=404, detail="NOT FOUND!")
    tag.name = update.name
    tag.slug = generate_slug(update.name)

    session.commit()
    session.refresh(tag)
    return tag


@router.delete("{tag_id}", status_code=204)
async def tag_delete(session: db_dep, tag_id: int):
    stmt = select(Tag).where(Tag.id == tag_id)
    res = session.execute(stmt)
    tag = res.scalars().first()

    if not tag:
        raise HTTPException(status_code=404, detail="NOT FOUND")

    session.delete(tag)
    session.refresh(tag)
    session.commit()
