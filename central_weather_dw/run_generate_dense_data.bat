@echo off
chcp 65001 > nul
echo ==============================================================================
echo ĐANG SINH BỘ DỮ LIỆU DÀY ĐẶC KHO DỮ LIỆU MIỀN TRUNG 28 NĂM (1999 - 2026)
echo ==============================================================================
python generate_dense_data.py
echo.
echo ==============================================================================
echo ĐÃ HOÀN TẤT SINH DỮ LIỆU THÀNH CÔNG!
echo Bạn chỉ cần quay lại Power BI Desktop và bấm nút REFRESH (Làm mới) trên thanh Home.
echo ==============================================================================
pause
