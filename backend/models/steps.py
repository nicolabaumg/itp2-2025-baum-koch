from .recipe import RecipeModels
from sqlalchemy import Column, VARCHAR, DATE, DateTime, INTEGER, ForeignKey
from database.config import Base


class StepsModels(Base):
    __tablename__ = "steps"
    steps_id = Column(INTEGER, unique=True, primary_key=True)
    recipe_id = Column(INTEGER, ForeignKey("recipe.id"), nullable=False)
    text = Column(VARCHAR)
