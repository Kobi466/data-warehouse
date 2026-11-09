# CẨM NANG THIẾT KẾ & VẬN HÀNH POWER BI DASHBOARD
## DỰ ÁN: KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH THÀNH MIỀN TRUNG (1999 - 2026)

---

## I. TỔNG QUAN MÔ HÌNH DỮ LIỆU TRONG POWER BI (MODEL VIEW)

Hệ thống được thiết kế theo mô hình **Fact Constellation (Galaxy Schema)** gồm 5 bảng Dimension dùng chung (Conformed Dimensions) và 6 bảng Fact.

### Sơ Đồ Thiết Lập Mối Quan Hệ (Relationships - 1 to Many `1:*`, Single Cross Filter):

```
                       ┌──────────────────────┐
                       │       dim_date       │
                       │     (date_key [1])   │
                       └──────────┬───────────┘
                                  │ 1
                                  │ *
     ┌────────────────────────────┼────────────────────────────┐
     │                            │                            │
┌────┴────────────────┐  ┌────────┴───────────┐  ┌─────────────┴──────┐
│  fact_temperature   │  │ fact_precipitation │  │      fact_wind     ├──* 1── dim_wind_direction
│  (date_key, loc_key)│  │ (date_key, loc_key)│  │ (date_key, loc_key)│        (direction_id)
└────┬────────────────┘  └────────┬───────────┘  └─────────────┬──────┘
     │ *                          │ *                          │ *
     │                            │                            │
     ├────────────────────────────┼────────────────────────────┤
     │ *                          │ *                          │ *
┌────┴────────────────┐  ┌────────┴───────────┐  ┌─────────────┴──────┐
│  fact_atmospheric   │  │fact_solar_radiation│  │ fact_extreme_events│
│  (date_key, loc_key)│  │ (date_key, loc_key)│  │ (date_key, loc_key)│
└────┬────────────────┘  └────────┬───────────┘  └─────────────┬──────┘
     │ *                          │ *                          │ *
     │ 1                          │ 1                          │ 1
     └────────────────────────────┼────────────────────────────┘
                                  │
                       ┌──────────┴───────────┐
                       │     dim_location     │
                       │   (location_key [1]) │
                       └──────────────────────┘
                       (Còn có: dim_weather_condition nối với fact_precipitation qua weather_condition_key)
```

#### Bảng Kiểm Tra Khóa Ngoại (Foreign Keys):
1. `dim_date[date_key]` (1) ──> `fact_*[date_key]` (*) [Active]
2. `dim_location[location_key]` (1) ──> `fact_*[location_key]` (*) [Active]
3. `dim_wind_direction[direction_id]` (1) ──> `fact_wind[direction_id]` (*) [Active]
4. `dim_weather_condition[weather_condition_key]` (1) ──> `fact_precipitation[weather_condition_key]` (*) [Active]

---

## II. THIẾT KẾ CHI TIẾT 3 TRANG DASHBOARD

---

### TRANG 1: TỔNG QUAN KHÍ HẬU & BÃO LŨ MIỀN TRUNG
*(Central Vietnam Climate & Disaster Overview)*

#### 1. Hàng Thẻ Chỉ Số Tổng Quan (KPI Cards - Trên Cùng):
- **Card 1**: `[Avg Temperature]` — Nhãn: *Nhiệt Độ Trung Bình (°C)* (Ví dụ: 25.4°C).
- **Card 2**: `[Total Rain]` — Nhãn: *Tổng Lượng Mưa Tích Lũy (mm)* (Ví dụ: 12,450 mm).
- **Card 3**: `[Avg Wind Speed]` — Nhãn: *Tốc Độ Gió TB (m/s)* (Ví dụ: 14.8 m/s).
- **Card 4**: `[Extreme Events Count]` — Nhãn: *Số Đợt Thiên Tai Cực Đoan* (Ví dụ: 24 đợt).
- **Card 5**: `[Avg Water Balance]` — Nhãn: *Cán Cân Tài Nguyên Nước* (Giá trị > 0: Thừa nước; < 0: Thiếu nước).

#### 2. Cụm Bộ Lọc Tương Tác (Slicers - Góc Trái):
- **Slicer 1**: `dim_date[year]` (Dropdown hoặc Between slider: 1999 – 2026).
- **Slicer 2**: `dim_location[city_name]` (11 tỉnh/thành miền Trung: Huế, Đà Nẵng, Hà Tĩnh, Quảng Trị, Quảng Ngãi...).
- **Slicer 3**: `dim_location[sub_region]` (Bắc Trung Bộ / Duyên hải Nam Trung Bộ / Tây Nguyên chuyển tiếp).
- **Slicer 4**: `dim_date[season]` (Mùa mưa lũ / Mùa khô nóng / Mùa chuyển tiếp).
- **Slicer 5**: `dim_weather_condition[main_group]` (Mưa lớn, Bão & Áp thấp, Giông lốc...).

