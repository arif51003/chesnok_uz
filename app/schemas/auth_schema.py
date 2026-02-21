from datetime import datetime
from pydantic import BaseModel,EmailStr,model_validator
from fastapi import HTTPException
from .common import ProfessionInline

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password:str
    password2:str

    @model_validator(mode="after")
    def chek_pwd(self):
        if self.password != self.password2:
            raise ValueError(
                "Password do not match"
            )
        return self
            
class UserLoginRequest(BaseModel):
    email:EmailStr
    password:str
    
class UserProfilRequest(BaseModel):
    email:str
    password:str
    first_name:str | None = None
    last_name:str | None = None
    bio: str |None = None
    
    
class UserProfileResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None
    posts_count: int
    posts_read_count: int
    profession: ProfessionInline | None = None
    is_active: bool
    is_staff: bool
    is_superuser: bool
    is_deleted: bool
    
    
class UserRegisterResponse(BaseModel):
    email:EmailStr
    created_at: datetime
    
    
class UserProfileResponse(BaseModel):
    id: int
    email: str
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None

class RefreshTokenRequest(BaseModel):
    refresh_token: str