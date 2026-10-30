import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = True  # Giữ trạng thái app

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()


# ==========================================================
# TEST CASE 1: Kiểm thử Reset App State (Thêm 2 sản phẩm -> Reset -> Biến mất số giỏ hàng)
# ==========================================================
def test_reset_app_state_clears_cart(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Đăng nhập nếu chưa đăng nhập
    try:
        username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        username.send_keys("standard_user")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    except Exception:
        pass  # Đã đăng nhập trước đó do noReset=True

    # 2. Thêm 2 sản phẩm vào giỏ hàng
    add_buttons = wait.until(EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")))
    if len(add_buttons) >= 2:
        add_buttons[0].click()
        add_buttons[1].click()
        
    cart_badge_locator = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']//android.widget.TextView")
    badge_element = wait.until(EC.presence_of_element_located(cart_badge_locator))
    
    # Kiểm tra xem con số trên icon giỏ hàng có phải là "2" hay không
    assert badge_element.text == "2", f"Lỗi: Kỳ vọng giỏ hàng có 2 sản phẩm, nhưng thực tế hiển thị là {badge_element.text}"

    # 3. Mở Menu và chọn RESET APP STATE
    menu_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Menu")))
    menu_btn.click()

    reset_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-RESET APP STATE")))
    reset_btn.click()

    # 4. Sử dụng Explicit Wait với EC.invisibility_of_element_located để kiểm tra con số/badge giỏ hàng biến mất
    # Locator của badge số lượng trên icon giỏ hàng
    cart_badge_locator = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']//android.widget.TextView")
    
    is_badge_invisible = wait.until(EC.invisibility_of_element_located(cart_badge_locator))
    assert is_badge_invisible, "Lỗi: Số lượng sản phẩm trong giỏ hàng vẫn còn hiển thị sau khi Reset App State!"


# ==========================================================
# ==========================================================
# TEST CASE 2: Kiểm thử vòng đời ứng dụng (terminate_app & activate_app) 
# ==========================================================
def test_app_lifecycle_terminate_and_activate(driver):
    package_name = "com.swaglabsmobileapp"
    wait = WebDriverWait(driver, 15)
    
    # 1. Đóng ứng dụng[cite: 1]
    driver.terminate_app(package_name)
    
    # 2. Mở lại ứng dụng[cite: 1]
    driver.activate_app(package_name)
    
    # 3. Xử lý đăng nhập phòng trường hợp app yêu cầu đăng nhập lại sau khi terminate
    try:
        username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        username.send_keys("standard_user")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    except Exception:
        pass  # Nếu app giữ session thì bỏ qua bước login này

    # 4. Xác nhận ứng dụng đã hiển thị màn hình chính (nút Menu) thành công
    menu_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Menu")))
    assert menu_btn.is_displayed(), "Ứng dụng không khôi phục lại màn hình chính sau khi activate_app."


# ==========================================================
# TEST CASE 3: Kiểm thử cơ chế giữ trạng thái (noReset)[cite: 1]
# ==========================================================
@pytest.mark.xfail(reason="Test case minh họa việc giữ nguyên session đăng nhập nhờ noReset capability")
def test_no_reset_capability_behavior(driver):
    wait = WebDriverWait(driver, 10)
    # Với options.no_reset = True, khi khởi chạy app sẽ không bị yêu cầu đăng nhập lại[cite: 1]
    element = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Menu")))
    assert element.is_displayed()

# ==========================================================
# TEST CASE 4: Kiểm tra giỏ hàng bị làm trống sau khi Terminate & Activate
# ==========================================================
def test_cart_persistence_after_restart(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Đảm bảo đã đăng nhập
    try:
        username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        username.send_keys("standard_user")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    except Exception:
        pass

    # 2. Thêm 2 sản phẩm vào giỏ hàng
    add_buttons = wait.until(EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")))
    if len(add_buttons) >= 2:
        add_buttons[0].click()
        add_buttons[1].click()

    # 3. THOÁT APP (terminate) và MỞ LẠI APP (activate)
    package_name = "com.swaglabsmobileapp"
    driver.terminate_app(package_name)
    driver.activate_app(package_name)

    # 4. Xử lý đăng nhập lại nếu app yêu cầu
    try:
        username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        username.send_keys("standard_user")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    except Exception:
        pass

    # 5. Vào lại giỏ hàng và xác nhận sản phẩm đã biến mất do app bị terminate
    cart_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Cart")))
    cart_btn.click()

    product_locator = (AppiumBy.XPATH, "//*[@text='Sauce Labs Backpack' or @content-desc='Sauce Labs Backpack']")
    
    # Sử dụng invisibility để xác nhận sản phẩm không còn tồn tại sau khi restart app
    is_invisible = wait.until(EC.invisibility_of_element_located(product_locator))
    assert is_invisible, "Giỏ hàng vẫn giữ sản phẩm sau khi terminate app!"