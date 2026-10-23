## I. Tóm tắt điều đã học được trong tuần

1. **Kiến trúc Appium:**
   * Hiểu được mô hình Client-Server của Appium: Script test (Python) hoạt động như một Client gửi request qua giao thức WebDriver đến Appium Server, sau đó Appium Server chuyển lệnh sang driver `UiAutomator2` để điều khiển ứng dụng trên Android.
2. **Quy trình chạy test:**
   * Biết cách khởi động máy ảo Android (AVD) thông qua Android Studio và kiểm tra kết nối thiết bị bằng `adb devices`.
   * Biết cách khởi động Appium Server từ Command Line.
   * Biết cách viết và chạy kịch bản kiểm thử cơ bản (`test_smoke.py`) bằng framework `pytest`.

---

## II. Trả lời các câu hỏi đọc tài liệu trước buổi học

### 1. Appium Client, Appium Server và Driver lần lượt chạy ở đâu?
* **Appium Client:** Chạy ngay trên máy tính của tester (trong chính kịch bản Python/Pytest đang thực thi).
* **Appium Server:** Chạy trên máy tính của tester (dưới dạng dịch vụ Node.js lắng nghe ở cổng mặc định `4723`).
* **UiAutomator2 Driver:** Được Appium cài đặt và chạy trực tiếp bên trong thiết bị/máy ảo Android để tương tác với hệ điều hành và app.

### 2. Bạn chọn cấu hình máy ảo Android (AVD) nào và vì sao?
* **Cấu hình chọn:** Google Pixel 8, Android Version 11.0 (API Level 37).
* **Lý do chọn:** Đây là phiên bản stable, nhẹ, chạy mượt mà trên đa số máy tính sinh viên và tương thích rất tốt với driver `UiAutomator2` của Appium mà không gặp lỗi thiếu tài nguyên.

### 3. Cài file `.apk` vào máy ảo bằng cách nào?
* **Cách 1 (Kéo thả):** Kéo trực tiếp file `SwagLabs.apk` từ thư mục máy tính và thả vào màn hình máy ảo Android đang chạy.
* **Cách 2 (Dùng ADB Command):** Mở Terminal và gõ lệnh:
  ```bash
  adb install path/to/SwagLabs.apk
  ```
* **Cách 3 (Tự động hóa qua Appium):** Khai báo đường dẫn file `.apk` trong thông số `app` của `Desired Capabilities` trong script Python, Appium sẽ tự động đẩy và cài app vào máy ảo mỗi khi chạy test.

---

## III. Nhật ký trao đổi với AI (AI Prompting & Self-Learning)

* **Câu hỏi đã hỏi AI:**
  > *"Làm sao để sửa lỗi `WebDriverException: Original error: Could not find AVD` khi chạy script Appium Python?"*
* **Câu trả lời từ AI:**
  > AI hướng dẫn kiểm tra lại tên máy ảo trong Android Studio, đảm bảo tên truyền vào tham số `deviceName` hoặc `avd` trùng khớp chính xác với kết quả trả về từ lệnh `adb devices`.
* **Đánh giá câu trả lời:**
  * Câu trả lời của AI **chính xác**.
  * **Thực tế gặp phải:** Lỗi xảy ra do nhập sai tên thiết bị emulator. Sau khi sửa tên `deviceName` thành `"emulator-5554"` thì script chạy thành công.

---

## IV. Đóng góp và ghi chú cá nhân

* **Lỗi gặp phải khi cài đặt:** Ban đầu quên chưa cài `uiautomator2` driver cho Appium nên bị báo lỗi driver unsupported.
* **Cách xử lý:** Đã sửa bằng cách chạy lệnh `appium driver install uiautomator2`.