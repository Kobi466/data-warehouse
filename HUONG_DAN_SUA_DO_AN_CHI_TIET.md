# CẨM NANG HƯỚNG DẪN HOÀN THIỆN & SỬA LỖI DASHBOARD POWER BI
## ĐỒ ÁN: KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH THÀNH MIỀN TRUNG (1999 - 2026)

> **Dành cho nhóm làm đồ án**: File này hướng dẫn chi tiết từng bước từ A đến Z để bạn và đồng đội sau khi kéo code từ Git về (`git pull`) có thể mở file `ouput/dashboard.pbix` hoặc tạo mới trên Power BI Desktop, sửa triệt để các lỗi số liệu phi lý và nâng cấp giao diện đạt điểm tối đa trước hội đồng phản biện.

---

## 📌 MỤC LỤC
1. [Tóm tắt các lỗi cần sửa ngay trên Dashboard](#1-tóm-tắt-các-lỗi-cần-sửa-ngay)
2. [Bước 1: Sửa các công thức DAX Measures (Chỉ mất 2 phút)](#2-bước-1-sửa-nhanh-toàn-bộ-dax-measures-bằng-dax-query-view)
3. [Bước 2: Sửa thiết lập Visual trên Trang 2 (Hồ sơ thiên tai)](#3-bước-2-sửa-thiết-lập-visual-trên-trang-2-hồ-sơ-thiên-tai)
4. [Bước 3: Sửa hiển thị trên Trang 3 (Cảnh báo sinh kế)](#4-bước-3-sửa-hiển-thị-trên-trang-3-cảnh-báo-sinh-kế)
5. [Bước 4: Nâng cấp thiết kế Dashboard đẹp mắt & chuyên nghiệp](#5-bước-4-nâng-cấp-thiết-kế-dashboard-chuẩn-chuyên-nghiệp)
6. [Kịch bản trả lời phản biện nếu thầy cô chất vấn](#6-kịch-bản-trả-lời-phản-biện-khi-bảo-vệ)

---

## 1. TÓM TẮT CÁC LỖI CẦN SỬA NGAY

Khi mở file `ouput/dashboard.pbix` hoặc xem các ảnh chụp màn hình trong thư mục `ouput/`, hiện tại đang có 4 điểm bất hợp lý lớn:

| Vị trí | Hiện tượng bị lỗi | Nguyên nhân | Hậu quả khi bảo vệ |
| :--- | :--- | :--- | :--- |
| **Trang 2 (Card KPI)** | Gió bão cực đại hiển thị **`2K`** (~2.000 km/h) | Power BI tự động tính **SUM** gió của cả 19 trận bão | Thầy cô trừ điểm nặng vì vận tốc gió vượt tốc độ âm thanh |
| **Trang 2 (Card KPI)** | Mưa 24h kỷ lục hiển thị **`14K`** (14.165 mm) | Power BI tự động tính **SUM** lượng mưa đỉnh của tất cả các đợt bão | Sai bản chất khí tượng (kỷ lục thật là 970 mm tại Huế năm 1999) |
| **Trang 3 (Bảng)** | Cả 11 tỉnh thành đều báo **`⛔ ĐÌNH CHỈ THI CÔNG`** | Công thức DAX cũ lấy `[Total Rain]` (>15.000 mm của 28 năm) thay vì lượng mưa ngày | Bảng bị đơ cứng, không phản ánh đúng thời tiết từng vùng |
| **Trang 1 (Card KPI)** | Khi lọc mùa hè, "Số đợt thiên tai" hiện **`--`** | `COUNTROWS` trả về giá trị rỗng (`BLANK`) | Nhìn giao diện thiếu chuyên nghiệp |

---

## 2. BƯỚC 1: SỬA NHANH TOÀN BỘ DAX MEASURES BẰNG DAX QUERY VIEW

Nhóm đã chuẩn bị sẵn file kịch bản DAX đã sửa lỗi toàn bộ tại:
👉 `central_weather_dw/pbix_project/dax_query_view_script.dax`

### Các bước thực hiện (1 click):
1. Mở file **`dashboard.pbix`** bằng **Power BI Desktop**.
2. Nhìn sang thanh công cụ dọc bên trái, nhấp vào biểu tượng thứ 4: **DAX query view** (biểu tượng trang giấy có dấu tính toán).
3. Mở file `central_weather_dw/pbix_project/dax_query_view_script.dax` bằng Notepad hoặc VS Code -> Nhấn `Ctrl + A` -> `Ctrl + C` để copy toàn bộ.
4. Dán đè toàn bộ nội dung vào khung soạn thảo của tab DAX Query View trong Power BI.
5. Nhấn nút **Run** (Chạy) ở góc trên để kiểm tra kết quả tính toán.
6. Một thanh thông báo màu vàng xuất hiện: **"Update model with changes (28)"** -> **Nhấp vào nút này**.
   *(Tất cả 28 measures trong mô hình sẽ tự động được cập nhật công thức chuẩn nhất!)*

---

## 3. BƯỚC 2: SỬA THIẾT LẬP VISUAL TRÊN TRANG 2 (HỒ SƠ THIÊN TAI)

Sau khi cập nhật DAX, bạn chuyển về tab **Report View** (biểu tượng đồ thị trên cùng bên trái):

### A. Sửa thẻ Card "Gió bão cực đại":
1. Nhấp chuột chọn thẻ Card **"Gió bão cực đại (km/h)"** (thẻ đầu tiên bên trái).
2. Nhìn sang bảng **Build visual** (Xây dựng hình ảnh) bên phải:
   - Xóa trường `max_wind_speed_kmh` đang có ra khỏi ô **Field**.
   - Kéo Measure mới: **`[Max Storm Wind Speed]`** (nằm trong bảng `fact_precipitation`) thả vào ô **Field**.
   - *Kết quả hiển thị*: Thẻ sẽ chuyển từ **2K** thành con số chuẩn xác: **`160`** (km/h của bão Xangsane).

### B. Sửa thẻ Card "Mưa 24h đỉnh kỷ lục":
1. Nhấp chuột chọn thẻ Card **"Mưa 24h đỉnh kỷ lục (mm)"** (thẻ thứ 3).
2. Ở bảng **Build visual**:
   - Xóa trường `peak_rainfall_24h_mm` cũ ra khỏi ô **Field**.
   - Kéo Measure mới: **`[Max Peak Rainfall 24h]`** thả vào ô **Field**.
   - *Kết quả hiển thị*: Thẻ sẽ chuyển từ **14K** thành **`970`** (mm của Đại hồng thủy Huế 1999).

---

## 4. BƯỚC 3: SỬA HIỂN THỊ TRÊN TRANG 3 (CẢNH BÁO SINH KẾ)

Trang 3 hiện tại đã được nạp Measure `[Construction Recommendation]` mới (dùng lượng mưa bình quân ngày thay vì tổng mưa 28 năm).

1. Mở **Trang 3 (Cảnh báo sinh kế)**.
2. Kiểm tra bảng **"Construction Recommendation"** bên trái:
   - Giờ đây, chỉ các tỉnh đang có mưa lớn trong mùa bão lũ (như Thừa Thiên Huế, Quảng Nam, Quảng Trị) mới báo đình chỉ hoặc hạn chế thi công.
   - Các tỉnh vùng cao hoặc thời tiết bình thường (Lâm Đồng, Đắk Lắk, Khánh Hòa) sẽ chuyển sang trạng thái: `✅ THI CÔNG BÌNH THƯỜNG`.
3. Kiểm tra bảng **"Water Recommendation"** bên phải:
   - Khi chọn mùa lũ cao điểm (tháng 9-11), các hồ chứa sông Hương, Thu Bồn, Trà Khúc sẽ hiển thị: `🌊 Cắt lũ hạ du: Chủ động mở cửa xả đáy đón lũ...`.

---

## 5. BƯỚC 4: NÂNG CẤP THIẾT KẾ DASHBOARD CHUẨN CHUYÊN NGHIỆP

Để Dashboard đạt điểm cao nhất về mặt thẩm mỹ và thuyết trình, hãy tinh chỉnh lại bố cục như sau:

### Gợi ý bố cục Trang 1 (Tổng quan khí hậu)
* **Thêm Slicer Tỉnh/Thành dạng Dropdown hoặc Buttons**: Đặt các nút bấm chọn nhanh các tỉnh tiêu biểu: *Toàn miền Trung, Huế (Rốn mưa), Đà Nẵng (Đô thị ven biển), Hà Tĩnh (Bão Bắc Trung Bộ), Khánh Hòa (Nắng ấm)*.
* **Thay đổi màu sắc biểu đồ đường/cột**:
  * Cột tổng lượng mưa: Chọn màu **Xanh dương đậm** (`#0284C7`).
  * Đường nhiệt độ trung bình: Chọn màu **Cam ấm** (`#EA580C`).
* **Sắp xếp lại Card KPI**: Bật viền nhẹ (Border 1px, màu `#E2E8F0`, bo góc 8px) để thẻ trông hiện đại như giao diện SaaS cao cấp.

### Gợi ý bố cục Trang 2 (Thiên tai lịch sử)
* **Bảng chi tiết thiên tai**: 
  * Chọn cột `estimated_damage_billion_vnd` -> Vào tab **Cell elements** -> Bật **Data bars** (Thanh dữ liệu màu đỏ nhạt). Khi nhìn vào bảng, người xem sẽ nhận ra ngay trận bão nào gây thiệt hại lớn nhất mà không cần đọc số.
* **Thêm biểu đồ cột xếp hạng thiệt hại**: Tạo 1 biểu đồ Clustered Bar Chart xếp hạng 5 đợt thiên tai tàn phá nặng nhất:
  1. Bão số 12 (Damrey 2017) - 13.500 Tỷ
  2. Bão số 9 (Molave 2020) - 10.500 Tỷ
  3. Bão số 10 (Doksuri 2017) - 7.000 Tỷ
  4. Lũ lịch sử Hà Tĩnh 2020 - 5.500 Tỷ
  5. Bão Xangsane 2006 - 5.300 Tỷ

### Gợi ý bố cục Trang 3 (Cảnh báo & Sinh kế)
* Giảm bớt độ rộng của các bảng chữ, thay vào đó tạo **3 Thẻ Trạng Thái Lớn (Hero Cards)**:
  * 🚨 **Cấp báo động lũ**: Dùng Measure `[Flood Warning Level]`
  * 🚢 **An toàn hàng hải & tàu cá**: Dùng Measure `[Marine Safety Status]`
  * ⛰️ **Nguy cơ sạt lở đất**: Dùng Measure `[Landslide Risk Level]`
* Người xem khi bấm vào bất kỳ tỉnh nào sẽ thấy ngay tình trạng khẩn cấp của địa phương đó đổi màu tức thì.

---

## 6. KỊCH BẢN TRẢ LỜI PHẢN BIỆN KHI BẢO VỆ

Nếu thầy cô trong hội đồng hỏi, bạn hãy tự tin trả lời theo các luận điểm kỹ thuật sau:

### Câu 1: "Tại sao nhóm chọn Galaxy Schema (Fact Constellation) thay vì Star Schema truyền thống?"
> **Trả lời:** *"Dạ thưa thầy/cô, trong khí tượng thủy văn, các hiện tượng vật lý có chu kỳ lấy mẫu và bản chất đo lường hoàn toàn độc lập. Ví dụ bức xạ mặt trời chỉ đo ban ngày, gió đo theo vận tốc gián đoạn, còn thiên tai đo theo từng sự kiện bão lũ. Nếu gộp chung vào 1 bảng Fact Star Schema khổng lồ, bảng sẽ bị thưa dữ liệu (sparse matrix) với hàng triệu giá trị NULL gây lãng phí bộ nhớ. Galaxy Schema cho phép tách thành 6 bảng Fact chuyên biệt nhưng vẫn liên kết chặt chẽ thông qua 5 Conformed Dimensions (Ngày, Địa điểm, Thời tiết, Hướng gió), tối ưu hóa tuyệt đối cho kiến trúc in-memory VertiPaq của Power BI."*

### Câu 2: "Mức độ chi tiết (Grain) của hệ thống là gì?"
> **Trả lời:** *"Dạ thưa thầy/cô, hệ thống tuân thủ 2 cấp Grain rõ ràng theo Ralph Kimball: **Daily Grain** cho các bảng quan trắc môi trường (Nhiệt độ, Lượng mưa, Gió, Khí quyển, Bức xạ) và **Event Grain** (Cấp độ sự kiện) cho bảng `fact_extreme_events` để lưu giữ toàn bộ hồ sơ 24 trận bão lũ lịch sử từ 1999 đến 2026."*

### Câu 3: "Dự án này mang lại giá trị thực tế gì ngoài việc chỉ hiển thị số liệu lịch sử?"
> **Trả lời:** *"Dạ điểm đột phá của đề tài nằm ở Trang 3 - **Prescriptive Analytics (Phân tích khuyến nghị hành động)**. Hệ thống không chỉ dừng lại ở báo cáo mô tả mà tự động tính toán các chỉ số phái sinh như Cán cân nước (Rain - Evapotranspiration), Độ bão hòa đất và Gió giật để đưa ra 3 khuyến nghị sinh kế sống còn: Lịch thời vụ nông nghiệp tránh lũ sớm trước 31/08, Cảnh báo an toàn thi công công trình và Quy chế vận hành liên hồ chứa cắt lũ hạ du cho người dân miền Trung."*

---
*Chúc nhóm hoàn thành xuất sắc buổi bảo vệ đồ án!*
