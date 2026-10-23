# Danh sách Test Case - Màn hình Đăng nhập (Swag Labs)
## Testcase 1: Đăng nhập thành công
- Input: 
    + username: standard_user 
    + pw: secret_sauce
- Kết quả mong đợi: đăng nhập thành công và truy cập vào màn Products
## Testcase 2: Đăng nhập thất bại với sai tên username
- Input: 
    + username: locked_out_user 
    + pw: secret_sauce
- Kết quả mong đợi: hiển thị "Tài khoản bị khóa"
## Testcase 3: Đăng nhập thất bại do bỏ trống pw
- Input: 
    + username: standard_user 
    + pw: bỏ trống mật khẩu
- Kết quả mong đợi: báo “Password is required”