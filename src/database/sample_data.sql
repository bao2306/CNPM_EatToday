USE EatToday;

-- Thêm Category
INSERT INTO Category (name, description) VALUES
('Món chính', 'Các món chính cho bữa ăn'),
('Món phụ', 'Ăn kèm hoặc nhẹ'),
('Tráng miệng', 'Bánh, chè, hoa quả'),
('Đồ uống', 'Nước, sinh tố, cà phê');

-- Thêm Ingredient
INSERT INTO Ingredient (name, unit) VALUES
('Thịt gà', 'gram'),
('Thịt bò', 'gram'),
('Cơm trắng', 'bát'),
('Trứng', 'quả'),
('Sữa', 'ml');

-- Thêm Food
INSERT INTO Food (category_id, name, description, calories) VALUES
(1, 'Cơm gà xối mỡ', 'Món cơm gà chiên giòn, ăn kèm dưa leo', 650),
(1, 'Bò xào rau củ', 'Thịt bò xào cùng rau củ tươi', 550),
(3, 'Chè khúc bạch', 'Tráng miệng ngọt mát', 300);

-- Thêm Recipe
INSERT INTO Recipe (food_id, ingredient_id, quantity) VALUES
(1, 1, 200), -- Cơm gà dùng 200g gà
(1, 3, 1),   -- 1 bát cơm
(2, 2, 150), -- Bò xào 150g thịt bò
(2, 4, 1);   -- 1 quả trứng

-- Thêm User
INSERT INTO User (username, password, email, preferences, budget, diet_type) VALUES
('ngocanh', 'hashed_pass1', 'ngocanh@example.com', 'Thích đồ chiên', 100000, 'Normal'),
('minhquan', 'hashed_pass2', 'quan@example.com', 'Ưa đồ ngọt', 150000, 'Keto');

-- Thêm History
INSERT INTO History (user_id, food_id) VALUES
(1, 1),
(1, 2),
(2, 3);
