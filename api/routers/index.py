from . import order, customer, ingredient, menu_item, payment, order_item, promo, review



def load_routes(app):
    app.include_router(order.router)
    app.include_router(customer.router)
    app.include_router(ingredient.router)
    app.include_router(menu_item.router)
    app.include_router(payment.router)
    app.include_router(order_item.router)
    app.include_router(promo.router)
    app.include_router(review.router)
