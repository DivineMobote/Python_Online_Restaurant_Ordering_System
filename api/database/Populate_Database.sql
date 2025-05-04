-- populate db

USE sandwich_maker_api;

-- INGREDIENTS
INSERT INTO ingredients (name, quantity)
VALUES
('Bread', 100),
('Bacon', 100),
('Ham', 100),
('Lettuce', 100),
('Tomato', 100),
('Cheese', 100),
('Ketchup', 100),
('Drink', 100),
('Mayo', 100),
('Turkey', 100),
('Potatoes', 100);

-- MENU ITEMS
INSERT INTO menuitems (name, description, price, calories, category,vegetarian, vegan, gluten_free)
VALUES
('BLT', 'Bacon, Lettuce, Tomato Sandwich', 10.00, 200, 'Sandwich',False,False,False),
('Everything Sandwich', 'All Our Ingredients Under One Bun', 15.00, 400, 'Sandwich',False,False,False),
('Fries', 'French Fries', 3.00, 200, 'Sides',True,True,False),
('Drink', 'Pepsi and Coke Products', 2.50, 100, 'Drinks',True,True,True);

-- RECIPES
-- BLT
INSERT INTO recipes (menuitem_id, ingredient_id, amount)
VALUES
(1, 1, 2),  -- Bread
(1, 2, 3),  -- Bacon
(1, 4, 1),  -- Lettuce
(1, 5, 1);  -- Tomato

-- Everything Sandwich
INSERT INTO recipes (menuitem_id, ingredient_id, amount)
VALUES
(2, 1, 2),  -- Bread
(2, 2, 2),  -- Bacon
(2, 3, 2),  -- Ham
(2, 4, 1),  -- Lettuce
(2, 5, 1),  -- Tomato
(2, 6, 2),  -- Cheese
(2, 7, 1),  -- Ketchup
(2, 9, 1),  -- Mayo
(2, 10, 2); -- Turkey

-- Fries
INSERT INTO recipes (menuitem_id, ingredient_id, amount)
VALUES
(3, 11, 2), -- Potatoes
(3, 7, 1); -- Ketchup

-- Drink
INSERT INTO recipes (menuitem_id, ingredient_id, amount)
VALUES
(4, 8, 1); -- Drink

-- CUSTOMERS
INSERT INTO customers (name, phone, address, is_guest)
VALUES
('John Doe', '7041111111', '1111 Road Rd Charlotte, NC', FALSE),
('Jane Smith', '8282222222', '2222 Street Str Charlotte, NC', FALSE),
('Brad Guest', '55555555555', '2222 Street Str Charlotte, NC', TRUE); -- Guest

-- ORDERS
INSERT INTO orders (status, type, time_placed, customer_id)
VALUES
('Complete', 'Takeout', '2025-04-25', 1),
('Pending', 'Takeout', '2025-04-25', 2),
('Complete', 'Delivery', '2025-04-28', 3);

-- ORDER ITEMS
INSERT INTO orderitems (item, quantity, order_id, menuitem_id)
VALUES
('BLT', 2, 1, 1),  -- 2 BLTs for order 1
('Everything Sandwich', 1, 2, 2),  -- 1 Everything Sandwich for order 2
('Fries', 3, 3, 3);  -- 3 Fries for order 3

-- PAYMENTS
INSERT INTO payments (completion_status, type, amount, order_id,time_paid)
VALUES
('Complete', 'Card', 30.00, 1,'2025-04-25'),  -- Payment for order 1
('Pending', 'Cash', 15.00, 2,'2025-04-25'),  -- Payment for order 2
('Complete', 'Card', 9.00, 3,'2025-04-25');  -- Payment for order 3

-- PROMOS
INSERT INTO promos (discount, exp_date_YYYY_MM_DD, code)
VALUES
(7, '2024-12-31', '2024SALE'),
(5, '2025-05-31', 'SPRINGSALE'),
(3, '2025-08-31', 'SUMMERSALE');

-- REVIEWS
INSERT INTO reviews (rating, comment, customer_id, order_id)
VALUES
(5, 'Great', 1, 1),  -- Review for order 1 by customer 1
(4, 'Good', 2, 2),  -- Review for order 2 by customer 2
(3, 'Okay', 3, 3);  -- Review for order 3 by guest user

SELECT * FROM ingredients;
SELECT * FROM menuitems;
SELECT * FROM recipes;
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM orderitems;
SELECT * FROM payments;
SELECT * FROM promos;
SELECT * FROM reviews;