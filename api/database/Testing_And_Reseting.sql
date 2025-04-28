-- reset db (testing)
-- SET FOREIGN_KEY_CHECKS = 0;
-- TRUNCATE TABLE recipes;
-- TRUNCATE TABLE ingredients;
-- TRUNCATE TABLE menuitems;
-- TRUNCATE TABLE customers;
-- TRUNCATE TABLE payments;
-- TRUNCATE TABLE promos;
-- TRUNCATE TABLE orderitems;
-- TRUNCATE TABLE orders;
-- TRUNCATE TABLE reviews;
-- SET FOREIGN_KEY_CHECKS = 1;

-- reset all (usually not necessary)
drop database sandwich_maker_api;
create database sandwich_maker_api;