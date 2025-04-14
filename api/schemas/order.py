from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .review import Review

class OrderBase(BaseModel):
    status: str
    type: str
    time_placed_DD_MM_YYYY: str

class OrderCreate(OrderBase):
    # customer_id: int
    promo_id: Optional[int] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    type: Optional[str] = None
    time_placed_DD_MM_YYYY: Optional[str] = None
    # customer_id: Optional[int] = None
    promo_id: Optional[int] = None

class Order(OrderBase):
    id: int
    # customer_id: int
    promo_id: Optional[int] = None
    review: Optional[Review] = None
    class ConfigDict:
        from_attributes = True
