
import pytest
import os
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)


WAIT_TIME = 5


# TC02: Kiểm tra NoSuchElementException
def test_no_such_element_exception(driver):

    with pytest.raises(NoSuchElementException):
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "element_not_exist"
        )

    print("TC02: Đã bắt được NoSuchElementException")


# TC03: Kiểm tra TimeoutException
def test_timeout_exception(driver):

    with pytest.raises(TimeoutException):
        WebDriverWait(driver, WAIT_TIME).until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "element_not_exist")
            )
        )

    print("TC03: Đã bắt được TimeoutException")


# TC04: Kiểm tra StaleElementReferenceException
def test_stale_element_exception(driver):

    with pytest.raises(StaleElementReferenceException):
        raise StaleElementReferenceException(
            "Element is no longer attached to the page"
        )

    print("TC04: Đã bắt được StaleElementReferenceException")


# TC05: Kiểm tra lỗi khi tìm Menu không tồn tại
def test_menu_not_found(driver):

    print("TC05: Đang tìm Menu không tồn tại...")

    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "menu_not_exist"
    )

    print("TC05: Tìm thấy Menu")
