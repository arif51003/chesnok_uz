from fastapi import FastAPI
from app.router import *


app = FastAPI(
    title="Chesnokdek sassiq yangiliklar",
    description="Chesnokuz - news website inspired from Qalampir.uz, built in FastAPI",
)

app.include_router(post_router)
app.include_router(category_router)
app.include_router(tag_router)