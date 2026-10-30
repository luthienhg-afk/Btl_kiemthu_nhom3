T7 – A2: Trạng thái ứng dụng & Reset App State

## 1. Mục tiêu

Tìm hiểu và thực hành kiểm thử trạng thái ứng dụng Swag Labs trên Android bằng Appium, tập trung vào chức năng RESET APP STATE và các kỹ thuật hỗ trợ kiểm thử tự động.

## 2. Phân công nhiệm vụ

2.1. Linh

Phụ trách làm slide thuyết trình.

Tổng hợp ý kiến và sửa lỗi.

2.2. Đức

Tìm hiểu Cookies (mục 3.7).

Giải thích khái niệm, tác dụng và cách sử dụng Explicit Waits (mục 5.1).

Trình bày khái niệm, cách sử dụng và ví dụ minh họa.

Liên hệ việc sử dụng Cookies trong kiểm thử tự động.

2.3. Mai Anh

Tìm hiểu Desired Capabilities (mục 7.6).

Trình bày khái niệm, vai trò và cách khai báo cấu hình.

Chuẩn bị ví dụ minh họa và giới thiệu các cấu hình thường dùng trong Appium.

2.4. Trưởng nhóm

Tổng hợp tài liệu của các thành viên.

Xây dựng và kiểm tra demo RESET APP STATE trên Swag Labs Android.

Kiểm thử bằng pytest, lưu ảnh minh chứng.

Quản lý nhánh GitHub, tổng hợp sản phẩm và hoàn thiện báo cáo.

## 3. Phạm vi thực hiện

Ứng dụng: Swag Labs trên Android.

Chức năng: Menu → RESET APP STATE.

Nội dung tìm hiểu:

Mục 3.7: Cookies.

Mục 5.1: Explicit Waits.

Mục 7.6: Desired Capabilities.

## 4. Các kỹ thuật cần minh họa

terminate_app: Kết thúc ứng dụng.

activate_app: Mở hoặc đưa ứng dụng trở lại hoạt động.

noReset: Capability điều khiển việc đặt lại dữ liệu ứng dụng khi khởi tạo session.

EC.invisibility_of_element_located: Chờ phần tử biến mất hoặc không còn hiển thị.

pytest.mark.xfail: Đánh dấu test được dự kiến thất bại.

## 5. Kết quả kiểm thử

Lệnh chạy:

`python -m pytest -v -s test_reset_app_state.py`

Kết quả ghi nhận:
- Tổng số test case: 4
- Passed: 3
- Failed: 0
- XFailed: 0
- XPassed: 1
- Thời gian chạy: 74,97 giây

Các test đã Passed:
1. `test_reset_app_state_clears_cart`
2. `test_app_lifecycle_terminate_and_activate`
3. `test_cart_persistence_after_restart`

Test cần xem xét:
- `test_no_reset_capability_behavior` được đánh dấu `pytest.mark.xfail` nhưng thực tế thành công (XPASS). Cần kiểm tra lại lý do đánh dấu `xfail` và xác nhận hành vi mong đợi của test.

Ảnh minh chứng được lưu trong thư mục `anh/`.
