from datetime import datetime
from sqlalchemy import Column, VARCHAR, DateTime
from database.config import Base


class RecipeModels(Base):
    __tablename__ = "recipe"
    title = Column(VARCHAR)
    description = Column(VARCHAR)
    create_time = Column(DateTime, default=datetime.utcnow())
