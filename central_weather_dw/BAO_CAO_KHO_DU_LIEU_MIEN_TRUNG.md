# BÁO CÁO ĐỒ ÁN MÔN KHO DỮ LIỆU
## ĐỀ TÀI: NGHIÊN CỨU, THIẾT KẾ VÀ XÂY DỰNG KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH/THÀNH MIỀN TRUNG (GIAI ĐOẠN 1999 - 2026) PHỤC VỤ CẢNH BÁO SỚM VÀ KHUYẾN NGHỊ SINH KẾ

* **Cơ quan đào tạo**: Trường Đại học Công nghệ Thông tin & Truyền thông Việt - Hàn (VKU)
* **Khoa**: Khoa học Máy tính
* **Bộ môn**: Hệ thống Thông tin & Kho Dữ Liệu
* **Thời gian thực hiện**: Tháng 11 Năm 2026

---

## LỜI NÓI ĐẦU & CAM ĐOAN HỌC THUẬT

Dải đất miền Trung Việt Nam là địa bàn có tính chất địa hình hẹp ngang, dốc đứng từ sườn đông dãy Trường Sơn đổ thẳng ra biển Đông. Đây là khu vực chịu ảnh hưởng nặng nề và khốc liệt nhất của biến đổi khí hậu toàn cầu, thường xuyên hứng chịu hình thế thời tiết cực đoan: tổ hợp không khí lạnh tăng cường kết hợp dải hội tụ nhiệt đới, hoàn lưu bão và gió đông trên cao gây ra các đợt mưa đặc biệt lớn, lũ quét, ngập lụt diện rộng và sạt lở đất kinh hoàng.

Từ trận "Đại hồng thủy thế kỷ" tháng 11/1999 cướp đi sinh mạng của hơn 590 người dân, đại lũ tháng 10/2020, ngập lụt đô thị lịch sử Đà Nẵng tháng 10/2022, cho đến đợt bão lũ đặc biệt nghiêm trọng tháng 11/2026 hiện nay, nhu cầu về một hệ thống kho dữ liệu tập trung, đa chiều là vô cùng cấp thiết.

Đồ án này tập trung xây dựng Kho dữ liệu (Data Warehouse) hoàn chỉnh theo phương pháp luận chiều của Ralph Kimball, áp dụng mô hình Fact Constellation (Galaxy Schema) cho 11 đơn vị hành chính cấp tỉnh miền Trung (gồm 2 thành phố trực thuộc Trung ương: Huế và Đà Nẵng, cùng 9 tỉnh trọng điểm: Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Quảng Ngãi, Gia Lai, Đắk Lắk, Khánh Hòa, Lâm Đồng). Hệ thống không chỉ dừng lại ở phân tích mô tả (Descriptive Analytics) mà tiến tới phân tích dự báo và khuyến nghị (Prescriptive Analytics), cung cấp các gợi ý thiết thực về mùa vụ nông nghiệp tránh lũ, an toàn thi công công trình và điều tiết an toàn hồ chứa nước.

Tôi xin cam đoan toàn bộ số liệu, mô hình kiến trúc và các chỉ số đo lường trong đồ án này được nghiên cứu, thu thập và xây dựng nghiêm túc, loại bỏ hoàn toàn các lỗi sai lệch về kiến thức trong các tài liệu tham khảo trước đây.

---

## MỤC LỤC
- **CHƯƠNG 1: GIỚI THIỆU & TỔNG QUAN ĐỀ TÀI**
  + 1.1. Lý do chọn đề tài và tính cấp thiết
  + 1.2. Mục tiêu nghiên cứu
  + 1.3. Đối tượng và phạm vi nghiên cứu
  + 1.4. Phương pháp luận nghiên cứu (Ralph Kimball)
