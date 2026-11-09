# HƯỚNG DẪN CHI TIẾT TẠO VÀ CHẠY DỰ ÁN POWER BI (.PBIX) TRÊN WINDOWS 11
## Đề Tài: Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh Thành Miền Trung (1999 - 2026)

Chào bạn! Dưới đây là hướng dẫn chi tiết từng bước để bạn hoàn thiện và lưu file `Central_Vietnam_Weather_DW.pbix` trên máy tính Windows 11 của bạn, sử dụng toàn bộ bộ dữ liệu chuẩn hóa và mã nguồn đã được tạo sẵn trong thư mục `central_weather_dw/`.

---

## 🚀 CÁCH XEM NHANH DASHBOARD TRƯỚC (INTERACTIVE PREVIEW)
Bạn không cần chờ đợi! Bạn có thể xem và tương tác ngay lập tức với giao diện 3 trang Dashboard chuẩn Power BI bằng cách:
1. Mở File Explorer trên Windows, vào thư mục:
   `D:\MyFiles\Weather-datawarehouse\central_weather_dw\pbix_project\`
2. Nhấp đúp chuột vào file: **`interactive_preview.html`** (sẽ mở bằng Microsoft Edge hoặc Google Chrome).
3. Bạn có thể:
   - Chuyển đổi giữa 3 trang: **Trang 1: Tổng quan khí hậu**, **Trang 2: Thiên tai lịch sử 1999 - 2026**, **Trang 3: Cảnh báo sinh kế & nông nghiệp**.
   - Lọc thử theo Tỉnh/Thành phố (Huế, Đà Nẵng, Hà Tĩnh...).
   - Xem biểu đồ hoa gió (Radar chart), biểu đồ cột lượng mưa, ma trận cảnh báo bão lũ và các hộp khuyến nghị sinh kế.

---

## 🛠️ CÁC BƯỚC XÂY DỰNG FILE `.PBIX` CHUẨN TRONG POWER BI DESKTOP

### BƯỚC 1: KHỞI ĐỘNG POWER BI DESKTOP VÀ NẠP DỮ LIỆU
1. Mở phần mềm **Power BI Desktop** trên Windows.
2. Tại màn hình chính, chọn tab **Home (Trang chủ)** -> Nhấn nút **Transform Data (Biến đổi dữ liệu)** để mở cửa sổ **Power Query Editor**.
3. Nạp 11 bảng dữ liệu:
   - Trong Power Query Editor, nhấn **New Source (Nguồn mới)** -> Chọn **Blank Query (Truy vấn trống)**.
   - Nhấn nút **Advanced Editor (Bộ soạn thảo nâng cao)** trên thanh công cụ.
   - Mở file: `D:\MyFiles\Weather-datawarehouse\central_weather_dw\pbix_project\power_query_setup.m`
   - Copy từng đoạn mã M của 11 bảng (từ bảng 1 `dim_location` đến bảng 11 `fact_atmospheric`) và dán vào Advanced Editor.
   - Đổi tên truy vấn (Query Name) ở bảng điều khiển bên phải cho khớp:
     * `dim_location`
     * `dim_date`
     * `dim_weather_condition`
     * `dim_wind_direction`
     * `dim_time`
     * `fact_extreme_events`
     * `fact_precipitation`
     * `fact_temperature`
     * `fact_wind`
     * `fact_solar_radiation`
     * `fact_atmospheric`
4. Sau khi nạp đủ 11 bảng, nhấn nút **Close & Apply (Đóng và Áp dụng)** ở góc trên bên trái. Power BI sẽ tải toàn bộ dữ liệu vào bộ nhớ đệm in-memory VertiPaq.

---

### BƯỚC 2: THIẾT LẬP MỐI QUAN HỆ TRONG MODEL VIEW (GALAXY SCHEMA)
1. Ở thanh điều hướng bên trái của Power BI Desktop, nhấp vào biểu tượng **Model View (Chế độ xem mô hình)** (biểu tượng thứ 3 hình sơ đồ quan hệ).
2. Kiểm tra và kéo thả tạo các mối quan hệ (Relationships - 1 to Many `1:*`, Single filter direction):
   - Nối `dim_date[date_key]` với:
     * `fact_temperature[date_key]`
     * `fact_precipitation[date_key]`
     * `fact_wind[date_key]`
     * `fact_solar_radiation[date_key]`
     * `fact_atmospheric[date_key]`
     * `fact_extreme_events[date_key]`
   - Nối `dim_location[location_key]` với:
     * `fact_temperature[location_key]`
     * `fact_precipitation[location_key]`
     * `fact_wind[location_key]`
     * `fact_solar_radiation[location_key]`
     * `fact_atmospheric[location_key]`
     * `fact_extreme_events[location_key]`
   - Nối `dim_wind_direction[direction_id]` -> `fact_wind[direction_id]`.
   - Nối `dim_weather_condition[weather_condition_key]` -> `fact_precipitation[weather_condition_key]`.

---

### BƯỚC 3: TẠO BỘ ĐO LƯỜNG DAX (26 DAX MEASURES)
1. Chuyển sang **Report View (Chế độ xem báo cáo)** (biểu tượng đầu tiên).
2. Ở bảng điều khiển **Data (Dữ liệu)** bên phải:
   - Nhấp chuột phải vào bảng `fact_precipitation` -> Chọn **New Measure (Biện pháp đo mới)**.
3. Mở file `D:\MyFiles\Weather-datawarehouse\central_weather_dw\pbix_project\dax_measures.dax`.
4. Lần lượt copy từng công thức DAX và dán vào thanh công thức (Formula Bar), bao gồm:
   - Nhóm KPI: `[Avg Temperature]`, `[Total Rain]`, `[Avg Rain Daily]`, `[Avg Wind Speed]`, `[Extreme Events Count]`, `[Total Disaster Damage (Billion VND)]`, `[Total Affected Population]`.
   - Nhóm Thủy văn & Cân bằng nước: `[Avg Water Balance]`, `[Avg Soil Saturation]`, `[Total Evapotranspiration]`, `[Avg Soil Moisture]`.
   - Nhóm Cảnh báo bão lũ: `[Flood Warning Level]`, `[Landslide Risk Level]`, `[Marine Safety Status]`.
   - Nhóm Khuyến nghị sinh kế: `[Crop Recommendation]`, `[Construction Recommendation]`, `[Water Recommendation]`.

---

### BƯỚC 4: BỐ CỤC 3 TRANG BÁO CÁO (DASHBOARD REPORT)
Mở file `D:\MyFiles\Weather-datawarehouse\central_weather_dw\pbix_project\DASHBOARD_DESIGN_GUIDE.md` để xem hướng dẫn kéo thả chi tiết:

- **Trang 1: Tổng Quan Khí Hậu & Bão Lũ Miền Trung**:
  + 5 Thẻ KPI Card trên cùng (`Avg Temperature`, `Total Rain`, `Avg Wind Speed`, `Extreme Events Count`, `Avg Water Balance`).
  + Hàng bộ lọc Slicers: `dim_location[city_name]`, `dim_date[year]`, `dim_date[season]`.
  + Biểu đồ Line & Clustered Column: Xu hướng lượng mưa và nhiệt độ qua các năm.
  + Biểu đồ Clustered Bar: Xếp hạng lượng mưa tích lũy 11 tỉnh thành.
  + Biểu đồ Radar: Hoa gió phân bố tốc độ và hướng gió theo mùa.

- **Trang 2: Phân Tích Thiên Tai Lịch Sử 1999 - 2026**:
  + Thẻ tóm tắt thiệt hại kinh tế và số dân bị ảnh hưởng.
  + Bảng ma trận các sự kiện thiên tai lịch sử (Đại hồng thủy 1999, Bão Xangsane 2006, Đại lũ kép 2020, Ngập lụt Đà Nẵng 2022, Mưa lũ tháng 11/2026).
  + Biểu đồ Scatter / Bubble: Tương quan lượng mưa đỉnh 24h, cấp gió và thiệt hại kinh tế.

- **Trang 3: Cảnh Báo Sớm & Hỗ Trợ Sinh Kế**:
  + Thẻ cảnh báo động: Cấp báo động lũ, Nguy cơ sạt lở đất sườn dốc, Cảnh báo an toàn cho tàu thuyền ngư dân.
  + Bảng lịch mùa vụ nông nghiệp tránh lũ (`Crop Recommendation`).
  + Hướng dẫn an toàn thi công công trình xây dựng (`Construction Recommendation`).
  + Khuyến nghị điều tiết liên hồ chứa cắt lũ (`Water Recommendation`).

---

### BƯỚC 5: LƯU FILE DỰ ÁN
1. Nhấn **File** -> **Save As (Lưu dưới dạng)**.
2. Trỏ vào thư mục: `D:\MyFiles\Weather-datawarehouse\central_weather_dw\`
3. Đặt tên file: **`Central_Vietnam_Weather_DW.pbix`** và nhấn **Save**.

Như vậy, bạn đã có một dự án Power BI hoàn chỉnh, trực quan, chuyên nghiệp, vượt xa đồ án cũ về cả quy mô dữ liệu lẫn giá trị thực tiễn phục vụ cộng đồng miền Trung!
