from . import customers, menu_items, payments, promos, reviews, ingredients, order_items, orders, order_details

def load_routes(app):
    app.include_router(customers.router)
    app.include_router(menu_items.router)
    app.include_router(payments.router)
    app.include_router(promos.router)
    app.include_router(reviews.router)
    app.include_router(ingredients.router)
    app.include_router(order_items.router)
    app.include_router(orders.router)
    app.include_router(order_details.router)
