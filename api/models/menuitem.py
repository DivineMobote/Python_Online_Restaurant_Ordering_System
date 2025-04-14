from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(300))
    price = Column(DECIMAL)
    calories = Column(Integer)
    category = Column(String(50))

    # order_items = relationship("OrderItem", back_populates="menu_item")
    # ingredients = relationship("Ingredient", back_populates="menu_item")
    orderitems = relationship("OrderItem", back_populates="menuitem", cascade="all, delete-orphan")
    recipes = relationship("Recipe", back_populates="menuitem")

