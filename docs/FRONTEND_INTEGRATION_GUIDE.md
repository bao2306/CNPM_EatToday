# 🚀 Frontend Integration Guide

## 📋 Overview

Hướng dẫn tích hợp frontend với **EatToday API** cho React, Flutter (mobile), và vanilla JavaScript. Tài liệu này hỗ trợ các bà nội trợ và admin tích hợp giao diện người dùng với API để quản lý thực đơn, nguyên liệu, và tài khoản.

---

## 🔧 Setup & Configuration

### 1. Environment Variables
```javascript
// .env (cho React/JS)
REACT_APP_API_BASE_URL=http://127.0.0.1:5000
REACT_APP_WS_URL=ws://127.0.0.1:5000
REACT_APP_APP_NAME=EatToday
```
```dart
// env.dart (cho Flutter)
const String apiBaseUrl = 'http://127.0.0.1:5000';
const String appName = 'EatToday';
```
### 2. API Client Setup (Axios cho React/JS)

```javascript
// api/client.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor - Add auth token
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor - Handle errors
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error.response?.data || error);
  }
);

export default apiClient;
```

### 3. API Client Setup (http cho Flutter)
```dart
// lib/api/client.dart
import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiClient {
  final String baseUrl;

  ApiClient({required this.baseUrl});

  Future<dynamic> get(String endpoint) async {
    final url = Uri.parse('$baseUrl/$endpoint');
    final response = await http.get(
      url,
      headers: {
        'Content-Type': 'application/json',
        if (await _getToken() != null) 'Authorization': 'Bearer ${await _getToken()}',
      },
    );
    return _handleResponse(response);
  }

  Future<dynamic> post(String endpoint, dynamic data) async {
    final url = Uri.parse('$baseUrl/$endpoint');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json',
        if (await _getToken() != null) 'Authorization': 'Bearer ${await _getToken()}',
      },
      body: jsonEncode(data),
    );
    return _handleResponse(response);
  }

  Future<String?> _getToken() async {
    // Giả định token được lưu trong shared preferences
    return null; // Thêm logic lưu token nếu có
  }

  dynamic _handleResponse(http.Response response) {
    final data = jsonDecode(response.body);
    if (response.statusCode == 401) {
      // Xử lý logout hoặc redirect
    }
    return data;
  }
}

final apiClient = ApiClient(baseUrl: apiBaseUrl);
```

---
## 🔐 Authentication Integration
### 1. Auth Service (React/JS)

```javascript
// services/authService.js
import apiClient from '../api/client';

class AuthService {
  async register(userData) {
    const response = await apiClient.post('/api/auth/register', userData);
    return response;
  }

  async login(email, password) {
    const response = await apiClient.post('/api/auth/login', {
      email,
      password,
    });
    
    if (response.success) {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
    }
    
    return response;
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login';
  }

  getCurrentUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }

  isAuthenticated() {
    return !!localStorage.getItem('access_token');
  }
}

export default new AuthService();
```

### 2. Auth Service (Flutter)
```dart
// lib/services/auth_service.dart
import 'package:http/http.dart' as http;
import 'dart:convert';

class AuthService {
  final String baseUrl;

  AuthService({required this.baseUrl});

  Future<Map<String, dynamic>> register(Map<String, dynamic> userData) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/auth/register'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(userData),
    );
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> login(String email, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'email': email, 'password': password}),
    );
    final data = jsonDecode(response.body);
    if (data['success']) {
      // Lưu token và user (giả định)
    }
    return data;
  }

  void logout() {
    // Xóa token và user
    // Ví dụ: SharedPreferences.remove('access_token');
  }

  bool isAuthenticated() {
    // Kiểm tra token (giả định)
    return false; // Thêm logic kiểm tra token
  }
}

final authService = AuthService(baseUrl: apiBaseUrl);
```

### 3. React Auth Hook
```javascript
// hooks/useAuth.js
import { useState, useEffect, createContext, useContext } from 'react';
import authService from '../services/authService';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const currentUser = authService.getCurrentUser();
    setUser(currentUser);
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    const response = await authService.login(email, password);
    if (response.success) {
      setUser(response.data.user);
    }
    return response;
  };

  const logout = () => {
    authService.logout();
    setUser(null);
  };

  const value = {
    user,
    login,
    logout,
    loading,
    isAuthenticated: authService.isAuthenticated(),
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
```

