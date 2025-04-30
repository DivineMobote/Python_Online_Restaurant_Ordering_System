from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promo as model
from sqlalchemy.exc import SQLAlchemyError
from datetime import date


def create(db: Session, request):
    new_item = model.Promo(
        discount=request.discount,
        code=request.code,
        exp_date_YYYY_MM_DD=request.exp_date_YYYY_MM_DD if hasattr(request, 'exp_date_YYYY_MM_DD') else None
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
        result = db.query(model.Promo).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Promo).filter(model.Promo.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Promo).filter(model.Promo.id == item_id)
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
        item = db.query(model.Promo).filter(model.Promo.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def apply_promo_code(db: Session, code: str):
    promo = db.query(model.Promo).filter(model.Promo.code == code).first()

    if not promo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promo code not found."
        )

    if promo.exp_date_YYYY_MM_DD and promo.exp_date_YYYY_MM_DD < date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Promo code expired."
        )

    return promo