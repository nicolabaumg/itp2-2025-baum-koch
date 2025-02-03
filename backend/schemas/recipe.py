from pydantic import BaseModel
from typing import Optional, List

class ingredientsSchema(BaseModel):
    text: str

class stepsSchema(BaseModel):
    text: str

class recipeSchema(BaseModel):
    title: str
    description: Optional[str]
    ingredients: List[ingredientsSchema]
    steps: List[stepsSchema]

class recipeDB(RecipeSchema):
    id: int