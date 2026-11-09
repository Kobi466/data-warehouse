"""
Script sinh bộ dữ liệu dày đặc chuẩn hóa cho Kho Dữ Liệu Miền Trung (1999 - 2026)
Đảm bảo tính chân thực theo khoa học khí tượng, chuỗi thời gian liên tục 28 năm trên 11 tỉnh thành.
"""

import os
import csv
import random
import math
from datetime import date, timedelta

# Cố định seed ngẫu nhiên để tái lặp 100%
random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 11 đơn vị hành chính miền Trung 2026
LOCATIONS = [
    {"key": 1, "name": "Thanh Hóa", "base_temp": 24.5, "rain_factor": 0.90, "foehn": 1.15, "highland": False, "elev": 9},
    {"key": 2, "name": "Nghệ An", "base_temp": 24.8, "rain_factor": 1.00, "foehn": 1.35, "highland": False, "elev": 12},
    {"key": 3, "name": "Hà Tĩnh", "base_temp": 24.7, "rain_factor": 1.15, "foehn": 1.40, "highland": False, "elev": 6},
    {"key": 4, "name": "Quảng Trị", "base_temp": 25.2, "rain_factor": 1.25, "foehn": 1.45, "highland": False, "elev": 15},
    {"key": 5, "name": "Huế", "base_temp": 25.0, "rain_factor": 1.60, "foehn": 1.20, "highland": False, "elev": 10}, # Rốn mưa
    {"key": 6, "name": "Đà Nẵng", "base_temp": 26.0, "rain_factor": 1.20, "foehn": 1.10, "highland": False, "elev": 8},
    {"key": 7, "name": "Quảng Ngãi", "base_temp": 26.2, "rain_factor": 1.18, "foehn": 1.05, "highland": False, "elev": 14},
    {"key": 8, "name": "Gia Lai", "base_temp": 22.5, "rain_factor": 1.05, "foehn": 0.80, "highland": True, "elev": 750},
    {"key": 9, "name": "Đắk Lắk", "base_temp": 23.5, "rain_factor": 0.95, "foehn": 0.80, "highland": True, "elev": 500},
    {"key": 10, "name": "Khánh Hòa", "base_temp": 27.0, "rain_factor": 0.80, "foehn": 0.90, "highland": False, "elev": 11}, # Nắng nhiều
    {"key": 11, "name": "Lâm Đồng", "base_temp": 18.2, "rain_factor": 1.10, "foehn": 0.60, "highland": True, "elev": 1500} # Mát lạnh quanh năm
]

# Chu kỳ ENSO qua 28 năm (1999 - 2026)
ENSO_MAP = {
    1999: "La Nina mạnh", 2000: "La Nina", 2001: "Neutral", 2002: "El Nino",
    2003: "El Nino", 2004: "Neutral", 2005: "Neutral", 2006: "El Nino yếu",
    2007: "La Nina", 2008: "La Nina", 2009: "El Nino", 2010: "La Nina mạnh",
    2011: "La Nina", 2012: "Neutral", 2013: "Neutral", 2014: "Neutral",
    2015: "El Nino rất mạnh", 2016: "El Nino / Neutral", 2017: "La Nina yếu",
    2018: "Neutral", 2019: "El Nino", 2020: "La Nina mạnh", 2021: "La Nina",
    2022: "La Nina liên tiếp", 2023: "El Nino mạnh", 2024: "Neutral sang La Nina",
    2025: "El Nino", 2026: "Neutral"
}

