from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    discount = Column(DECIMAL)
    exp_date_DD_MM_YYYY = Column(String(10))
    code = Column(String(50))

    orders = relationship("Order", back_populates="promo", cascade="all, delete-orphan")
