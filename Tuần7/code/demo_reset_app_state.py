from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================
# 1. CAU HINH UNG DUNG
# ==================================================

PACKAGE = "com.swaglabsmobileapp"
PRODUCT = "Sauce Labs Backpack"
APPIUM_SERVER = "http://127.0.0.1:4723"

WAIT_TIME = 15

driver = None


# ==================================================
# 2. DESIRED CAPABILITIES
# ==================================================

options = UiAutomator2Options()

options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"

options.app_package = PACKAGE
options.app_activity = "com.swaglabsmobileapp.MainActivity"

# Yeu cau Appium giu lai du lieu ung dung
# khi khoi tao session, neu co the.
options.no_reset = True


# ==================================================
# 3. CAC HAM HO TRO
# ==================================================

def find_element(accessibility_id, text=None):
    """Tim phan tu bang accessibility ID hoac text."""

    elements = driver.find_elements(
        AppiumBy.ACCESSIBILITY_ID,
        accessibility_id
    )

    if elements:
        return elements[0]

    if text:
        xpath = (
            "//*[@text='" + text + "' "
            "or @content-desc='" + text + "']"
        )

        elements = driver.find_elements(
            AppiumBy.XPATH,
            xpath
        )

        if elements:
            return elements[0]

    return None


def wait_for_element(accessibility_id, text=None):
    """Cho toi khi phan tu xuat hien."""

    return WebDriverWait(
        driver, WAIT_TIME
    ).until(
        lambda d: find_element(accessibility_id, text)
    )


def click_element(accessibility_id, text=None):
    """Tim lai phan tu va thu bam neu DOM thay doi."""

    from selenium.common.exceptions import (
        StaleElementReferenceException,
        ElementClickInterceptedException,
    )

    def click_when_ready(d):
        element = find_element(accessibility_id, text)

        if element is None:
            return False

        try:
            if not element.is_displayed() or not element.is_enabled():
                return False

            element.click()
            return True

        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
        ):
            return False

    WebDriverWait(driver, WAIT_TIME).until(click_when_ready)

def product_locator():
    """Tra ve locator cua san pham trong gio hang."""
    return (
        AppiumBy.XPATH,
        "//*[@text='Sauce Labs Backpack' "
        "or @content-desc='Sauce Labs Backpack']"
    )

def login_if_needed():
    """Cho man hinh san sang, sau do dang nhap neu can."""

    print("    Dang cho giao dien ung dung...")

    def detect_screen(d):
        username = find_element("test-Username")
        password = find_element("test-Password")

        if username and password:
            return "login"

        if find_element("test-Menu"):
            return "home"

        return False

    # Cho toi khi nhan dien duoc man hinh login hoac trang chinh
    screen = WebDriverWait(driver, 30).until(
        detect_screen
    )

    if screen == "login":
        username = wait_for_element("test-Username")
        password = wait_for_element("test-Password")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        click_element("test-LOGIN", "LOGIN")

        print("    Da gui thong tin dang nhap.")

    # Cho trang chinh tai hien
    wait_for_element("test-Menu")
    wait_for_element("test-Cart")

    print("    PASS: Giao dien chinh da san sang.")


# ==================================================
# 4. DEMO CHINH
# ==================================================

try:
    print("\n" + "=" * 48)
    print(" DEMO TUAN 7 - APP STATE & RESET APP STATE")
    print("=" * 48)

    # ------------------------------------------------
    # BUOC 1: KET NOI APPIUM
    # ------------------------------------------------

    driver = webdriver.Remote(
        APPIUM_SERVER,
        options=options
    )

    print("\n[1] Ket noi Appium thanh cong.")
    print("[1] Da khoi tao phien Android.")

    # ------------------------------------------------
    # BUOC 2: TERMINATE APP VA ACTIVATE APP
    # ------------------------------------------------

    print("\n[2] DEMO VONG DOI UNG DUNG")

    driver.terminate_app(PACKAGE)
    print("    Da dong ung dung bang terminate_app().")

    driver.activate_app(PACKAGE)
    print("    Da mo lai ung dung bang activate_app().")

    # ------------------------------------------------
    # BUOC 3: DANG NHAP / KIEM TRA PHIEN
    # ------------------------------------------------

    print("\n[3] KIEM TRA TRANG THAI DANG NHAP")

    login_if_needed()

    # ------------------------------------------------
    # BUOC 4: THEM SAN PHAM VAO GIO
    # ------------------------------------------------

    print("\n[4] THEM SAN PHAM VAO GIO HANG")

    add_button = wait_for_element(
        "test-ADD TO CART",
        "ADD TO CART"
    )

    add_button.click()

    print("    Da bam ADD TO CART.")

    # ------------------------------------------------
    # BUOC 5: XAC NHAN SAN PHAM CO TRONG GIO
    # ------------------------------------------------

    print("\n[5] KIEM TRA TRUOC KHI RESET")

    click_element("test-Cart", "CART")

    WebDriverWait(driver, WAIT_TIME).until(
        lambda d: PRODUCT in d.page_source
    )

    print("    PASS: Gio hang co", PRODUCT)

    # ------------------------------------------------
    # ------------------------------------------------
    # BUOC 6: KIEM TRA TRANG THAI SAU KHI MO GIO HANG
    # ------------------------------------------------

    print("\n[6] KIEM TRA TRANG THAI UNG DUNG")

    if find_element("test-CONTINUE SHOPPING", "CONTINUE SHOPPING"):
        click_element(
            "test-CONTINUE SHOPPING",
            "CONTINUE SHOPPING"
        )
    else:
        wait_for_element("test-Menu")

    print("    PASS: Da tro ve man hinh san pham.")
    # ------------------------------------------------
    print("\n[7] THUC HIEN RESET APP STATE")

    # Cho nut Menu hien thi va bam lai neu giao dien thay doi
    wait_for_element("test-Menu", "Menu")
    click_element("test-Menu", "Menu")

# Cho menu Reset App State xuat hien roi moi bam
    wait_for_element("test-RESET APP STATE", "Reset App State")
    click_element(
        "test-RESET APP STATE",
        "Reset App State"
        )

    print("    Da chon Reset App State.")
    # ------------------------------------------------
    # BUOC 8: MO GIO HANG VA CHO SAN PHAM BI AN
    # ------------------------------------------------

    print("\n[8] KIEM TRA SAU KHI RESET")

    wait_for_element("test-Cart")
    click_element("test-Cart", "CART")

    WebDriverWait(driver, WAIT_TIME).until(
        lambda d: "YOUR CART" in d.page_source
    )

    # Explicit Wait: doi den khi san pham khong con hien thi.
    WebDriverWait(driver, WAIT_TIME).until(
        EC.invisibility_of_element_located(
            product_locator()
        )
    )

    print("    PASS: San pham khong con hien thi.")
    print("    PASS: Explicit Wait da xac nhan ket qua.")

    # Kiem tra bo sung bang page source.
    if PRODUCT not in driver.page_source:
        print("    PASS: Gio hang khong con", PRODUCT)
        print("\nKET LUAN: RESET APP STATE THANH CONG.")
    else:
        raise AssertionError(
            "San pham van con trong gio hang sau khi reset."
        )

    print("\nDEMO HOAN TAT: TAT CA CAC BUOC DA CHAY.")

except Exception as e:
    print("\n" + "=" * 48)
    print("DEMO THAT BAI")
    print("Loai loi:", type(e).__name__)
    print("Chi tiet:", str(e))
    print("=" * 48)

    raise

finally:
    if driver is not None:
        driver.quit()
        print("\nDa dong phien Appium.")
