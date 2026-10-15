# Ghi chú học tập Tuần 4 - Nhóm Web
## Đăng
## 1. Điều đã học
- Hiểu cách cấu hình Selenium WebDriver với Python và cách tự động hóa kiểm thử giao diện trang web đơn giản.

## 2. Trả lời câu hỏi phản biện
- **Các bước trong script Selenium:** Gồm khởi tạo thư viện, khởi tạo `webdriver.Chrome()`, dùng `driver.get()` mở URL, lấy dữ liệu tiêu đề (`driver.title`), dùng `assert` kiểm tra kết quả và gọi `driver.quit()` đóng trình duyệt.
- **Quy tắc đặt tên của Pytest:** Pytest tự động nhận diện các file bắt đầu bằng `test_` và các hàm test bắt đầu bằng `test_`.

## 3. Khai báo sử dụng AI
- **Đã hỏi AI:** Cách xử lý lỗi cú pháp và cách chạy file test đúng chuẩn bằng Python/Pytest.
- **Đánh giá câu trả lời:** AI hỗ trợ chính xác, giúp tôi hiểu rõ vòng đời của một script kiểm thử tự động.

## Đức
Câu 1: Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?
    Script Selenium gồm nhập thư viện (import), khởi tạo trình duyệt (webdriver.Chrome()), truy cập website (driver.get()), kiểm tra kết quả (assert) và đóng trình duyệt (driver.quit()).
Câu 2: pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?
    pytest mặc định tìm file test_*.py hoặc *_test.py, hàm bắt đầu bằng test_ và lớp kiểm thử bắt đầu bằng Test.
Câu 3: Selenium dùng để làm gì?
    Selenium dùng để tự động điều khiển trình duyệt và kiểm thử website.
Câu 4: pytest dùng để làm gì?
    pytest dùng để chạy bài kiểm thử và xác định chương trình có hoạt động đúng như mong đợi hay không.

## Linh
## 1. Trả lời các câu hỏi đọc tài liệu
### Câu 1: Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử?
Một kịch bản Selenium chuẩn gồm 8 bước cơ bản:
1. **Khởi tạo trình duyệt** `driver = webdriver.Chrome()` 
2. **Mở trang web** `driver.get("https://the-internet.herokuapp.com/")` 
3. **Lấy thông tin tiêu đề trang** `driver.title` 
4. **Thiết lập thời gian chờ** (ví dụ: `driver.implicitly_wait(0.5)`).
5. **Tìm phần tử HTML** (ví dụ: `driver.find_element(...)`).
6. **Thao tác trên phần tử** (ví dụ: `.click()`, `.send_keys()`).
7. **Lấy dữ liệu phần tử** (ví dụ: `element.text`).
8. **Đóng trình duyệt** `driver.quit()` - Đóng trình duyệt.

### Câu 2: pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?
Pytest áp dụng quy tắc Test Discovery tự động như sau:
- Tệp kiểm thử (Files): Tên file bắt đầu bằng `test_` (ví dụ: `test_smoke.py`) hoặc kết thúc bằng `_test.py`.
- Hàm kiểm thử (Functions): Các hàm bên trong file phải bắt đầu bằng `test_` (ví dụ: `test_smoke_the_internet_title()`).
- Lớp (Classes): Tên lớp bắt đầu bằng `Test` (không chứa hàm `__init__`).


## 2. Nhật ký thực hành & Điều đã học được
- Đã cài đặt thành công Python, thư viện Selenium, Pytest và Google Chrome.
- Viết và chạy thành công bài kiểm thử đầu tiên `test_smoke.py` kiểm tra tiêu đề trang `the-internet`.
- Đã thử sửa sai cố ý dòng assert để quan sát giao diện báo lỗi (FAILED) trên terminal của Pytest.


## 3. Nhật ký trao đổi với AI (Gemini)
- **Câu hỏi cho AI:** 
  - Hỏi về 8 bước của Selenium Script và quy tắc tìm bài test của Pytest.
  - Hỏi về cách ý nghĩa màn hình trả kết quả khi dùng pytest
  - Hỏi chi tiết hơn về Selenium, Pytest và Driver
- **Bài học rút ra:** 
    - Hiểu rõ bản chất 8 bước chạy của Selenium và quy tắc đặt tên file/hàm trong Pytest. 
    - Hiểu định nghĩa đơn giản của Selenium như 1 thư viện điều khiển tự động. Còn Pytest là 1 khung kiểm thử, Driver Là Trình phiên dịch / Phiên dịch viên nối giữa code Selenium và trình duyệt web thật.

## Mai Anh