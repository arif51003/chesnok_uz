from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class PostCreateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    user_id: int | None = None
    category_id : int | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "EXAMPLE",
                    "body": "Example bo'gannan kiyn bodysi nimayam bo'sin",
                    "user_id": 9,
                    "category_id":4
                }
            ]
        }
    }


class PostListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 5,
                    "title": "Chesnok-sarimsoq emas",
                    "slug": "chesnok--sarimsoq-emas",
                    "is_active": "true",
                    "created_at": "2026-01-09T13-23-54.000Z",
                }
            ]
        }
    }


class PostUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    category_id: int | None = None
    # is_active:bool | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "O'sha mavzu",
                    "body": "O'sha mavzu haqida ancha muncha unaqa bunaqa narsalar aytish mumkun ",
                    "category_id": 3,
                }
            ]
        }
    }

class Categories(str, Enum):
    TECHNOLOGY = "texnologiya"
    MEDICINA = "tibbiyot"
    EDUCATION = "talim"
    BUISSNESS = "biznes"
    SINCE = "ilm"
    PSIXOLOGY = "psixologiya"
    SPORT = "sport"
    CULTURE = "madaniyat"
    IT = "it"


class CookieData(BaseModel):
    key: str
    value: str
