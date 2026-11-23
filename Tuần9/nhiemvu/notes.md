# T9 – A2: Đăng nhập nhanh & tài khoản problem_user

## 1. Mục tiêu

Tìm hiểu và thực hành kiểm thử chức năng đăng nhập bằng tài khoản `problem_user` trên ứng dụng Swag Labs (Android) bằng Appium, đồng thời tìm hiểu cách tương tác với trang, thao tác với WebElement và chụp ảnh màn hình trong kiểm thử tự động.

## 2. Phân công nhiệm vụ

### 2.1. Linh

- Tìm hiểu mục 7.20: WebElement.
- Tìm hiểu mục 8.7: Screenshot.
- Trình bày khái niệm WebElement và các thao tác thường dùng với phần tử.
- Tìm hiểu cách sử dụng `click()`, `send_keys()`, thuộc tính `text`, `get_attribute()` và `screenshot()`.
- Trình bày cách chụp, lưu ảnh màn hình và ảnh của từng WebElement làm minh chứng kiểm thử.

### 2.2. MAnh

- Tìm hiểu mục 3.1: Interacting with the page.
- Trình bày cách tìm kiếm và tương tác với các phần tử trên trang/màn hình.
- Tìm hiểu quy trình nhập dữ liệu vào ô Username, Password và nhấn nút Login.
- Minh họa thao tác cuộn màn hình bằng lệnh Appium `mobile: scrollGesture`.
- Tổng hợp ví dụ sử dụng các thao tác tương tác trong ứng dụng Swag Labs Android.

### 2.3. Đức

- Phụ trách làm slide thuyết trình.
- Tổng hợp nội dung mục 3.1, 7.20 và 8.7 từ các thành viên.
- Trình bày quy trình đăng nhập bằng tài khoản `problem_user` và các thao tác kiểm thử liên quan.
- Hoàn thiện slide, kiểm tra nội dung và hình thức trình bày.

### 2.4. Đăng

- Phụ trách xây dựng code demo kiểm thử trên Swag Labs Android.
- Viết file `demo_login_problem_user.py` để trình diễn trực tiếp các thao tác Appium.
- Viết file `test_login_problem_user.py` gồm 5 test case kiểm thử.
- Thực hiện đăng nhập bằng tài khoản `problem_user`.
- Kiểm tra thông tin tên và giá sản phẩm.
- Kiểm tra thao tác cuộn danh sách sản phẩm bằng `scrollGesture`.
- Kiểm tra các phần tử hình ảnh ImageView.
- Thực hiện chụp ảnh toàn màn hình và chụp ảnh riêng WebElement.
- Chạy chương trình demo và pytest, kiểm tra kết quả và tổng hợp code.

## 3. Phạm vi thực hiện

- Ứng dụng: Swag Labs trên Android.
- Chức năng chính: Đăng nhập bằng tài khoản `problem_user`.
- Màn hình: Màn hình đăng nhập và màn hình danh sách sản phẩm (Products).
- Nội dung tìm hiểu:
  - Mục 3.1: Interacting with the page.
  - Mục 7.20: WebElement.
  - Mục 8.7: Screenshot.
- Công cụ và thư viện: Appium, Python, pytest, Selenium.
- Các thao tác và chức năng minh họa:
  - Nhập Username và Password.
  - Nhấn nút Login.
  - Đọc tên và giá sản phẩm.
  - Lấy thuộc tính phần tử bằng `get_attribute()`.
  - Cuộn danh sách sản phẩm bằng `mobile: scrollGesture`.
  - Kiểm tra các phần tử hình ảnh ImageView.
  - Chụp ảnh toàn màn hình và chụp ảnh riêng WebElement.

## 4. Các kỹ thuật cần minh họa

- `send_keys()`: Nhập dữ liệu vào các trường Username và Password.
- `click()`: Nhấn nút Login hoặc tương tác với phần tử.
- `.text`: Lấy nội dung văn bản hiển thị của WebElement.
- `get_attribute()`: Lấy giá trị thuộc tính của WebElement, ví dụ thuộc tính `text`.
- `mobile: scrollGesture`: Thực hiện thao tác cuộn trên màn hình Android thông qua Appium UiAutomator2.
- `is_displayed()`: Kiểm tra phần tử có đang hiển thị hay không.
- `driver.save_screenshot(filename)`: Chụp và lưu ảnh toàn bộ màn hình ứng dụng.
- `element.screenshot(filename)`: Chụp và lưu ảnh riêng của một WebElement.
- `WebDriverWait` và `expected_conditions`: Chờ phần tử xuất hiện, hiển thị hoặc có thể tương tác trước khi thao tác.
- `pytest.fixture`: Khởi tạo và đóng Appium driver phục vụ từng test case.
- `assert`: Kiểm tra điều kiện và xác định kết quả đạt hoặc không đạt của test case.

## 5. Kết quả kiểm thử

### 5.1. Chạy chương trình demo

Lệnh chạy:

`python demo_login_problem_user.py`

Kết quả ghi nhận:
- Tổng số test case: 5.
- Passed: 5.
- Failed: 0.
- Các test case đều thực hiện thành công:
  - TC01: Đăng nhập problem_user.
  - TC02: Kiểm tra tên và giá sản phẩm.
  - TC03: Thực hiện scrollGesture.
  - TC04: Kiểm tra ImageView.
  - TC05: Screenshot màn hình và WebElement.
- Thông tin sản phẩm ghi nhận:
  - Tên sản phẩm: `Sauce Labs Backpack`.
  - Giá sản phẩm: `$29.99`.
  - Kết quả cuộn: `True`.
  - Tổng số ImageView: 10.
  - ImageView đang hiển thị: 10.

### 5.2. Kiểm thử bằng pytest

Lệnh chạy:

`python -m pytest -v -s test_login_problem_user.py`

Kết quả ghi nhận:
- Tổng số test case: 5.
- Passed: 5.
- Failed: 0.
- Thời gian chạy: 125.91 giây (0:02:05).
- Các test case Passed:
  - `test_tc01_login_problem_user`
  - `test_tc02_check_product_information`
  - `test_tc03_scroll_products`
  - `test_tc04_check_product_images`
  - `test_tc05_take_screenshots`

### 5.3. Ảnh minh chứng

- Ảnh chụp màn hình được lưu trong thư mục `screenshots/`.
- Ảnh từ chương trình demo:
  - `problem_user_full_screen.png`: Ảnh chụp toàn bộ màn hình.
  - `problem_user_element.png`: Ảnh chụp riêng WebElement.
- Ảnh từ chương trình pytest:
  - `tc05_full_screen.png`: Ảnh chụp toàn bộ màn hình.
  - `tc05_product_element.png`: Ảnh chụp riêng WebElement.
- Các ảnh được lưu trong thư mục `screenshots/` cùng cấp với file code.