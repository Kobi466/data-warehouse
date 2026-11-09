# Kế Hoạch Triển Khai: Bộ Sản Phẩm Tài Liệu Đồ Án Kho Dữ Liệu Thời Tiết & Thiên Tai Miền Trung (1999 - 2026)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng trọn vẹn bộ 3 sản phẩm tài liệu học thuật hoàn chỉnh (Báo cáo nghiên cứu Word 5 chương, Bài thuyết trình & Ngân hàng câu hỏi phản biện Word, Slide trình chiếu PowerPoint) cho đồ án Kho dữ liệu Thời tiết & Thiên tai Miền Trung, đặt trong thư mục độc lập `central_weather_dw/` (tách biệt hoàn toàn với thư mục tham chiếu `docs/`).

**Architecture:** Thiết kế Kho Dữ Liệu theo mô hình Fact Constellation (Galaxy Schema) theo phương pháp luận chiều của Ralph Kimball: 5 Conformed Dimensions và 6 Fact Tables phân tích chuyên sâu các hiện tượng thời tiết cực đoan, bão lũ, ngập lụt, sạt lở và cân bằng tài nguyên nước.

**Tech Stack:** Python 3.11+, `python-docx` (sinh file Word chuẩn format), `python-pptx` (sinh slide PowerPoint hiện đại), kiến trúc dữ liệu Galaxy Schema / OLAP Kimball.

**Spec:** Kế thừa nghiệp vụ và các chỉ số khí tượng từ thư mục tham chiếu `docs/`, nâng cấp toàn diện phạm vi không gian (11 tỉnh/thành miền Trung), thời gian (1999 - 2026) và sửa dứt điểm các lỗi văn bản trong tài liệu cũ.

---

## Global Constraints

- **Tách biệt tuyệt đối**: Thư mục `docs/` cũ giữ nguyên 100% làm tài liệu tham khảo và đối sánh. Toàn bộ sản phẩm đồ án mới được tạo trong `central_weather_dw/`.
- **Phạm vi đối tượng**: Tập trung đúng **11 đơn vị hành chính cấp tỉnh của Miền Trung** (gồm 9 tỉnh: Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Quảng Ngãi, Gia Lai, Đắk Lắk, Khánh Hòa, Lâm Đồng và 2 thành phố trực thuộc Trung ương: **Huế** và **Đà Nẵng**).
- **Phạm vi thời gian**: Chuỗi dữ liệu gần 28 năm (từ trận **Đại hồng thủy thế kỷ tháng 11/1999** đến đợt thiên tai tháng **11/2026** hiện nay).
- **Phạm vi công việc**: Trọng tâm là tạo ra các **sản phẩm tài liệu hoàn chỉnh như trong thư mục `docs/`**, chưa triển khai code kỹ thuật ETL phức tạp.
- **Quy chuẩn chất lượng tài liệu**: Định dạng chuẩn đồ án tốt nghiệp công nghệ thông tin (Font Times New Roman/Calibri, căn lề chuẩn, bảng biểu rõ ràng, không có lỗi copy-paste lạc đề).

---

## Review Focus (Các Vấn Đề Phản Biện Cốt Lõi Cần Làm Rõ Trong Tài Liệu)

1. **Tính cấp thiết và thực tế của 11 đơn vị hành chính miền Trung**: Làm rõ vì sao chọn 11 tỉnh thành sau cải cách hành chính (Huế và Đà Nẵng là 2 cực phát triển đô thị ven biển, các tỉnh còn lại đại diện cho các lưu vực sông xung yếu).
2. **Khắc phục lỗi kiến thức ở bản cũ**: Bản cũ dính lỗi copy-paste về "thương mại điện tử" và đứt đoạn ở mục 2.3.2. Bản mới phải hoàn thiện 100% cả 5 chương về khí tượng thủy văn.
3. **Mô hình Galaxy Schema vs Star Schema**: Giải thích vì sao cần 6 Fact riêng biệt thay vì 1 Fact khổng lồ (tránh thưa dữ liệu và phân tách các chỉ số đo lường độc lập).
4. **Mức độ chi tiết (Grain)**: Giải trình grain của hệ thống (Daily Grain cho các chỉ số quan trắc và Event Grain cho các đợt bão lũ cực đoan).
5. **Khuyến nghị hành động (Prescriptive Analytics)**: Dữ liệu giúp gì cho người dân miền Trung? (Lịch thời vụ tránh lũ, cảnh báo an toàn thi công xây dựng, bản đồ cảnh báo nguy cơ thiếu nước/ngập sâu).

