from pydantic import BaseModel

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


