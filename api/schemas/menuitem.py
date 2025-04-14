from typing import List, Optional
from pydantic import BaseModel
# from .ingredients import Ingredient
# from .order_items import OrderItem

class MenuItemBase(BaseModel):
    name: str
    price: float
    description: str
    calories: int
    category: str

class MenuItemCreate(MenuItemBase):
    # order_item_ids: List[int]
    # ingredient_ids: List[int]
    pass
class MenuItemUpdate(BaseModel):
    # order_item_ids: Optional[List[int]] = None
    # ingredient_ids: Optional[List[int]] = None
    calories: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int
    # ingredients: List[int]
    # order_item_ids: List[int]

    class ConfigDict:
        from_attributes = True