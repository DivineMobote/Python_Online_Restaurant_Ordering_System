from . import order, customer, ingredient, menuitem, payment, orderitem, promo, review, recipe

from ..dependencies.database import engine


def index():
    order.Base.metadata.create_all(engine)
    orderitem.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    menuitem.Base.metadata.create_all(engine)
    promo.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    recipe.Base.metadata.create_all(engine)
