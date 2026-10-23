import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    # Đã cập nhật đúng đường dẫn tuyệt đối tới file APK trong thư mục làm việc
    options.app = r"C:\tester\.pytest_cache\app\swaglabs.apk"
    options.no_reset = False

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestSwagLabsLogin:

    def test_01_check_login_elements_exist(self, driver):
        """Bài 1: Kiểm tra các thành phần giao diện màn hình đăng nhập"""
        wait = WebDriverWait(driver, 15)
        
        username_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Password")))
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")))
        
        assert username_field.is_displayed(), "Không tìm thấy ô nhập Username"
        assert password_field.is_displayed(), "Không tìm thấy ô nhập Password"
        assert login_button.is_displayed(), "Không tìm thấy nút Login"

    def test_02_invalid_login(self, driver):
        """Bài 2: Đăng nhập với thông tin sai và kiểm tra thông báo lỗi"""
        wait = WebDriverWait(driver, 15)
        
        username_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Password")))
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")))
        
        # Nhập sai tài khoản/mật khẩu
        username_field.clear()
        username_field.send_keys("locked_out_user")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Kiểm tra hiển thị thông báo lỗi từ hệ thống
        error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Error message")))
        assert error_message.is_displayed(), "Không hiển thị thông báo lỗi khi đăng nhập thất bại"

    def test_03_valid_login_success(self, driver):
        """Bài 3: Đăng nhập thành công và xác nhận chuyển trang sản phẩm"""
        wait = WebDriverWait(driver, 15)
        
        username_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Password")))
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")))
        
        # Sử dụng tài khoản chuẩn hợp lệ
        username_field.clear()
        username_field.send_keys("standard_user")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Kiểm tra tiêu đề trang sản phẩm xuất hiện sau khi đăng nhập thành công
        products_title = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")))
        assert products_title.is_displayed(), "Đăng nhập thành công nhưng không chuyển đến trang sản phẩm"