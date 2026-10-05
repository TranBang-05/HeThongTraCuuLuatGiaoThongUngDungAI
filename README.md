# HƯỚNG DẪN SỬ DỤNG

## HỆ THỐNG TRA CỨU LUẬT GIAO THÔNG ỨNG DỤNG TRÍ TUỆ NHÂN TẠO

## 1. Giới thiệu

### 1.1. Mục đích

Hệ thống tra cứu Luật giao thông được xây dựng nhằm hỗ trợ người dùng tìm kiếm và tham khảo các quy định pháp luật liên quan đến giao thông bằng cách nhập câu hỏi hoặc tình huống thực tế dưới dạng ngôn ngữ tự nhiên.

Hệ thống tiếp nhận câu hỏi, thực hiện quá trình phân tích và tìm kiếm các điều luật có mức độ phù hợp với nội dung truy vấn. Kết quả tra cứu cung cấp các thông tin liên quan đến văn bản pháp luật, nội dung quy định và thông tin xử phạt khi dữ liệu có chứa các thông tin tương ứng.

### 1.2. Đối tượng sử dụng

Hệ thống hướng đến các đối tượng có nhu cầu tìm hiểu và tra cứu các quy định pháp luật trong lĩnh vực giao thông, chẳng hạn như:
- Sinh viên, học sinh.
- Người tham gia giao thông.
- Người có nhu cầu tìm hiểu các quy định về giao thông.

### 1.3. Phạm vi sử dụng

Hệ thống hỗ trợ tra cứu các quy định pháp luật giao thông được xây dựng và lưu trữ trong cơ sở dữ liệu của hệ thống.

Kết quả tra cứu có mục đích hỗ trợ người dùng tìm kiếm và tham khảo thông tin, không thay thế việc đối chiếu với văn bản pháp luật hiện hành.

## 2. Yêu cầu sử dụng hệ thống

Để triển khai và sử dụng hệ thống, máy tính cần đáp ứng các yêu cầu cơ bản sau:
- Hệ điều hành Windows hoặc hệ điều hành có khả năng hỗ trợ Python.
- Python đã được cài đặt.
- Các thư viện cần thiết của hệ thống đã được cài đặt.
- Trình duyệt web như Google Chrome, Microsoft Edge hoặc Firefox.

## 3. Khởi động hệ thống

Mở thư mục dự án và thực hiện lệnh sau tại Terminal hoặc Command Prompt:

```bash
python -m streamlit run app.py
```

Sau khi lệnh được thực thi, Streamlit sẽ khởi động ứng dụng và cung cấp địa chỉ truy cập. Mở địa chỉ được hiển thị trên trình duyệt để truy cập giao diện hệ thống.

### 3.1. Tra cứu thông tin

Sau khi hệ thống được khởi động bằng Streamlit, người dùng có thể thực hiện tra cứu thông qua giao diện trên trình duyệt.

Bước 1: Nhập câu hỏi hoặc tình huống giao thông vào ô “Nhập câu hỏi”.
Ví dụ: “Xe máy vượt đèn đỏ bị phạt bao nhiêu?”

Bước 2: Nhấn nút “Tra cứu ngay”.

Bước 3: Xem danh sách các điều luật được hệ thống trả về và lựa chọn kết quả phù hợp với nội dung cần tra cứu.

### 3.2. Xem kết quả

Mỗi kết quả tra cứu có thể bao gồm các thông tin sau:
- Văn bản: Tên văn bản pháp luật liên quan.
- Mã điều luật: Thông tin xác định điều luật tương ứng.
- Căn cứ pháp lý: Điều, khoản và văn bản liên quan.
- Nội dung quy định: Nội dung của điều luật được hệ thống lưu trữ.
- Thông tin xử phạt: Mức phạt, thông tin trừ điểm giấy phép lái xe (GPLX) và hình thức xử phạt bổ sung nếu có.

Các kết quả được sắp xếp theo mức độ phù hợp với câu hỏi của người dùng.

## 4. Lưu ý khi sử dụng

Để nâng cao khả năng tìm kiếm và giúp hệ thống xác định đúng nội dung cần tra cứu, người dùng nên lưu ý:
- Nên nhập câu hỏi có nội dung cụ thể và thể hiện rõ vấn đề cần tra cứu.
- Có thể sử dụng câu hỏi bằng ngôn ngữ tự nhiên, không bắt buộc phải nhập chính xác tên hoặc số điều luật.
- Khi tra cứu mức phạt, nên nêu rõ loại phương tiện và hành vi vi phạm nếu có thể.
- Nếu hệ thống không trả về kết quả phù hợp, người dùng nên viết lại câu hỏi và bổ sung các từ khóa cụ thể hơn.
- Kết quả tra cứu phụ thuộc vào phạm vi và chất lượng dữ liệu pháp luật được xây dựng trong hệ thống.
- Thông tin hiển thị có mục đích hỗ trợ tra cứu và tham khảo.
- Khi sử dụng thông tin cho các trường hợp thực tế, người dùng nên đối chiếu với văn bản pháp luật hiện hành để bảo đảm tính chính xác và phù hợp với quy định tại thời điểm tra cứu.