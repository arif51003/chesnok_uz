from datetime import datetime
from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    user_id:int | None = None


class PostListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime


class PostUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None
    # is_active:bool | None = None
    
class CategoryListResonse(BaseModel):
    id:int | None = None
    name:str | None = None
    
class CategoryCreateRequest(BaseModel):
    name:str |None = None
    
class TagCreateRequest(BaseModel):
    name:str | None = None
    
class TagsResponse(BaseModel):
    id:int |None = None
    name:str |None = None
    slug:str | None = None