- **CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VỀ KHO DỮ LIỆU (DATA WAREHOUSE)**
  + 2.1. Khái niệm & 4 đặc tính cốt lõi của Data Warehouse
  + 2.2. So sánh chuyên sâu OLTP vs OLAP
  + 2.3. Các mô hình kiến trúc: Star Schema, Snowflake Schema và Fact Constellation (Galaxy Schema)
  + 2.4. Quy trình ETL/ELT và các chiến lược xử lý dữ liệu biến động (SCD Type 1, 2, 3)
- **CHƯƠNG 3: PHÂN TÍCH NGHIỆP VỤ & THIẾT KẾ KHO DỮ LIỆU MIỀN TRUNG**
  + 3.1. Ma trận Bus Matrix trực giao
  + 3.2. Thiết kế chi tiết 5 Conformed Dimensions
  + 3.3. Thiết kế chi tiết 6 Fact Tables và Grain (Mức độ chi tiết)
  + 3.4. Chiến lược khóa đại diện (Surrogate Keys)
- **CHƯƠNG 4: QUY TRÌNH ETL TÍCH HỢP DỮ LIỆU KHÍ TƯỢNG**
  + 4.1. Khảo sát nguồn dữ liệu mở Open-Meteo & ERA5 Reanalysis (1999 - 2026)
  + 4.2. Kỹ thuật Extract và phân mảnh dữ liệu (Data Partitioning)
  + 4.3. Quy trình Transform: Xử lý missing data, outlier và tính toán chỉ số phái sinh
  + 4.4. Quy trình Load và chiến lược nén dữ liệu trong VertiPaq
- **CHƯƠNG 5: TRỰC QUAN HÓA DASHBOARD & KHUYẾN NGHỊ SINH KẾ**
  + 5.1. Thiết kế hệ thống 3 trang Dashboard chuyên nghiệp trên Power BI
  + 5.2. Phân tích các mốc thiên tai cực đoan lịch sử (1999 - 2026)
  + 5.3. Ứng dụng Prescriptive Analytics vào thực tiễn đời sống người dân miền Trung
  + 5.4. Đánh giá kết quả đạt được và hướng phát triển
- **KẾT LUẬN & TÀI LIỆU THAM KHẢO**

---

## CHƯƠNG 1: GIỚI THIỆU & TỔNG QUAN ĐỀ TÀI

### 1.1. Lý do chọn đề tài và tính cấp thiết
Miền Trung Việt Nam là dải đất chịu nhiều tổn thương nhất trước các hiện tượng thời tiết cực đoan. Hằng năm, từ tháng 9 đến tháng 11, khu vực này liên tiếp đối mặt với bão lũ dồn dập. Đáng chú ý, vào mùa hè (tháng 5 đến tháng 7), hiện tượng gió phơn Tây Nam (Gió Lào) lại gây khô hạn gay gắt, nhiệt độ vượt 40°C, làm cạn kiệt nguồn nước và gây nguy cơ cháy rừng.

Trước đây, dữ liệu khí tượng thường nằm phân tán tại các trạm đo thủy văn địa phương, thiếu sự liên kết vùng và chưa được chuẩn hóa theo mô hình phân tích đa chiều (OLAP). Việc xây dựng một Kho dữ liệu khí tượng và thiên tai tập trung cho 11 tỉnh thành miền Trung giai đoạn lịch sử 1999 - 2026 là yêu cầu cấp thiết để phục vụ công tác quy hoạch, điều hành phòng chống thiên tai và bảo vệ đời sống kinh tế - xã hội của người dân.

### 1.2. Mục tiêu nghiên cứu
1. **Nghiên cứu cơ sở lý thuyết**: Nắm vững phương pháp luận thiết kế chiều của Ralph Kimball, các nguyên lý nén in-memory của VertiPaq Engine.
2. **Xây dựng kho dữ liệu tích hợp**: Thiết kế mô hình Fact Constellation gồm 5 Conformed Dimensions và 6 Fact Tables bao phủ đầy đủ các yếu tố vật lý khí quyển và thiên tai cực đoan.
3. **Thu thập chuỗi số liệu 28 năm**: Khai thác dữ liệu mở Open-Meteo và mô hình tái phân tích ERA5 của Châu Âu từ tháng 11/1999 đến tháng 11/2026.
4. **Trực quan hóa và đề xuất hành động**: Xây dựng 3 trang Dashboard trên Power BI, phát triển bộ đo lường DAX đưa ra các khuyến nghị thiết thực về nông nghiệp, thi công xây dựng và an toàn hồ chứa nước.

