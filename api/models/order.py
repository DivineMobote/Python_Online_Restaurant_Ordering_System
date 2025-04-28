from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(50), default="pending")
    type = Column(String(50))
    time_placed = Column(DATETIME, default=date.today)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="orders")
    review = relationship("Review", back_populates="order", uselist=False)
    promo_id = Column(Integer, ForeignKey("promos.id"), nullable=True)
    promo = relationship("Promo", back_populates="orders")
    payments = relationship("Payment", back_populates="order", uselist=False)
    orderitems = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
