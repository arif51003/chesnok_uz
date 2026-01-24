from .posts import router as post_router
from .categories import router as category_router
from .tags import router as tag_router

__all = [post_router,category_router,tag_router]
