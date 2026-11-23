
import os
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================
# 1. CAU HINH APPIUM
# ==================================================

APPIUM_SERVER = "http://127.0.0.1:4723"

CAPABILITIES = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:udid": "emulator-5554",
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
    "appium:noReset": False,
    "appium:newCommandTimeout": 300
}

USERNAME = "problem_user"
PASSWORD = "secret_sauce"
WAIT_TIME = 20

SCREENSHOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "screenshots"
)


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

PRODUCT_IMAGES = (
    AppiumBy.CLASS_NAME, "android.widget.ImageView"
)


# ==================================================
# 3. FIXTURE
# ==================================================

@pytest.fixture
def driver():

    options = UiAutomator2Options().load_capabilities(
        CAPABILITIES
    )

    app_driver = webdriver.Remote(
        command_executor=APPIUM_SERVER,
        options=options
    )

    yield app_driver

    app_driver.quit()


@pytest.fixture
def wait(driver):

    return WebDriverWait(driver, WAIT_TIME)


# ==================================================
# 4. HAM DUNG CHUNG
# ==================================================

def login_problem_user(driver, wait):

    username = wait.until(
        EC.element_to_be_clickable(USERNAME_FIELD)
    )

    password = wait.until(
        EC.element_to_be_clickable(PASSWORD_FIELD)
    )

    username.clear()
    username.send_keys(USERNAME)

    password.clear()
    password.send_keys(PASSWORD)

    wait.until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    ).click()

    wait.until(
        EC.visibility_of_element_located(PRODUCTS_TITLE)
    )


# ==================================================
# TC01 - DANG NHAP BANG TAI KHOAN problem_user
# ==================================================

def test_tc01_login_problem_user(driver, wait):

    username = wait.until(
        EC.visibility_of_element_located(USERNAME_FIELD)
    )

    password = wait.until(
        EC.visibility_of_element_located(PASSWORD_FIELD)
    )

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    login = wait.until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    )

    login.click()

    products = wait.until(
        EC.visibility_of_element_located(PRODUCTS_TITLE)
    )

    assert products.is_displayed()


# ==================================================
# TC02 - KIEM TRA TEN VA GIA SAN PHAM
# ==================================================

def test_tc02_check_product_information(driver, wait):

    login_problem_user(driver, wait)

    names = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_NAMES)
    )

    prices = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_PRICES)
    )

    assert len(names) > 0
    assert len(prices) > 0

    # Kiem tra text
    product_name = names[0].text
    product_price = prices[0].text

    assert product_name.strip() != ""
    assert product_price.strip() != ""

    # Kiem tra get_attribute()
    price_attribute = prices[0].get_attribute("text")

    assert price_attribute is not None


# ==================================================
# TC03 - KIEM TRA SCROLL GESTURE
# ==================================================

def test_tc03_scroll_products(driver, wait):

    login_problem_user(driver, wait)

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

    assert result is True

    names = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_NAMES)
    )

    assert len(names) > 0


# ==================================================
# TC04 - KIEM TRA IMAGEVIEW
# ==================================================

def test_tc04_check_product_images(driver, wait):

    login_problem_user(driver, wait)

    images = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_IMAGES)
    )

    assert len(images) > 0

    visible_images = [
        image for image in images
        if image.is_displayed()
    ]

    assert len(visible_images) > 0


# ==================================================
# TC05 - KIEM TRA SCREENSHOT
# ==================================================

def test_tc05_take_screenshots(driver, wait):

    login_problem_user(driver, wait)

    os.makedirs(
        SCREENSHOT_DIR,
        exist_ok=True
    )

    # Screenshot toan bo man hinh
    full_screen = os.path.join(
        SCREENSHOT_DIR,
        "tc05_full_screen.png"
    )

    assert driver.save_screenshot(full_screen)

    assert os.path.exists(full_screen)

    # Screenshot WebElement
    product = wait.until(
        EC.visibility_of_element_located(PRODUCT_NAMES)
    )

    element_screen = os.path.join(
        SCREENSHOT_DIR,
        "tc05_product_element.png"
    )

    assert product.screenshot(element_screen)

    assert os.path.exists(element_screen)
