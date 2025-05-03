from typing import Optional, List
from pydantic import BaseModel, Field

class SearchQuery(BaseModel):
    query: str = Field(..., min_length=1, max_length=100, description="Search query string")
    category: Optional[str] = Field(None, description="Category to search within")
    price_min: Optional[float] = Field(None, ge=0, description="Minimum price for filtering")
    price_max: Optional[float] = Field(None, ge=0, description="Maximum price for filtering")
    
    class Config:
        from_attributes = True

class SearchResult(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    
    class Config:
        from_attributes = True

class SearchResponse(BaseModel):
    results: List[SearchResult]
    count: int
    query: str