# Các ngày thiên tai lịch sử cực đoan (giữ trọn vẹn khớp với fact_extreme_events)
HISTORICAL_PEAKS = {
    (19991102, 5): {"rain": 970.0, "wind": 18.5, "gust": 26.0, "cond": 10, "sat": 100, "risk": 5},
    (19991102, 6): {"rain": 650.0, "wind": 16.5, "gust": 24.5, "cond": 10, "sat": 98, "risk": 5},
    (19991103, 4): {"rain": 720.0, "wind": 17.0, "gust": 25.0, "cond": 10, "sat": 99, "risk": 5},
    (19991103, 7): {"rain": 680.0, "wind": 16.0, "gust": 24.0, "cond": 10, "sat": 97, "risk": 5},
    (20061001, 6): {"rain": 420.0, "wind": 32.0, "gust": 44.5, "cond": 15, "sat": 95, "risk": 5}, # Bão Xangsane
    (20061001, 5): {"rain": 380.0, "wind": 26.0, "gust": 36.0, "cond": 15, "sat": 92, "risk": 4},
    (20131115, 7): {"rain": 620.0, "wind": 15.5, "gust": 22.0, "cond": 10, "sat": 98, "risk": 5}, # Quảng Ngãi
    (20170915, 3): {"rain": 350.0, "wind": 29.0, "gust": 40.0, "cond": 15, "sat": 94, "risk": 4}, # Bão Doksuri
    (20171104, 10): {"rain": 410.0, "wind": 28.0, "gust": 38.0, "cond": 15, "sat": 96, "risk": 5}, # Bão Damrey
    (20201008, 4): {"rain": 850.0, "wind": 16.5, "gust": 23.5, "cond": 10, "sat": 100, "risk": 5}, # Lũ kép 2020
    (20201008, 5): {"rain": 920.0, "wind": 17.5, "gust": 25.0, "cond": 10, "sat": 100, "risk": 5},
    (20201018, 3): {"rain": 800.0, "wind": 15.0, "gust": 22.0, "cond": 10, "sat": 99, "risk": 5}, # Hồ Kẻ Gỗ
    (20201019, 2): {"rain": 540.0, "wind": 14.0, "gust": 20.0, "cond": 9, "sat": 95, "risk": 4},
    (20201028, 6): {"rain": 460.0, "wind": 31.0, "gust": 42.0, "cond": 15, "sat": 96, "risk": 5}, # Bão Molave
    (20201028, 7): {"rain": 580.0, "wind": 30.0, "gust": 40.0, "cond": 15, "sat": 98, "risk": 5},
    (20221014, 6): {"rain": 795.0, "wind": 18.0, "gust": 26.0, "cond": 10, "sat": 100, "risk": 5}, # Ngập lụt Đà Nẵng
    (20221014, 5): {"rain": 680.0, "wind": 16.5, "gust": 24.0, "cond": 10, "sat": 98, "risk": 5},
    (20240907, 1): {"rain": 380.0, "wind": 22.0, "gust": 32.0, "cond": 9, "sat": 92, "risk": 4}, # Bão Yagi
    (20241027, 6): {"rain": 450.0, "wind": 25.0, "gust": 35.0, "cond": 15, "sat": 95, "risk": 4}, # Bão Trami
    (20241027, 5): {"rain": 710.0, "wind": 24.0, "gust": 34.0, "cond": 10, "sat": 99, "risk": 5},
    (20261108, 3): {"rain": 350.0, "wind": 16.0, "gust": 23.0, "cond": 9, "sat": 94, "risk": 4}, # Đợt 11/2026
    (20261109, 5): {"rain": 550.0, "wind": 17.5, "gust": 25.0, "cond": 10, "sat": 98, "risk": 5},
    (20261109, 6): {"rain": 420.0, "wind": 16.0, "gust": 23.0, "cond": 10, "sat": 95, "risk": 4},
    (20261110, 7): {"rain": 480.0, "wind": 16.5, "gust": 24.0, "cond": 9, "sat": 96, "risk": 5},
    (20261111, 4): {"rain": 390.0, "wind": 15.5, "gust": 22.5, "cond": 10, "sat": 94, "risk": 4},
    (20261112, 8): {"rain": 120.0, "wind": 12.0, "gust": 18.0, "cond": 8, "sat": 78, "risk": 3}
}


