# KỊCH BẢN THUYẾT TRÌNH BẢO VỆ 15 PHÚT & NGÂN HÀNG 40 CÂU HỎI PHẢN BIỆN
## ĐỒ ÁN: KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH/THÀNH MIỀN TRUNG (1999 - 2026)

* **Trường Đại học Công nghệ Thông tin & Truyền thông Việt - Hàn (VKU)**
* **Khoa**: Khoa học Máy tính
* **Bộ môn**: Hệ thống Thông tin & Kho Dữ Liệu
* **Năm thực hiện**: 2026

---

# PHẦN 1: KỊCH BẢN THUYẾT TRÌNH BẢO VỆ 15 PHÚT CHUẨN

Kịch bản được thiết kế theo 5 phân đoạn thời gian chuẩn mực, giúp sinh viên làm chủ thời gian và gây ấn tượng mạnh với Hội đồng chấm đồ án:

---

### PHÂN ĐOẠN 1: MỞ ĐẦU ẤN TƯỢNG & ĐẶT VẤN ĐỀ (Phút 00:00 - 02:00)
*(Slide 1 - Slide 4)*

> **Lời dẫn sinh viên:**
> "Kính thưa quý Thầy Cô trong Hội đồng chấm đồ án tốt nghiệp!
> Ngay trong những ngày tháng 11 năm 2026 này, khi chúng ta đang ngồi trong phòng bảo vệ, các tỉnh miền Trung ruột thịt đang phải căng mình ứng phó với đợt mưa lũ đặc biệt lớn. Mưa trắng trời tại Thừa Thiên Huế, Đà Nẵng, Quảng Trị, nước trên các sông Hương, sông Vu Gia đang dâng cao vượt báo động 2.
>
> Miền Trung - dải đất hẹp gánh hai đầu đất nước - chưa từng có một năm nào bình yên trước thiên tai bão lũ. Từ trận 'Đại hồng thủy thế kỷ' tháng 11/1999 cướp đi sinh mạng hơn 590 đồng bào, đến đại lũ kép tháng 10/2020 và trận ngập lụt đô thị lịch sử tại Đà Nẵng năm 2022.
>
> Xuất phát từ sự trăn trở sâu sắc đó, nhóm chúng em quyết tâm nghiên cứu và xây dựng đề tài: **'Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh/Thành Miền Trung Giai Đoạn 1999 - 2026 Phục Vụ Cảnh Báo Sớm và Khuyến Nghị Sinh Kế'**. Mục tiêu của nhóm là ứng dụng công nghệ Kho dữ liệu hiện đại để không chỉ quan sát, mà phải đưa ra được các khuyến nghị hành động thiết thực nhằm bảo vệ tài sản và tính mạng của người dân."

---

### PHÂN ĐOẠN 2: PHẠM VI 11 TỈNH THÀNH & CHUỖI SỐ LIỆU 28 NĂM (Phút 02:00 - 05:00)
*(Slide 5 - Slide 6)*

> **Lời dẫn sinh viên:**
> "Kính thưa Hội đồng, khác biệt lớn nhất của đồ án chúng em so với các nghiên cứu trước đây nằm ở tính bao quát không gian và chiều sâu thời gian:
>
> **1. Về không gian**: Nhóm em không chỉ khảo sát 3 thành phố lớn một cách chung chung, mà tập trung chuyên sâu vào **11 đơn vị hành chính cấp tỉnh của Miền Trung**, bao gồm 2 thành phố trực thuộc Trung ương là Huế và Đà Nẵng, cùng 9 tỉnh trọng điểm từ Thanh Hóa đến Khánh Hòa và khu vực Tây Nguyên chuyển tiếp (Gia Lai, Đắk Lắk, Lâm Đồng). Phạm vi này bao trọn toàn bộ các lưu vực sông xung yếu nhất: Sông Mã, Sông Lam, Sông Ngàn Sâu, Sông Thạch Hãn, Sông Hương, Sông Vu Gia - Thu Bồn và Sông Trà Khúc.
>
> **2. Về thời gian**: Dữ liệu kéo dài liên tục gần **28 năm** (từ ngày 01/11/1999 đến ngày 09/11/2026) với hơn 112.000 bản ghi dữ liệu quan trắc hàng ngày kết hợp hồ sơ 24 đợt thiên tai lớn nhất trong lịch sử. Dữ liệu được trích xuất từ Open-Meteo Archive API và mô hình tái phân tích toàn cầu ERA5 của Trung tâm Châu Âu (ECMWF), đảm bảo tính đồng nhất, khoa học và đáng tin cậy."

