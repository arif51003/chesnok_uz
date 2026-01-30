from datetime import datetime
from sqlalchemy import String, Boolean, func, DateTime, ForeignKey, Text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


class User(BaseModel):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    avatar_id: Mapped[int] = mapped_column(
        ForeignKey("media.id", ondelete="SET NULL"), nullable=True
    )
    profession_id: Mapped[int] = mapped_column(
        ForeignKey("profession.id"), nullable=True
    )
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    post_count: Mapped[int] = mapped_column(BigInteger, default=0)
    post_read_count: Mapped[int] = mapped_column(BigInteger, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    posts: Mapped[list["Post"]] = relationship(
        "Post", back_populates="user", cascade="all,delete-orphan", passive_deletes=True
    )
    kasb: Mapped["Profession"] = relationship("Profession", back_populates="user")
    comments: Mapped[list["Comment"]] = relationship(
        "Comment", back_populates="user", passive_deletes=True
    )
    avatar: Mapped["Media"] = relationship("Media", foreign_keys=[avatar_id])

    def __repr__(self):
        return f"User:{self.first_name} {self.last_name}"


class Post(BaseModel):
    __tablename__ = "post"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="cascade"))
    title: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=True)
    views_count: Mapped[int] = mapped_column(BigInteger, default=0)
    likes_count: Mapped[int] = mapped_column(BigInteger, default=0)
    comments_count: Mapped[int] = mapped_column(BigInteger, default=0)
    mins_read: Mapped[int] = mapped_column(BigInteger, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
    category: Mapped["Category"] = relationship("Category", back_populates="post")
    postmedia: Mapped[list["PostMedia"]] = relationship(
        "PostMedia", back_populates="post"
    )
    tagpost: Mapped[list["PostTag"]] = relationship("PostTag", back_populates="post")

    def __repr__(self):
        return f"Post:{self.title}"


class Comment(BaseModel):
    __tablename__ = "comment"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="cascade"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="cascade"))

    text: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    post: Mapped["Post"] = relationship("Post", back_populates="comments")
    user: Mapped["User"] = relationship("User", back_populates="comments")

    def __repr__(self):
        return f"Comment:{self.text}"


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(100), unique=True)

    post: Mapped[list["Post"]] = relationship("Post", back_populates="category")

    def __repr__(self):
        return f"Category:{self.name}"


class Profession(Base):
    __tablename__ = "profession"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    user: Mapped[list["User"]] = relationship("User", back_populates="kasb")

    def __repr__(self):
        return f"Profession:{self.name}"


class Tag(Base):
    __tablename__ = "tag"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String(100), unique=True)

    tagpost: Mapped[list["PostTag"]] = relationship("PostTag", back_populates="tag")

    def __repr__(self):
        return f"Tag:{self.name}"


class Media(Base):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    url: Mapped[str] = mapped_column(String(100))

    postmedia: Mapped[list["PostMedia"]] = relationship(
        "PostMedia", back_populates="media"
    )
    user: Mapped["User"] = relationship("User", back_populates="avatar")

    def __repr__(self):
        return f"Media:{self.url}"


class PostMedia(Base):
    __tablename__ = "postmedia"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    media: Mapped["Media"] = relationship("Media", back_populates="postmedia")
    post: Mapped["Post"] = relationship("Post", back_populates="postmedia")

    def __repr__(self):
        return f"PostMedia: {self.post_id}-{self.media_id}"


class PostTag(Base):
    __tablename__ = "postag"
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)

    tag: Mapped["Tag"] = relationship("Tag", back_populates="tagpost")
    post: Mapped["Post"] = relationship("Post", back_populates="tagpost")


class UserSearch(Base):
    __tablename__ = "user_search"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    term: Mapped[str] = mapped_column(String(50))
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    count: Mapped[int] = mapped_column(BigInteger, default=1)


class Devices(Base):
    __tablename__ = "device"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_agent: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    last_active: Mapped[datetime] = mapped_column()

    likes: Mapped[list["Likes"]] = relationship("Likes", back_populates="device")


class Likes(Base):
    __tablename__ = "likes"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    device_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("device.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )

    device: Mapped["Devices"] = relationship("Devices", back_populates="likes")
