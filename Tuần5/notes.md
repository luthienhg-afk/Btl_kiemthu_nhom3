## Đăng
### 1. Điều đã học được:
- Đã biết cách sử dụng **Chrome DevTools (F12)** để phân tích thẻ HTML, tra cứu thuộc tính `id`, `name`, `CSS Selector` để định vị chính xác các ô nhập dữ liệu và nút bấm trên trang web.
- Biết cách thiết lập cấu trúc kiểm thử tự động bằng **Selenium WebDriver** kết hợp với **Pytest**.
- Hiểu cách sử dụng cơ chế chờ **`WebDriverWait`** và **`expected_conditions`** để xử lý bài toán trang web chuyển hướng chậm, tránh lỗi `NoSuchElementException` hoặc gãy `assert`.

### 2. Trả lời các câu hỏi phản hồi tuần:
* **Câu 1:** *Với ô tên đăng nhập ở trang `/login`, nên xác định bằng cách nào là ổn định nhất, vì sao?*
  -> **Trả lời:** Nên ưu tiên chọn thuộc tính **`id`** (ví dụ: `By.ID, "username"`). Nguyên do vì trong tiêu chuẩn W3C của Web, `id` là thuộc tính duy nhất trên toàn trang, giúp Selenium định vị phần tử nhanh nhất và không bị ảnh hưởng khi giao diện giao diện/CSS thay đổi.
* **Câu 2:** *Muốn nhập chữ vào một ô thì dùng lệnh gì?*
  -> **Trả lời:** Sử dụng lệnh `.send_keys("nội dung cần nhập")` gọi từ đối tượng element đã tìm được

### 3. Nhận xét về việc sử dụng AI:
- **Đã hỏi AI:** Đã hỏi AI về nguyên nhân gây ra lỗi `AssertionError` ở bài kiểm thử đăng nhập thành công khi trang web chưa kịp tải xong URL mới.
- **Kết quả:** AI trả lời hoàn toàn chính xác, hướng dẫn áp dụng `WebDriverWait` thay vì dùng hàm `time.sleep()` cố định.

## Đức
Câu hỏi 1: Test case là gì? Tại sao cần viết test case trước khi kiểm thử?
    Test case là trường hợp kiểm thử gồm các bước thực hiện, dữ liệu đầu vào và kết quả mong đợi. Viết test case trước giúp xác định rõ nội dung cần kiểm tra, tránh bỏ sót trường hợp quan trọng và dễ đánh giá kết quả kiểm thử.

Câu hỏi 2: Vì sao cần kiểm thử đăng nhập với nhiều dữ liệu khác nhau?
    Vì người dùng có thể nhập thông tin đúng, sai hoặc bỏ trống. Kiểm thử nhiều trường hợp giúp phát hiện lỗi và đảm bảo hệ thống xử lý đúng. Ví dụ, nhập sai mật khẩu thì hệ thống phải từ chối đăng nhập và hiển thị thông báo lỗi.

## Diệu Linh

# Ghi chú cá nhân Tuần 05 - Diệu Linh

## 1. Trả lời các câu hỏi đọc tài liệu chuẩn bị trước buổi học
### Câu 1: Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?
- **Trả lời:** Nên xác định bằng **`ID`** (`By.ID, "username"`). 
- **Lý do:** Thuộc tính `id` trên một trang HTML chuẩn là duy nhất (unique), có tốc độ tìm kiếm nhanh nhất trong Selenium và ít bị thay đổi nhất khi giao diện web hoặc cấu trúc CSS thay đổi.

### Câu 2: Muốn nhập chữ vào một ô thì dùng lệnh gì?
- **Trả lời:** Dùng phương thức **`.send_keys("chuỗi_cần_nhập")`** của đối tượng phần tử (`WebElement`) trong Selenium.

### Câu 3: Làm thế nào để biết id của một ô nhập trên trang?
- **Trả lời:** Mở trang web trên trình duyệt Google Chrome -> Nhấp chuột phải vào ô nhập liệu cần kiểm tra -> Chọn **Inspect** (hoặc **Kiểm tra**) để mở công cụ Chrome DevTools. Tại bảng DOM HTML hiện ra, quan sát giá trị nằm trong thuộc tính `id="..."` của thẻ `<input>`.


## 2. Nhật ký thực hành & Điều đã học được
- **Tương tác với Form Đăng nhập:** Học cách sử dụng Selenium để tự động điền thông tin vào các ô `input` bằng `send_keys()`, nhấp vào nút Đăng nhập bằng `click()`, và trích xuất văn bản thông báo bằng thuộc tính `.text`.
- **Sử dụng Pytest Fixture:** Áp dụng `@pytest.fixture` cho hàm `driver()` giúp tự động khởi tạo trình duyệt Chrome trước mỗi bài test và tự đóng trình duyệt sau khi test xong (`yield` và `driver.quit()`), giúp mã nguồn gọn gàng và độc lập.
- **Sửa lỗi cú pháp thực tế:** Nhận biết và khắc phục lỗi gõ sai tên phương thức `send_key()` thành `send_keys()` (có chữ `s` ở cuối) để bài test chạy chính xác.


## 3. Nhật ký trao đổi với AI (Gemini)
- **Đã hỏi AI những gì:**
  - Hỏi cách trả lời các câu hỏi tài liệu Tuần 5.
  - Hỏi cách lấy thuộc tính HTML bằng Chrome DevTools.
  - Hỏi cách viết mã nguồn 3 bài test cho trang `/login` bằng Pytest & Selenium và cách xử lý khi gõ sai lệnh `send_key()`.
  - Hỏi nguyên lý chạy của Pytest khi quản lý 3 bài test trong cùng 1 tệp.

- **Bài học rút ra:** Nắm vững cơ chế định vị phần tử (`Locators`), hiểu cách đọc và gõ đúng cú pháp các lệnh của Selenium Python.

## Mai Anh