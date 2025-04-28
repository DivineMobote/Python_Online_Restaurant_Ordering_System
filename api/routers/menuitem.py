from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import menuitem as controller
from ..schemas import menuitem as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu_items"
)

@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/filter", response_model=list[schema.MenuItem])
def filter_items(
    db: Session = Depends(get_db),
    vegetarian: bool| None = None,
    vegan: bool| None = None,
    gluten_free: bool | None = None,
    category: str | None = None
):
    return controller.filter_by_category(db, vegetarian, vegan, gluten_free, category)

@router.get("/{item_id}", response_model=schema.MenuItem)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.MenuItem)
def update(item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