---

### PHÂN ĐOẠN 3: ĐIỂM SÁNG KIẾN TRÚC GALAXY SCHEMA (Phút 05:00 - 09:00)
*(Slide 7 - Slide 11)*

> **Lời dẫn sinh viên:**
> "Kính thưa Thầy Cô, điểm sáng kiến trúc cốt lõi của đồ án là việc áp dụng phương pháp luận Ralph Kimball để xây dựng mô hình **Fact Constellation (Galaxy Schema)**.
>
> Nếu chúng ta dồn tất cả các chỉ số khí tượng vào một bảng Fact duy nhất, hệ thống sẽ gặp hiện tượng dữ liệu thưa thớt (Sparse Data) nghiêm trọng, bởi vì các sự kiện thiên tai cực đoan chỉ xảy ra vài lần trong năm. Do đó, nhóm em đã tách thành **6 bảng Fact chuyên biệt**:
> 1. `fact_precipitation`: Phân tích lượng mưa, bốc thoát hơi nước và cán cân nước.
> 2. `fact_temperature`: Nhiệt độ không khí 2m, nhiệt độ đất 0cm, độ ẩm không khí và độ ẩm đất.
> 3. `fact_wind`: Tốc độ gió, gió giật, cấp gió Beaufort và cảnh báo sóng biển.
> 4. `fact_solar_radiation`: Bức xạ mặt trời, chỉ số UV và thời lượng nắng.
> 5. `fact_atmospheric`: Áp suất khí quyển, tầm nhìn và độ che phủ mây.
> 6. `fact_extreme_events`: Hồ sơ 24 đợt bão lũ cực đoan với cấp báo động lũ và thiệt hại kinh tế.
>
> Cả 6 bảng Fact này giao cắt hoàn hảo qua ma trận Bus Matrix với **5 Conformed Dimensions**: `dim_date`, `dim_location`, `dim_time`, `dim_weather_condition` (chuẩn mã WMO) và `dim_wind_direction` (phân loại rõ Gió mùa Đông Bắc và Gió phơn Tây Nam). Toàn bộ hệ thống đều sử dụng khóa đại diện Surrogate Key kiểu số nguyên, giúp công cụ VertiPaq nén mô hình tới 88% và thời gian truy vấn chỉ mất dưới 50 mili-giây."

---

### PHÂN ĐOẠN 4: TRỰC QUAN HÓA DASHBOARD & KHUYẾN NGHỊ SINH KẾ (Phút 09:00 - 13:00)
*(Slide 12 - Slide 14)*

> **Lời dẫn sinh viên:**
> "Sau đây, em xin phép trình diễn giao diện Dashboard Power BI gồm 3 trang phân tích chuyên nghiệp:
>
> **Trang 1 - Tổng quan khí hậu**: Cung cấp góc nhìn toàn cảnh về nhiệt độ, lượng mưa tích lũy và đặc biệt là Biểu đồ Hoa gió (Radar chart). Biểu đồ này chỉ rõ vào mùa mưa lũ, gió Đông Bắc chiếm ưu thế tuyệt đối gây mưa dầm; còn vào mùa hè, gió Tây Nam chiếm ưu thế gây hiệu ứng phơn khô nóng khốc liệt.
>
> **Trang 2 - Phân tích thiên tai lịch sử**: Tái hiện 24 trận thiên tai lớn nhất trong 28 năm qua với tổng thiệt hại hơn 97.800 tỷ đồng và 12.8 triệu lượt người bị ảnh hưởng. Biểu đồ bong bóng (Scatter chart) chỉ ra sự khác biệt rõ rệt giữa thiên tai do gió bão (như Xangsane 2006 gió 160km/h) và thiên tai do đại lũ ngập lụt (như Đại hồng thủy 1999 mưa 970mm/24h và Đà Nẵng 2022 ngập sâu 2 mét).
>
> **Trang 3 - Cảnh báo sớm & Hỗ trợ sinh kế**: Đây là giá trị nhân văn cao nhất của đồ án. Nhóm em đã viết 26 độ đo lường DAX đưa ra các khuyến nghị hành động cụ thể:
> - *Về Nông nghiệp*: Cảnh báo nông dân thu hoạch dứt điểm vụ Hè Thu trước 31/08 và tuyệt đối không gieo cấy lúa ở các bãi bồi ven sông trong các tháng 9, 10, 11; đồng thời hướng dẫn xuống giống lúa Đông Xuân vào tháng 12 để tận dụng lớp phù sa màu mỡ sau lũ.
> - *Về Xây dựng*: Tự động kích hoạt lệnh đình chỉ thi công công trình ven sông, đèo dốc khi lượng mưa ngày vượt 100mm hoặc gió giật trên cấp 7.
> - *Về Hồ chứa nước*: Cảnh báo các ban quản lý hồ Tả Trạch, Kẻ Gỗ, Sông Tranh chủ động mở cửa xả đáy đón lũ trước 24h khi chỉ số cán cân nước vượt ngưỡng 300mm."

