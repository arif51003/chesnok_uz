from fastapi import FastAPI
from app.router import (
    post_router,
    category_router,
    tag_router,
    user_router,
    search_router,
    whether_router,
    auth_router
    )
from app.admins.settings import admin

from app.middlewares.times import timing_middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI(
    title="Chesnokdek sassiq yangiliklar",
    description="Chesnokuz - news website inspired from Qalampir.uz, built in FastAPI",
)

app.include_router(auth_router)
app.include_router(post_router)
app.include_router(category_router)
app.include_router(tag_router)
app.include_router(user_router)
app.include_router(search_router)
app.include_router(whether_router)


admin.mount_to(app=app)

app.middleware("http")(timing_middleware)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://example.com",
#         "https://www.example.com",
#         "http://localhost:3000",
#     ],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
#     allow_headers=["Authorization", "Content-Type"],
# )

# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=[
#         "example.com",
#         "www.example.com",
#         "api.example.com",
#         "localhost",
#         "127.0.0.1",
#     ],
# )