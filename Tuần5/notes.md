# Trả lời các câu hỏi ở phần đọc
## 1. Làm thế nào để tìm accessibility id của một nút trong ứng dụng?
Để tìm Accessibility ID của một phần tử/nút trên giao diện ứng dụng, thực hiện qua các bước sau:
- Sử dụng công cụ Appium Inspector (hoặc Android Studio Layout Inspector) để kết nối vào phiên làm việc (session) của máy ảo đang chạy ứng dụng.
- Dùng con trỏ chuột nhấp trực tiếp vào nút hoặc phần tử cần kiểm tra trên màn hình xem trước (preview) của Appium Inspector.
- Quan sát bảng thông tin chi tiết phần tử (Element Details) ở cột bên phải, tìm đến mục accessibility id (trên Android tương ứng với thuộc tính content-desc hoặc mã định danh test do nhà phát triển đặt).
## 2. Vì sao trên điện thoại nên ưu tiên accessibility id?
Accessibility ID luôn là chiến lược định vị được ưu tiên số 1 vì:
- Tốc độ thực thi nhanh nhất: Appium và hệ điều hành mobile truy tìm phần tử qua Accessibility ID nhanh hơn rất nhiều so với XPath 
- Độ ổn định cao: Accessibility ID ít bị thay đổi khi giao diện ứng dụng cập nhật thiết kế hoặc thay đổi bố cục (layout)
- Đa ngôn ngữ (Multi-language): Thuộc tính này thường cố định trong code nguồn, giúp kịch bản kiểm thử không bị gãy khi ứng dụng chuyển đổi giữa các ngôn ngữ hiển thị khác nhau (như Tiếng Việt / Tiếng Anh).
## 3. Sau khi đọc phải tự trả lời được: Nếu kết quả thực tế khác mong đợi thì pytest báo gì?
Khi kết quả thực tế khác với mong đợi :
- pytest (hoặc unittest) sẽ đánh dấu bài test đó ở trạng thái FAILED (hoặc ERROR).
- Hệ thống sẽ in ra thông báo lỗi AssertionError kèm theo đoạn so sánh chi tiết giữa giá trị thực tế (Actual) và giá trị mong đợi (Expected).   - Trình kiểm thử cung cấp bảng Stacktrace chỉ rõ chính xác dòng code bị lỗi và thông điệp cảnh báo do người viết test cài đặt (ví dụ: "Không tìm thấy màn Products!" hoặc "Password is required").
# nếu có dùng AI thì ghi đã hỏi AI điều gì, câu trả lời có đúng không, mình hiểu thêm được gì.
- Đã hỏi AI điều gì: Hỏi AI cách tối ưu code test đăng nhập 3 trường hợp bằng cách viết hàm trợ lý do_login để tránh lặp lại đoạn code nhập liệu.
- Câu trả lời có đúng không: Câu trả lời của AI chính xác hoàn toàn. Code chạy thành công cả 3 testcase trên máy ảo 
- Mình hiểu thêm được gì: Biết cách phân biệt giữa thuộc tính accessibility id cố định và chuỗi XPath linh hoạt nhưng chậm hơn. Biết cách đọc thông báo lỗi AssertionError để xác định chính xác nguyên nhân bài test thất bại khi kết quả không như kỳ vọng.  