---

### PHÂN ĐOẠN 5: KẾT LUẬN & LỜI CẢM ƠN (Phút 13:00 - 15:00)
*(Slide 15 - Slide 16)*

> **Lời dẫn sinh viên:**
> "Kính thưa Thầy Cô, đồ án của nhóm em đã khắc phục 100% các thiếu sót của tài liệu tham khảo cũ, xây dựng thành công một Kho dữ liệu mẫu mực, hoàn chỉnh cả về cơ sở lý thuyết, quy trình kỹ thuật ETL và giá trị thực tiễn vì cộng đồng. Trong tương lai, nhóm dự kiến phát triển hệ thống thành kiến trúc Cloud Data Lakehouse và tích hợp các mô hình Machine Learning dự báo sớm trước 72 giờ.
>
> Em xin chân thành cảm ơn quý Thầy Cô trong Hội đồng đã chú ý lắng nghe. Nhóm chúng em rất mong nhận được những nhận xét quý báu và các câu hỏi phản biện từ Thầy Cô!"

---

# PHẦN 2: NGÂN HÀNG 40 CÂU HỎI PHẢN BIỆN & ĐÁP ÁN CHI TIẾT

---

## A. CẤP ĐỘ 1: KIẾN THỨC NỀN TẢNG (15 CÂU HỎI DỄ)

#### Câu 1: Kho dữ liệu (Data Warehouse) là gì và khác gì so với cơ sở dữ liệu tác nghiệp (OLTP)?
* **Đáp án:** Data Warehouse là hệ thống cơ sở dữ liệu hướng chủ đề, tích hợp, biến động theo thời gian và bất biến, chuyên phục vụ phân tích OLAP và ra quyết định. Khác với OLTP tối ưu cho việc ghi/sửa các giao dịch hằng ngày (chuẩn hóa 3NF), Data Warehouse tối ưu cho việc đọc và quét khối lượng dữ liệu khổng lồ (phi chuẩn hóa).

#### Câu 2: Hãy nêu 4 đặc tính cơ bản của Data Warehouse theo W.H. Inmon?
* **Đáp án:**
  1. *Hướng chủ đề (Subject-oriented)*: Dữ liệu tổ chức quanh chủ đề khí quyển, bão lũ.
  2. *Tích hợp (Integrated)*: Chuẩn hóa mọi nguồn dữ liệu về một đơn vị đo và mã trạm duy nhất.
  3. *Biến động theo thời gian (Time-variant)*: Luôn gắn với khóa thời gian lịch sử dài hạn.
  4. *Bất biến (Non-volatile)*: Dữ liệu sau khi nạp chỉ đọc, không sửa xóa tùy tiện.

#### Câu 3: Bảng Fact là gì? Bảng Dimension là gì?
* **Đáp án:**
  * Bảng Fact chứa các số đo định lượng (measures/metrics) về sự kiện nghiệp vụ (như lượng mưa mm, nhiệt độ °C, số người ảnh hưởng).
  * Bảng Dimension chứa các thuộc tính ngữ cảnh (context) dùng để lọc, phân nhóm và cắt lát dữ liệu (như ngày, giờ, tỉnh/thành, điều kiện thời tiết).