#### 3. Các Biểu Đồ Trực Quan Chính:
- **Visual 1 (Line & Clustered Column Chart)**: *Xu Hướng Lượng Mưa & Nhiệt Độ Qua Các Năm (1999 - 2026)*
  - X-axis: `dim_date[year]`
  - Column Y-axis: `[Total Rain]` (Cột màu xanh nước biển)
  - Line Y-axis: `[Avg Temperature]` (Đường màu cam nhiệt đới)
- **Visual 2 (Clustered Bar Chart)**: *Xếp Hạng Lượng Mưa Tích Lũy Theo 11 Tỉnh Thành*
  - Y-axis: `dim_location[city_name]`
  - X-axis: `[Total Rain]`
  - *Ý nghĩa*: Thấy rõ Huế, Quảng Trị, Đà Nẵng và Quảng Ngãi luôn là tâm mưa lớn nhất cả nước.
- **Visual 3 (Radar Chart - Biểu đồ Hoa Gió)**: *Phân Bố Tốc Độ & Hướng Gió Theo Mùa*
  - Category: `dim_wind_direction[name_vn]` (Bắc, Đông Bắc, Tây Nam...)
  - Measure: `[Avg Wind Speed]`
  - *Ý nghĩa*: Nhận diện rõ hướng gió bão Đông Bắc (mùa đông) và hướng gió phơn Tây Nam khô nóng (mùa hè).
- **Visual 4 (Line Chart)**: *Tương Quan Giữa Nhiệt Độ Không Khí và Nhiệt Độ Lớp Đất Bề Mặt*
  - X-axis: `dim_date[month_name]`
  - Y-axis: `AVERAGE(fact_temperature[temperature_2m])` và `AVERAGE(fact_temperature[temperature_soil_0cm])`.

---

### TRANG 2: PHÂN TÍCH CHUYÊN SÂU THIÊN TAI LỊCH SỬ 1999 - 2026
*(Historic Extreme Events & Flood Inundation Analysis)*

#### 1. Thẻ Tóm Tắt Thiệt Hại (Top Cards):
- **Card 1**: `[Total Disaster Damage (Billion VND)]` — *Tổng Thiệt Hại Ước Tính (Tỷ VNĐ)*.
- **Card 2**: `[Total Affected Population]` — *Tổng Số Lượt Người Dân Bị Ảnh Hưởng*.
- **Card 3**: `MAX(fact_extreme_events[peak_rainfall_24h_mm])` — *Lượng Mưa 24h Đỉnh Kỷ Lục (mm)* (970 mm tại Huế 1999 / 795 mm tại Đà Nẵng 2022).
- **Card 4**: `MAX(fact_wind[wind_gusts_10m])` — *Gió Giật Đỉnh Bão (m/s)* (45.5 m/s - Cấp 14 cuồng phong).

#### 2. Biểu Đồ & Bảng Phân Tích Sự Kiện Lịch Sử:
- **Visual 1 (Scatter / Bubble Chart)**: *Ma Trận Thiên Tai Cực Đoan (Lượng Mưa vs Gió vs Thiệt Hại)*
  - X-axis: `fact_extreme_events[peak_rainfall_24h_mm]` (Lượng mưa 24h)
  - Y-axis: `fact_extreme_events[max_wind_speed_kmh]` (Tốc độ gió)
  - Size: `fact_extreme_events[estimated_damage_billion_vnd]` (Mức độ thiệt hại)
  - Legend: `fact_extreme_events[event_type]`
  - *Ý nghĩa*: Nhận diện sự kiện nào gây thiệt hại do bão gió (như Xangsane 2006, Molave 2020) và sự kiện nào gây thiệt hại do đại lũ ngập lụt (như Đại hồng thủy 1999, Lũ kép 2020).
- **Visual 2 (Matrix Table - Ma Trận Lũ Lụt Lưu Vực Sông)**:
  - Rows: `dim_location[major_river_basin]` (Sông Hương, Sông Vu Gia - Thu Bồn, Sông Trà Khúc, Sông Ngàn Sâu...)
  - Columns: `dim_date[year]` (1999, 2006, 2013, 2020, 2022, 2024, 2026)
  - Values: `MAX(fact_extreme_events[flood_alarm_level])`
  - *Ý nghĩa*: Theo dõi tần suất các con sông lớn miền Trung vượt mức Báo động 3.
