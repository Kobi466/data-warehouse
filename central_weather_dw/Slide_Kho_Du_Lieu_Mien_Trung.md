# BỘ SLIDE TRÌNH CHIẾU BẢO VỆ ĐỒ ÁN (16 TRANG)
## ĐỀ TÀI: KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH/THÀNH MIỀN TRUNG (1999 - 2026)

* **Trường Đại học Công nghệ Thông tin & Truyền thông Việt - Hàn (VKU)**
* **Khoa**: Khoa học Máy tính
* **Bộ môn**: Hệ thống Thông tin & Kho Dữ Liệu
* **Tông màu thiết kế khuyến nghị**: Deep Navy (#1F497D), Ocean Sky Blue (#0078D4), Pure White (#FFFFFF), Warning Red (#A80000).

---

### SLIDE 1: TRANG BÌA ĐỀ TÀI
* **Tiêu đề chính**: KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH THÀNH MIỀN TRUNG (1999 - 2026)
* **Tiêu đề phụ**: Nghiên Cứu Chuỗi Số Liệu 28 Năm Phục Vụ Cảnh Báo Sớm và Khuyến Nghị Sinh Kế Người Dân
* **Sinh viên thực hiện**: Nhóm Đồ Án Kho Dữ Liệu VKU
* **Giảng viên hướng dẫn**: Giảng viên Bộ môn Kho Dữ Liệu & Hệ thống Thông tin
* **Ghi chú thuyết trình**: Giới thiệu trang trọng tên đề tài, cơ quan đào tạo và mục đích cốt lõi của nghiên cứu.

---

### SLIDE 2: NỘI DUNG BÁO CÁO (MỤC LỤC 5 PHẦN)
* **Phần 1**: Đặt vấn đề & Tính cấp thiết của thiên tai Miền Trung.
* **Phần 2**: Cơ sở lý thuyết Kho Dữ Liệu & Phương pháp luận Ralph Kimball.
* **Phần 3**: Phân tích nghiệp vụ & Thiết kế kiến trúc Fact Constellation (Galaxy Schema).
* **Phần 4**: Quy trình ETL tích hợp chuỗi dữ liệu mở Open-Meteo & ERA5 (1999 - 2026).
* **Phần 5**: Trực quan hóa Dashboard Power BI & Khuyến nghị hỗ trợ cộng đồng.
* **Điểm nhấn**: Khắc phục dứt điểm sai sót trong tài liệu tham khảo cũ và nâng tầm giá trị thực tiễn.

---

### SLIDE 3: TÍNH CẤP THIẾT CỦA THIÊN TAI MIỀN TRUNG
* Miền Trung là dải đất hẹp ngang, dốc đứng, hứng chịu mọi loại hình thiên tai khắc nghiệt nhất cả nước.
* **Chuỗi thiên tai lịch sử**:
  + *Tháng 11/1999*: "Đại hồng thủy thế kỷ" (Mưa 970mm/24h tại Huế, hơn 590 người thiệt mạng).
  + *Tháng 10/2020*: Đại lũ kép lịch sử trên các sông Thạch Hãn, sông Hương, sông Ngàn Sâu.
  + *Tháng 10/2022*: Mưa cực đoan đô thị Đà Nẵng (795mm), ngập sâu 1.5m - 2.0m.
  + *Tháng 11/2026 (Hiện tại)*: Đợt bão lũ đặc biệt lớn đang diễn ra trên diện rộng.
* **Đòi hỏi cấp bách**: Cần một hệ thống kho dữ liệu đa chiều, tập trung để phân tích quy luật và đưa ra cảnh báo sớm.

---

### SLIDE 4: MỤC TIÊU NGHIÊN CỨU & GIÁ TRỊ THỰC TIỄN
* Xây dựng Kho dữ liệu chuẩn quốc tế theo phương pháp luận chiều Kimball.
* Khai thác chuỗi dữ liệu gần 28 năm (1999 - 2026) cho 11 đơn vị hành chính cấp tỉnh miền Trung.
* Chuyển đổi từ phân tích mô tả quá khứ (Descriptive) sang khuyến nghị hành động tương lai (Prescriptive).
* Hỗ trợ người dân: Lịch mùa vụ nông nghiệp tránh lũ, an toàn thi công công trình và điều tiết hồ chứa.

---

### SLIDE 5: ĐỐI TƯỢNG & PHẠM VI NGHIÊN CỨU
* **Phạm vi không gian**: 11 đơn vị hành chính cấp tỉnh Miền Trung:
  + *2 Thành phố trực thuộc Trung ương*: Huế và Đà Nẵng (2 cực phát triển đô thị ven biển).
  + *9 Tỉnh trọng điểm*: Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Quảng Ngãi, Gia Lai, Đắk Lắk, Khánh Hòa, Lâm Đồng.
* **Phạm vi thời gian**: Gần 28 năm liên tục (01/11/1999 đến 09/11/2026).
* **Quy mô dữ liệu**: Hơn 112.000 bản ghi dữ liệu quan trắc hàng ngày kết hợp 24 đợt thiên tai cực đoan.

---

### SLIDE 6: PHƯƠNG PHÁP LUẬN THIẾT KẾ RALPH KIMBALL
* **Bước 1 - Business Process**: Giám sát khí quyển, mưa lũ và thiên tai cực đoan.
* **Bước 2 - Declare Grain**: Daily Grain cho quan trắc môi trường và Event Grain cho thiên tai.
* **Bước 3 - Identify Dimensions**: 5 Conformed Dimensions dùng chung.
* **Bước 4 - Identify Facts**: 6 bảng Fact chuyên biệt tối ưu hóa lưu trữ và truy vấn.
* Sử dụng khóa đại diện Surrogate Key kiểu số nguyên tăng tốc tối đa phép JOIN trong bộ nhớ.

---

### SLIDE 7: KIẾN TRÚC TỔNG THỂ FACT CONSTELLATION (GALAXY SCHEMA)
* **5 Conformed Dimensions**: `dim_date`, `dim_location`, `dim_time`, `dim_weather_condition`, `dim_wind_direction`.
* **6 Fact Tables chuyên biệt**: `fact_precipitation`, `fact_temperature`, `fact_wind`, `fact_solar_radiation`, `fact_atmospheric`, `fact_extreme_events`.
* **Ma trận Bus Matrix**: Kết nối trực giao, loại bỏ hoàn toàn hiện tượng dữ liệu thưa thớt (Sparse Data).
* Tính linh hoạt cao, dễ dàng tích hợp thêm các cảm biến IOT hoặc ảnh vệ tinh mới.

---

### SLIDE 8: THIẾT KẾ CHI TIẾT 5 CONFORMED DIMENSIONS
* `dim_date`: Tích hợp thêm cờ Mùa bão lũ (`is_typhoon_season`), chu kỳ mùa vụ và Pha ENSO (El Niño / La Niña).
* `dim_location`: Tọa độ, cao độ, phân vùng rủi ro và các lưu vực sông chính (Sông Hương, Sông Vu Gia - Thu Bồn...).
* `dim_weather_condition`: Chuẩn hóa theo bảng mã thời tiết WMO quốc tế.
* `dim_wind_direction`: 16 hướng gió, nhận diện rõ Gió mùa Đông Bắc và Gió phơn Tây Nam khô nóng.
* `dim_time`: 24 khung giờ và các cửa sổ thời gian hoạt động an toàn ngoài trời.

---

### SLIDE 9: THIẾT KẾ CHI TIẾT 6 FACT TABLES & GRAIN
* `fact_precipitation`: Lượng mưa (mm), xác suất mưa, bốc thoát hơi nước, cán cân nước, độ bão hòa đất.
* `fact_temperature`: Nhiệt độ không khí 2m, nhiệt độ đất 0cm, độ ẩm không khí, độ ẩm đất.
* `fact_wind`: Tốc độ gió 10m, gió giật, cấp gió Beaufort, tình trạng biển cho tàu thuyền.
* `fact_solar_radiation`: Bức xạ mặt trời, chỉ số UV, thời lượng nắng.
* `fact_atmospheric`: Áp suất khí quyển, tầm nhìn xa, độ che phủ mây.
* `fact_extreme_events`: Mưa đỉnh 24h, cấp báo động lũ (BĐ1 - BĐ3), thiệt hại kinh tế, người ảnh hưởng.

---

### SLIDE 10: QUY TRÌNH ETL TÍCH HỢP DỮ LIỆU
* **Nguồn dữ liệu**: Open-Meteo Historical Archive API kết hợp mô hình tái phân tích toàn cầu ERA5 (ECMWF).
* **Extract**: Trích xuất dữ liệu phân mảnh theo năm và tọa độ 11 tỉnh thành để kiểm soát lưu lượng.
* **Transform**: Nội suy tuyến tính dữ liệu khuyết thiếu, làm sạch ngoại lai, tính toán chỉ số phái sinh (`water_balance`).
* **Load**: Tự động hóa nạp dữ liệu vào VertiPaq Engine bằng tập lệnh Power Query M chuẩn hóa.

---

### SLIDE 11: LÀM SẠCH DỮ LIỆU & BẢO TOÀN GIÁ TRỊ CỰC ĐOAN
* Xử lý khuyết thiếu bằng nội suy tuyến tính dựa trên các trạm đo lân cận có cùng đặc điểm địa hình.
* Bảo tồn các giá trị mưa kỷ lục (Huế 970mm, Đà Nẵng 795mm) thông qua kiểm tra chéo với niên giám thiên tai quốc gia.
* Chuẩn hóa toàn bộ hệ thống đơn vị đo lường theo chuẩn quốc tế (°C, mm, m/s, hPa).
* Đảm bảo tính toàn vẹn tham chiếu (Referential Integrity) giữa 6 bảng Fact và 5 Dimension đạt 100%.

---

### SLIDE 12: DASHBOARD TRANG 1 - TỔNG QUAN KHÍ HẬU
* Hàng thẻ KPI: Nhiệt độ trung bình, Lượng mưa tích lũy, Tốc độ gió TB, Sự kiện cực đoan, Cán cân nước.
* Bộ lọc Slicers: 11 Tỉnh/Thành phố, Năm (1999 - 2026), Mùa khí hậu.
* Biểu đồ xu hướng Line & Column: Diễn biến lượng mưa và nhiệt độ qua 28 năm.
* Biểu đồ Hoa gió (Radar Chart): Nhận diện hướng gió bão Đông Bắc và gió phơn Tây Nam khô nóng.
* Biểu đồ cột xếp hạng lượng mưa tích lũy: Thừa Thiên Huế, Đà Nẵng, Quảng Trị luôn đứng đầu cả nước.

---

### SLIDE 13: DASHBOARD TRANG 2 - PHÂN TÍCH THIÊN TAI LỊCH SỬ (1999 - 2026)
* Thống kê tổng hợp: Thiệt hại hơn 97.800 tỷ đồng và 12.8 triệu lượt người dân bị ảnh hưởng.
* Biểu đồ ma trận bong bóng (Scatter Chart): Tương quan Lượng mưa 24h vs Cấp gió giật vs Mức độ thiệt hại.
* Phân loại nguyên nhân: Thiệt hại do bão gió mạnh (Xangsane 2006) vs Thiệt hại do đại lũ ngập lụt (1999, 2020, 2022).
* Bảng chi tiết 24 sự kiện thiên tai và các biện pháp ứng phó khẩn cấp của chính quyền.

---

### SLIDE 14: DASHBOARD TRANG 3 - CẢNH BÁO SỚM & HỖ TRỢ SINH KẾ
* **Hệ thống cảnh báo động**: Cấp báo động lũ sông (BĐ1 - BĐ3+), Nguy cơ sạt lở đất đồi núi, An toàn cấm biển ngư dân.
* **Khuyến nghị nông nghiệp (`[Crop Recommendation]`)**: Tuyệt đối không gieo cấy lúa vùng trũng tháng 9-11; Xuống giống lúa Đông Xuân tháng 12 tận dụng phù sa.
* **Khuyến nghị xây dựng (`[Construction Recommendation]`)**: Đình chỉ thi công khi mưa > 100mm hoặc gió > cấp 7.
* **Quản lý hồ chứa (`[Water Recommendation]`)**: Xả đáy đón lũ trước 24h khi cán cân nước > 300mm.

---

### SLIDE 15: KẾT LUẬN & HƯỚNG PHÁT TRIỂN ĐỀ TÀI
* Xây dựng thành công Kho dữ liệu mẫu mực, giải quyết trọn vẹn bài toán khí tượng bão lũ miền Trung.
* Khắc phục 100% các sai sót trong tài liệu tham khảo cũ.
* **Hướng mở rộng 1**: Chuyển đổi lên kiến trúc Cloud Data Lakehouse (Delta Lake / Spark) để lưu trữ ảnh vệ tinh và radar.
* **Hướng mở rộng 2**: Huấn luyện mô hình Deep Learning (LSTM / Transformer) dự báo mưa lũ cực đoan trước 72 giờ.
* **Hướng mở rộng 3**: Xây dựng ứng dụng di động cảnh báo thiên tai theo định vị GPS thời gian thực cho người dân.

---

### SLIDE 16: LỜI CẢM ƠN & HỘI ĐỒNG PHẢN BIỆN (Q&A)
* Xin chân thành cảm ơn quý Thầy Cô trong Hội đồng chấm đồ án tốt nghiệp!
* Kính chúc quý Thầy Cô sức khỏe, hạnh phúc và thành công!
* Nhóm sinh viên rất mong nhận được những ý kiến đóng góp quý báu của quý Thầy Cô!