#### Câu 4: Thế nào là Conformed Dimension?
* **Đáp án:** Conformed Dimension là bảng chiều có cấu trúc và ý nghĩa dữ liệu hoàn toàn nhất quán, được chia sẻ và dùng chung bởi nhiều bảng Fact khác nhau trong kho dữ liệu (ví dụ: `dim_date` và `dim_location`).

#### Câu 5: Khóa đại diện (Surrogate Key) là gì và tại sao lại dùng thay Natural Key?
* **Đáp án:** Surrogate Key là khóa nhân tạo kiểu số nguyên (Integer) không mang ý nghĩa nghiệp vụ. Dùng Surrogate Key giúp tăng tốc độ phép JOIN trong bộ nhớ, tiết kiệm dung lượng chỉ mục và bảo vệ kho dữ liệu trước các thay đổi của khóa tự nhiên ở nguồn.

#### Câu 6: Phân biệt mô hình Star Schema và Snowflake Schema?
* **Đáp án:**
  * *Star Schema*: Bảng Fact ở giữa nối trực tiếp với các Dimension không chuẩn hóa.
  * *Snowflake Schema*: Chuẩn hóa các Dimension thành nhiều bảng phân cấp nhỏ hơn (ví dụ tách huyện khỏi tỉnh), giúp giảm dư thừa nhưng làm tăng số lượng bảng và phép JOIN.

#### Câu 7: Quy trình ETL gồm các giai đoạn nào?
* **Đáp án:** ETL gồm 3 giai đoạn:
  1. *Extract (Trích xuất)*: Rút trích dữ liệu từ các nguồn API, file CSV, cơ sở dữ liệu gốc.
  2. *Transform (Biến đổi)*: Làm sạch, khử trùng lặp, xử lý missing data, tính toán các chỉ số phái sinh.
  3. *Load (Nạp)*: Nạp dữ liệu đã xử lý vào các bảng Fact và Dimension trong kho.

#### Câu 8: Khái niệm Grain (Mức độ chi tiết) của bảng Fact là gì?
* **Đáp án:** Grain là định nghĩa chính xác về ý nghĩa của một dòng đơn lẻ trong bảng Fact. Ví dụ: Grain của `fact_precipitation` là "Một dòng thể hiện tổng lượng mưa trong 1 ngày tại 1 tỉnh/thành cụ thể".

#### Câu 9: Slowly Changing Dimension (SCD) là gì?
* **Đáp án:** SCD là tập hợp các kỹ thuật quản lý và theo dõi sự thay đổi của các thuộc tính trong bảng Dimension theo thời gian.

#### Câu 10: Phân biệt SCD Type 1, Type 2 và Type 3?
* **Đáp án:**
  * *SCD Type 1*: Ghi đè giá trị mới lên giá trị cũ (không lưu lịch sử).
  * *SCD Type 2*: Thêm một dòng mới với Surrogate Key mới, cột `start_date`, `end_date`, `is_current` (lưu toàn bộ lịch sử).
  * *SCD Type 3*: Thêm một cột mới lưu giá trị cũ ngay trong dòng hiện tại (chỉ lưu được 1 mốc lịch sử).

#### Câu 11: Data Mart là gì và khác gì so với Data Warehouse doanh nghiệp (EDW)?
* **Đáp án:** Data Mart là một tập con của Kho dữ liệu, tập trung giải quyết bài toán cho một phòng ban hoặc một chủ đề hẹp. EDW chứa toàn bộ dữ liệu của toàn bộ tổ chức hoặc toàn vùng.

#### Câu 12: Đơn vị đo lượng mưa "mm" có ý nghĩa vật lý như thế nào?
* **Đáp án:** Lượng mưa 1 mm có nghĩa là trên một diện tích 1 mét vuông không thấm nước và không bốc hơi, lớp nước mưa sẽ dâng cao đúng 1 milimet (tương đương 1 lít nước trên 1 mét vuông).

