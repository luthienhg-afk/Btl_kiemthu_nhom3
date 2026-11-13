import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


# 1. FIXTURE KHỞI TẠO & ĐÓNG DRIVER (PYTEST)
@pytest.fixture(scope="module")
def driver():
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android Emulator",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:autoGrantPermissions": True,
        "appium:noReset": False,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    appium_driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield appium_driver
    appium_driver.quit()


def get_cart_count(driver):
    """Đọc số lượng sản phẩm trên badge Giỏ hàng (dùng find_elements & text)"""
    badges = driver.find_elements(
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@content-desc='test-Cart']//android.widget.TextView"
    )
    if len(badges) > 0 and badges[0].text.isdigit():
        return int(badges[0].text)
    return 0


# 2. BƯỚC 1: ĐĂNG NHẬP VÀO MÀN HÌNH PRODUCTS
def test_01_login(driver):
    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))).send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    products_header = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS"))
    )
    assert products_header.is_displayed()


# 3. CHỨC NĂNG THÊM VÀO GIỎ HÀNG (find_elements, click, text)
def test_02_add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Thêm 2 sản phẩm đầu tiên
    for _ in range(2):
        add_buttons = wait.until(
            EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART"))
        )
        assert len(add_buttons) > 0
        add_buttons[0].click()
        time.sleep(0.5)

    assert get_cart_count(driver) == 2


# 4. CHỨC NĂNG KÉO THẢ VÀO GIỎ HÀNG (3.3 Drag & Drop, 7.2 ActionChains & mobile: dragGesture)
def test_03_drag_and_drop_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Bấm nút Toggle chuyển sang dạng danh sách (List View) để hiện icon kéo (test-Drag Handle)
    toggle_btns = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Toggle")
    if toggle_btns:
        toggle_btns[0].click()
        time.sleep(1)

    def get_source_and_drop_coords():
        # Lấy nút kéo của sản phẩm cuối cùng trên màn hình (chắc chắn chưa được thêm ở test_02)
        handles = wait.until(
            EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, "test-Drag Handle"))
        )
        src = handles[-1]

        # Vùng đích thả của Swag Labs là thanh "Drag here to add" (test-Cart drop zone)
        # nằm ngay bên dưới header PRODUCTS (khoảng giữa chiều ngang, Y = 22% chiều cao màn hình)
        drop_zones = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Cart drop zone")
        if drop_zones:
            tgt = drop_zones[0]
            tx = tgt.location["x"] + tgt.size["width"] // 2
            ty = tgt.location["y"] + tgt.size["height"] // 2
        else:
            # Tính tọa độ chính xác thanh ngang dưới header PRODUCTS
            products_bar = wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS"))
            )
            window_size = driver.get_window_size()
            tx = window_size["width"] // 2
            ty = products_bar.location["y"] + products_bar.size["height"] + 60
            tgt = products_bar

        return src, tgt, tx, ty

    # --- CÁCH 1: Áp dụng 7.2 ActionChains (click_and_hold, move_to_element, release, perform) ---
    source, target, _, _ = get_source_and_drop_coords()
    actions = ActionChains(driver)
    actions.click_and_hold(source).pause(0.5).move_to_element(target).release().perform()
    time.sleep(1)

    # --- CÁCH 2: Dùng W3C mobile: dragGesture kéo thẳng vào thanh Drop Zone ---
    if get_cart_count(driver) < 3:
        source_fresh, _, end_x, end_y = get_source_and_drop_coords()
        start_x = source_fresh.location["x"] + source_fresh.size["width"] // 2
        start_y = source_fresh.location["y"] + source_fresh.size["height"] // 2

        driver.execute_script(
            "mobile: dragGesture",
            {
                "startX": start_x,
                "startY": start_y,
                "endX": end_x,
                "endY": end_y,
                "speed": 1200
            }
        )
        time.sleep(1)

    assert get_cart_count(driver) == 3, f"Kéo thả thất bại, giỏ hàng hiện có: {get_cart_count(driver)}"


# 5. CHỨC NĂNG SỬA / XÓA SẢN PHẨM & POPUP/ALERT (3.5 Popup dialogs, 7.3 Alerts)
def test_04_edit_and_remove_from_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Mở màn hình Giỏ hàng (Cart)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
    time.sleep(1)

    # Sửa giỏ hàng: Xóa bớt 1 sản phẩm (từ 3 xuống còn 2)
    remove_buttons = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, "test-REMOVE"))
    )
    assert len(remove_buttons) > 0
    remove_buttons[0].click()
    time.sleep(0.5)

    # Xử lý 3.5 Popup dialogs / 7.3 Alerts (nếu có hộp thoại xác nhận)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        confirm_btns = driver.find_elements(AppiumBy.ID, "android:id/button1")
        if confirm_btns:
            confirm_btns[0].click()

    # Kiểm tra badge giỏ hàng giảm từ 3 xuống còn 2
    assert get_cart_count(driver) == 2

    # Xóa sạch toàn bộ sản phẩm còn lại trong giỏ hàng
    while get_cart_count(driver) > 0:
        btns = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")
        if btns:
            btns[0].click()
            time.sleep(0.5)
        else:
            break

    assert get_cart_count(driver) == 0

# 6. KIỂM THỬ NGOẠI LỆ (7.1 Exceptions: NoSuchElementException & pytest.raises)
def test_05_verify_exception_when_cart_empty(driver):
    """
    Khi giỏ hàng đã trống, việc tìm kiếm nút 'test-REMOVE' phải ném ra NoSuchElementException.
    """
    driver.implicitly_wait(0)
    with pytest.raises(NoSuchElementException):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")