from typing import List, Optional
from pydantic import BaseModel
from .review import Review
# from .orders import Order

class CustomerBase(BaseModel):
    # id: int
    name: str
    phone: str
    address: str
    is_guest: bool
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None
    # order_ids: Optional[List[int]] = None

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
    # order_ids: List[int]
    review: Optional[Review] = None
    class Config:
        from_attributes = True