---

## File Structure

```
central_weather_dw/
├── PLAN.md                                        # Bản kế hoạch chi tiết này
├── BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx            # Sản phẩm 1: Báo cáo đồ án 5 chương hoàn chỉnh
├── BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx     # Sản phẩm 2: Kịch bản 15 phút & Ngân hàng 40 câu hỏi
├── Slide_Kho_Du_Lieu_Mien_Trung.pptx              # Sản phẩm 3: Bộ slide trình chiếu 16 trang
└── generate_documents.py                          # Script Python tự động sinh 3 file trên chuẩn format
```

---

## Danh Sách Nhiệm Vụ Chi Tiết (Tasks)

### Task 1: Biên Soạn Báo Cáo Đồ Án Hoàn Chỉnh 5 Chương (`BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx`)

**Files:**
- Output: `central_weather_dw/BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx`
- Script: `central_weather_dw/build_report.py`

**Nội dung chi tiết 5 Chương chuẩn học thuật:**
- **Trang bìa & Lời nói đầu**: Đề tài: *"PHÂN TÍCH VÀ XÂY DỰNG KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH THÀNH MIỀN TRUNG GIAI ĐOẠN 1999 - 2026 PHỤC VỤ CẢNH BÁO VÀ SINH KẾ NGƯỜI DÂN"*. Lời nói đầu chuẩn xác 100% về bão lũ, biến đổi khí hậu miền Trung (loại bỏ hoàn toàn lỗi thương mại điện tử).
- **Chương 1: Giới thiệu & Tổng quan Đề tài**:
  - 1.1. Lý do chọn đề tài (bối cảnh thiên tai miền Trung, rốn bão lũ, trận đại hồng thủy 1999 đến bão lũ 11/2026).
  - 1.2. Mục tiêu nghiên cứu (4 mục tiêu: Nghiên cứu nghiệp vụ, Thiết kế Galaxy Schema, Quy trình ETL Open-Meteo, Khai thác phân tích & Prescriptive BI).
  - 1.3. Đối tượng và phạm vi (Không gian: 11 tỉnh thành gồm 2 TP TW Huế, Đà Nẵng và 9 tỉnh; Thời gian: 1999 - 2026; Nghiệp vụ: Bão, lũ, ngập lụt, sạt lở, cán cân nước).
  - 1.4. Phương pháp luận nghiên cứu (Ralph Kimball Dimensional Modeling).
- **Chương 2: Cơ sở Lý thuyết về Kho Dữ Liệu (Data Warehouse)**:
  - 2.1. Khái niệm & 4 đặc tính (Subject-oriented, Integrated, Time-variant, Non-volatile).
  - 2.2. So sánh chuyên sâu OLTP vs OLAP, Data Warehouse vs Data Mart vs Data Lakehouse.
  - 2.3. Các mô hình dữ liệu: Star Schema, Snowflake Schema, Fact Constellation (Galaxy Schema).
  - 2.4. Quy trình ETL/ELT và các chiến lược xử lý biến động dữ liệu (SCD Type 1, 2, 3).
- **Chương 3: Phân tích Nghiệp vụ & Thiết kế Kho Dữ Liệu Miền Trung**:
  - 3.1. Ma trận Bus Matrix trực giao giữa 6 Fact và 5 Dimension.
  - 3.2. Thiết kế chi tiết 5 Dimension: `dim_date` (thêm mùa bão lũ, pha ENSO), `dim_time`, `dim_location` (11 tỉnh thành, lưu vực sông chính, đặc trưng địa hình), `dim_weather_condition`, `dim_wind_direction` (gió mùa Đông Bắc, gió phơn Tây Nam).
  - 3.3. Thiết kế chi tiết 6 Fact: `fact_temperature`, `fact_precipitation` (mưa tích lũy, cân bằng nước), `fact_wind`, `fact_solar_radiation`, `fact_atmospheric`, `fact_extreme_events` (cấp bão, mức báo động lũ BĐ1-BĐ3, thiệt hại).
  - 3.4. Định danh Grain và chiến lược khóa đại diện (Surrogate Keys).
