from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db
from datetime import date
from typing import Optional

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/revenue-by-date/", response_model=schema.RevenueReport)
def get_revenue_by_date(
    search_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return controller.get_revenue_by_date(db, search_date=search_date)

@router.get("/{item_id}", response_model=schema.Payment)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Payment)
def update(item_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
