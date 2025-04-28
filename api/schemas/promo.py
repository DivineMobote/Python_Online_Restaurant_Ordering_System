from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from .order import Order
from sqlalchemy import Date

class PromoBase(BaseModel):
    discount: int
    exp_date_YYYY_MM_DD: date
    code: str

class PromoCreate(PromoBase):
    pass

class PromoUpdate(BaseModel):
    discount: Optional[int] = None
    exp_date_YYYY_MM_DD: Optional[date] = None
    code: Optional[str] = None

class Promo(PromoBase):
    id: int
    order: Optional[Order] = None
    class ConfigDict:
        from_attributes = True