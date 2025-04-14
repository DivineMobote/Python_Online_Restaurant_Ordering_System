from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderItem(Base):
    __tablename__ = "orderitems"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(50))
    quantity = Column(Integer)

    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="orderitems")
    menuitem_id = Column(Integer, ForeignKey("menuitems.id"))
    menuitem = relationship("MenuItem", back_populates="orderitems")