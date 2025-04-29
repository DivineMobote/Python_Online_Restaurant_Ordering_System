from typing import List, Optional
from pydantic import BaseModel
from datetime import date

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

class RevenueReport(BaseModel):
    Date: str
    Total_Revenue: str

class Payment(PaymentBase):
    id: int
    order_id: int
    time_paid: date

    class ConfigDict:
        from_attributes = True