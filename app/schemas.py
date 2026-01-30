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


class CategoryListResonse(BaseModel):
    id: int | None = None
    name: str | None = None

    model_config = {"json_schema_extra": {"examples": [{"id": 4, "name": "Health"}]}}


class CategoryCreateRequest(BaseModel):
    name: str | None = None

    model_config = {"json_schema_extra": {"examples": [{"name": "Animals"}]}}


class TagCreateRequest(BaseModel):
    name: str | None = None

    model_config = {"json_schema_extra": {"examples": [{"name": "Tramp"}]}}


class TagsResponse(BaseModel):
    id: int | None = None
    name: str | None = None
    slug: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [{"id": 77, "name": "Elon Mask", "slug": "elon-mask"}]
        }
    }


class UserCreateRequest(BaseModel):
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None
    profession_id: int | None = None
    is_staff: bool | None = False
    is_superuser: bool | None = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "example@github.net",
                    "password": "44drfw423de5",
                    "first_name": "Arifbek",
                    "last_name": "Masharipov",
                    "bio": "Men dasturchi bo'lishni yoshligimdan xohlaganman",
                    "profession_id": 5,
                    "is_staff": "true",
                    "is_superuser": "false",
                }
            ]
        }
    }


class UserListResponse(BaseModel):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    email: str
    bio: str | None = None
    is_staff: bool | None = False
    is_superuser: bool | None = False
    is_active: bool | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 69,
                    "first_name": "Asror",
                    "last_name": "Baxrornov",
                    "email": "asror@gmail.com",
                    "bio": "Buncha maladesman",
                    "is_staff": "false",
                    "is_superuser": "false",
                    "is_active": "true",
                }
            ]
        }
    }


class UserUpdateRequest(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str
    password: str
    bio: str | None = None
    profession_id: int | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Arifbek",
                    "last_name": "Masharipov",
                    "email": "example@github.net",
                    "password": "44drfw423de5",
                    "bio": "Men dasturchi bo'lishni yoshligimdan xohlaganman",
                    "profession_id": 5,
                    "is_staff": "true",
                    "is_superuser": "false",
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
