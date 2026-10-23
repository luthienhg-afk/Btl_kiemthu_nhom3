import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Cấu hình thông số kết nối tới Appium Server & App Swag Labs
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='emulator-5554',                       # Tên lấy từ `adb devices`
    appPackage='com.swaglabsmobileapp',                # Package của Swag Labs
    appActivity='com.swaglabsmobileapp.MainActivity'  # Activity chính của Swag Labs
)

appium_server_url = 'http://127.0.0.1:4723'

class SwagLabsSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        # Khởi tạo driver kết nối với Appium
        options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.driver.implicitly_wait(10)  # Chờ tối đa 10s để tìm element

    def test_check_username_field(self) -> None:
        # Tìm ô nhập Username theo Accessibility ID
        username_field = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, 
            value='test-Username'
        )
        
        # Kiểm tra ô Username có đang hiển thị trên màn hình không
        self.assertTrue(username_field.is_displayed(), "Lỗi: Không tìm thấy ô nhập Username!")
        print("\n[SUCCESS] Chạy thành công: Đã mở Swag Labs và tìm thấy ô nhập Username!")

    def tearDown(self) -> None:
        # Đóng ứng dụng sau khi kiểm thử xong
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()