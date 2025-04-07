from datetime import datetime
from sqlalchemy import Column, VARCHAR, DateTime, INTEGER, ForeignKey
from database.config import Base

class RecipeModels(Base):
    __tablename__ = "recipe"
    id = Column(INTEGER, unique=True, primary_key=True, autoincrement=True)
    title = Column(VARCHAR)
    description_short = Column(VARCHAR)
    description_long = Column(VARCHAR)
    create_time = Column(DateTime, default=datetime.utcnow())
    user_id = Column(VARCHAR, ForeignKey("users.username"), nullable=False)  # Fremdschlüssel

    def __init__(self, title: str, description_short: str, description_long: str, user_id: str):
        self.title = title
        self.description_short = description_short
        self.description_long = description_long
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"<RecipeModels(id={self.id}, title={self.title}, user_id={self.user_id})>"
