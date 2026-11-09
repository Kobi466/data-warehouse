@echo off
chcp 65001 > nul
echo ==============================================================================
echo ĐANG TẠO BỘ 3 TÀI LIỆU ĐỒ ÁN KHO DỮ LIỆU MIỀN TRUNG (1999 - 2026)
echo ==============================================================================
python build_all_documents.py
echo.
echo ==============================================================================
echo ĐÃ HOÀN TẤT TẠO 3 FILE TÀI LIỆU CHUẨN MICROSOFT OFFICE:
echo 1. BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx (5 Chương Hoàn Chỉnh)
echo 2. BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx (Kịch bản 15p & 40 Q&A)
echo 3. Slide_Kho_Du_Lieu_Mien_Trung.pptx (16 Slides Hiện Đại)
echo ==============================================================================
pause
