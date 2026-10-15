import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Định nghĩa một fixture của pytest để quản lý trình duyệt tự động
@pytest.fixture
def driver():
    # Khởi tạo một phiên làm việc mới với trình duyệt Google Chrome
    browser = webdriver.Chrome()
    # Đặt thời gian chờ ngầm định tối đa 10 giây cho các lệnh tìm kiếm phần tử
    browser.implicitly_wait(10)
    yield browser  # Cung cấp đối tượng browser cho hàm test chạy
    # Sau khi test xong, tự động đóng trình duyệt để giải phóng bộ nhớ
    browser.quit()

# -------------------------------------------------------------------------
# BÀI 1: KIỂM THỬ ĐĂNG NHẬP THÀNH CÔNG
# -------------------------------------------------------------------------
def test_login_success(driver):
    # Bước 1: Mở trang web đăng nhập mẫu bằng URL
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Bước 2: Tìm ô nhập tên đăng nhập (Username) dựa vào thuộc tính ID và nhập tài khoản đúng
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    
    # Bước 3: Tìm ô nhập mật khẩu (Password) dựa vào thuộc tính ID và nhập mật khẩu đúng
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # Bước 4: Tìm nút đăng nhập bằng CSS Selector dựa vào class .radius và thực hiện click chuột
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    
    # Bước 5: Sử dụng WebDriverWait để chủ động chờ tối đa 10 giây cho đến khi URL chuyển sang trang bảo mật chứa chữ "secure"
    WebDriverWait(driver, 10).until(EC.url_contains("secure"))
    
    # Bước 6: Kiểm tra (assert) xem trong đường dẫn URL hiện tại có thực sự chứa từ "secure" hay không (đảm bảo đăng nhập thành công)
    assert "secure" in driver.current_url

# -------------------------------------------------------------------------
# BÀI 2: KIỂM THỬ ĐĂNG NHẬP THẤT BẠI (Do sai mật khẩu)
# -------------------------------------------------------------------------
def test_login_failed_wrong_password(driver):
    # Bước 1: Mở lại trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Bước 2: Nhập đúng tên đăng nhập nhưng nhập sai mật khẩu cố ý
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("sai_mat_khau_123")
    
    # Bước 3: Click vào nút đăng nhập
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    
    # Bước 4: Lấy nội dung thông báo lỗi hiển thị trên trang (thông qua phần tử có ID là flash)
    error_text = driver.find_element(By.ID, "flash").text
    
    # Bước 5: Kiểm tra xem câu thông báo lỗi có chứa đoạn text "Your password is invalid!" hay không
    assert "Your password is invalid!" in error_text

# -------------------------------------------------------------------------
# BÀI 3: KIỂM THỬ ĐĂNG NHẬP THẤT BẠI (Do để trống thông tin)
# -------------------------------------------------------------------------
def test_login_failed_empty_input(driver):
    # Bước 1: Mở trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Bước 2: Bỏ trống hoàn toàn hai ô username và password, bấm nút đăng nhập luôn
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    
    # Bước 3: Lấy nội dung thông báo lỗi hệ thống trả về
    error_text = driver.find_element(By.ID, "flash").text
    
    # Bước 4: Kiểm tra xem thông báo lỗi có nhắc đến việc sai tên đăng nhập/trống thông tin hay không
    assert "Your username is invalid!" in error_text