- **Chương 4: Quy trình ETL Tích hợp Dữ liệu Khí tượng**:
  - 4.1. Khảo sát nguồn dữ liệu mở Open-Meteo & ERA5 Reanalysis (1940 đến nay).
  - 4.2. Kỹ thuật Extract và phân mảnh dữ liệu (Data Partitioning).
  - 4.3. Quy trình Transform: Xử lý missing data, outlier, tính toán chỉ số phái sinh (`water_balance`, cấp gió Beaufort, phân loại cảnh báo lũ).
  - 4.4. Quy trình Load và chiến lược đánh chỉ mục (Indexing) tối ưu hóa truy vấn.
- **Chương 5: Báo Cáo Trực Quan Hóa (Dashboard) & Khuyến Nghị Ứng Phó Thiên Tai**:
  - 5.1. Thiết kế hệ thống Dashboard đa chiều (Climate Overview Dashboard miền Trung).
  - 5.2. Phân tích các đợt thiên tai lịch sử: Đại hồng thủy 1999, Đại lũ 2020, ngập lụt Đà Nẵng 2022, bão lũ 11/2026.
  - 5.3. Hệ thống gợi ý Prescriptive Analytics: Khuyến nghị mùa vụ nông nghiệp tránh lũ, cảnh báo thi công xây dựng, quản lý an toàn hồ chứa và tài nguyên nước.
  - 5.4. Đánh giá kết quả đạt được, hạn chế và hướng phát triển (AI Machine Learning dự báo sớm chuỗi thời gian).
- **Kết luận & Danh mục tài liệu tham khảo**.

- [ ] **Step 1: Viết script `build_report.py` sử dụng `python-docx` định dạng tài liệu chuyên nghiệp.**
- [ ] **Step 2: Chạy script để tạo ra file `central_weather_dw/BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx`.**
- [ ] **Step 3: Kiểm tra định dạng bảng biểu, tiêu đề, và nội dung không bị lỗi font.**

---

### Task 2: Soạn Thảo Bài Thuyết Trình & Ngân Hàng 40 Câu Hỏi Phản Biện (`BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx`)

**Files:**
- Output: `central_weather_dw/BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx`
- Script: `central_weather_dw/build_defense_guide.py`

**Nội dung chi tiết 2 phần:**
1. **Phần 1: Kịch bản thuyết trình bảo vệ đồ án (15 phút chuẩn)**
   - Phân đoạn 1 (2 phút): Mở đầu ấn tượng, kết nối trực tiếp với đợt mưa lũ đặc biệt lớn tháng 11/2026 tại miền Trung đang diễn ra.
   - Phân đoạn 2 (3 phút): Tính cấp thiết của 11 tỉnh thành và lý do chọn mốc từ Đại hồng thủy 11/1999.
   - Phân đoạn 3 (4 phút): Điểm sáng kiến trúc Galaxy Schema (5 Dim, 6 Fact, Bus Matrix, Surrogate Key).
   - Phân đoạn 4 (4 phút): Trực quan hóa Dashboard, phân tích bão lũ và các khuyến nghị hỗ trợ người dân (nông nghiệp, xây dựng, cứu hộ).
   - Phân đoạn 5 (2 phút): Kết luận, bài học kinh nghiệm và lời cảm ơn hội đồng.
2. **Phần 2: Ngân hàng 40 câu hỏi phản biện bảo vệ (chia 3 cấp độ kèm đáp án chi tiết)**
   - *Mức Dễ (15 câu)*: Khái niệm Data Warehouse, 4 đặc tính Inmon, OLTP vs OLAP, Fact vs Dimension, Star vs Snowflake, SCD Type 1 & 2, Data Mart, Metadata, Grain...
   - *Mức Trung bình (15 câu)*: Tại sao chọn Galaxy Schema cho 11 tỉnh miền Trung? Xử lý dữ liệu thưa trong `fact_extreme_events`? Tại sao tách `dim_wind_direction`? Cách tính `water_balance`? Xử lý missing values từ API? Chiến lược tạo Surrogate Key...
   - *Mức Nâng cao & Câu hỏi Tình huống hóc búa (10 câu)*:
     - So sánh Data Lakehouse (Delta Lake / Iceberg) với RDBMS truyền thống cho dữ liệu khí hậu.
     - Nếu API cập nhật lại số liệu ngày hôm qua thì DW xử lý ra sao?
     - Đồ án giải quyết thế nào khi có sáp nhập địa giới hành chính (SCD Type mấy)?
     - Tại sao chọn mốc 1999 và độ trễ dữ liệu của Open-Meteo ERA5 ảnh hưởng gì đến tính realtime?
     - Chiến lược Partitioning và Indexing khi bảng Fact lên tới hàng chục triệu bản ghi.
     - Tích hợp Feature Store để huấn luyện mô hình Machine Learning dự báo thời tiết ngắn hạn.

