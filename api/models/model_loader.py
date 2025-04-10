from . import order, customer, ingredient, menu_item, payment, order_item, promo, review

from ..dependencies.database import engine


def index():
    order.Base.metadata.create_all(engine)
    order_item.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    promo.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
