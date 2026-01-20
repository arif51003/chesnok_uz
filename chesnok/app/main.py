import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.config import project_name

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info(f"{project_name} ishladi")
    yield
    logger.info(f"{project_name} finished")
    
app=FastAPI(
    title=project_name,
    lifespan=lifespan()
)