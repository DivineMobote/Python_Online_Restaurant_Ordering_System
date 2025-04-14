from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menuitem_id = Column(Integer, ForeignKey("menuitems.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    menuitem = relationship("MenuItem", back_populates="recipes")
    ingredient = relationship("Ingredient", back_populates="recipes")