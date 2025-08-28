-- Sample data for EatToday application

-- Insert Categories
INSERT INTO Category (name, description) VALUES
('Breakfast', 'Morning meals to start the day'),
('Lunch', 'Meals served around noon'),
('Dinner', 'Evening meals for the family'),
('Dessert', 'Sweet dishes'),
('Drink', 'Beverages and smoothies');

-- Insert Foods
INSERT INTO Food (name, category_id, description) VALUES
('Pho Bo', 2, 'Vietnamese beef noodle soup'),
('Banh Mi', 1, 'Vietnamese baguette sandwich'),
('Com Tam', 2, 'Broken rice with grilled pork'),
('Che Ba Mau', 4, 'Vietnamese three-color dessert'),
('Sinh To Xoai', 5, 'Mango smoothie');

-- Insert Ingredients
INSERT INTO Ingredient (name, unit) VALUES
('Beef', 'grams'),
('Rice Noodles', 'grams'),
('Pork', 'grams'),
('Mango', 'pieces'),
('Milk', 'ml'),
('Sugar', 'grams');

-- Insert Recipes
INSERT INTO Recipe (food_id, ingredient_id, quantity) VALUES
(1, 1, 200),  -- Pho Bo: 200g Beef
(1, 2, 150),  -- Pho Bo: 150g Rice Noodles
(3, 3, 200),  -- Com Tam: 200g Pork
(5, 4, 1),    -- Mango Smoothie: 1 Mango
(5, 5, 100),  -- Mango Smoothie: 100ml Milk
(5, 6, 20);   -- Mango Smoothie: 20g Sugar

-- Insert Users
INSERT INTO "User" (username, password_hash, email, role) VALUES
('admin', 'hashed_password_123', 'admin@eattoday.com', 'admin'),
('mary', 'hashed_password_abc', 'mary@example.com', 'housewife');

-- Insert History
INSERT INTO History (user_id, food_id, planned_date) VALUES
(2, 1, '2025-08-26'),
(2, 3, '2025-08-27'),
(2, 5, '2025-08-27');
