from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class recipeSchema(BaseModel):
    title: str
    description_short: str
    description_long: str 
    create_time: Optional[datetime]
    user_id: str  

class recipeDB(recipeSchema):
    id: int