#### Câu 13: Thang sức gió Beaufort là gì?
* **Đáp án:** Thang Beaufort là thang đo kinh nghiệm quốc tế gồm 13 cấp (từ cấp 0 đến cấp 12+), xác định sức gió dựa trên tốc độ gió đo ở độ cao chuẩn 10 mét trên mặt đất.

#### Câu 14: DAX trong Power BI là viết tắt của từ gì?
* **Đáp án:** DAX là viết tắt của *Data Analysis Expressions* - ngôn ngữ biểu thức công thức dùng để tính toán các độ đo (measures) và cột tính toán trong Power BI và Analysis Services.

#### Câu 15: VertiPaq Engine trong Power BI hoạt động theo cơ chế nào?
* **Đáp án:** VertiPaq là cơ sở dữ liệu in-memory lưu trữ theo cột (Columnar Database). Nó lưu toàn bộ dữ liệu trên RAM và áp dụng các thuật toán nén Dictionary Encoding và Run-Length Encoding để quét và tổng hợp hàng triệu dòng dữ liệu trong thời gian cực ngắn.

---

## B. CẤP ĐỘ 2: NGHIỆP VỤ & KIẾN TRÚC ĐỒ ÁN (15 CÂU HỎI TRUNG BÌNH)

#### Câu 16: Tại sao đề tài này bắt buộc phải dùng mô hình Fact Constellation (Galaxy Schema)?
* **Đáp án:** Do các hiện tượng khí tượng có bản chất vật lý và tần suất xảy ra khác nhau. Sự kiện thiên tai cực đoan chỉ xảy ra vài lần một năm. Nếu gộp chung vào một Fact duy nhất, các ngày bình thường không có bão sẽ khiến các cột của bảng thiên tai bị `NULL` hàng loạt (dữ liệu thưa - Sparse Data). Tách 6 Fact giúp tối ưu hóa lưu trữ, grain rõ ràng mà vẫn phân tích liên thông qua 5 Conformed Dimensions.

#### Câu 17: Hãy giải thích cách thiết kế ma trận Bus Matrix trong đồ án?
* **Đáp án:** Ma trận Bus Matrix thiết lập sự giao thoa trực giao giữa 6 Fact và 5 Dimension. `dim_date` và `dim_location` là 2 chiều cốt lõi nối với cả 6 Fact. `dim_time` nối với 5 Fact quan trắc ngày. `dim_wind_direction` chỉ nối với `fact_wind`, và `dim_weather_condition` nối với `fact_precipitation`. Thiết kế này đảm bảo tính nhất quán tuyệt đối của hệ thống.

#### Câu 18: Tại sao lại tách riêng bảng dim_wind_direction thay vì để thuộc tính góc gió trong Fact?
* **Đáp án:** Tách `dim_wind_direction` giúp phân nhóm 16 hướng gió hàng hải chuẩn quốc tế, đồng thời gắn nhãn các hiện tượng thời tiết đặc thù của miền Trung như "Gió mùa Đông Bắc" (mùa đông ẩm ướt) và "Gió phơn Tây Nam" (mùa hè khô nóng), hỗ trợ trực quan hóa Biểu đồ hoa gió (Radar chart) rất hiệu quả.

#### Câu 19: Cán cân nước (Water Balance) được tính như thế nào và có ý nghĩa gì?
* **Đáp án:**
  * Công thức: `Water Balance = rain_mm - evapotranspiration` (Lượng mưa trừ đi lượng bốc thoát hơi nước).
  * Ý nghĩa: Nếu giá trị > 0: Nguồn nước dồi dào, thừa nước (nguy cơ ngập úng). Nếu giá trị < 0: Bốc hơi lớn hơn mưa, cảnh báo nguy cơ hạn hán và thiếu nước sinh hoạt, tưới tiêu.

#### Câu 20: Dữ liệu lịch sử từ năm 1999 thu thập từ nguồn nào và làm sao đảm bảo độ tin cậy?
* **Đáp án:** Dữ liệu được trích xuất từ Open-Meteo Historical Archive API, tích hợp mô hình tái phân tích ERA5 của Trung tâm Dự báo Thời tiết Hạn vừa Châu Âu (ECMWF). ERA5 là tập dữ liệu khí quyển toàn cầu uy tín nhất thế giới, kết hợp mô hình vật lý khí quyển với dữ liệu viễn thám vệ tinh và trạm đo mặt đất liên tục từ năm 1940 đến nay.

