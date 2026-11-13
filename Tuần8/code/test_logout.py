
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)

WAIT_TIME = 20


def login(driver):
    """Đăng nhập vào ứng dụng Swag Labs."""
    wait = WebDriverWait(driver, WAIT_TIME)

    username = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        )
    )
    username.send_keys("standard_user")

    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "test-Password"
    ).send_keys("secret_sauce")

    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
        )
    )


def test_logout_success(driver):
    """TC01: Kiểm tra chức năng đăng xuất."""
    wait = WebDriverWait(driver, WAIT_TIME)

    try:
        login(driver)

        # Mở Menu
        menu = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
            )
        )
        menu.click()

        # Chọn LOGOUT
        logout = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT")
            )
        )
        logout.click()

        # Xác nhận quay về màn hình Login
        wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Username")
            )
        )

        assert driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).is_displayed()

        print("Đăng xuất thành công!")

    except (
        NoSuchElementException,
        TimeoutException,
        StaleElementReferenceException
    ) as e:
        driver.save_screenshot("logout_error.png")
        pytest.fail(f"Lỗi khi đăng xuất: {e}")

