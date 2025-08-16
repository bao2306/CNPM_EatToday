# Ứng dụng Lên Kế Hoạch Bữa Ăn Gia Đình

## I. Tổng quan dự án

### 1. Mục tiêu
Xây dựng một ứng dụng web nhằm:
- Hỗ trợ người dùng quản lý nguyên liệu sẵn có và công thức nấu ăn.  
- Tự động gợi ý thực đơn theo ngày/tuần dựa trên nhu cầu dinh dưỡng, sở thích và số lượng thành viên trong gia đình.  
- Sinh danh sách mua sắm (shopping list) từ thực đơn đã lên kế hoạch.  
- Cung cấp thống kê dinh dưỡng, đảm bảo bữa ăn cân bằng.  

### 2. Phạm vi ứng dụng
Ứng dụng tập trung vào các chức năng:
- Đăng ký/đăng nhập người dùng.  
- Quản lý nguyên liệu và công thức món ăn.  
- Lập kế hoạch bữa ăn hằng ngày/tuần.  
- Sinh danh sách mua sắm.  
- Thống kê, gợi ý dinh dưỡng cơ bản.  

Trong giai đoạn mở rộng, ứng dụng có thể tích hợp:
- AI gợi ý thực đơn thông minh.  
- Kết nối với dịch vụ giao hàng siêu thị.  
- Xuất báo cáo thực đơn ra PDF/Excel để chia sẻ.  

### 3. Giả định và Ràng buộc
- Hệ thống chỉ phục vụ cho việc lên kế hoạch bữa ăn gia đình, không phải là một nền tảng nấu ăn chuyên nghiệp hay dịch vụ giao đồ ăn.  
- Hệ thống quản lý công thức, nguyên liệu và kế hoạch bữa ăn, không phải là phần mềm kế toán, quản lý kho hay mua sắm trực tuyến toàn diện.  
- Hệ thống hỗ trợ sinh danh sách mua sắm, nhưng không tích hợp trực tiếp với siêu thị hoặc đơn vị cung cấp thực phẩm bên ngoài.  
- Hệ thống có chức năng thống kê dinh dưỡng cơ bản, không phải là một ứng dụng y tế chuyên sâu hay phần mềm theo dõi sức khỏe toàn diện.

## Yêu cầu chức năng  
### Các tác nhân  

- **Guest (Khách vãng lai):** Người dùng chưa đăng nhập, chỉ có thể xem giới thiệu ứng dụng hoặc một số công thức mẫu.  
- **User (Người dùng/Thành viên gia đình):** Người dùng có tài khoản, đăng nhập để quản lý nguyên liệu, công thức, lập kế hoạch bữa ăn.  
- **Planner (Người lập kế hoạch):** Lên kế hoạch bữa ăn, sinh danh sách mua sắm và xem thống kê dinh dưỡng.  
- **Nutritionist (Chuyên gia dinh dưỡng):** Cung cấp dữ liệu dinh dưỡng, đưa ra khuyến nghị về chế độ ăn.  
- **Admin (Quản trị viên):** Quản lý tài khoản, công thức mặc định và giám sát hệ thống.
