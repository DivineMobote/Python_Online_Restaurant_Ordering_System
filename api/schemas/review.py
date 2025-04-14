from typing import List, Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    order_id: int
    customer_id: int

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
    # order_id: Optional[int] = None

class Review(ReviewBase):
    id: int
    order_id: int
    customer_id: int

    class ConfigDict:
        from_attributes = True