---
## 🍲 Meal Suggestions Integration
## 1. Meal Suggestions Service (React/JS)
```javascript
// services/mealSuggestionsService.js
import apiClient from '../api/client';

class MealSuggestionsService {
  async getMeals(params = {}) {
    const queryString = new URLSearchParams(params).toString();
    return await apiClient.get(`/api/meals?${queryString}`);
  }

  async suggestMeal(preferences) {
    return await apiClient.post('/api/meals/suggest', preferences);
  }

  async getCategories() {
    return await apiClient.get('/api/meals/categories');
  }
}

export default new MealSuggestionsService();
```

### 2. Meal Suggestions Component (React)
```javascript
// components/MealSuggestionsList.jsx
import React, { useState, useEffect } from 'react';
import mealSuggestionsService from '../services/mealSuggestionsService';

const MealSuggestionsList = () => {
  const [meals, setMeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    page: 1,
    limit: 10,
    category: '',
    max_time: '',
  });

  useEffect(() => {
    loadMeals();
  }, [filters]);

  const loadMeals = async () => {
    try {
      setLoading(true);
      const response = await mealSuggestionsService.getMeals(filters);
      if (response.success) {
        setMeals(response.data);
      }
    } catch (error) {
      console.error('Load meals error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (category) => {
    setFilters(prev => ({ ...prev, category, page: 1 }));
  };

  if (loading) return <div>Đang tải...</div>;

  return (
    <div className="meal-suggestions-list">
      <div className="filters">
        <select value={filters.category} onChange={(e) => handleCategoryChange(e.target.value)}>
          <option value="">Tất cả loại món</option>
          <option value="mon_nam">Món mặn</option>
          <option value="mon_chay">Món chay</option>
          <option value="mon_can">Món canh</option>
          <option value="mon_xao">Món xào</option>
        </select>
      </div>

      <div className="meals-grid">
        {meals.map(meal => (
          <div key={meal.id} className="meal-card">
            <img src={meal.image} alt={meal.title} />
            <h3>{meal.title}</h3>
            <p>Thời gian nấu: {meal.cooking_time} phút</p>
            <p>Nguyên liệu: {meal.ingredients.join(', ')}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MealSuggestionsList;
```

### 3. Suggest Meal Form (React)
```javascript
// components/SuggestMealForm.jsx
import React, { useState } from 'react';
import mealSuggestionsService from '../services/mealSuggestionsService';
import { useAuth } from '../hooks/useAuth';

const SuggestMealForm = () => {
  const { isAuthenticated } = useAuth();
  const [formData, setFormData] = useState({
    preferences: '',
    budget: '',
    ingredients_available: '',
  });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isAuthenticated) {
      setMessage('Vui lòng đăng nhập để gợi ý thực đơn.');
      return;
    }

    try {
      const response = await mealSuggestionsService.suggestMeal(formData);
      if (response.success) {
        setMessage(`Gợi ý thành công: ${response.data.title}`);
      }
    } catch (error) {
      setMessage('Có lỗi xảy ra khi gợi ý.');
    }
  };

  return (
    <div className="suggest-meal-form">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Sở thích (ví dụ: mon_nam, thit_bo)</label>
          <input
            type="text"
            value={formData.preferences}
            onChange={(e) => setFormData({ ...formData, preferences: e.target.value })}
          />
        </div>
        <div className="input-group">
          <label>Ngân sách (VND)</label>
          <input
            type="number"
            value={formData.budget}
            onChange={(e) => setFormData({ ...formData, budget: e.target.value })}
          />
        </div>
        <div className="input-group">
          <label>Nguyên liệu sẵn có (dùng dấu phẩy)</label>
          <input
            type="text"
            value={formData.ingredients_available}
            onChange={(e) => setFormData({ ...formData, ingredients_available: e.target.value })}
          />
        </div>
        <button type="submit">Gợi ý thực đơn</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default SuggestMealForm;
```
---

## 🛒 Shopping List Integration
### 1. Shopping List Service (React/JS)
```javascript
// services/shoppingListService.js
import apiClient from '../api/client';

class ShoppingListService {
  async getShoppingList(params = {}) {
    const queryString = new URLSearchParams(params).toString();
    return await apiClient.get(`/api/shopping-list?${queryString}`);
  }

  async updateItem(ingredientId, purchased) {
    return await apiClient.post('/api/shopping-list/update', { ingredient_id: ingredientId, purchased });
  }
}

export default new ShoppingListService();
```

