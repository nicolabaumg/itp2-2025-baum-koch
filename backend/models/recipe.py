from datetime import datetime
from sqlalchemy import Column, VARCHAR, DateTime, INTEGER
from database.config import Base


class RecipeModels(Base):
    __tablename__ = "recipe"
    id = Column(INTEGER, unique=True, primary_key=True)
    title = Column(VARCHAR)
    description_short = Column(VARCHAR)
    description_long = Column(VARCHAR)
    create_time = Column(DateTime, default=datetime.now())

  