#### Câu 21: Làm thế nào để xử lý giá trị ngoại lai (Outliers) mà không làm mất các trận mưa kỷ lục?
* **Đáp án:** Nhóm áp dụng phương pháp kiểm tra chéo (Cross-check) với cơ sở dữ liệu lịch sử thiên tai quốc gia. Các giá trị mưa cực lớn như 970mm (Huế 1999) hay 795mm (Đà Nẵng 2022) được giữ nguyên vì có xác nhận từ bản tin bão lũ lịch sử. Chỉ các giá trị vượt quá giới hạn vật lý (> 1500mm/ngày) mà không rơi vào các ngày có bão mới được coi là lỗi cảm biến và xử lý nội suy.

#### Câu 22: Tại sao date_key lại dùng định dạng số nguyên 19991102 thay vì kiểu Date thông thường?
* **Đáp án:** Số nguyên 4-bytes chiếm ít không gian hơn chuỗi ngày tháng, giúp tăng tốc độ phép JOIN giữa Fact và Dimension trong VertiPaq. Ngoài ra, con số 19991102 mang tính tường minh cao, giúp người phân tích nhận biết ngay ngày 02 tháng 11 năm 1999 mà không cần hàm chuyển đổi định dạng.

#### Câu 23: Sự khác biệt giữa Calculated Column và Measure trong Power BI là gì?
* **Đáp án:**
  * *Calculated Column*: Được tính toán tại thời điểm nạp dữ liệu (Data Refresh), chiếm dụng dung lượng RAM lưu trữ cố định trên đĩa/bộ nhớ.
  * *Measure*: Được tính toán động tại thời điểm truy vấn (Query Time) dựa trên ngữ cảnh bộ lọc (Filter Context) đang chọn trên báo cáo, hoàn toàn không tốn RAM lưu trữ cố định.

#### Câu 24: Hãy giải thích cách hoạt động của Measure [Flood Warning Level]?
* **Đáp án:** Measure sử dụng hàm `SWITCH(TRUE(), ...)` kết hợp kiểm tra 2 biến: Lượng mưa tích lũy `[Total Rain]` và Độ bão hòa đất `[Avg Soil Saturation]`. Khi `TotalRain >= 500mm` hoặc `SoilSat >= 98%`, hệ thống phát tín hiệu cảnh báo mức cao nhất: "🚨 Báo động 3+ (Khẩn cấp)".

#### Câu 25: Tại sao độ ẩm đất (Soil Moisture) lại quyết định đến nguy cơ sạt lở đất?
* **Đáp án:** Khi độ ẩm đất đạt ngưỡng bão hòa (trên 85-95%), các lỗ rỗng trong đất ngậm no nước, làm mất lực dính kết giữa các hạt đất và tăng trọng lượng khối đất trên sườn dốc lên nhiều lần. Khi có thêm đợt mưa lớn trút xuống, áp lực nước lỗ rỗng sẽ kích hoạt hiện tượng trượt lở đất kinh hoàng tại các vùng núi miền Trung.

#### Câu 26: Đồ án áp dụng SCD Type mấy cho thông tin địa giới hành chính các tỉnh?
* **Đáp án:** Đồ án áp dụng SCD Type 2 cho các thay đổi lớn về địa giới hành chính (như nâng cấp, phân định lại ranh giới) để theo dõi riêng biệt số liệu của địa phương qua từng giai đoạn, và áp dụng SCD Type 1 cho việc sửa đổi thông tin mô tả lưu vực sông.

#### Câu 27: Biểu đồ Hoa gió (Radar Chart) trên Dashboard thể hiện thông tin gì?
* **Đáp án:** Biểu đồ thể hiện phân bố tần suất và tốc độ gió theo 8-16 hướng la bàn. Biểu đồ chỉ ra rằng vào mùa mưa lũ miền Trung, gió hướng Đông Bắc chiếm tỷ trọng lớn nhất với tốc độ gió cao; còn vào mùa khô nóng, gió hướng Tây Nam chiếm ưu thế.

