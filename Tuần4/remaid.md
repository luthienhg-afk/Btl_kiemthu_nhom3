# HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY BÀI KIỂM THỬ TỰ ĐỘNG (MOBILE APP) - TUẦN 04

Thư mục này chứa bài kiểm thử tự động đầu tiên (Smoke Test) cho ứng dụng Mobile **Swag Labs** sử dụng **Appium** và **pytest**.

---

## 1. Yêu cầu môi trường (Prerequisites)

Trước khi chạy, hãy đảm bảo máy tính của bạn đã cài đặt các công cụ sau:

*   **Node.js**: Phiên bản LTS (dùng để cài và chạy Appium Server).
*   **Python**: Phiên bản 3.10+
*   **Java JDK**: JDK 17 (Cấu hình biến môi trường `JAVA_HOME`).
*   **Android Studio**: Cài đặt Android SDK và tạo một máy ảo Android (AVD) - ví dụ: Pixel 4 / Android 11+. (Cấu hình biến môi trường `ANDROID_HOME`).
*   **Appium Server**: Cài đặt qua terminal bằng lệnh:
    ```bash
    npm install -g appium
    ```
*   **UiAutomator2 Driver**: Cài đặt driver kiểm thử cho Android:
    ```bash
    appium driver install uiautomator2
    ```

---

## 2. Cài đặt Thư viện Python

Mở terminal/cmd tại thư mục dự án và cài đặt các thư viện cần thiết:

```bash
pip install pytest Appium-Python-Client
```

---

## 3. Chuẩn bị ứng dụng và máy ảo

1.  **Tải file ứng dụng (`.apk`)**: Tải file Swag Labs `.apk` về và lưu vào thư mục dự án (hoặc biết chính xác đường dẫn file).
2.  **Bật máy ảo Android**:
    *   Mở Android Studio -> **Virtual Device Manager** -> Bấm **Play** để khởi động máy ảo (AVD).
    *   Hoặc kết nối điện thoại Android thật đã bật chế độ **USB Debugging**.
3.  **Kiểm tra thiết bị kết nối**:
    Mở terminal và gõ:
    ```bash
    adb devices
    ```
    *Ghi lại mã thiết bị (`device_name`, ví dụ: `emulator-5554`).*

---

## 4. Các bước khởi chạy Automation Test

### Bước 1: Khởi động Appium Server
Mở 01 cửa sổ Terminal/Command Prompt mới và gõ lệnh:
```bash
appium
```
*(Giữ cửa sổ này chạy ngầm trong suốt quá trình test).*

### Bước 2: Chạy bài kiểm thử (test_smoke.py)
Mở một cửa sổ Terminal khác tại thư mục `tuan-04/` và chạy lệnh:

```bash
pytest test_smoke.py
```

---

## 5. Kết quả mong đợi

*   Appium Server nhận kết nối từ script Python.
*   Ứng dụng Swag Labs tự động mở trên máy ảo Android.
*   Hệ thống kiểm tra sự tồn tại của ô nhập đăng nhập (**Username** / **Password**).
*   Terminal hiển thị thông báo test thành công: **`1 passed`**.