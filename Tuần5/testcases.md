## Test Case 1: Đăng nhập thành công với thông tin hợp lệ
- **Mô tả:** Kiểm tra hệ thống cho phép người dùng đăng nhập thành công khi nhập đúng Tên đăng nhập và Mật khẩu.
- **Các bước thực hiện:**
  1. Mở trình duyệt và truy cập vào trang đăng nhập của ứng dụng web.
  2. Click vào ô "Tên đăng nhập" (Username) và nhập giá trị hợp lệ (Ví dụ: `admin_test`).
  3. Click vào ô "Mật khẩu" (Password) và nhập giá trị hợp lệ (Ví dụ: `12345678`).
  4. Nhấn nút "Đăng nhập" (Login).
- **Dữ liệu nhập:** Username = `admin_test`, Password = `12345678`
- **Kết quả mong đợi:** Đăng nhập thành công, hệ thống điều hướng người dùng sang trang chủ
---

## Test Case 2: Đăng nhập thất bại do sai mật khẩu
- **Mô tả:** Kiểm tra hệ thống từ chối đăng nhập và hiển thị thông báo lỗi khi người dùng nhập đúng tên đăng nhập nhưng sai mật khẩu.
- **Các bước thực hiện:**
  1. Truy cập trang đăng nhập.
  2. Nhập tên đăng nhập hợp lệ (`admin_test`).
  3. Nhập mật khẩu **sai** (`sai_mat_khau_123`).
  4. Nhấn nút "Đăng nhập".
- **Dữ liệu nhập:** Username = `admin_test`, Password = `sai_mat_khau_123`
- **Kết quả mong đợi:** Đăng nhập thất bại, giữ nguyên ở trang đăng nhập và hiển thị thông báo lỗi ("Mật khẩu không chính xác").

---

## Test Case 3: Đăng nhập thất bại do để trống ô thông tin
- **Mô tả:** Kiểm tra hệ thống cảnh báo khi người dùng để trống các trường bắt buộc (Username hoặc Password).
- **Các bước thực hiện:**
  1. Truy cập trang đăng nhập.
  2. Để trống cả hai ô Tên đăng nhập và Mật khẩu.
  3. Nhấn nút "Đăng nhập".
- **Dữ liệu nhập:** Để trống (`""`)
- **Kết quả mong đợi:** Hiển thị thông báo yêu cầu nhập thông tin tại các ô còn trống