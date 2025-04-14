from typing import List, Optional
from pydantic import BaseModel
from .review import Review
from .order import Order

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str
    is_guest: bool
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None

class CustomerCreate(CustomerBase):
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_guest: Optional[bool] = None
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None


class Customer(CustomerBase):
    id: int
    # last_order_id: Optional[int]
    # last_payment_id: Optional[int]
    review: Optional[Review] = None
    order: Optional[Order] = None

    class Config:
        from_attributes = True

