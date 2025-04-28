from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orderitem as model
from sqlalchemy.exc import SQLAlchemyError
from api.models.order import Order
# from ..schemas.menuitem import MenuItem
from api.models.menuitem import MenuItem
from api.models.recipe import Recipe
from api.models.ingredient import Ingredient


def create(db: Session, request):
    order = db.query(Order).filter(Order.id == request.order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with ID {request.order_id} not found"
        )
    menuitem = db.query(MenuItem).filter(MenuItem.id == request.menuitem_id).first()
    if not menuitem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"MenuItem with ID {request.menuitem_id} not found"
        )
    new_item = model.OrderItem(
        item=request.item,
        quantity=request.quantity,
        menuitem_id=request.menuitem_id,
        order_id=request.order_id
    )

    try:
        db.add(new_item)
        db.commit()

        recipes = db.query(Recipe).filter(Recipe.menuitem_id == menuitem.id).all()

        for recipe in recipes:
            ingredient = db.query(Ingredient).filter(Ingredient.id == recipe.ingredient_id).first()
            if not ingredient:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found!")

            required_amount = recipe.amount * new_item.quantity
            if ingredient.quantity < required_amount:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough ingredient stock.")

            ingredient.quantity -= required_amount

        db.commit()

        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.OrderItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id)
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
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