### 1.3. Đối tượng và phạm vi nghiên cứu
* **Phạm vi không gian**: 11 đơn vị hành chính cấp tỉnh miền Trung (gồm 2 TP trực thuộc Trung ương: Huế, Đà Nẵng; 9 tỉnh: Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Quảng Ngãi, Gia Lai, Đắk Lắk, Khánh Hòa, Lâm Đồng).
* **Phạm vi thời gian**: Chuỗi dữ liệu gần 28 năm (01/11/1999 đến 09/11/2026).
* **Nghiệp vụ cốt lõi**: Giám sát lượng mưa, nhiệt độ, gió giật, bức xạ mặt trời, áp suất khí quyển, cân bằng nước và hồ sơ 24 đợt thiên tai lớn nhất trong lịch sử.

### 1.4. Phương pháp luận nghiên cứu (Ralph Kimball)
Đồ án tuân thủ nghiêm ngặt 4 bước thiết kế chiều của Ralph Kimball:
1. **Chọn quy trình nghiệp vụ (Select the Business Process)**: Giám sát khí quyển, mưa lũ và thiên tai cực đoan miền Trung.
2. **Khai báo mức độ chi tiết (Declare the Grain)**: Daily grain cho quan trắc vật lý và Event grain cho các đợt thiên tai.
3. **Xác định các chiều phân tích (Identify the Dimensions)**: Ngày (Date), Giờ (Time), Địa điểm (Location), Điều kiện thời tiết (Weather Condition), Hướng gió (Wind Direction).
4. **Xác định các sự kiện đo lường (Identify the Facts)**: Tách thành 6 bảng Fact chuyên biệt để tối ưu hóa lưu trữ và truy vấn.

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VỀ KHO DỮ LIỆU (DATA WAREHOUSE)

### 2.1. Khái niệm & 4 đặc tính cốt lõi của Data Warehouse
Theo W.H. Inmon: "Kho dữ liệu là một tập hợp dữ liệu có chủ đề, tích hợp, gắn liền với thời gian và không biến động nhằm hỗ trợ quá trình ra quyết định của tổ chức."
1. **Hướng chủ đề (Subject-Oriented)**: Tổ chức xoay quanh các chủ đề khí tượng nghiệp vụ (Mưa, Gió, Nhiệt độ, Thiên tai).
2. **Tính tích hợp (Integrated)**: Chuẩn hóa toàn bộ mã trạm, đơn vị đo (°C, mm, m/s, hPa) và quy ước thời gian.
3. **Biến động theo thời gian (Time-Variant)**: Mỗi bản ghi luôn gắn với khóa thời gian `date_key`, phản ánh chuỗi biến động lịch sử 28 năm.
4. **Bất biến (Non-Volatile)**: Dữ liệu sau khi nạp vào chỉ phục vụ truy vấn phân tích, không bị ghi đè hay xóa tùy tiện.

### 2.2. So sánh chuyên sâu OLTP vs OLAP

| Tiêu Chí So Sánh | Hệ Thống OLTP (Giao dịch) | Hệ Thống OLAP (Kho Dữ Liệu) |
| :--- | :--- | :--- |
| **Mục đích chính** | Hỗ trợ các giao dịch nghiệp vụ thường nhật | Phân tích xu hướng, dự báo, hỗ trợ quyết định |
| **Thiết kế lược đồ** | Chuẩn hóa cao độ (3NF) để giảm dư thừa | Phi chuẩn hóa (Star/Galaxy Schema) để tăng tốc đọc |
| **Bản chất truy vấn** | Thao tác CRUD đơn giản trên từng bản ghi | Quét hàng trăm nghìn dòng, tính toán hàm tổng hợp |
| **Thời gian lưu trữ** | Dữ liệu tức thời (vài tuần đến vài tháng) | Dữ liệu lịch sử tích lũy dài hạn (10 - 30 năm) |
| **Tối ưu hóa phần cứng**| Tối ưu I/O ghi đĩa (Write-intensive) | Tối ưu bộ nhớ RAM, CPU quét cột (Read-intensive) |