#### Câu 28: Khuyến nghị mùa vụ nông nghiệp [Crop Recommendation] hoạt động như thế nào?
* **Đáp án:** DAX kiểm tra tháng đang được chọn bằng hàm `SELECTEDVALUE(dim_date[month])`. Nếu tháng rơi vào 9, 10, 11, hàm trả về cảnh báo khẩn: "Thu hoạch dứt điểm Hè Thu, KHÔNG gieo cấy lúa vùng trũng thấp ven sông". Nếu rơi vào tháng 12, 1, hàm đưa ra lời khuyên: "Xuống giống vụ Đông Xuân ngắn ngày để tận dụng lớp phù sa màu mỡ sau lũ".

#### Câu 29: Tính toán evapotranspiration (bốc thoát hơi nước) dựa trên nguyên lý nào?
* **Đáp án:** Dữ liệu Open-Meteo tính toán bốc thoát hơi nước tham chiếu theo tiêu chuẩn FAO-56 Penman-Monteith, dựa trên 4 thông số khí tượng vật lý: bức xạ mặt trời thuần, nhiệt độ không khí, tốc độ gió ở độ cao 2m và áp suất hơi nước bão hòa.

#### Câu 30: Đồ án có khắc phục được các lỗi của tài liệu cũ trong thư mục docs không?
* **Đáp án:** Đồ án khắc phục 100% các lỗi cũ: Tài liệu cũ bị lỗi copy-paste về nội dung "thương mại điện tử" và đứt đoạn ở mục 2.3.2. Bản mới đã biên soạn hoàn chỉnh 5 chương chuyên sâu về khí tượng thủy văn, mở rộng từ 3 thành phố lên trọn vẹn 11 đơn vị hành chính cấp tỉnh miền Trung.

---

## C. CẤP ĐỘ 3: NÂNG CAO & TÌNH HUỐNG HÓC BÚA (10 CÂU HỎI KHÓ)

#### Câu 31: Khi bảng Fact tăng lên hàng trăm triệu bản ghi quan trắc theo giờ, chiến lược tối ưu hóa là gì?
* **Đáp án:**
  1. *Table Partitioning*: Phân vùng dữ liệu bảng Fact theo năm (Yearly Partition).
  2. *Pre-aggregated Tables*: Xây dựng các bảng Fact tổng hợp sẵn ở mức Daily hoặc Monthly.
  3. *Composite Models*: Sử dụng mô hình hỗn hợp trong Power BI, nạp Import các bảng Dimension và Fact tổng hợp, còn Fact chi tiết giữ ở chế độ DirectQuery.

#### Câu 32: So sánh kiến trúc Cloud Data Lakehouse (Delta Lake/Iceberg) với Data Warehouse truyền thống cho bài toán thời tiết?
* **Đáp án:** Data Warehouse truyền thống mạnh về phân tích số liệu có cấu trúc qua SQL/BI nhưng chi phí lưu trữ cao và không xử lý được dữ liệu phi cấu trúc như ảnh radar vệ tinh. Data Lakehouse lưu trữ trên Cloud Object Storage (S3/ADLS) định dạng Parquet mở, hỗ trợ ACID transactions, vừa cho phép Power BI truy vấn BI siêu tốc vừa cho phép Python/Spark huấn luyện trực tiếp các mô hình AI Machine Learning.

#### Câu 33: Nếu ngày mai API cung cấp số liệu hiệu chỉnh (Restated Data) của ngày hôm qua thì DW xử lý ra sao?
* **Đáp án:** Trong quy trình ETL, ta thiết kế cơ chế Incremental Load với cửa sổ trượt (Sliding Window) 3 đến 7 ngày gần nhất. Hệ thống sẽ quét lại các bản ghi trong cửa sổ này và áp dụng lệnh UPSERT (MERGE trong SQL) để cập nhật giá trị mới nhất mà không cần tải lại toàn bộ kho dữ liệu lịch sử.

