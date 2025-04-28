from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean, Float
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    discount = Column(Integer)
    exp_date_YYYY_MM_DD = Column(Date)
    code = Column(String(50))

    orders = relationship("Order", back_populates="promo", cascade="all, delete-orphan")

