from typing import Optional
from pydantic import BaseModel
# from .menu_items import MenuItem


class OrderItemBase(BaseModel):
    item: str
    quantity: int


class OrderItemCreate(OrderItemBase):
    order_id: int
    menuitem_id: int

class OrderItemUpdate(BaseModel):
    # order_id: Optional[int] = None
    # menu_item_id: Optional[int] = None
    quantity: Optional[int] = None
    item: Optional[str] = None

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    menuitem_id: int
    # menu_item: MenuItem = None

    class ConfigDict:
        from_attributes = True