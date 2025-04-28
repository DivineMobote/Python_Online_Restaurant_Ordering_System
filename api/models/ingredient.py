from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    recipes = relationship("Recipe", back_populates="ingredient", cascade="all, delete-orphan")
