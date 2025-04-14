from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from .orderitem import OrderItem
from .review import Review
from .payment import Payment

class OrderBase(BaseModel):
    status: str
    type: str
    time_placed_DD_MM_YYYY: str

class OrderCreate(OrderBase):
    promo_id: Optional[int] = None
    customer_id: int
class OrderUpdate(BaseModel):
    status: Optional[str] = None
    type: Optional[str] = None
    time_placed_DD_MM_YYYY: Optional[str] = None
    promo_id: Optional[int] = None

class Order(OrderBase):
    id: int
    promo_id: Optional[int] = None
    review: Optional[Review] = None
    customer_id: int
    orderitem: Optional[OrderItem] = None

    payment: Optional[Payment] = None
    class ConfigDict:
        from_attributes = True