def build_date_dimension():
    """Tạo bảng dim_date đầy đủ 28 năm (1999 - 2026) gồm 12 tháng mỗi năm + các ngày bão lũ lịch sử."""
    dates = []
    seen = set()

    # 1. Thêm mốc đại diện các tháng từ 1999 đến 2026 (ngày 15 mỗi tháng)
    for y in range(1999, 2027):
        max_m = 11 if y == 2026 else 12 # Năm 2026 đến tháng 11
        for m in range(1, max_m + 1):
            d = date(y, m, 15)
            d_key = int(d.strftime("%Y%m%d"))
            if d_key not in seen:
                seen.add(d_key)
                dates.append(d)

    # 2. Thêm các ngày thiên tai cực đoan lịch sử (để khớp chuẩn fact_extreme_events)
    extreme_dates = [
        date(1999, 11, 1), date(1999, 11, 2), date(1999, 11, 3), date(1999, 11, 4), date(1999, 11, 5), date(1999, 11, 6),
        date(2006, 10, 1), date(2006, 10, 2),
        date(2013, 11, 14), date(2013, 11, 15),
        date(2017, 9, 15), date(2017, 11, 4),
        date(2020, 10, 6), date(2020, 10, 7), date(2020, 10, 8), date(2020, 10, 18), date(2020, 10, 19), date(2020, 10, 28),
        date(2022, 10, 14), date(2022, 10, 15),
        date(2024, 9, 7), date(2024, 10, 27),
        date(2026, 11, 7), date(2026, 11, 8), date(2026, 11, 9), date(2026, 11, 10), date(2026, 11, 11), date(2026, 11, 12)
    ]
    for d in extreme_dates:
        d_key = int(d.strftime("%Y%m%d"))
        if d_key not in seen:
            seen.add(d_key)
            dates.append(d)

    dates.sort()

    rows = []
    for d in dates:
        d_key = int(d.strftime("%Y%m%d"))
        y, m, day = d.year, d.month, d.day
        q = f"Quý {(m - 1) // 3 + 1}"
        m_name = f"Tháng {m}"

        # Xác định mùa khí hậu miền Trung
        if m in [1, 2]:
            season = "Mùa đông rét"
        elif m in [3, 4]:
            season = "Mùa xuân ấm"
        elif m in [5, 6, 7]:
            season = "Mùa nắng nóng phơn"
        elif m == 8:
            season = "Mùa mưa bão đầu mùa"
        elif m in [9, 10, 11]:
            season = "Mùa mưa lũ cao điểm"
        else:
            season = "Mùa đông lạnh"

        # Lịch mùa vụ nông nghiệp
        if m in [12, 1, 2, 3]:
            crop = "Vụ Đông Xuân"
        elif m in [4, 5, 6, 7, 8]:
            crop = "Vụ Hè Thu"
        else:
            crop = "Mùa mưa lũ né vụ / Vụ Thu Đông"

        enso = ENSO_MAP.get(y, "Neutral")
        is_typhoon = 1 if (m in [8, 9, 10, 11] or d in extreme_dates) else 0

        rows.append({
            "date_key": d_key,
            "full_date": d.strftime("%Y-%m-%d"),
            "day": day,
            "month": m,
            "month_name": m_name,
            "quarter": q,
            "year": y,
            "season": season,
            "crop_season": crop,
            "enso_phase": enso,
            "is_typhoon_season": is_typhoon
        })

    return rows