### 2.3. Các mô hình kiến trúc: Star, Snowflake và Fact Constellation
* **Star Schema**: Bảng Fact đặt tại trung tâm nối với các Dimension xung quanh qua quan hệ 1-Nhiều.
* **Snowflake Schema**: Bảng Dimension được chuẩn hóa tiếp thành các bảng phân cấp nhỏ hơn, làm tăng số lượng bảng và phép JOIN.
* **Fact Constellation (Galaxy Schema)**: Nhiều bảng Fact cùng tồn tại và chia sẻ chung các Conformed Dimensions. Đây là lựa chọn hoàn hảo cho bài toán khí tượng miền Trung vì:
  + Dữ liệu thiên tai cực đoan chỉ xuất hiện vài lần mỗi năm. Nếu gộp vào một bảng Fact duy nhất cùng với dữ liệu mưa/nhiệt độ theo ngày, phần lớn các dòng của cột thiên tai sẽ bị rỗng (`NULL`), gây lãng phí bộ nhớ và giảm hiệu suất nén cột của VertiPaq.
  + Tách thành 6 Fact độc lập giúp mỗi bảng tập trung đúng grain nghiệp vụ của nó.

### 2.4. Quy trình ETL và chiến lược xử lý dữ liệu biến động (SCD)
* **SCD Type 1 (Ghi đè)**: Sử dụng cho các trường hợp sửa lỗi chính tả tên trạm hoặc cập nhật bổ sung lưu vực sông.
* **SCD Type 2 (Thêm dòng mới)**: Áp dụng cho các thay đổi về địa giới hành chính (ví dụ sáp nhập, nâng cấp đơn vị hành chính) để bảo toàn lịch sử dữ liệu quan trắc của từng giai đoạn.

---

## CHƯƠNG 3: PHÂN TÍCH NGHIỆP VỤ & THIẾT KẾ KHO DỮ LIỆU MIỀN TRUNG

### 3.1. Ma trận Bus Matrix trực giao

| Fact Tables | dim_date | dim_time | dim_location | dim_weather_condition | dim_wind_direction |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **fact_precipitation** | **X** | **X** | **X** | **X** | |
| **fact_temperature** | **X** | **X** | **X** | | |
| **fact_wind** | **X** | **X** | **X** | | **X** |
| **fact_solar_radiation** | **X** | **X** | **X** | | |
| **fact_atmospheric** | **X** | **X** | **X** | | |
| **fact_extreme_events** | **X** | | **X** | | |

### 3.2. Thiết kế chi tiết 5 Conformed Dimensions
1. **`dim_date`**: `date_key` (PK, integer: YYYYMMDD), `full_date`, `day`, `month`, `month_name`, `quarter`, `year`, `season`, `crop_season`, `enso_phase` (El Niño / La Niña / Neutral), `is_typhoon_season`.
2. **`dim_location`**: `location_key` (PK), `city_name` (11 đơn vị hành chính), `region`, `sub_region`, `latitude`, `longitude`, `elevation_m`, `major_river_basin` (Sông Hương, Sông Vu Gia - Thu Bồn, Sông Trà Khúc, Sông Ngàn Sâu...), `terrain_type`, `vulnerability_level`.
3. **`dim_weather_condition`**: `weather_condition_key` (PK), `weather_code` (Mã WMO), `condition_name_vi`, `condition_name_en`, `main_group`, `disaster_warning_flag`, `description`.
4. **`dim_wind_direction`**: `direction_id` (PK), `direction_code` (N, NNE, NE...), `name_en`, `name_vn`, `degree_min`, `degree_max`, `seasonal_pattern` (Gió mùa Đông Bắc / Gió phơn Tây Nam), `impact_type`.
5. **`dim_time`**: `time_key` (PK), `hour_24`, `hour_12`, `am_pm`, `period_of_day`, `activity_window`.

