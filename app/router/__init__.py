from .posts import router as post_router
from .categories import router as category_router
from .tags import router as tag_router
from .users import router as user_router
from .usersearch import router as search_router
from .whether import router as whether_router
from .auth import router as auth_router
__all = [user_router, 
         post_router, 
         category_router, 
         tag_router,
         search_router,
         whether_router,
         auth_router]
