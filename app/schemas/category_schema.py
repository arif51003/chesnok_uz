from pydantic import BaseModel
from enum import Enum

class CategoryListResonse(BaseModel):
    id: int | None = None
    name: str | None = None

    model_config = {"json_schema_extra": {"examples": [{"id": 4, "name": "Health"}]}}


class CategoryCreateRequest(BaseModel):
    name: str | None = None

    model_config = {"json_schema_extra": {"examples": [{"name": "Animals"}]}}


