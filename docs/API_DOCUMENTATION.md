# 📚 EatToday API Documentation

## 🌟 Overview

**EatToday API** là một RESTful API cơ bản được phát triển cho ứng dụng hỗ trợ bà nội trợ lập kế hoạch bữa ăn hàng ngày, sử dụng Flask và kiến trúc đơn giản. API này giúp quản lý người dùng, gợi ý thực đơn cá nhân hóa, và theo dõi nguyên liệu, với mục tiêu hỗ trợ gia đình Việt Nam trong việc lên thực đơn hiệu quả.

### 🎯 Key Features
  - **Authentication & Authorization** - Xác thực dựa trên JWT với đăng ký đơn giản.
  - **Meal Suggestion Management** - Tạo và quản lý gợi ý thực đơn dựa trên sở thích.
  - **Ingredient Tracking** - Theo dõi nguyên liệu sẵn có và danh sách mua sắm.
  - **Basic Notification** - Thông báo qua email (chưa hoàn thiện).

### 🔧 Technical Stack
  - **Backend**: Flask, SQLite
  - **Authentication**: JWT
  - **Database**: SQLite
  - **Documentation**: OpenAPI cơ bản (tích hợp thủ công)

---

## 🚀 Getting Started

### Base URL

```
Production: https://api.jewelry-auction.com
Development: http://127.0.0.1:5000
```

### Authentication
API sử dụng JWT Bearer tokens:

```http
Authorization: Bearer <your-jwt-token>
```

### Response Format
Tất cả responses đều có format chuẩn:
```json
{
  "success": true,
  "message": "Thông báo thành công",
  "data": { ... },
  "pagination": { ... }
}
```
Note: Một số endpoint có thể trả về lỗi nếu dữ liệu không hợp lệ hoặc chưa hoàn thiện.


---
## 🔐 Authentication Endpoints

### POST /api/auth/register
Đăng ký tài khoản mới cho nội trợ

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "first_name": "Trương",
  "last_name": "Gia A",
  "phone": "0901234567"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Đăng ký thành công! Vui lòng kiểm tra email để xác thực.",
  "data": {
    "user": {
      "id": 1,
      "email": "user@example.com",
      "full_name": "Trương Gia A",
      "is_email_verified": false
    }
  }
}
```

### POST /api/auth/login
Đăng nhập

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Đăng nhập thành công!",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "role": "housewife",
      "is_email_verified": true
    }
  }
}
```

### POST /api/auth/verify-email
Xác thực email(chưa hoàn thiện)

**Request Body:**
```json
{
  "email": "user@example.com",
  "verification_code": "123456"
}
```
**Response:**
```json
{
  "success": false,
  "message": "Chức năng đang phát triển."
}
```

---

## 🍲 Meal Suggestions Endpoints

### GET /api/meals
Lấy danh sách gợi ý món ăn

**Query Parameters:**

  - `page` (int): Trang hiện tại (default: 1)
  - `limit` (int): Số món mỗi trang (default: 10)
  - `category` (string): Lọc theo loại (ví dụ: "mon_man", "mon_chay")
  - `max_time` (int): Thời gian nấu tối đa (phút)

**Response:**
```json
{
  "success": true,
  "message": "Lấy danh sách món ăn thành công",
  "data": [
    {
      "id": 1,
      "title": "Canh chua cá lóc",
      "description": "Món canh chua đặc trưng miền Tây...",
      "category": "mon_man",
      "cooking_time": 30,
      "ingredients": ["cá lóc", "cà chua", "dọc mùng(bạc hà)", "giá(đậu đỗ)", "me tươi/ chanh tươi/ nước cốt me/ nước cốt chanh"],
      "image": "canh_chua.jpg",
      "suggested": true
    }
  ]
}
```
**Response:**
```json
{
  "success": false,
  "message": "Lỗi server khi truy vấn dữ liệu."
}
```

### POST /api/meals/suggest
Tạo gợi ý thực đơn mới (Requires authentication)

**Request Body:**
```json
{
  "preferences": "mon_nam, thit_bo",
  "budget": 500000,
  "ingredients_available": ["thit_bo", "ot_chuong", "hanh_tay"]
}
```
**Response:**
```json
{
  "success": true,
  "message": "Gợi ý thực đơn thành công",
  "data": {
    "meal_id": 1,
    "title": "Bò lúc lắc",
    "ingredients_needed": ["dau_hoi"]
  }
}
```
**Response:**
```json
{
  "success": false,
  "message": "Dữ liệu đầu vào không hợp lệ."
}
```

### GET /api/meals/categories
Lấy danh sách loại món ăn

