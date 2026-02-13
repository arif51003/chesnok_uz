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
