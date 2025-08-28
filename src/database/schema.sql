-- Database: EatToday
CREATE DATABASE IF NOT EXISTS EatToday;
USE EatToday;

-- Bảng danh mục món ăn
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Bảng nguyên liệu
CREATE TABLE Ingredient (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(50)
);

-- Bảng món ăn
CREATE TABLE Food (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    calories INT,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- Bảng công thức
CREATE TABLE Recipe (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    food_id INT,
    ingredient_id INT,
    quantity FLOAT,
    FOREIGN KEY (food_id) REFERENCES Food(food_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

-- Bảng người dùng
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    preferences TEXT,   -- sở thích ăn uống
    budget DECIMAL(10,2),
    diet_type VARCHAR(50) -- ví dụ: Vegan, Keto, Low-carb
);

-- Lịch sử gợi ý / chọn món
CREATE TABLE History (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    food_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);
