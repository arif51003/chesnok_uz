
from sqlalchemy.orm import mapped_column,Mapped,session
from sqlalchemy import Integer, Boolean,String,DateTime,func
from app.db import Base

class BaseID(Base):
    id : Mapped[int]= mapped_column(Integer,primary_key=True,autoincrement=True)
class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

class User(BaseID,TimestampMixin):
    __tablename__="users"
    
    username: Mapped[str]=mapped_column(String(50),unique=True,nullable=False)
    email : Mapped[str] = mapped_column(String,unique=True,nullable=False)
    password : Mapped[str] = mapped_column(String,nullable=False)
    is_active : Mapped[bool] = mapped_column(Boolean,default=True)
    
    first_name : Mapped[str] = mapped_column()
    
    