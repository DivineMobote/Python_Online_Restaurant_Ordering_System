from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    status: str
    type: str
    address: str
    time_placed: Optional[datetime] = None

class OrderCreate(OrderBase):
    customer_id: int
    promo_id: Optional[int] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    type: Optional[str] = None
    address: Optional[str] = None
    time_placed: Optional[datetime] = None
    customer_id: Optional[int] = None
    promo_id: Optional[int] = None

class Order(OrderBase):
    id: int
    customer_id: int
    promo_id: Optional[int]

    class ConfigDict:
        from_attributes = True
