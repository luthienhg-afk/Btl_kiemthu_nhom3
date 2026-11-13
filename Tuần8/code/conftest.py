
import pytest
import os
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = True

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver

    driver.quit()


# Tự động chụp ảnh khi test thất bại
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshot_dir = os.path.join(
                os.path.dirname(__file__),
                "screenshots"
            )

            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            filename = os.path.join(
                screenshot_dir,
                f"{item.name}_{timestamp}.png"
            )

            try:
                result = driver.save_screenshot(filename)

                if result:
                    print(f"\nDA CHUP ANH LOI: {filename}")
                else:
                    print("\nKHONG THE CHUP ANH LOI!")

            except Exception as e:
                print(f"\nLOI KHI CHUP ANH: {e}")
