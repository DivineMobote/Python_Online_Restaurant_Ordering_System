from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .ingredient import Ingredient
from .menuitem import MenuItem

class RecipeBase(BaseModel):
    amount: int

class RecipeCreate(RecipeBase):
    menuitem_id: int
    ingredient_id: int
    pass
class RecipeUpdate(BaseModel):
    menuitem_id: Optional[int] = None
    ingredient_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    menuitem: MenuItem = None
    ingredient: Ingredient = None

    class ConfigDict:
        from_attributes = True
