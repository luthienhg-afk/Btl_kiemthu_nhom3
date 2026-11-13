# T8 – A2: Đăng xuất & Ngoại lệ

## 1. Mục tiêu

Tìm hiểu và thực hành kiểm thử chức năng đăng xuất trên ứng dụng Swag Labs (Android) bằng Appium, đồng thời tìm hiểu cách xử lý ngoại lệ và chụp ảnh màn hình khi kiểm thử thất bại.

## 2. Phân công nhiệm vụ

### 2.1. Linh

- Tìm hiểu mục 8.7: Screenshot.
- Trình bày mục đích chụp ảnh màn hình trong kiểm thử tự động.
- Tìm hiểu cách sử dụng `save_screenshot()` của Appium/Selenium.
- Trình bày cách lưu ảnh, đặt tên ảnh và sử dụng ảnh làm minh chứng khi test thất bại.

### 2.2. Mai Anh

- Tìm hiểu mục 7.1: Exceptions.
- Trình bày khái niệm ngoại lệ và vai trò của việc xử lý ngoại lệ trong kiểm thử tự động.
- Tìm hiểu và minh họa các ngoại lệ: `NoSuchElementException`, `TimeoutException`, `StaleElementReferenceException`.
- Giải thích cách sử dụng `pytest.raises()` để kiểm tra ngoại lệ mong đợi.

### 2.3. Đức

- Phụ trách làm slide thuyết trình.
- Tổng hợp nội dung mục 7.1 và 8.7 từ các thành viên.
- Trình bày quy trình kiểm thử đăng xuất và xử lý ngoại lệ.
- Hoàn thiện slide, kiểm tra nội dung và hình thức trình bày.

### 2.4. Đăng

- Phụ trách xây dựng code demo kiểm thử trên Swag Labs Android.
- Viết và chạy test case kiểm tra chức năng đăng xuất: Menu → LOGOUT.
- Viết các test case minh họa `NoSuchElementException`, `TimeoutException` và `StaleElementReferenceException`.
- Cấu hình pytest hook để tự động chụp ảnh màn hình khi test thất bại.
- Kiểm tra kết quả chạy test, lưu ảnh minh chứng và tổng hợp code demo.

## 3. Phạm vi thực hiện

- Ứng dụng: Swag Labs trên Android.
- Chức năng chính: Menu → LOGOUT.
- Nội dung tìm hiểu:
  - Mục 7.1: Exceptions.
  - Mục 8.7: Screenshot.
- Công cụ và thư viện: Appium, Python, pytest, Selenium.
- Các ngoại lệ minh họa:
  - `NoSuchElementException`.
  - `TimeoutException`.
  - `StaleElementReferenceException`.
- Chức năng chụp ảnh: `save_screenshot()` và pytest hook `pytest_runtest_makereport`.

## 4. Các kỹ thuật cần minh họa

- `pytest.raises()`: Kiểm tra một đoạn code có phát sinh đúng ngoại lệ mong đợi hay không.
- `NoSuchElementException`: Xảy ra khi không tìm thấy phần tử theo locator.
- `TimeoutException`: Xảy ra khi điều kiện chờ không được đáp ứng trong thời gian quy định.
- `StaleElementReferenceException`: Xảy ra khi tham chiếu đến phần tử không còn hợp lệ.
- `driver.save_screenshot(filename)`: Chụp và lưu ảnh màn hình ứng dụng.
- `pytest_runtest_makereport`: Hook của pytest dùng để kiểm tra kết quả từng giai đoạn chạy test và thực hiện chụp ảnh khi test thất bại.
- `os.makedirs(..., exist_ok=True)`: Tạo thư mục lưu ảnh nếu thư mục chưa tồn tại.
- `datetime.now()`: Tạo dấu thời gian để đặt tên ảnh, tránh ghi đè ảnh cũ.

## 5. Kết quả kiểm thử

### 5.1. Kiểm thử ngoại lệ

Lệnh chạy:

`python -m pytest -v -s test_exceptions.py`

Kết quả ghi nhận từ lần chạy:
- Tổng số test case: 4
- Passed: 3
- Failed: 1
- Test thất bại: `test_menu_not_found`
- Ngoại lệ hiển thị: `NoSuchElementException`
- Nguyên nhân: Appium không tìm thấy phần tử theo locator được cung cấp.

Lưu ý:
- Các test dùng `pytest.raises()` sẽ Passed nếu ngoại lệ đúng như mong đợi được phát sinh.
- Nếu không dùng `pytest.raises()` và thao tác tìm phần tử phát sinh ngoại lệ ngoài dự kiến, test sẽ Failed.
- Nếu dùng `pytest.raises()` để chờ ngoại lệ nhưng phần tử thực tế tồn tại và không phát sinh ngoại lệ, test cũng sẽ Failed.

### 5.2. Kiểm thử đăng xuất

Lệnh chạy:

`python -m pytest -v -s test_logout.py`

Kết quả ghi nhận:
- Tổng số test case: 1
- Passed: 1
- Failed: 0
- Test Passed: `test_logout_success`
- Thông báo: `Đăng xuất thành công!`

### 5.3. Ảnh minh chứng

- Lưu ảnh chụp màn hình khi test thất bại trong thư mục `screenshots/`.
- Tên ảnh nên bao gồm tên test case và thời gian chụp, ví dụ: `test_menu_not_found_YYYYMMDD_HHMMSS.png`.
- Chỉ những test thực sự Failed mới kích hoạt điều kiện chụp ảnh trong hook nếu hook được cấu hình với `report.when == "call" and report.failed`.
- Các test ngoại lệ Passed nhờ `pytest.raises()` không tự động được xem là test thất bại và không kích hoạt hook chụp ảnh lỗi.
