from datetime import datetime
from sqlalchemy import Integer,String, Boolean,func,DateTime,ForeignKey,Text
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base

class BaseModel(Base):
    __abstract__=True
    
    id:Mapped[int]= mapped_column(Integer,primary_key=True)
    created_at:Mapped[datetime]= mapped_column(DateTime(timezone=True),default=func.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),default=func.now(),onupdate=func.now())
    
class Media(Base):
    __tablename__="media"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    url: Mapped[str] = mapped_column(String(100))
    
    
class PostMedia(Base):
    __tablename__='postmedia'
    
    post_id : Mapped[int] = mapped_column(ForeignKey('post.id'),primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey('media.id'))
    
    def __repr__(self):
        return f"PostMedia: {self.post_id}-{self.media_id}"
    
class Post(BaseModel):
    __tablename__='post'
    
    title : Mapped[str] = mapped_column(String(255))
    slug : Mapped[str] = mapped_column(String(100),unique=True)
    body : Mapped[str] = mapped_column(Text)
    is_active : Mapped[bool]= mapped_column(Boolean,default=True)
    
    def __repr__(self):
        return {self.title}
    