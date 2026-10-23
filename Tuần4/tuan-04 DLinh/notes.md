# Trả lời 1 số câu ở phần đọc
## 1. pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?
Thư viện pytest tự tìm bài kiểm thử dựa vào các quy tắc đặt tên mặc định như sau:
- tên file bắt đầu bằng test_ (vd test_smoke.py)
- tên hàm test bắt đầu bằng test_ (vd: def test_login_success())
- tên lớp bắt đầu bằng Test và không chứa hàm __init__ (Ví dụ: class TestAppium:)
## 2. Appium client, Appium server và driver lần lượt chạy ở đâu?
- Appium client: Chạy trên máy tính cá nhân (nơi chứa script code test bằng Python hoặc Java của bạn)
- Appium server: Chạy trên máy tính cá nhân dưới dạng một Node.js HTTP Server trung gian để nhận và phiên dịch lệnh
- Driver (UiAutomator2): Chạy trực tiếp trên thiết bị Android (máy ảo hoặc điện thoại thật) để tương tác và điều khiển ứng dụng
## 3. Bạn chọn cấu hình máy ảo nào và vì sao?
- Cấu hình chọn: Pixel 4 running Android 11.0 (API Level 30 - R)
- Lý do: Đây là bản cấu hình máy tiêu chuẩn, ổn định, tương thích mượt mà với Appium và UiAutomator2, đồng thời tối ưu bộ nhớ nên không chiếm quá nhiều dung lượng RAM của máy tính.
## 4. Cài file .apk vào máy ảo bằng cách nào?
Có 2 cách để cài file .apk vào máy ảo:
- C1: sau khi khởi động máy ảo, kéo trực tiếp file .apk vào giao diện máy
- C2: Sử dụng câu lệnh ADB trong Command Prompt/Terminal khi máy ảo đang chạy:   db install <đường_dẫn_tới_file_app.apk>
# Tham khảo từ AI
- Cách cài Android và thiết lập máy ảo
- Các câu hỏi về appium, driver và android
=> hiểu sơ bộ về cách kiểm thử trên app
