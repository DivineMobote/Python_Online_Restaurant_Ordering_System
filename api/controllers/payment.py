from string import printable

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends

import api.models.order
from ..models import payment as model
from sqlalchemy.exc import SQLAlchemyError
from api.models.order import Order
from api.models.orderitem import OrderItem
from api.models.menuitem import MenuItem
from datetime import date
from api.models.promo import Promo
from typing import Optional


def create(db: Session, request):
    if request.order_id is not None:
        order = db.query(Order).filter(Order.id == request.order_id).first()
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order with ID {request.Order_id} not found"
            )

        total_cost = 0
        orderitems = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()

        for orderitem in orderitems:
            menuitem = db.query(MenuItem).filter(MenuItem.id == orderitem.menuitem_id).first()
            if menuitem:
                total_cost += menuitem.price * orderitem.quantity
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Menu item with ID {orderitem.menuitem_id} not found"
                )

        total_cost = 0
        for orderitem in order.orderitems:
            menuitem = db.query(MenuItem).filter(
                MenuItem.id == orderitem.menuitem_id).first()
            if menuitem:
                total_cost += menuitem.price * orderitem.quantity
        if order.promo_id:
            promo = db.query(Promo).filter(Promo.id == order.promo_id).first()
            if promo:
                today = date.today()
                if promo.exp_date_YYYY_MM_DD >= today:
                    print(f"Promo discount amount: {promo.discount}")
                    total_cost -= promo.discount
                    if total_cost < 0:
                        total_cost = 0
                    print(f"Total cost after promo: {total_cost}")
                else:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Promo code expired"
                    )
        if float(request.amount) != float(total_cost):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Payment amount does not match the order total"
            )

        valid_payment_types = ["Cash", "Card"]
        if request.type not in valid_payment_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid payment type '{request.type}'. Must be 'Cash' or 'Card'."
            )

        order.status = "Complete"
        db.commit()
        db.refresh(order)
    new_item = model.Payment(
        completion_status="Complete",
        type=request.type,
        amount=total_cost,
        order_id=request.order_id
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
        result = db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id)
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
        item = db.query(model.Payment).filter(model.Payment.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_revenue_by_date(db: Session, search_date: Optional[date] = None):
    try:

        payments = db.query(model.Payment).filter(
            model.Payment.time_paid == search_date
        ).all()
        total_revenue = sum(payment.amount for payment in payments)
        printable_revenue = f"${total_revenue:,.2f}"
        if not search_date:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Please enter a valid date(YYYY-MM-DD)!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return {
        "Date": search_date.isoformat(),
        "Total_Revenue": printable_revenue
    }