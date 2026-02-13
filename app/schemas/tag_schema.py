from pydantic import BaseModel

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