def generate_all_facts(date_rows):
    """Sinh dữ liệu cho 5 bảng Fact vật lý theo đặc trưng địa lý và chuỗi thời gian."""
    fact_precip = []
    fact_temp = []
    fact_wind = []
    fact_solar = []
    fact_atmos = []

    precip_id = 1
    temp_id = 1
    wind_id = 1
    solar_id = 1
    atmos_id = 1

    for d_info in date_rows:
        d_key = d_info["date_key"]
        month = d_info["month"]
        year = d_info["year"]
        enso = d_info["enso_phase"]

        # Hệ số ENSO
        enso_rain_mult = 1.0
        enso_temp_offset = 0.0
        if "La Nina" in enso:
            enso_rain_mult = 1.35 if "mạnh" in enso else 1.20
            enso_temp_offset = -0.6
        elif "El Nino" in enso:
            enso_rain_mult = 0.75 if "mạnh" in enso else 0.85
            enso_temp_offset = 0.8

        for loc in LOCATIONS:
            l_key = loc["key"]
            b_temp = loc["base_temp"]
            r_factor = loc["rain_factor"]
            foehn = loc["foehn"]
            highland = loc["highland"]

            # Kiểm tra xem có phải điểm cực trị lịch sử không
            peak = HISTORICAL_PEAKS.get((d_key, l_key))

            if peak:
                # Ngày có bão lũ lịch sử đỉnh cao
                rain = peak["rain"]
                w_speed = peak["wind"]
                w_gust = peak["gust"]
                cond_key = peak["cond"]
                soil_sat = peak["sat"]
                flood_score = peak["risk"]

                # Nhiệt độ ngày bão lũ mưa dầm: mát mẻ / se lạnh
                temp_2m = round(b_temp - 3.5 + random.uniform(-0.5, 0.5), 1)
                temp_max = round(temp_2m + 1.8, 1)
                temp_min = round(temp_2m - 1.5, 1)
                rh = random.randint(95, 100)
                soil_moist = round(0.44 + (soil_sat / 100.0) * 0.06, 2)
                evap = round(random.uniform(0.8, 1.5), 1)
                w_balance = round(rain - evap, 1)
                rain_prob = round(random.uniform(0.95, 0.99), 2)

                dir_id = 3 if month in [9, 10, 11, 12] else 5 # Đông Bắc hoặc Đông
                beaufort = 7 if w_speed >= 14 else (9 if w_speed >= 20 else 11)
                sea_cond = "Biển động dữ dội" if w_speed >= 20 else "Biển động rất mạnh"

                shortwave = round(random.uniform(2.5, 4.5), 1)
                direct_rad = round(shortwave * 0.15, 1)
                diffuse_rad = round(shortwave - direct_rad, 1)
                uv = round(random.uniform(0.8, 1.5), 1)
                sunshine = 0.0

                surf_press = round(970.0 if cond_key == 15 else 1002.0 + random.uniform(-2, 2), 1)
                sea_press = round(surf_press + 1.2, 1)
                vis = round(random.uniform(1.5, 3.5), 1)
                cloud = random.randint(95, 100)
                cloud_low = random.randint(90, 98)
                cloud_high = random.randint(80, 92)

            else:
                # Ngày khí tượng bình thường theo mùa
                # 1. Tính nhiệt độ
                if month in [1, 2]: # Đông
                    temp_base = b_temp - 4.5
                elif month in [3, 4]: # Xuân
                    temp_base = b_temp - 1.0
                elif month in [5, 6, 7]: # Hè - Gió Lào
                    temp_base = b_temp + (3.5 * (foehn - 0.5))
                elif month == 8: # Chuyển mùa
                    temp_base = b_temp + 1.5
                elif month in [9, 10, 11]: # Mùa mưa
                    temp_base = b_temp - 1.5
                else: # Tháng 12
                    temp_base = b_temp - 3.5

                temp_2m = round(temp_base + enso_temp_offset + random.uniform(-1.2, 1.2), 1)
                temp_max = round(temp_2m + random.uniform(2.5, 5.0), 1)
                temp_min = round(temp_2m - random.uniform(2.0, 4.0), 1)
                temp_soil = round(temp_2m + random.uniform(-0.5, 1.2), 1)

                # 2. Tính mưa và độ ẩm
                if month in [9, 10, 11]:
                    # Mùa mưa miền Trung
                    rain_mean = 180.0 * r_factor * enso_rain_mult
                    rain = round(max(0.0, random.gauss(rain_mean, rain_mean * 0.45)), 1)
                    rh = random.randint(82, 95)
                    soil_sat = min(96, int(60 + (rain / 20.0) + random.randint(0, 10)))
                    cond_key = 10 if rain > 100 else (9 if rain > 50 else (8 if rain > 15 else 7))
                    dir_id = random.choice([3, 4, 5]) # NE, ENE, E
                    w_speed = round(random.uniform(6.5, 14.0), 1)
                    w_gust = round(w_speed * random.uniform(1.3, 1.6), 1)
                elif month in [5, 6, 7]:
                    # Mùa hè khô nóng, gió Lào
                    rain_mean = 25.0 * r_factor * (1.2 if highland else 0.4)
                    rain = round(max(0.0, random.gauss(rain_mean, 15.0)), 1) if random.random() < 0.35 else 0.0
                    rh = random.randint(45, 65) if not highland else random.randint(65, 80)
                    soil_sat = random.randint(20, 45)
                    cond_key = 1 if rain == 0 else (11 if rain > 15 else 7)
                    dir_id = random.choice([11, 12, 13]) if not highland else random.choice([7, 8]) # SW gió Lào
                    w_speed = round(random.uniform(4.5, 9.5), 1)
                    w_gust = round(w_speed * random.uniform(1.2, 1.5), 1)
                else:
                    # Các tháng khác
                    rain_mean = 50.0 * r_factor
                    rain = round(max(0.0, random.gauss(rain_mean, 25.0)), 1) if random.random() < 0.5 else 0.0
                    rh = random.randint(70, 85)
                    soil_sat = random.randint(35, 65)
                    cond_key = 2 if rain == 0 else (7 if rain < 15 else 8)
                    dir_id = random.choice([1, 2, 3, 6, 7])
                    w_speed = round(random.uniform(3.5, 7.5), 1)
                    w_gust = round(w_speed * random.uniform(1.2, 1.4), 1)

                soil_moist = round(0.18 + (soil_sat / 100.0) * 0.28, 2)
                apparent_temp = round(temp_2m + (rh / 100.0) * 3.0 - (w_speed * 0.3), 1)

                # Bốc thoát hơi nước (tháng nóng bốc nhiều)
                evap_base = 5.5 if month in [5, 6, 7] else (3.2 if month in [8, 9, 10, 11] else 2.5)
                evap = round(evap_base + random.uniform(-0.6, 0.8), 1)
                w_balance = round(rain - evap, 1)
                rain_prob = round(min(0.95, max(0.05, rain / 120.0 + (0.1 if rh > 80 else 0))), 2)

                flood_score = 5 if rain > 250 else (4 if rain > 120 else (3 if rain > 50 else (2 if rain > 15 else 1)))

                # Gió & biển
                beaufort = 6 if w_speed >= 10.8 else (5 if w_speed >= 8.0 else (4 if w_speed >= 5.5 else 3))
                sea_cond = "Biển động" if w_speed >= 10.8 else ("Sóng trung bình" if w_speed >= 8.0 else "Biển êm")

                # Bức xạ mặt trời
                if rain > 50:
                    shortwave = round(random.uniform(3.0, 7.0), 1)
                    sunshine = round(random.uniform(0.0, 2.0), 1)
                elif month in [5, 6, 7]:
                    shortwave = round(random.uniform(18.0, 24.5), 1)
                    sunshine = round(random.uniform(7.5, 11.5), 1)
                else:
                    shortwave = round(random.uniform(11.0, 17.0), 1)
                    sunshine = round(random.uniform(4.0, 8.0), 1)

                direct_rad = round(shortwave * (0.65 if sunshine > 5 else 0.3), 1)
                diffuse_rad = round(shortwave - direct_rad, 1)
                uv = round(min(12.0, max(1.0, (shortwave / 24.0) * 11.0 + random.uniform(-0.5, 0.5))), 1)

                # Khí quyển & mây
                surf_press = round(1012.0 - (loc["elev"] * 0.09) + random.uniform(-3, 3), 1)
                sea_press = round(surf_press + (loc["elev"] * 0.09), 1)
                vis = round(random.uniform(8.0, 15.0) if rain < 10 else random.uniform(3.0, 6.0), 1)
                cloud = random.randint(80, 100) if rain > 15 else random.randint(20, 65)
                cloud_low = int(cloud * random.uniform(0.6, 0.9))
                cloud_high = int(cloud * random.uniform(0.5, 0.8))

            # Nạp vào các bảng Fact
            fact_precip.append({
                "fact_precip_id": precip_id,
                "date_key": d_key,
                "location_key": l_key,
                "weather_condition_key": cond_key,
                "rain_mm": rain,
                "rain_probability": rain_prob,
                "evapotranspiration": evap,
                "water_balance": w_balance,
                "soil_saturation_pct": soil_sat,
                "flood_risk_score": flood_score
            })
            precip_id += 1

            fact_temp.append({
                "fact_temp_id": temp_id,
                "date_key": d_key,
                "location_key": l_key,
                "temperature_2m": temp_2m,
                "temperature_max": temp_max,
                "temperature_min": temp_min,
                "temperature_soil_0cm": temp_soil if 'temp_soil' in locals() else temp_2m,
                "relative_humidity_pct": rh,
                "soil_moisture": soil_moist,
                "apparent_temperature": apparent_temp if 'apparent_temp' in locals() else temp_2m
            })
            temp_id += 1

            fact_wind.append({
                "fact_wind_id": wind_id,
                "date_key": d_key,
                "location_key": l_key,
                "direction_id": dir_id,
                "wind_speed_10m": w_speed,
                "wind_gusts_10m": w_gust,
                "beaufort_scale": beaufort,
                "sea_condition": sea_cond
            })
            wind_id += 1

            fact_solar.append({
                "fact_solar_id": solar_id,
                "date_key": d_key,
                "location_key": l_key,
                "shortwave_radiation": shortwave,
                "direct_radiation": direct_rad,
                "diffuse_radiation": diffuse_rad,
                "uv_index": uv,
                "sunshine_duration_hours": sunshine
            })
            solar_id += 1

            fact_atmos.append({
                "fact_atmos_id": atmos_id,
                "date_key": d_key,
                "location_key": l_key,
                "surface_pressure_hpa": surf_press,
                "sea_level_pressure_hpa": sea_press,
                "visibility_km": vis,
                "cloud_cover_pct": cloud,
                "cloud_low_pct": cloud_low,
                "cloud_high_pct": cloud_high
            })
            atmos_id += 1

    return fact_precip, fact_temp, fact_wind, fact_solar, fact_atmos


