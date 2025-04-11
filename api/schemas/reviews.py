from typing import List, Optional
from pydantic import BaseModel
from .orders import Order
from .customers import Customer

class ReviewBase(BaseModel):
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    customer_id: int
    order_id: int

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
    customer_id: Optional[int] = None
    order_id: Optional[int] = None

class Review(ReviewBase):
    id: int
    customer_id: int
    order_id: int

    class ConfigDict:
        from_attributes = True