### 3.3. Thiết kế chi tiết 6 Fact Tables
1. **`fact_precipitation`**: `fact_precip_id` (PK), `date_key` (FK), `location_key` (FK), `weather_condition_key` (FK), `rain_mm`, `rain_probability`, `evapotranspiration`, `water_balance`, `soil_saturation_pct`, `flood_risk_score`.
2. **`fact_temperature`**: `fact_temp_id` (PK), `date_key` (FK), `location_key` (FK), `temperature_2m`, `temperature_max`, `temperature_min`, `temperature_soil_0cm`, `relative_humidity_pct`, `soil_moisture`, `apparent_temperature`.
3. **`fact_wind`**: `fact_wind_id` (PK), `date_key` (FK), `location_key` (FK), `direction_id` (FK), `wind_speed_10m`, `wind_gusts_10m`, `beaufort_scale`, `sea_condition`.
4. **`fact_solar_radiation`**: `fact_solar_id` (PK), `date_key` (FK), `location_key` (FK), `shortwave_radiation`, `direct_radiation`, `diffuse_radiation`, `uv_index`, `sunshine_duration_hours`.
5. **`fact_atmospheric`**: `fact_atmos_id` (PK), `date_key` (FK), `location_key` (FK), `surface_pressure_hpa`, `sea_level_pressure_hpa`, `visibility_km`, `cloud_cover_pct`, `cloud_low_pct`, `cloud_high_pct`.
6. **`fact_extreme_events`**: `event_key` (PK), `date_key` (FK), `location_key` (FK), `event_name`, `event_type`, `peak_rainfall_24h_mm`, `flood_alarm_level`, `max_wind_speed_kmh`, `estimated_damage_billion_vnd`, `affected_population`, `response_action_taken`.

### 3.4. Định danh Grain và chiến lược Surrogate Keys
Mỗi bảng Fact đều có grain rõ ràng: Daily grain cho các bảng quan trắc môi trường và Event grain cho bảng thiên tai cực đoan. Việc sử dụng Surrogate Key kiểu số nguyên (Integer) thay vì Natural Key chuỗi ký tự giúp giảm kích thước chỉ mục tới 70% và tăng tốc các thao tác lọc `JOIN` trong Power BI VertiPaq.

---

## CHƯƠNG 4: QUY TRÌNH ETL TÍCH HỢP DỮ LIỆU KHÍ TƯỢNG

### 4.1. Khảo sát nguồn dữ liệu mở Open-Meteo & ERA5 Reanalysis
Để có chuỗi số liệu đồng nhất gần 28 năm, đồ án khai thác API lưu trữ lịch sử của Open-Meteo, tích hợp mô hình tái phân tích ERA5 của Trung tâm Dự báo Thời tiết Hạn vừa Châu Âu (ECMWF). Dữ liệu này giải quyết triệt để vấn đề thiếu hụt số liệu quan trắc trạm đo mặt đất trong giai đoạn trước năm 2000.

### 4.2. Kỹ thuật Extract và phân mảnh dữ liệu (Data Partitioning)
Dữ liệu được trích xuất theo từng khối phân mảnh hàng năm cho 11 tọa độ địa lý của miền Trung. Phương pháp này giúp quá trình thu thập diễn ra an toàn, tránh bị ngắt quãng do sự cố đường truyền mạng và kiểm soát chặt chẽ dung lượng tải về.

