from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order as model
from sqlalchemy.exc import SQLAlchemyError
from api.models.promo import Promo
from api.models.customer import Customer
from datetime import date
from typing import Optional


def create(db: Session, request):
    customer = db.query(Customer).filter(Customer.id == request.customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with ID {request.customer_id} not found"
        )
    if request.promo_id is not None:
        promo = db.query(Promo).filter(Promo.id == request.promo_id).first()
        if not promo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Promo with ID {request.promo_id} not found"
            )
    new_item = model.Order(
        status="Pending",
        type=request.type,
        customer_id=request.customer_id,
        promo_id = request.promo_id if hasattr(request, 'promo_id') else None
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_by_date_range(
    db: Session,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    query = db.query(model.Order)
    if start_date:
        query = query.filter(model.Order.time_placed >= start_date)
    if end_date:
        query = query.filter(model.Order.time_placed <= end_date)
    return query.all()


def filter_by_type(db: Session, order_type: str):
    order_type = order_type.capitalize()
    valid_types = ["Takeout", "Delivery"]
    if order_type not in valid_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order type. Must be 'Takeout' or 'Delivery'."
        )

    return db.query(model.Order).filter(model.Order.type == order_type).all()

