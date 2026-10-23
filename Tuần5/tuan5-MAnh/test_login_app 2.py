import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver():
    """Thiết lập phiên làm việc chung cho toàn bộ class Test với timeout mở rộng"""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.app = r"C:\tester\.pytest_cache\app\swaglabs.apk"
    options.no_reset = False

    # Cấu hình timeout chống lỗi khởi tạo instrumentation
    options.set_capability("appium:adbExecTimeout", 60000)
    options.set_capability("appium:androidInstallTimeout", 90000)
    options.set_capability("appium:uiautomator2ServerLaunchTimeout", 60000)
    options.set_capability("appium:uiAutomator2ServerInstallTimeout", 60000)

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
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Login")))
        
        assert username_field.is_displayed(), "Không tìm thấy ô nhập Username"
        assert password_field.is_displayed(), "Không tìm thấy ô nhập Password"
        assert login_button.is_displayed(), "Không tìm thấy nút Login"

    def test_02_invalid_login(self, driver):
        """Bài 2: Đăng nhập với thông tin sai (locked_out_user) và kiểm tra thông báo lỗi"""
        wait = WebDriverWait(driver, 15)
        
        # 💡 Khởi động lại app trước khi chạy test 02 để đảm bảo màn hình sạch sẽ
        driver.terminate_app("com.swaglabsmobileapp")
        driver.activate_app("com.swaglabsmobileapp")
        
        username_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Password")))
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Login")))
        
        # Nhập tài khoản bị khóa
        username_field.clear()
        username_field.send_keys("locked_out_user")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        
        # Ẩn bàn phím ảo trước khi bấm Login
        try:
            driver.hide_keyboard()
        except Exception:
            pass
            
        login_button.click()
        
        # 💡 Sử dụng XPath linh hoạt bắt thông báo lỗi của Swag Labs
        error_message = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[@content-desc='test-Error message' or contains(@text, 'locked') or contains(@text, 'Sorry')]"))
        )
        assert error_message.is_displayed(), "Không hiển thị thông báo lỗi khi đăng nhập thất bại"

    def test_03_valid_login_success(self, driver):
        """Bài 3: Đăng nhập thành công với standard_user và xác nhận chuyển trang sản phẩm"""
        wait = WebDriverWait(driver, 15)
        
        # 💡 Khởi động lại app trước khi chạy test 03 để đảm bảo màn hình sạch sẽ
        driver.terminate_app("com.swaglabsmobileapp")
        driver.activate_app("com.swaglabsmobileapp")
        
        username_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password_field = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Password")))
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Login")))
        
        # Sử dụng tài khoản chuẩn hợp lệ
        username_field.clear()
        username_field.send_keys("standard_user")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        
        # Ẩn bàn phím ảo trước khi bấm Login
        try:
            driver.hide_keyboard()
        except Exception:
            pass
            
        login_button.click()
        
        # Kiểm tra biểu tượng giỏ hàng xuất hiện xác nhận vào trang sản phẩm thành công
        cart_icon = wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Cart"))
        )
        assert cart_icon.is_displayed(), "Đăng nhập thành công nhưng không hiển thị biểu tượng giỏ hàng trên trang sản phẩm"