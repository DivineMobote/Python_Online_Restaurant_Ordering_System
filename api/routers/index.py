from . import customer, menuitem, payment, promo, review, ingredient, orderitem, order, recipe, search

def load_routes(app):
    app.include_router(customer.router)
    app.include_router(menuitem.router)
    app.include_router(payment.router)
    app.include_router(promo.router)
    app.include_router(review.router)
    app.include_router(ingredient.router)
    app.include_router(orderitem.router)
    app.include_router(order.router)
    app.include_router(recipe.router)
    app.include_router(search.router)