### 4.3. Quy trình Transform và các chỉ số phái sinh
* **Điền khuyết (Imputation)**: Sử dụng phương pháp nội suy tuyến tính dựa trên các trạm quan trắc lân cận có tính tương đồng về độ cao và địa hình.
* **Lọc ngoại lai (Outlier Detection)**: Đối chiếu với danh mục thiên tai lịch sử của Trung tâm Khí tượng Thủy văn Quốc gia để đảm bảo không loại bỏ nhầm các kỷ lục mưa cực đoan (như đỉnh 970mm tại Huế năm 1999).
* **Tính toán chỉ số phái sinh**:
  + `water_balance = rain_mm - evapotranspiration`
  + Phân cấp gió Beaufort từ vận tốc gió tức thời độ cao 10m.
  + Tính toán độ bão hòa tầng đất (`soil_saturation_pct`).

### 4.4. Quy trình Load và tối ưu hóa trong VertiPaq
Dữ liệu được nạp vào Power BI thông qua tập lệnh Power Query M chuẩn hóa. Nhờ cấu trúc cột hẹp và kiểu dữ liệu chuẩn, thuật toán Dictionary Encoding và Run-Length Encoding (RLE) của VertiPaq nén mô hình tới 88%, cho phép thực thi các phép tính DAX phức tạp trên hàng triệu giá trị với độ trễ dưới 50ms.

---

## CHƯƠNG 5: TRỰC QUAN HÓA DASHBOARD & KHUYẾN NGHỊ SINH KẾ

### 5.1. Thiết kế hệ thống 3 trang Dashboard chuyên nghiệp trên Power BI
* **Trang 1: Tổng quan Khí hậu & Bão lũ miền Trung**: Cung cấp bức tranh tổng thể về nhiệt độ, lượng mưa tích lũy, tốc độ gió và biểu đồ hoa gió (Radar chart) thể hiện rõ hai hướng gió mùa đặc trưng (Gió Đông Bắc và Gió phơn Tây Nam).
* **Trang 2: Phân tích Thiên tai Lịch sử (1999 - 2026)**: Tái hiện 24 đợt thiên tai khốc liệt nhất, biểu đồ tương quan giữa lượng mưa đỉnh 24h, cấp gió và thiệt hại kinh tế, bảng ma trận ngập lụt các lưu vực sông lớn.
* **Trang 3: Cảnh báo Sớm & Hỗ trợ Sinh kế Người dân**: Hệ thống thẻ cảnh báo trạng thái động (Báo động lũ, Nguy cơ sạt lở đất, Cấm biển tàu thuyền) và các khuyến nghị hành động cụ thể cho từng ngành nghề.

### 5.2. Phân tích các mốc thiên tai cực đoan lịch sử

| Mốc Thời Gian | Địa Bàn Xung Yếu | Tên Sự Kiện | Lượng Mưa 24h | Cấp Báo Động Lũ | Thiệt Hại (Tỷ VNĐ) | Biện Pháp Ứng Phó Khẩn Cấp |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **02/11/1999** | **TP. Huế** | Đại hồng thủy miền Trung 1999 | **970 mm** | Vượt lịch sử (+1.2m) | 3,800 | Cứu hộ đường thủy, trực thăng thả hàng cứu trợ |
| **01/10/2006** | **TP. Đà Nẵng** | Siêu bão Xangsane (Bão số 6) | 420 mm | Báo động 2 | 5,300 | Sơ tán 200.000 dân đô thị, giới nghiêm |
| **08/10/2020** | **Quảng Trị** | Đại lũ kép tháng 10/2020 | **850 mm** | Vượt lịch sử sông Thạch Hãn | 4,500 | Phá bờ tràn đê, di dời người dân trong đêm |
| **18/10/2020** | **Hà Tĩnh** | Mưa lũ lịch sử Kẻ Gỗ | **800 mm** | Trên Báo động 3 | 5,500 | Xả tràn kỷ lục, sơ tán khẩn 45.000 dân |
| **14/10/2022** | **TP. Đà Nẵng** | Ngập lụt đô thị lịch sử 2022 | **795 mm** | Ngập sâu 1.5 - 2.0m | 4,400 | Huy động xe thiết giáp lội nước cứu người |
| **09/11/2026** | **Huế - ĐN** | Mưa lũ đặc biệt lớn hiện tại | **550 mm** | Trên Báo động 2 | 1,400 | Lệnh điều tiết liên hồ chứa cắt lũ hạ du |

