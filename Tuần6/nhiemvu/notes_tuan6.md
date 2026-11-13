# T6 – A2: Kiểm thử chức năng kéo thả và xóa sản phẩm trong giỏ hàng

## 1. Mục tiêu

Tìm hiểu và thực hành kiểm thử chức năng kéo thả, thêm sản phẩm vào giỏ hàng và xóa sản phẩm khỏi giỏ hàng trên ứng dụng Swag Labs bằng Appium và pytest. Kiểm tra các trường hợp giỏ hàng có sản phẩm và giỏ hàng trống.

## 2. Phân công nhiệm vụ

### 2.1. Đức

- Tìm hiểu mục 3.3.
- Tìm hiểu mục 3.5.
- Tổng hợp nội dung, khái niệm và ví dụ minh họa theo tài liệu học tập.

### 2.2. Mai Anh

- Tìm hiểu mục 7.1.
- Tìm hiểu mục 7.2.
- Tổng hợp nội dung, cách sử dụng và ví dụ minh họa theo tài liệu học tập.

### 2.3. Linh

- Phụ trách làm slide thuyết trình.
- Tìm hiểu mục 7.3.
- Tổng hợp nội dung của các thành viên và hoàn thiện slide.

### 2.4. Đăng

- Phụ trách xây dựng code demo kiểm thử trên ứng dụng Swag Labs Android.
- Viết và chạy các test case đăng nhập, thêm sản phẩm vào giỏ hàng, kéo thả sản phẩm, chỉnh sửa và xóa sản phẩm khỏi giỏ hàng.
- Kiểm tra trường hợp giỏ hàng trống và xử lý ngoại lệ liên quan.
- Tổng hợp kết quả chạy pytest và ảnh minh chứng.

## 3. Phạm vi thực hiện

- Ứng dụng: Swag Labs trên Android.
- Nội dung kiểm thử:
  - Đăng nhập.
  - Thêm sản phẩm vào giỏ hàng.
  - Thực hiện thao tác kéo thả sản phẩm vào giỏ hàng.
  - Chỉnh sửa và xóa sản phẩm khỏi giỏ hàng.
  - Kiểm tra ngoại lệ khi giỏ hàng trống.
- Công cụ: Appium, Python và pytest.
- File kiểm thử: `test_keo_tha_xoa.py`.

## 4. Các kỹ thuật cần minh họa

- Đăng nhập ứng dụng trước khi thực hiện các thao tác kiểm thử.
- Tìm kiếm và tương tác với phần tử giao diện bằng Appium.
- Thêm sản phẩm vào giỏ hàng và xác minh sản phẩm đã được thêm.
- Thực hiện thao tác kéo thả (drag and drop).
- Chỉnh sửa hoặc xóa sản phẩm khỏi giỏ hàng.
- Kiểm tra trạng thái giỏ hàng trống và xác minh ngoại lệ trong trường hợp tương ứng.

## 5. Kết quả kiểm thử

Lệnh chạy:

`python -m pytest -v -s test_keo_tha_xoa.py`

Kết quả ghi nhận:
- Tổng số test case: 5
- Passed: 5
- Failed: 0
- Thời gian chạy: 46,24 giây

Các test case đã Passed:

1. `test_01_login`
2. `test_02_add_to_cart`
3. `test_03_drag_and_drop_to_cart`
4. `test_04_edit_and_remove_from_cart`
5. `test_05_verify_exception_when_cart_empty`

Kết luận:

- Cả 5 test case đều thực hiện thành công theo kết quả pytest được cung cấp.
- Chức năng đăng nhập, thêm sản phẩm, kéo thả, chỉnh sửa và xóa sản phẩm trong giỏ hàng đã được kiểm thử.
- Test case kiểm tra ngoại lệ khi giỏ hàng trống cũng có kết quả Passed.

Ảnh minh chứng:
- Ảnh kết quả chạy pytest được lưu kèm trong tài liệu/báo cáo của nhóm.
- Nếu có ảnh chụp màn hình trong quá trình chạy test, lưu chúng vào thư mục ảnh minh chứng của tuần 6.
