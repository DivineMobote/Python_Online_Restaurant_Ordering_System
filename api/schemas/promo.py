from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
# from .orders import Order

class PromoBase(BaseModel):
    discount: float
    exp_date_DD_MM_YYYY: str
    code: str

class PromoCreate(PromoBase):
    pass

class PromoUpdate(BaseModel):
    discount: Optional[float] = None
    exp_date_DD_MM_YYYY: Optional[str] = None
    code: Optional[str] = None

class Promo(PromoBase):
    id: int
    # order_ids: List[Order]

    class ConfigDict:
        from_attributes = True