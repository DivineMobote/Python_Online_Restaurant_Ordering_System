from typing import List, Optional
from pydantic import BaseModel
# from .menu_items import MenuItem


class IngredientBase(BaseModel):
    name: str
    quantity: int


class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True