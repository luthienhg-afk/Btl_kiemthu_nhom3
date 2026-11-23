
import os
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================
# 1. CAU HINH
# ==================================================

APPIUM_SERVER = "http://127.0.0.1:4723"

CAPABILITIES = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:udid": "emulator-5554",
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
    "appium:noReset": True,
    "appium:newCommandTimeout": 300
}

USERNAME = "problem_user"
PASSWORD = "secret_sauce"
WAIT_TIME = 20

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ==================================================
# 2. LOCATORS
# ==================================================

USERNAME_FIELD = (
    AppiumBy.ACCESSIBILITY_ID, "test-Username"
)

PASSWORD_FIELD = (
    AppiumBy.ACCESSIBILITY_ID, "test-Password"
)

LOGIN_BUTTON = (
    AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
)

PRODUCTS_TITLE = (
    AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS"
)

PRODUCT_NAMES = (
    AppiumBy.ACCESSIBILITY_ID, "test-Item title"
)

PRODUCT_PRICES = (
    AppiumBy.ACCESSIBILITY_ID, "test-Price"
)

PRODUCT_ITEMS = (
    AppiumBy.ACCESSIBILITY_ID, "test-Item"
)

PRODUCT_IMAGES = (
    AppiumBy.CLASS_NAME, "android.widget.ImageView"
)


# ==================================================
# 3. HAM HO TRO
# ==================================================

driver = None
wait = None
results = []


def check_result(name, function):
    try:
        function()
        results.append((name, True))
        print(f"[PASS] {name}")

    except Exception as error:
        results.append((name, False))
        print(f"[FAIL] {name}: {error}")


def get_element(locator):
    return wait.until(
        EC.presence_of_element_located(locator)
    )


def get_elements(locator):
    return wait.until(
        EC.presence_of_all_elements_located(locator)
    )


def screenshot_path(filename):
    return os.path.join(SCREENSHOT_DIR, filename)


# ==================================================
# 4. TC01 - DANG NHAP PROBLEM_USER
# ==================================================

def tc01_login_problem_user():

    username = get_element(USERNAME_FIELD)
    password = get_element(PASSWORD_FIELD)

    username.clear()
    username.send_keys(USERNAME)

    password.clear()
    password.send_keys(PASSWORD)

    login = get_element(LOGIN_BUTTON)
    login.click()

    get_element(PRODUCTS_TITLE)


# ==================================================
# 5. TC02 - KIEM TRA TEN VA GIA SAN PHAM
# ==================================================

def tc02_check_product_information():

    names = get_elements(PRODUCT_NAMES)
    prices = get_elements(PRODUCT_PRICES)

    assert len(names) > 0, "Khong tim thay ten san pham"
    assert len(prices) > 0, "Khong tim thay gia san pham"

    product_name = names[0].text
    product_price = prices[0].text

    price_attribute = prices[0].get_attribute("text")

    assert product_name.strip() != ""
    assert product_price.strip() != ""

    print("   Ten san pham:", product_name)
    print("   Gia san pham:", product_price)
    print("   get_attribute(text):", price_attribute)


# ==================================================
# 6. TC03 - KIEM TRA SCROLL GESTURE
# ==================================================

def tc03_scroll_products():

    size = driver.get_window_size()

    width = size["width"]
    height = size["height"]

    result = driver.execute_script(
        "mobile: scrollGesture",
        {
            "left": int(width * 0.1),
            "top": int(height * 0.25),
            "width": int(width * 0.8),
            "height": int(height * 0.6),
            "direction": "down",
            "percent": 0.75
        }
    )

    assert isinstance(result, bool)

    print("   Scroll result:", result)

    # Kiem tra lai san pham sau khi cuon
    names = get_elements(PRODUCT_NAMES)

    assert len(names) > 0


# ==================================================
# 7. TC04 - KIEM TRA IMAGEVIEW
# ==================================================

def tc04_check_product_images():

    images = get_elements(PRODUCT_IMAGES)

    assert len(images) > 0, "Khong tim thay ImageView"

    visible_images = [
        image for image in images
        if image.is_displayed()
    ]

    assert len(visible_images) > 0

    print("   Tong so ImageView:", len(images))
    print("   ImageView dang hien thi:", len(visible_images))


# ==================================================
# 8. TC05 - CHUP MAN HINH VA WEBELEMENT
# ==================================================

def tc05_take_screenshots():

    # Chup toan bo man hinh
    full_screen = screenshot_path(
        "problem_user_full_screen.png"
    )

    assert driver.save_screenshot(full_screen)

    # Chup rieng WebElement
    names = get_elements(PRODUCT_NAMES)

    product_element = names[0]

    element_screen = screenshot_path(
        "problem_user_element.png"
    )

    assert product_element.screenshot(element_screen)

    assert os.path.exists(full_screen)
    assert os.path.exists(element_screen)

    print("   Full screenshot:", full_screen)
    print("   WebElement screenshot:", element_screen)


# ==================================================
# 9. CHUONG TRINH CHINH
# ==================================================

def main():

    global driver, wait

    print("DEMO APPIUM - PROBLEM_USER")
    print("=" * 45)

    try:
        options = UiAutomator2Options().load_capabilities(
            CAPABILITIES
        )

        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER,
            options=options
        )

        wait = WebDriverWait(driver, WAIT_TIME)

        # TC01
        check_result(
            "TC01 - Dang nhap problem_user",
            tc01_login_problem_user
        )

        # TC02
        check_result(
            "TC02 - Kiem tra ten va gia san pham",
            tc02_check_product_information
        )

        # TC03
        check_result(
            "TC03 - Thuc hien scrollGesture",
            tc03_scroll_products
        )

        # TC04
        check_result(
            "TC04 - Kiem tra ImageView",
            tc04_check_product_images
        )

        # TC05
        check_result(
            "TC05 - Screenshot man hinh va WebElement",
            tc05_take_screenshots
        )

    except Exception as error:
        print("[FAIL] Khoi tao Appium:", error)

    finally:

        if driver is not None:
            driver.quit()

        print("=" * 45)
        print("KET QUA DEMO")

        passed = sum(1 for _, result in results if result)
        failed = len(results) - passed

        print(f"PASS: {passed}")
        print(f"FAIL: {failed}")
        print(f"TONG SO TC: {len(results)}")

        print("=" * 45)


if __name__ == "__main__":
    main()
