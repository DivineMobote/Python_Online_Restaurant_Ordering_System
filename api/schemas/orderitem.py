from typing import Optional
from pydantic import BaseModel


class OrderItemBase(BaseModel):
    item: str
    quantity: int


class OrderItemCreate(OrderItemBase):
    order_id: int
    menuitem_id: int

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    item: Optional[str] = None

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    menuitem_id: int

    class ConfigDict:
        from_attributes = True