from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class recipeSchema(BaseModel):
    title: str
    description_short: str
    description_long: str 
    create_time: Optional[datetime]


class recipeDB(recipeSchema):
    id: int