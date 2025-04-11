from typing import List, Optional
from pydantic import BaseModel
from .reviews import Review
from .orders import Order

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str
    is_guest: bool = False


class CustomerCreate(CustomerBase):
    last_order_id: Optional[int] = None
    last_payment_id: Optional[int] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_guest: Optional[bool] = None
    last_order_id: Optional[int] = None
    last_payment_id: Optional[int] = None


class Customer(CustomerBase):
    id: int
    last_order_id: Optional[int]
    last_payment_id: Optional[int]
    review_ids: List[Review]
    order_ids: List[Order]

    class ConfigDict:
        from_attributes = True
