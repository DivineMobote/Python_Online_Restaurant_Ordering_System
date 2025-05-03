from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from api.dependencies.database import get_db
from api.schemas.search import SearchResponse, SearchResult
from api.repositories.search import search_menu_items

router = APIRouter(
    prefix="/search",
    tags=["search"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=SearchResponse)
def search(
    query: str = Query(..., min_length=1, max_length=100, description="Search query string"),
    category: Optional[str] = None,
    price_min: Optional[float] = Query(None, ge=0),
    price_max: Optional[float] = Query(None, ge=0),
    db: Session = Depends(get_db)
):
    """
    Search for menu items based on query string and optional filters
    
    Parameters:
    - query: Search query string (required)
    - category: Filter by category (optional)
    - price_min: Minimum price filter (optional)
    - price_max: Maximum price filter (optional)
    
    Returns:
    - SearchResponse containing matching menu items
    """
    # Validate price range if both are provided
    if price_min is not None and price_max is not None and price_min > price_max:
        raise HTTPException(status_code=400, detail="Minimum price cannot be greater than maximum price")
    
    # Perform search
    results = search_menu_items(db, query, category, price_min, price_max)
    
    # Convert to response model
    search_results = [
        SearchResult(
            id=item.id,
            name=item.name,
            description=item.description,
            price=item.price,
            category=item.category,
            image_url=item.image_url if hasattr(item, 'image_url') else None
        ) for item in results
    ]
    
    # Return response
    return SearchResponse(
        results=search_results,
        count=len(search_results),
        query=query
    )