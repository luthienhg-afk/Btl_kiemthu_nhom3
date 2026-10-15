# Bước 1: Nhập (Import) các thư viện cần thiết từ Selenium
from selenium import webdriver


def test_smoke_the_internet():
  # Bước 2: Khởi tạo trình duyệt WebDriver (Mở Google Chrome)
  driver = webdriver.Chrome()

  try:
    # Bước 3: Điều hướng tới trang web cần kiểm tra ("The Internet")
    driver.get("https://the-internet.herokuapp.com/")

    # Bước 4: Lấy tiêu đề thực tế của trang web hiện tại
    actual_title = driver.title
    print(f"Tiêu đề lấy được từ trang web là: {actual_title}")

    # Bước 5: Kiểm tra / Xác nhận (Assert) xem tiêu đề có đúng là "The Internet" không
    assert actual_title == "The Internet", (
        f"Lỗi: Tiêu đề không khớp! Nhận được: '{actual_title}'"
    )
    print("Kiểm tra tiêu đề thành công!")

  finally:
    # Bước 6: Đóng trình duyệt và kết thúc phiên làm việc để giải phóng tài nguyên
    driver.quit()