- [ ] **Step 1: Viết script `build_defense_guide.py` sử dụng `python-docx`.**
- [ ] **Step 2: Chạy script tạo ra file `central_weather_dw/BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx`.**
- [ ] **Step 3: Kiểm tra cấu trúc câu hỏi, phân cấp rõ ràng và nội dung câu trả lời chuẩn xác.**

---

### Task 3: Thiết Kế Bộ Slide Trình Chiếu Chuẩn Báo Cáo (`Slide_Kho_Du_Lieu_Mien_Trung.pptx`)

**Files:**
- Output: `central_weather_dw/Slide_Kho_Du_Lieu_Mien_Trung.pptx`
- Script: `central_weather_dw/build_slides.py`

**Cấu trúc 16 Slide trình chiếu hiện đại:**
- Slide 1: Bìa đề tài (Tên đề tài 11 tỉnh miền Trung 1999-2026, GVHD, Nhóm sinh viên).
- Slide 2: Mục lục 5 phần (Đặt vấn đề -> Cơ sở lý thuyết -> Thiết kế Kho dữ liệu -> ETL & Tích hợp -> Kết quả & Ứng dụng).
- Slide 3: Tính cấp thiết của đề tài (Hình ảnh & số liệu bão lũ miền Trung, kỷ lục 1999, 2020 và đợt thiên tai 11/2026).
- Slide 4: Mục tiêu nghiên cứu & Giá trị thực tiễn vì cộng đồng.
- Slide 5: Đối tượng & Phạm vi nghiên cứu (Bản đồ 11 tỉnh thành miền Trung: 2 TP TW Huế, Đà Nẵng + 9 tỉnh; dải thời gian 1999-2026).
- Slide 6: Phương pháp luận thiết kế Ralph Kimball.
- Slide 7: Kiến trúc tổng thể Galaxy Schema (Lược đồ trực quan 5 Dimensions & 6 Facts).
- Slide 8: Thiết kế chi tiết 5 Conformed Dimensions (Mở rộng Lưu vực sông & Địa hình).
- Slide 9: Thiết kế chi tiết 6 Fact Tables & Khái niệm Grain.
- Slide 10: Quy trình ETL tự động hóa từ Open-Meteo Archive API.
- Slide 11: Làm sạch dữ liệu: Xử lý Missing values, Outliers & Chuẩn hóa đơn vị.
- Slide 12: Hệ thống Dashboard Trực quan hóa: Theo dõi bão lũ & xu hướng biến đổi khí hậu.
- Slide 13: Ứng dụng Prescriptive Analytics 1: Đề xuất mùa vụ nông nghiệp tránh lũ.
- Slide 14: Ứng dụng Prescriptive Analytics 2: Cảnh báo an toàn thi công & Rủi ro cân bằng nước.
- Slide 15: Kết luận & Hướng mở rộng (Machine Learning dự báo, Cloud Lakehouse).
- Slide 16: Lời cảm ơn Thầy/Cô và Hội đồng - Q&A.

- [ ] **Step 1: Viết script `build_slides.py` sử dụng `python-pptx` với màu sắc chủ đạo xanh khí tượng (Deep Navy & Sky Blue) và xám chuyên nghiệp.**
- [ ] **Step 2: Chạy script tạo ra file `central_weather_dw/Slide_Kho_Du_Lieu_Mien_Trung.pptx`.**
- [ ] **Step 3: Kiểm tra slide mở được mượt mà, layout thoáng đãng, dễ theo dõi.**

---

### Task 4: Kiểm Thử Định Dạng & Bàn Giao Bộ Sản Phẩm

- [ ] **Step 1: Xác nhận 3 file chính đã được sinh đầy đủ trong `central_weather_dw/`:**
  - `central_weather_dw/BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx`
  - `central_weather_dw/BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx`
  - `central_weather_dw/Slide_Kho_Du_Lieu_Mien_Trung.pptx`
- [ ] **Step 2: Xác nhận thư mục `docs/` cũ hoàn toàn nguyên vẹn, không có bất kỳ file mới nào bị thêm vào `docs/`.**
- [ ] **Step 3: Tổng hợp báo cáo bàn giao chi tiết cho người dùng.**