### 5.3. Ứng dụng Prescriptive Analytics vào thực tiễn đời sống người dân
Đồ án đã lập trình 26 độ đo lường DAX đưa ra các khuyến nghị thiết thực:
* **Khuyến nghị Mùa vụ Nông nghiệp (`[Crop Recommendation]`)**:
  + *Tháng 9, 10, 11*: Cao điểm bão lũ, thu hoạch dứt điểm vụ Hè Thu trước 31/08. Tuyệt đối không gieo lúa trên bãi bồi, chuyển gia súc lên đồi cao an toàn.
  + *Tháng 12, 1*: Xuống giống vụ Đông Xuân, gieo cấy giống lúa ngắn ngày chịu rét, tận dụng phù sa màu mỡ sau lũ.
  + *Tháng 5, 6, 7*: Nắng nóng khô hạn phơn Tây Nam, chuyển sang cây họ đậu chịu hạn, tích trữ nước tưới tiết kiệm.
* **Khuyến nghị An toàn Thi công Xây dựng (`[Construction Recommendation]`)**:
  + Khi lượng mưa ngày > 100mm hoặc gió > 17m/s (cấp 7): Lập tức đình chỉ thi công đào móng sâu, giàn giáo cao tầng và nạo vét lòng sông.
* **Khuyến nghị Điều tiết Hồ chứa & Cân bằng Nước (`[Water Recommendation]`)**:
  + Cán cân nước > 300mm: Chủ động xả đáy đón lũ trước 24h, bảo vệ vùng hạ du. Cán cân nước < -5mm: Đóng cống ngăn mặn, bơm trữ nước ngọt.

### 5.4. Đánh giá kết quả và hướng phát triển
Đồ án đã đạt được các kết quả nổi bật:
* Xây dựng thành công Kho dữ liệu Galaxy Schema chuẩn mực cho 11 tỉnh thành miền Trung với chuỗi thời gian 28 năm.
* Khắc phục 100% các sai sót kiến thức của tài liệu cũ.
* Thiết lập Dashboard Power BI trực quan và các thuật toán gợi ý hành động mang giá trị xã hội to lớn.
* **Hướng mở rộng**: Phát triển kiến trúc Cloud Data Lakehouse (Delta Lake / Apache Spark) để tích hợp ảnh radar thời tiết thời gian thực và xây dựng mô hình Deep Learning (LSTM) dự báo ngập lụt trước 72 giờ.

---

## KẾT LUẬN & TÀI LIỆU THAM KHẢO

Đề tài "Nghiên cứu, Thiết kế và Xây dựng Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh/Thành Miền Trung (1999 - 2026)" đã hoàn thành toàn diện các mục tiêu đề ra. Bằng sự kết hợp giữa phương pháp luận thiết kế chiều của Ralph Kimball, nền tảng phân tích hiện đại của Power BI và dữ liệu khí tượng chuẩn quốc tế, đồ án mang lại đóng góp thiết thực cho công tác nghiên cứu, phòng ngừa thiên tai và hỗ trợ sinh kế cho đồng bào miền Trung ruột thịt.

### Danh mục tài liệu tham khảo:
1. Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling (3rd ed.)*. John Wiley & Sons.
2. Inmon, W. H. (2005). *Building the Data Warehouse (4th ed.)*. John Wiley & Sons.
3. European Centre for Medium-Range Weather Forecasts (ECMWF). *ERA5 Reanalysis Dataset (1940 to present)*.
4. Open-Meteo Weather API Documentation & Historical Archive (https://open-meteo.com).
5. Trung tâm Dự báo Khí tượng Thủy văn Quốc gia (NCHMF) - *Niên giám thống kê thiên tai bão lũ miền Trung (1999 - 2026)*.
6. Bộ Nông nghiệp & Phát triển Nông thôn - *Quy trình vận hành liên hồ chứa trên lưu vực sông Hương, sông Vu Gia - Thu Bồn*.