### 2. Shopping List Component (React)
```javascript
// components/ShoppingList.jsx
import React, { useState, useEffect } from 'react';
import shoppingListService from '../services/shoppingListService';
import { useAuth } from '../hooks/useAuth';

const ShoppingList = () => {
  const { isAuthenticated } = useAuth();
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (isAuthenticated) {
      loadItems();
    }
  }, [isAuthenticated]);

  const loadItems = async () => {
    try {
      setLoading(true);
      const response = await shoppingListService.getShoppingList();
      if (response.success) {
        setItems(response.data);
      }
    } catch (error) {
      console.error('Load shopping list error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdate = async (id, purchased) => {
    try {
      const response = await shoppingListService.updateItem(id, purchased);
      if (response.success) {
        setItems(items.map(item => item.id === id ? { ...item, purchased } : item));
      }
    } catch (error) {
      console.error('Update error:', error);
    }
  };

  if (loading) return <div>Đang tải...</div>;
  if (!isAuthenticated) return <p>Vui lòng đăng nhập để xem danh sách mua sắm.</p>;

  return (
    <div className="shopping-list">
      <h3>Danh sách mua sắm</h3>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.ingredient} ({item.quantity} kg) - 
            <input
              type="checkbox"
              checked={item.purchased || false}
              onChange={(e) => handleUpdate(item.id, e.target.checked)}
            />
            Đã mua
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShoppingList;
```
---

## 🎨 UI Components Examples
### 1. Loading Component
```javascript
// components/Loading.jsx
const Loading = ({ message = 'Đang tải...' }) => (
  <div className="loading">
    <div className="spinner"></div>
    <p>{message}</p>
  </div>
);
```

## 2. Error Boundary
```javascript
// components/ErrorBoundary.jsx
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Có lỗi xảy ra</h2>
          <p>Vui lòng tải lại trang hoặc liên hệ hỗ trợ.</p>
          <button onClick={() => window.location.reload()}>
            Tải lại trang
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
```
---

## 🧪 Testing Examples
### 1. API Service Tests (React/JS)
```javascript
// __tests__/authService.test.js
import authService from '../services/authService';

describe('AuthService', () => {
  test('should login successfully', async () => {
    const mockResponse = {
      success: true,
      data: {
        access_token: 'mock-token',
        user: { id: 1, email: 'test@example.com' }
      }
    };

    jest.spyOn(authService, 'login').mockResolvedValue(mockResponse);

    const result = await authService.login('test@example.com', 'password');
    expect(result.success).toBe(true);
    expect(result.data.access_token).toBe('mock-token');
  });
});
```
---

## 📱 Mobile Considerations
### 1. Responsive Design
```css
/* Mobile-first approach */
.meal-suggestions-list {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 768px) {
  .meal-suggestions-list {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .meal-suggestions-list {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## 2. Touch-friendly Buttons
```dart
// lib/widgets/touch_button.dart (Flutter)
import 'package:flutter/material.dart';

class TouchButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;

  const TouchButton({required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: EdgeInsets.symmetric(vertical: 10, horizontal: 20),
        decoration: BoxDecoration(
          color: Colors.blue,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Text(label, style: TextStyle(color: Colors.white)),
      ),
    );
  }
}
```
---

## 🔧 Best Practices
### 1. Error Handling

  - Xử lý lỗi API một cách nhẹ nhàng
  - Hiển thị thông báo lỗi bằng tiếng Việt
  = Thêm thử lại (retry) cho lỗi mạng

### 2. Performance

  - Sử dụng lazy loading cho hình ảnh món ăn
  - Áp dụng phân trang cho danh sách lớn
  - Lưu cache dữ liệu khi có thể

### 3. Security

  - Không lưu dữ liệu nhạy cảm trong localStorage
  = Kiểm tra đầu vào trước khi gửi API
  - Đảm bảo cấu hình CORS đúng

### 4. User Experience

  - Hiển thị trạng thái tải
  - Cập nhật giao diện ngay khi người dùng hành động
  - Cung cấp phản hồi rõ ràng
---

## 📞 Support
Nếu có vấn đề trong quá trình tích hợp:
  - **Email:** support@eattoday.com
  - **Documentation:**  https://docs.eattoday.com
  - **GitHub Issues:** https://github.com/bao2306/CPM_EatToday/issues
