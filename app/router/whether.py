import os
import httpx

from fastapi import APIRouter
from dotenv import load_dotenv
from app.schemas.schemas import WhetherChoise,WhetherResponse,CityChoise

load_dotenv()

router=APIRouter(
    prefix="/Whether",
    tags=[
        "Whether"
    ]
)

KEY=os.getenv("API_KEY")
URL="http://api.weatherapi.com/v1"

@router.get("/")
async def get_whether(city:CityChoise,choise:WhetherChoise):
    async with httpx.AsyncClient() as client:

        if choise == WhetherChoise.CURRENT:
            resp = await client.get(
                    url= f"{URL}/current.json?key={KEY}&q={city.value}"
                )
        
        elif choise == WhetherChoise.DAY:
            resp = await client.get(
                    url= f"{URL}/forecast.json?key={KEY}&q={city.value}"
                ) 
             
        else:
            resp = await client.get(
                    url= f"{URL}/forecast.json?key={KEY}&q={city.value}&days=7"
            )
            
    return resp.json()

