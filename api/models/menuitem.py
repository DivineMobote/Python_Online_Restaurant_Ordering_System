from sqlalchemy import Column, Integer, String, DECIMAL,Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)
    vegetarian = Column(Boolean, default=False)
    vegan = Column(Boolean, default=False)
    gluten_free = Column(Boolean, default=False)

    recipes = relationship("Recipe", back_populates="menuitem", cascade="all, delete-orphan")
    orderitems = relationship("OrderItem", back_populates="menuitem", cascade="all, delete-orphan")
