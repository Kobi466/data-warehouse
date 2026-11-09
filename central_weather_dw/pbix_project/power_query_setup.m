/*
================================================================================
POWER QUERY M SCRIPT TỰ ĐỘNG NẠP 11 BẢNG VÀO POWER BI DESKTOP
Dự án: Central Vietnam Weather & Disaster Data Warehouse (1999 - 2026)
================================================================================
Hướng dẫn sử dụng trong Power BI Desktop:
1. Mở Power BI Desktop -> Vào "Transform Data" (Biến đổi dữ liệu / Power Query Editor).
2. Vào tab "Home" -> Chọn "New Source" (Nguồn mới) -> Chọn "Folder" (Thư mục).
3. Trỏ đường dẫn đến thư mục: D:\MyFiles\Weather-datawarehouse\central_weather_dw\data
4. Hoặc tạo từng "Blank Query" (Truy vấn trống) và dán đoạn mã M tương ứng dưới đây:
================================================================================
*/

// ==========================================
// 1. DIMENSION: dim_location
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\dim_location.csv"),[Delimiter=",", Columns=10, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"location_key", Int64.Type},
        {"city_name", type text},
        {"region", type text},
        {"sub_region", type text},
        {"latitude", type number},
        {"longitude", type number},
        {"elevation_m", Int64.Type},
        {"major_river_basin", type text},
        {"terrain_type", type text},
        {"vulnerability_level", type text}
    })
in
    #"Changed Type"


// ==========================================
// 2. DIMENSION: dim_date
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\dim_date.csv"),[Delimiter=",", Columns=11, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"date_key", Int64.Type},
        {"full_date", type date},
        {"day", Int64.Type},
        {"month", Int64.Type},
        {"month_name", type text},
        {"quarter", type text},
        {"year", Int64.Type},
        {"season", type text},
        {"crop_season", type text},
        {"enso_phase", type text},
        {"is_typhoon_season", Int64.Type}
    })
in
    #"Changed Type"


// ==========================================
// 3. DIMENSION: dim_weather_condition
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\dim_weather_condition.csv"),[Delimiter=",", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"weather_condition_key", Int64.Type},
        {"weather_code", Int64.Type},
        {"condition_name_vi", type text},
        {"condition_name_en", type text},
        {"main_group", type text},
        {"disaster_warning_flag", Int64.Type},
        {"description", type text}
    })
in
    #"Changed Type"


// ==========================================
// 4. DIMENSION: dim_wind_direction
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\dim_wind_direction.csv"),[Delimiter=",", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"direction_id", Int64.Type},
        {"direction_code", type text},
        {"name_en", type text},
        {"name_vn", type text},
        {"degree_min", type number},
        {"degree_max", type number},
        {"seasonal_pattern", type text},
        {"impact_type", type text}
    })
in
    #"Changed Type"


// ==========================================
// 5. DIMENSION: dim_time
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\dim_time.csv"),[Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"time_key", Int64.Type},
        {"hour_24", Int64.Type},
        {"hour_12", Int64.Type},
        {"am_pm", type text},
        {"period_of_day", type text},
        {"activity_window", type text}
    })
in
    #"Changed Type"


// ==========================================
// 6. FACT: fact_extreme_events
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_extreme_events.csv"),[Delimiter=",", Columns=11, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"event_key", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"event_name", type text},
        {"event_type", type text},
        {"peak_rainfall_24h_mm", type number},
        {"flood_alarm_level", type text},
        {"max_wind_speed_kmh", type number},
        {"estimated_damage_billion_vnd", type number},
        {"affected_population", Int64.Type},
        {"response_action_taken", type text}
    })
in
    #"Changed Type"


// ==========================================
// 7. FACT: fact_precipitation
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_precipitation.csv"),[Delimiter=",", Columns=10, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"fact_precip_id", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"weather_condition_key", Int64.Type},
        {"rain_mm", type number},
        {"rain_probability", type number},
        {"evapotranspiration", type number},
        {"water_balance", type number},
        {"soil_saturation_pct", Int64.Type},
        {"flood_risk_score", Int64.Type}
    })
in
    #"Changed Type"


// ==========================================
// 8. FACT: fact_temperature
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_temperature.csv"),[Delimiter=",", Columns=10, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"fact_temp_id", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"temperature_2m", type number},
        {"temperature_max", type number},
        {"temperature_min", type number},
        {"temperature_soil_0cm", type number},
        {"relative_humidity_pct", Int64.Type},
        {"soil_moisture", type number},
        {"apparent_temperature", type number}
    })
in
    #"Changed Type"


// ==========================================
// 9. FACT: fact_wind
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_wind.csv"),[Delimiter=",", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"fact_wind_id", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"direction_id", Int64.Type},
        {"wind_speed_10m", type number},
        {"wind_gusts_10m", type number},
        {"beaufort_scale", Int64.Type},
        {"sea_condition", type text}
    })
in
    #"Changed Type"


// ==========================================
// 10. FACT: fact_solar_radiation
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_solar_radiation.csv"),[Delimiter=",", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"fact_solar_id", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"shortwave_radiation", type number},
        {"direct_radiation", type number},
        {"diffuse_radiation", type number},
        {"uv_index", type number},
        {"sunshine_duration_hours", type number}
    })
in
    #"Changed Type"


// ==========================================
// 11. FACT: fact_atmospheric
// ==========================================
let
    Source = Csv.Document(File.Contents("D:\MyFiles\Weather-datawarehouse\central_weather_dw\data\fact_atmospheric.csv"),[Delimiter=",", Columns=9, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"fact_atmos_id", Int64.Type},
        {"date_key", Int64.Type},
        {"location_key", Int64.Type},
        {"surface_pressure_hpa", type number},
        {"sea_level_pressure_hpa", type number},
        {"visibility_km", type number},
        {"cloud_cover_pct", Int64.Type},
        {"cloud_low_pct", Int64.Type},
        {"cloud_high_pct", Int64.Type}
    })
in
    #"Changed Type"
