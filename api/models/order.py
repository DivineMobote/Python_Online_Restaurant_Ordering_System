from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(50))
    type = Column(String(50))
    address = Column(String(200))
    time_placed = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    promo_id = Column(Integer, ForeignKey("promos.id"), nullable=True)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="orders")
    payment = relationship("Payment", back_populates="orders")
    promo = relationship("Promo", back_populates="orders")
    reviews = relationship("Review", back_populates="orders")