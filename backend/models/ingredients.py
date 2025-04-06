from .recipe import RecipeModels
from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey
from database.config import Base


class IngredientsModels(Base):
    __tablename__ = "ingredients"
    ingredients_id = Column(INTEGER, unique=True, primary_key=True)
    recipe_id = Column(INTEGER, ForeignKey("recipe.id"), nullable=False)
    text = Column(VARCHAR)
