from .posts import router as post_router
from .categories import router as category_router
from .tags import router as tag_router
from .users import router as user_router

__all = [user_router, post_router, category_router, tag_router]