def write_csv(filename, fieldnames, rows):
    path = os.path.join(DATA_DIR, filename)
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Đã ghi thành công: {filename} ({len(rows):,} dòng)")


def main():
    print("=== BẮT ĐẦU SINH BỘ DỮ LIỆU DÀY ĐẶC KHO DỮ LIỆU MIỀN TRUNG (1999 - 2026) ===")

    # 1. Sinh dim_date
    date_rows = build_date_dimension()
    write_csv("dim_date.csv", [
        "date_key", "full_date", "day", "month", "month_name", "quarter",
        "year", "season", "crop_season", "enso_phase", "is_typhoon_season"
    ], date_rows)

    # 2. Sinh các bảng Fact
    f_precip, f_temp, f_wind, f_solar, f_atmos = generate_all_facts(date_rows)

    write_csv("fact_precipitation.csv", [
        "fact_precip_id", "date_key", "location_key", "weather_condition_key",
        "rain_mm", "rain_probability", "evapotranspiration", "water_balance",
        "soil_saturation_pct", "flood_risk_score"
    ], f_precip)

    write_csv("fact_temperature.csv", [
        "fact_temp_id", "date_key", "location_key", "temperature_2m",
        "temperature_max", "temperature_min", "temperature_soil_0cm",
        "relative_humidity_pct", "soil_moisture", "apparent_temperature"
    ], f_temp)

    write_csv("fact_wind.csv", [
        "fact_wind_id", "date_key", "location_key", "direction_id",
        "wind_speed_10m", "wind_gusts_10m", "beaufort_scale", "sea_condition"
    ], f_wind)

    write_csv("fact_solar_radiation.csv", [
        "fact_solar_id", "date_key", "location_key", "shortwave_radiation",
        "direct_radiation", "diffuse_radiation", "uv_index", "sunshine_duration_hours"
    ], f_solar)

    write_csv("fact_atmospheric.csv", [
        "fact_atmos_id", "date_key", "location_key", "surface_pressure_hpa",
        "sea_level_pressure_hpa", "visibility_km", "cloud_cover_pct",
        "cloud_low_pct", "cloud_high_pct"
    ], f_atmos)

    print("\n✅ HOÀN THÀNH TẤT CẢ! Tổng cộng gần 4.000 dòng trên mỗi bảng Fact, bao phủ 28 năm và 11 tỉnh thành.")


if __name__ == "__main__":
    main()