- **Visual 3 (Detailed Events Table - Bảng Chi Tiết Sự Kiện Thiên Tai)**:
  - Cột: Ngày, Tỉnh/Thành, Tên sự kiện thiên tai, Lượng mưa 24h, Cấp báo động lũ, Thiệt hại (Tỷ đồng), Số dân ảnh hưởng, Biện pháp ứng phó khẩn cấp đã thực hiện.

---

### TRANG 3: CẢNH BÁO SỚM & HỖ TRỢ SINH KẾ NGƯỜI DÂN
*(Prescriptive Analytics: Community Support, Agriculture & Construction)*

Trang này là **điểm nhấn giá trị nhân văn cao nhất của đồ án**, chuyển đổi dữ liệu kho thành khuyến nghị hành động cụ thể cho đời sống người dân miền Trung:

#### 1. Hệ Thống Thẻ Trạng Thái Cảnh Báo Realtime (Alert Cards):
- **Alert Card 1**: `[Flood Warning Level]` (Hiển thị màu động: Xanh an toàn / Vàng BĐ1 / Cam BĐ2 / Đỏ BĐ3+).
- **Alert Card 2**: `[Landslide Risk Level]` (Cảnh báo nguy cơ sạt lở đất đồi núi sườn dốc).
- **Alert Card 3**: `[Marine Safety Status]` (Thông báo an toàn cho ngư dân vươn khơi bám biển).

#### 2. Khuyến Nghị Sinh Kế Cho Từng Ngành:
- **Visual 1 (Bảng Khuyến Nghị Nông Nghiệp & Lịch Mùa Vụ Tránh Lũ)**:
  - Rows: `dim_date[month_name]` (Tháng 1 đến Tháng 12)
  - Columns: `dim_location[city_name]`
  - Values: `[Crop Recommendation]`
  - *Ý nghĩa*: Cảnh báo người dân các tháng 9, 10, 11 tuyệt đối không gieo lúa ở bãi bồi ven sông; chuyển sang giống lúa ngắn ngày thu hoạch trước 31/08 để tránh bão sớm.
- **Visual 2 (Bảng Khuyến Nghị An Toàn Thi Công Xây Dựng)**:
  - Rows: `dim_date[month_name]`
  - Values: `[Avg Rain Daily]`, `[Avg Soil Moisture]`, `[Construction Recommendation]`
  - *Ý nghĩa*: Hướng dẫn các nhà thầu thi công hạ tầng giao thông, hầm đường bộ, kè đê biển dừng các hạng mục đào đất và giàn giáo khi thời tiết xấu.
- **Visual 3 (Biểu Đồ Cân Bằng Nước & Quản Lý Hồ Chứa)**:
  - X-axis: `dim_date[month_name]`
  - Y-axis: `[Total Rain]` và `[Total Evapotranspiration]`
  - Line Y2: `[Avg Water Balance]`
  - Bảng chú giải kèm Measure: `[Water Recommendation]` (Hướng dẫn xả đáy đón lũ trước bão và đóng cống ngăn mặn vào mùa khô).

---

## III. HƯỚNG DẪN 3 BƯỚC MỞ & TẠO FILE PBIX TRÊN WINDOWS

1. **Bước 1**: Mở phần mềm **Power BI Desktop** trên máy tính Windows của bạn.
2. **Bước 2 (Nạp dữ liệu)**:
   - Vào tab **Home** -> Nhấn **Transform Data** (Biến đổi dữ liệu).
   - Chọn **New Source** -> **Folder** -> Chọn đường dẫn: `D:\MyFiles\Weather-datawarehouse\central_weather_dw\data`.
   - Hoặc vào **Advanced Editor** dán các đoạn mã M trong file `power_query_setup.m` để tạo nhanh 11 bảng.
   - Nhấn **Close & Apply**.
3. **Bước 3 (Tạo Measures & Dựng Visuals)**:
   - Nhấp chuột phải vào bảng bất kỳ (ví dụ `fact_precipitation`) -> Chọn **New Measure**.
   - Copy các công thức trong file `dax_measures.dax` dán vào thanh công thức DAX.
   - Kéo thả các trường dữ liệu và Measures vào các visual containers theo đúng cẩm nang bố cục ở Mục II phía trên.
   - Nhấn **Save** lưu file với tên: `central_weather_dw\Central_Vietnam_Weather_DW.pbix`.
