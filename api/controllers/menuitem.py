from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menuitem as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.MenuItem(
    name=request.name,
    description = request.description,
    price = request.price,
    calories = request.calories,
    category = request.category,
    vegetarian=request.vegetarian,
    vegan=request.vegan ,
    gluten_free=request.gluten_free
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
        result = db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
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
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def filter_by_category(
        db: Session,
        vegetarian: bool = None,
        vegan: bool = None,
        gluten_free: bool = None,
        category: str = None
):
    try:
        query = db.query(model.MenuItem)

        if vegetarian is not None:
            query = query.filter(model.MenuItem.vegetarian == vegetarian)
        if vegan is not None:
            query = query.filter(model.MenuItem.vegan == vegan)
        if gluten_free is not None:
            query = query.filter(model.MenuItem.gluten_free == gluten_free)
        if category:
            query = query.filter(model.MenuItem.category == category)

        result = query.all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result