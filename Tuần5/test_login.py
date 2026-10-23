import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Thiết lập kết nối tới Appium Server và máy ảo trước mỗi test case"""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    
    # Cấu hình thời gian chờ để tương thích tốt với máy ảo Android đời cao
    options.set_capability('uiautomator2ServerLaunchTimeout', 90000)
    options.set_capability('adbExecTimeout', 60000)
    options.set_capability('enforceAppInstall', True)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    """Testcase 1: Đăng nhập thành công với standard_user"""
    wait = WebDriverWait(driver, 15)
    
    # Nhập username và password theo Testcase 1
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))).send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    
    # Bấm nút Login
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    
    # Kiểm tra kết quả mong đợi: Chuyển sang màn Products
    products_title = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")))
    assert products_title.is_displayed(), "Lỗi: Không truy cập được vào màn hình Products!"

def test_login_locked_out_user(driver):
    """Testcase 2: Đăng nhập thất bại với locked_out_user (tài khoản bị khóa)"""
    wait = WebDriverWait(driver, 15)
    
    # Nhập username bị khóa và password
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))).send_keys("locked_out_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    
    # Bấm nút Login
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    
    # Kiểm tra kết quả mong đợi: Hiển thị thông báo tài khoản bị khóa
    error_msg = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Error message")))
    assert error_msg.is_displayed(), "Lỗi: Không hiển thị thông báo tài khoản bị khóa!"

def test_login_empty_password(driver):
    """Testcase 3: Đăng nhập thất bại do bỏ trống password"""
    wait = WebDriverWait(driver, 15)
    
    # Chỉ nhập username, để trống password
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))).send_keys("standard_user")
    
    # Bấm nút Login trực tiếp khi chưa nhập password
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    
    # Kiểm tra kết quả mong đợi: Báo lỗi Password is required
    error_msg = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Error message")))
    assert error_msg.is_displayed(), "Lỗi: Không hiển thị thông báo yêu cầu nhập password!"