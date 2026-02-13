from datetime import datetime
from pydantic import BaseModel
from enum import Enum






class UserSearchResponse(BaseModel):
    term:str | None = None
    
    
class WhetherResponse(BaseModel):
    pass 

class WhetherChoise(str,Enum):
    CURRENT="CURRENT"
    DAY="DAYLY"
    WEEK="WEEKLY"
    
class CityChoise(str,Enum):
    TASHKENT="Tashkent"
    ASHGABAT="ASHGABAT"
    DUSHANBE="DUSHANBE"
    BISHKEK="BISHKEK"
    ALMATY="ALMATY"
    BERLIN="BERLIN"
    PARIS="PARIS"
    LONDON="LONDON"
    