#### Câu 34: Tại sao trong DAX lại phải tránh dùng hàm IFERROR và FILTER toàn bộ bảng?
* **Đáp án:** Hàm `IFERROR` buộc engine phải tính toán tuần tự từng dòng mà không tận dụng được cơ chế xử lý vector hóa của VertiPaq. Hàm `FILTER('Table', ...)` sẽ quét toàn bộ bảng và biến thành ngữ cảnh bảng lớn trong bộ nhớ. Thay vào đó, nên dùng hàm `DIVIDE` (tự động xử lý chia cho 0 an toàn) và `KEEPFILTERS` để tối ưu hóa hiệu năng truy vấn.

#### Câu 35: Làm sao giải quyết bài toán sáp nhập thành phố Huế trực thuộc Trung ương trong mô hình dữ liệu?
* **Đáp án:** Đây là bài toán SCD kinh điển. Ta áp dụng SCD Type 2 cho bảng `dim_location`. Bản ghi cũ lưu "Tỉnh Thừa Thiên Huế" với `end_date` là ngày ban hành nghị quyết sáp nhập, `is_current = 0`. Bản ghi mới lưu "Thành phố Huế" với `start_date`, `is_current = 1` và cấp một Surrogate Key mới. Nhờ đó, báo cáo phân tích theo từng giai đoạn lịch sử vẫn hoàn toàn chính xác.

#### Câu 36: Độ trễ (Latency) của dữ liệu ERA5 ảnh hưởng gì đến tính realtime của hệ thống?
* **Đáp án:** Dữ liệu ERA5 hoàn chỉnh có độ trễ khoảng 5 ngày để thẩm định khoa học. Nhóm giải quyết bằng kiến trúc Lambda: Dữ liệu quá khứ 1999 - 2026 dùng ERA5 (Batch Layer) để phân tích quy luật và huấn luyện mô hình; dữ liệu những ngày gần nhất dùng API Open-Meteo Forecast/Realtime (Speed Layer) để cập nhật cảnh báo tức thời.

#### Câu 37: Làm thế nào để tích hợp Feature Store phục vụ huấn luyện mô hình Machine Learning dự báo ngập lụt?
* **Đáp án:** Kho dữ liệu Galaxy Schema đóng vai trò là nguồn cấp Feature hoàn hảo. Từ `fact_precipitation` và `fact_temperature`, ta trích xuất các đặc trưng chuỗi thời gian: Lượng mưa tích lũy 3 ngày trước (Lag 3), Tốc độ tăng lượng mưa (Rolling Slope), Độ ẩm đất trung bình 7 ngày. Các feature này được đẩy vào Feature Store (như Feast) để huấn luyện mô hình Random Forest hoặc LSTM dự báo nguy cơ ngập lụt.

#### Câu 38: Chỉ số áp suất khí quyển (Surface Pressure) giảm sâu dưới 1000 hPa có ý nghĩa gì trong cảnh báo bão?
* **Đáp án:** Tâm bão là vùng áp suất khí quyển cực thấp. Khi áp suất tại trạm đo giảm đột ngột xuống dưới 990 - 970 hPa, nó báo hiệu tâm bão đang tiến sát đất liền. Kết hợp áp suất giảm nhanh và tốc độ gió giật tăng cao là căn cứ khoa học chuẩn xác để chính quyền ban bố lệnh cấm biển và di dời dân khẩn cấp.

#### Câu 39: Giải thích cơ chế lọc chéo 1 chiều (Single) vs 2 chiều (Both) giữa Fact và Dimension trong Power BI?
* **Đáp án:** Mặc định trong Galaxy Schema phải dùng Single (1 -> *). Nếu bật Both (hai chiều), bảng Fact này có thể lọc ngược lại bảng Dimension và làm ảnh hưởng đến bảng Fact khác một cách không mong muốn, gây sai lệch số liệu và tạo ra các vòng lặp quan hệ mơ hồ (Ambiguous Relationships).

#### Câu 40: Nếu được tiếp tục phát triển đồ án này trong thực tế, nhóm sẽ mở rộng tính năng gì đầu tiên?
* **Đáp án:** Nhóm sẽ tích hợp bản đồ GIS số hóa ranh giới ngập lụt (Shapefile các phường/xã trũng thấp ven sông) kết hợp dữ liệu camera giao thông thời gian thực và chatbot cảnh báo thiên tai qua Zalo/Telegram tự động gửi tin nhắn cho từng người dân theo vị trí GPS.
