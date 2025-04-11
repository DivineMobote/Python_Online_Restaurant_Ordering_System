from typing import List, Optional
from pydantic import BaseModel
from  .orders import Order

class PaymentBase(BaseModel):
    completion_status: str
    type: str
    amount: float

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    completion_status: Optional[str] = None
    type: Optional[str] = None
    amount: Optional[float] = None
    order_id: Optional[int] = None

class Payment(PaymentBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True