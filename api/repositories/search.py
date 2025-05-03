from sqlalchemy.orm import Session
from sqlalchemy import or_
from api.models.menuitem import MenuItem
from api.models.ingredient import Ingredient
from api.models.recipe import Recipe
from typing import List, Optional

def search_menu_items(
    db: Session, 
    query: str, 
    category: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None
) -> List[MenuItem]:
    """
    Search for menu items based on query string and optional filters
    
    Args:
        db: Database session
        query: Search query string
        category: Optional category filter
        price_min: Optional minimum price filter
        price_max: Optional maximum price filter
        
    Returns:
        List of MenuItem objects matching the search criteria
    """
    # Convert query to lowercase for case-insensitive search
    search_query = f"%{query.lower()}%"
    
    # Build a query that searches in both menu items and their ingredients
    base_query = db.query(MenuItem).distinct().filter(
        or_(
            MenuItem.name.ilike(search_query),
            MenuItem.description.ilike(search_query),
            # Join to search in ingredients
            MenuItem.id.in_(
                db.query(Recipe.menuitem_id)
                .join(Ingredient, Recipe.ingredient_id == Ingredient.id)
                .filter(Ingredient.name.ilike(search_query))
                .subquery()
            )
        )
    )
    
    # Apply category filter if provided
    if category:
        base_query = base_query.filter(MenuItem.category.ilike(f"%{category.lower()}%"))
    
    # Apply price filters if provided
    if price_min is not None:
        base_query = base_query.filter(MenuItem.price >= price_min)
    
    if price_max is not None:
        base_query = base_query.filter(MenuItem.price <= price_max)
    
    # Return results
    return base_query.all()