**Response:**
```json
{
  "success": true,
  "message": "Lấy danh sách loại món thành công",
  "data": {
    "categories": [
      {"value": "mon_nam", "label": "Món mặn"},
      {"value": "mon_chay", "label": "Món chay"},
      {"value": "mon_can", "label": "Món canh"},
      {"value": "mon_xao", "label": "Món xào"}
    ]
  }
}
```

---

## 🛒 Shopping List Endpoints

### GET /api/shopping-list
Lấy danh sách mua sắm

**Query Parameters:**

  - `page` (int): Trang hiện tại (default: 1)
  - `limit` (int): Số mục mỗi trang (default: 10)

**Response:**
```json
{
  "success": true,
  "message": "Lấy danh sách mua sắm thành công",
  "data": [
    {"id": 1, "ingredient": "thịt bò", "quantity": 0.5},
    {"id": 2, "ingredient": "ớt chuông", "quantity": 2}
    {"id": 3, "ingredient": "hành tây", "quantity": 1}
    {"id": 4, "ingredient": "gia vị", "quantity": nhà có}
  ]
}
```

### POST /api/shopping-list/update
Cập nhật trạng thái mua sắm (Requires authentication)

**Request Body:**
```json
{
  "ingredient_id": 1,
  "purchased": true
}
```
**Response:**
```json
{
  "success": true,
  "message": "Cập nhật trạng thái mua sắm thành công",
  "data": {"ingredient_id": 1, "purchased": true}
}
```

---

## 👩‍🍳 Admin Endpoints
### GET /api/admin/meals
Lấy danh sách tất cả món ăn (Admin only)

**Response:**
```json
{
  "success": true,
  "message": "Lấy danh sách món ăn thành công",
  "data": [...]
}
```

### POST /api/admin/meals
Thêm món ăn mới (Admin only)

**Request Body:**
```json
{
  "title": "Canh chua cá lóc",
  "category": "mon_can",
  "ingredients": ["cá lóc", "cà chua", "dọc mùng(bạc hà)", "giá(đậu đỗ)", "me tươi/ chanh tươi/ nước cốt me/ nước cốt chanh"],
  "cooking_time": 30,
  "image": "canh_chua.jpg",
}
```

---

## 📊 Error Handling

### Error Response Format
```json
{
  "success": false,
  "message": "Lỗi trong hệ thống",
  "errors": ["Chi tiết lỗi 1"]
}
```
### HTTP Status Codes
  - `200` - Success
  - `201` - Created
  - `400` - Bad Request
  - `401` - Unauthorized
  - `404` - Not Found
  - `500` - Internal Server Error

### Common Error Messages
```json
{
  "401": "Token không hợp lệ",
  "404": "Không tìm thấy món ăn",
  "500": "Lỗi server"
}
```

---

## 🔄 Pagination
Tất cả list endpoints đều hỗ trợ pagination:

**Request:**
```http
GET /api/meals?page=2&limit=5
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 5,
    "total": 20
  }
}
```

---

## 🚀 Rate Limiting

  - **Authentication endpoints:** 5 requests/minute
  - **Meal endpoints:** 10 requests/minute
  - **Admin endpoints:** 5 requests/minute


## 🧪 Testing

### Postman Collection
Hiện tại, file Postman Collection đã được cung cấp tại `/docs/postman_collection.json`. Bạn có thể import file này vào Postman để test các endpoint một cách dễ dàng. 
**Hướng dẫn:**
  1. Mở Postman và tạo một Collection mới với tên "EatToday API".
  2. Nhập file `/docs/postman_collection.json`.
  3. Sử dụng dữ liệu mẫu từ phần "Test Accounts" để test.

**Test Accounts**
```
Admin: admin@eattoday.com / admin123
Housewife: user@eattoday.com / user123
```

## 📅 Future Development Plans
Hiện tại, EatToday chưa hỗ trợ các tính năng nâng cao như thông báo real-time hoặc gợi ý thông minh bằng machine learning phức tạp. Tuy nhiên, nhóm dự kiến phát triển thêm:

  - **Real-time Updates:** Thông báo qua email hoặc push notification khi có gợi ý mới.
  - **Advanced Suggestions:** Tích hợp mô hình ML để gợi ý dựa trên lịch sử ăn uống.
  - **Integration:** Kết nối với ứng dụng mua sắm nguyên liệu trực tuyến.
  - **Những tính năng này sẽ được triển khai trong các phiên bản sau, tùy thuộc vào tiến độ học tập và hỗ trợ từ AI.**
    
---

## 📞 Support

- **Email**: support@eattoday.com
- **Documentation**: https://docs.eattoday.com
- **GitHub**: https://github.com/bao2306/CPM_EatToday
