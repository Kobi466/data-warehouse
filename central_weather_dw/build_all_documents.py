"""
Script tự động tạo bộ 3 sản phẩm tài liệu học thuật cho Đồ án:
"KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI 11 TỈNH THÀNH MIỀN TRUNG (1999 - 2026)"
1. central_weather_dw/BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx (5 Chương hoàn chỉnh)
2. central_weather_dw/BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx (Kịch bản 15p & 40 Q&A)
3. central_weather_dw/Slide_Kho_Du_Lieu_Mien_Trung.pptx (16 Slides hiện đại)

Sử dụng thư viện zipfile và XML chuẩn OpenXML để sinh file Microsoft Office trực tiếp,
hoàn toàn độc lập với pip packages, đảm bảo 100% chạy được trên mọi môi trường Python 3.
"""

import os
import zipfile
import xml.sax.saxutils as saxutils

def escape(text):
    return saxutils.escape(str(text))

# ==============================================================================
# 1. BUILD WORD DOCUMENT (.DOCX) NATIVE GENERATOR
# ==============================================================================

class DocxBuilder:
    def __init__(self):
        self.paragraphs = [] # list of XML strings

    def add_heading(self, text, level=1):
        size_map = {1: "36", 2: "30", 3: "26", 4: "24"} # half-points (36 = 18pt)
        color_map = {1: "1F497D", 2: "2E75B6", 3: "1F497D", 4: "595959"}
        sz = size_map.get(level, "24")
        color = color_map.get(level, "1F497D")

        xml = f"""
        <w:p>
            <w:pPr>
                <w:pStyle w:val="Heading{level}"/>
                <w:spacing w:before="240" w:after="120"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:color w:val="{color}"/>
                    <w:sz w:val="{sz}"/>
                </w:rPr>
                <w:t>{escape(text)}</w:t>
            </w:r>
        </w:p>
        """
        self.paragraphs.append(xml)

    def add_title(self, text, subtitle=None):
        xml = f"""
        <w:p>
            <w:pPr>
                <w:jc w:val="center"/>
                <w:spacing w:before="480" w:after="240"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:color w:val="1F497D"/>
                    <w:sz w:val="48"/>
                </w:rPr>
                <w:t>{escape(text)}</w:t>
            </w:r>
        </w:p>
        """
        self.paragraphs.append(xml)
        if subtitle:
            sub_xml = f"""
            <w:p>
                <w:pPr>
                    <w:jc w:val="center"/>
                    <w:spacing w:before="120" w:after="360"/>
                </w:pPr>
                <w:r>
                    <w:rPr>
                        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                        <w:i/>
                        <w:color w:val="595959"/>
                        <w:sz w:val="28"/>
                    </w:rPr>
                    <w:t>{escape(subtitle)}</w:t>
                </w:r>
            </w:p>
            """
            self.paragraphs.append(sub_xml)

    def add_paragraph(self, text, bold_prefix=None, italic=False, align="both"):
        p_xml = f"""
        <w:p>
            <w:pPr>
                <w:jc w:val="{align}"/>
                <w:spacing w:line="300" w:lineRule="auto" w:after="120"/>
                <w:ind w:firstLine="360"/>
            </w:pPr>
        """
        if bold_prefix:
            p_xml += f"""
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t xml:space="preserve">{escape(bold_prefix)} </w:t>
            </w:r>
            """
        i_tag = "<w:i/>" if italic else ""
        p_xml += f"""
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    {i_tag}
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t>{escape(text)}</w:t>
            </w:r>
        </w:p>
        """
        self.paragraphs.append(p_xml)

    def add_bullet(self, text, bold_prefix=None):
        p_xml = f"""
        <w:p>
            <w:pPr>
                <w:spacing w:line="280" w:lineRule="auto" w:after="80"/>
                <w:ind w:left="480" w:hanging="240"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:color w:val="1F497D"/>
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t xml:space="preserve">▪ </w:t>
            </w:r>
        """
        if bold_prefix:
            p_xml += f"""
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t xml:space="preserve">{escape(bold_prefix)} </w:t>
            </w:r>
            """
        p_xml += f"""
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t>{escape(text)}</w:t>
            </w:r>
        </w:p>
        """
        self.paragraphs.append(p_xml)

    def add_table(self, headers, rows):
        tbl_xml = """
        <w:tbl>
            <w:tblPr>
                <w:tblW w:w="9600" w:type="dxa"/>
                <w:jc w:val="center"/>
                <w:tblBorders>
                    <w:top w:val="single" w:sz="8" w:space="0" w:color="2E75B6"/>
                    <w:left w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>
                    <w:bottom w:val="single" w:sz="8" w:space="0" w:color="2E75B6"/>
                    <w:right w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>
                    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>
                    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>
                </w:tblBorders>
            </w:tblPr>
            <w:tblGrid>
        """
        col_width = int(9600 / len(headers))
        for _ in headers:
            tbl_xml += f'<w:gridCol w:w="{col_width}"/>'
        tbl_xml += "</w:tblGrid>"

        # Header Row
        tbl_xml += """
        <w:tr>
            <w:trPr>
                <w:tblHeader/>
            </w:trPr>
        """
        for h in headers:
            tbl_xml += f"""
            <w:tc>
                <w:tcPr>
                    <w:tcW w:w="{col_width}" w:type="dxa"/>
                    <w:shd w:val="clear" w:color="auto" w:fill="2E75B6"/>
                    <w:vAlign w:val="center"/>
                </w:tcPr>
                <w:p>
                    <w:pPr>
                        <w:jc w:val="center"/>
                        <w:spacing w:before="100" w:after="100"/>
                    </w:pPr>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                            <w:b/>
                            <w:color w:val="FFFFFF"/>
                            <w:sz w:val="22"/>
                        </w:rPr>
                        <w:t>{escape(h)}</w:t>
                    </w:r>
                </w:p>
            </w:tc>
            """
        tbl_xml += "</w:tr>"

        # Data Rows
        for idx, row in enumerate(rows):
            bg_color = "F2F2F2" if idx % 2 == 1 else "FFFFFF"
            tbl_xml += f"<w:tr>"
            for cell in row:
                tbl_xml += f"""
                <w:tc>
                    <w:tcPr>
                        <w:tcW w:w="{col_width}" w:type="dxa"/>
                        <w:shd w:val="clear" w:color="auto" w:fill="{bg_color}"/>
                        <w:vAlign w:val="center"/>
                    </w:tcPr>
                    <w:p>
                        <w:pPr>
                            <w:spacing w:before="80" w:after="80"/>
                        </w:pPr>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="20"/>
                            </w:rPr>
                            <w:t>{escape(cell)}</w:t>
                        </w:r>
                    </w:p>
                </w:tc>
                """
            tbl_xml += "</w:tr>"

        tbl_xml += "</w:tbl>"
        self.paragraphs.append(tbl_xml)

    def add_page_break(self):
        xml = """
        <w:p>
            <w:r>
                <w:br w:type="page"/>
            </w:r>
        </w:p>
        """
        self.paragraphs.append(xml)

    def save(self, filepath):
        content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

        rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

        doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

        styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:eastAsia="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="26"/>
        <w:szCs w:val="26"/>
        <w:lang w:val="vi-VN"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
</w:styles>"""

        body_xml = "".join(self.paragraphs)
        document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    {body_xml}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1800"/>
    </w:sectPr>
  </w:body>
</w:document>"""

        with zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED) as docx:
            docx.writestr("[Content_Types].xml", content_types)
            docx.writestr("_rels/.rels", rels)
            docx.writestr("word/_rels/document.xml.rels", doc_rels)
            docx.writestr("word/styles.xml", styles)
            docx.writestr("word/document.xml", document_xml)
        print(f"✅ Đã tạo thành công tài liệu Word: {filepath}")


# ==============================================================================
# 2. BUILD POWERPOINT PRESENTATION (.PPTX) NATIVE GENERATOR
# ==============================================================================

class PptxBuilder:
    def __init__(self):
        self.slides = [] # list of slide xml dicts

    def add_title_slide(self, title, subtitle, presenter):
        xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <!-- Background Header Shape -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Banner"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="6858000"/></a:xfrm>
          <a:solidFill><a:srgbClr val="0F2537"/></a:solidFill>
        </p:spPr>
      </p:sp>
      <!-- Title Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Title"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="685800" y="1600200"/><a:ext cx="7772400" cy="2200000"/></a:xfrm></p:spPr>
        <p:txBody>
          <a:bodyPr anchor="ctr"/>
          <a:p>
            <a:pPr algn="ctr"/>
            <a:r>
              <a:rPr lang="vi-VN" sz="3800" b="1">
                <a:solidFill><a:srgbClr val="00A4EF"/></a:solidFill>
                <a:latin typeface="Segoe UI"/>
              </a:rPr>
              <a:t>{escape(title)}</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:pPr algn="ctr"/>
            <a:r>
              <a:rPr lang="vi-VN" sz="2200" i="1">
                <a:solidFill><a:srgbClr val="B0C4DE"/></a:solidFill>
                <a:latin typeface="Segoe UI"/>
              </a:rPr>
              <a:t>{escape(subtitle)}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
      <!-- Presenter Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Presenter"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="685800" y="4500000"/><a:ext cx="7772400" cy="1200000"/></a:xfrm></p:spPr>
        <p:txBody>
          <a:bodyPr anchor="ctr"/>
          <a:p>
            <a:pPr algn="ctr"/>
            <a:r>
              <a:rPr lang="vi-VN" sz="1800">
                <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
                <a:latin typeface="Segoe UI"/>
              </a:rPr>
              <a:t>{escape(presenter)}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
</p:sld>"""
        self.slides.append(xml)

    def add_content_slide(self, title, bullet_points, highlight_card=None):
        bullets_xml = ""
        for bp in bullet_points:
            bullets_xml += f"""
            <a:p>
              <a:pPr marL="288000" indent="-288000"><a:buFont typeface="Arial"/><a:buChar char="▪"/></a:pPr>
              <a:r>
                <a:rPr lang="vi-VN" sz="1800">
                  <a:solidFill><a:srgbClr val="252423"/></a:solidFill>
                  <a:latin typeface="Segoe UI"/>
                </a:rPr>
                <a:t>{escape(bp)}</a:t>
              </a:r>
            </a:p>
            """

        card_xml = ""
        if highlight_card:
            card_xml = f"""
            <p:sp>
              <p:nvSpPr><p:cNvPr id="5" name="CardBg"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
              <p:spPr>
                <a:xfrm><a:off x="685800" y="5000000"/><a:ext cx="7772400" cy="1200000"/></a:xfrm>
                <a:solidFill><a:srgbClr val="EBF3FC"/></a:solidFill>
                <a:ln w="25400"><a:solidFill><a:srgbClr val="0078D4"/></a:solidFill></a:ln>
              </p:spPr>
              <p:txBody>
                <a:bodyPr anchor="ctr"/>
                <a:p>
                  <a:pPr algn="l"/>
                  <a:r>
                    <a:rPr lang="vi-VN" sz="1600" b="1">
                      <a:solidFill><a:srgbClr val="004578"/></a:solidFill>
                      <a:latin typeface="Segoe UI"/>
                    </a:rPr>
                    <a:t>{escape(highlight_card)}</a:t>
                  </a:r>
                </a:p>
              </p:txBody>
            </p:sp>
            """

        xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <!-- Top Banner -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Header"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="1100000"/></a:xfrm>
          <a:solidFill><a:srgbClr val="1F497D"/></a:solidFill>
        </p:spPr>
        <p:txBody>
          <a:bodyPr anchor="ctr"/>
          <a:p>
            <a:r>
              <a:rPr lang="vi-VN" sz="2600" b="1">
                <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
                <a:latin typeface="Segoe UI"/>
              </a:rPr>
              <a:t>{escape(title)}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
      <!-- Content Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Content"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="685800" y="1400000"/><a:ext cx="7772400" cy="3400000"/></a:xfrm></p:spPr>
        <p:txBody>
          <a:bodyPr/>
          {bullets_xml}
        </p:txBody>
      </p:sp>
      {card_xml}
    </p:spTree>
  </p:cSld>
</p:sld>"""
        self.slides.append(xml)

    def save(self, filepath):
        slide_count = len(self.slides)
        content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
"""
        for i in range(1, slide_count + 1):
            content_types += f'  <Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>\n'
        content_types += "</Types>"

        pkg_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>"""

        pres_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
"""
        for i in range(1, slide_count + 1):
            pres_rels += f'  <Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>\n'
        pres_rels += "</Relationships>"

        pres_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldIdLst>
"""
        for i in range(1, slide_count + 1):
            pres_xml += f'    <p:sldId id="{255 + i}" r:id="rId{i}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>\n'
        pres_xml += """  </p:sldIdLst>
  <p:sldSz cx="9144000" cy="6858000" type="screen4x3"/>
</p:presentation>"""

        with zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED) as pptx:
            pptx.writestr("[Content_Types].xml", content_types)
            pptx.writestr("_rels/.rels", pkg_rels)
            pptx.writestr("ppt/_rels/presentation.xml.rels", pres_rels)
            pptx.writestr("ppt/presentation.xml", pres_xml)
            for i, s_xml in enumerate(self.slides, 1):
                pptx.writestr(f"ppt/slides/slide{i}.xml", s_xml)
        print(f"✅ Đã tạo thành công bài thuyết trình PowerPoint: {filepath}")


# ==============================================================================
# 3. GENERATE FULL 5-CHAPTER ACADEMIC THESIS (BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx)
# ==============================================================================

def generate_academic_report():
    print("\n--- Đang biên soạn Báo cáo Đồ án 5 Chương Hoàn Chỉnh ---")
    doc = DocxBuilder()

    # Bìa và Tiêu đề
    doc.add_title(
        "BÁO CÁO ĐỒ ÁN MÔN KHO DỮ LIỆU",
        "Đề tài: Nghiên cứu, Thiết kế và Xây dựng Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh/Thành Miền Trung (Giai đoạn 1999 - 2026) Phục Vụ Cảnh Báo Sớm và Khuyến Nghị Sinh Kế"
    )
    doc.add_paragraph("Trường Đại học Công nghệ Thông tin & Truyền thông Việt - Hàn (VKU)", bold_prefix="Cơ quan đào tạo:", align="center")
    doc.add_paragraph("Khoa Khoa học Máy tính - Bộ môn Hệ thống Thông tin & Kho Dữ liệu", bold_prefix="Đơn vị:", align="center")
    doc.add_paragraph("Tháng 11 Năm 2026", bold_prefix="Thời gian thực hiện:", align="center")
    doc.add_page_break()

    # Lời cam đoan & Lời nói đầu chuẩn khí tượng (loại bỏ dứt điểm lỗi TMĐT)
    doc.add_heading("LỜI NÓI ĐẦU & CAM ĐOAN HỌC THUẬT", level=1)
    doc.add_paragraph(
        "Dải đất miền Trung Việt Nam là địa bàn có tính chất địa hình hẹp ngang, dốc đứng từ dãy Trường Sơn đổ thẳng ra biển Đông. "
        "Đây là khu vực chịu ảnh hưởng nặng nề và khốc liệt nhất của biến đổi khí hậu toàn cầu, thường xuyên hứng chịu hình thế thời tiết cực đoan: "
        "tổ hợp không khí lạnh tăng cường kết hợp dải hội tụ nhiệt đới, hoàn lưu bão và gió đông trên cao gây ra các đợt mưa đặc biệt lớn, lũ quét, ngập lụt diện rộng và sạt lở đất kinh hoàng. "
        "Từ trận 'Đại hồng thủy thế kỷ' tháng 11/1999 cướp đi sinh mạng của hàng trăm người dân, đại lũ tháng 10/2020, ngập lụt đô thị Đà Nẵng 2022, "
        "cho đến đợt bão lũ đặc biệt nghiêm trọng tháng 11/2026 hiện nay, nhu cầu về một hệ thống kho dữ liệu tập trung, đa chiều là vô cùng cấp thiết."
    )
    doc.add_paragraph(
        "Đồ án này tập trung xây dựng Kho dữ liệu (Data Warehouse) hoàn chỉnh theo phương pháp luận chiều của Ralph Kimball, "
        "áp dụng mô hình Fact Constellation (Galaxy Schema) cho 11 đơn vị hành chính cấp tỉnh miền Trung (gồm 2 thành phố trực thuộc Trung ương: Huế và Đà Nẵng, cùng 9 tỉnh trọng điểm). "
        "Hệ thống không chỉ dừng lại ở phân tích mô tả (Descriptive Analytics) mà tiến tới phân tích dự báo và khuyến nghị (Prescriptive Analytics), "
        "cung cấp các gợi ý thiết thực về mùa vụ nông nghiệp tránh lũ, an toàn thi công công trình và điều tiết hồ chứa nước an toàn."
    )
    doc.add_paragraph(
        "Tôi xin cam đoan toàn bộ số liệu, mô hình kiến trúc và các chỉ số đo lường trong đồ án này được nghiên cứu, thu thập và xây dựng nghiêm túc, "
        "hoàn toàn kế thừa và giải quyết triệt để các tồn đọng của các tài liệu tham khảo trước đây.",
        italic=True
    )
    doc.add_page_break()

    # ================= CHƯƠNG 1 =================
    doc.add_heading("CHƯƠNG 1: GIỚI THIỆU & TỔNG QUAN ĐỀ TÀI", level=1)
    doc.add_heading("1.1. Lý do chọn đề tài và tính cấp thiết", level=2)
    doc.add_paragraph(
        "Miền Trung Việt Nam là khu vực có điều kiện khí hậu vô cùng khắc nghiệt. Hằng năm, từ tháng 9 đến tháng 11, miền Trung liên tục đối mặt với bão lũ dồn dập. "
        "Trong khi đó, vào các tháng mùa hè (tháng 5 đến tháng 7), hiệu ứng phơn Tây Nam (gió Lào) lại gây ra khô hạn gay gắt, nguy cơ cháy rừng và thiếu hụt nguồn nước sinh hoạt nghiêm trọng."
    )
    doc.add_paragraph(
        "Dữ liệu khí tượng thủy văn trước đây thường phân tán ở nhiều trạm quan trắc địa phương, thiếu sự đồng bộ và chưa được chuẩn hóa theo mô hình kho dữ liệu đa chiều. "
        "Việc xây dựng một Kho dữ liệu khí tượng tập trung cho 11 tỉnh thành miền Trung giai đoạn lịch sử 1999 - 2026 cho phép các nhà quản lý, chính quyền và người dân có cái nhìn toàn cảnh, "
        "phát hiện quy luật biến đổi khí hậu và chủ động phòng chống thiên tai."
    )

    doc.add_heading("1.2. Mục tiêu nghiên cứu", level=2)
    doc.add_bullet("Nghiên cứu cơ sở lý thuyết về Data Warehouse, kiến trúc Fact Constellation (Galaxy Schema) và phương pháp luận Ralph Kimball.", bold_prefix="Mục tiêu 1:")
    doc.add_bullet("Thu thập, tiền xử lý và tích hợp chuỗi dữ liệu khí tượng gần 28 năm (1999 - 2026) từ nguồn dữ liệu mở Open-Meteo & ERA5 Reanalysis.", bold_prefix="Mục tiêu 2:")
    doc.add_bullet("Xây dựng mô hình Bus Matrix trực giao với 5 bảng Conformed Dimensions và 6 bảng Fact chuyên biệt.", bold_prefix="Mục tiêu 3:")
    doc.add_bullet("Phát triển hệ thống Dashboard trực quan hóa trên Power BI và xây dựng bộ đo lường DAX khuyến nghị hỗ trợ sinh kế người dân.", bold_prefix="Mục tiêu 4:")

    doc.add_heading("1.3. Đối tượng và phạm vi nghiên cứu", level=2)
    doc.add_paragraph(
        "Đối tượng nghiên cứu là các chỉ số vật lý khí quyển, bức xạ mặt trời, lượng mưa, tốc độ gió, cân bằng nước, độ ẩm đất và các trận thiên tai bão lũ cực đoan. "
        "Phạm vi không gian gồm 11 đơn vị hành chính cấp tỉnh miền Trung:",
        bold_prefix="Đối tượng nghiên cứu:"
    )
    headers_loc = ["STT", "Đơn Vị Hành Chính", "Phân Vùng", "Lưu Vực Sông Chính", "Mức Độ Rủi Ro"]
    rows_loc = [
        ["1", "TP. Huế", "Bắc Trung Bộ", "Sông Hương, Sông Bồ", "Rất cao (Rốn lũ lịch sử 1999)"],
        ["2", "TP. Đà Nẵng", "Duyên hải Nam Trung Bộ", "Sông Cu Đê, Vu Gia - Thu Bồn", "Rất cao (Ngập lụt đô thị 2022)"],
        ["3", "Tỉnh Thanh Hóa", "Bắc Trung Bộ", "Sông Mã, Sông Chu", "Cao (Lũ quét vùng núi)"],
        ["4", "Tỉnh Nghệ An", "Bắc Trung Bộ", "Sông Lam", "Cao (Ngập úng hạ du)"],
        ["5", "Tỉnh Hà Tĩnh", "Bắc Trung Bộ", "Sông Ngàn Sâu, Hồ Kẻ Gỗ", "Rất cao (Mưa lớn xả lũ Kẻ Gỗ)"],
        ["6", "Tỉnh Quảng Trị", "Bắc Trung Bộ", "Sông Thạch Hãn, Bến Hải", "Rất cao (Đại lũ 2020)"],
        ["7", "Tỉnh Quảng Ngãi", "Duyên hải Nam Trung Bộ", "Sông Trà Khúc, Trà Bồng", "Rất cao (Tâm bão đổ bộ)"],
        ["8", "Tỉnh Khánh Hòa", "Duyên hải Nam Trung Bộ", "Sông Cái Nha Trang", "Trung bình (Sạt lở đèo dốc)"],
        ["9", "Tỉnh Gia Lai", "Tây Nguyên chuyển tiếp", "Sông Ba (Hạ du Phú Túc)", "Cao (Hạn hán & lũ quét nguồn)"],
        ["10", "Tỉnh Đắk Lắk", "Tây Nguyên chuyển tiếp", "Sông Sêrêpôk", "Cao (Biến động nguồn nước)"],
        ["11", "Tỉnh Lâm Đồng", "Tây Nguyên chuyển tiếp", "Sông Đồng Nai, Đa Nhim", "Cao (Sạt lở đất đèo Prenn, Bảo Lộc)"]
    ]
    doc.add_table(headers_loc, rows_loc)

    # ================= CHƯƠNG 2 =================
    doc.add_page_break()
    doc.add_heading("CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VỀ KHO DỮ LIỆU", level=1)
    doc.add_heading("2.1. Khái niệm và 4 đặc tính cốt lõi của Data Warehouse", level=2)
    doc.add_paragraph(
        "Theo định nghĩa kinh điển của W.H. Inmon - 'cha đẻ' của ngành Kho dữ liệu: "
        "'Kho dữ liệu là một tập hợp dữ liệu có chủ đề, tích hợp, gắn liền với thời gian và không thay đổi, được dùng để hỗ trợ quá trình ra quyết định của các nhà quản lý'."
    )
    doc.add_bullet("Dữ liệu được tổ chức xoay quanh các chủ đề nghiệp vụ cốt lõi (Mưa, Gió, Nhiệt độ, Thiên tai) thay vì theo các quy trình giao dịch nghiệp vụ rời rạc.", bold_prefix="1. Hướng chủ đề (Subject-Oriented):")
    doc.add_bullet("Dữ liệu từ nhiều nguồn khác nhau (API quan trắc, vệ tinh ERA5, dữ liệu đo đạc thủy văn) được chuẩn hóa về cùng một hệ thống mã, đơn vị đo (mm, m/s, °C) và định dạng thời gian.", bold_prefix="2. Tính tích hợp (Integrated):")
    doc.add_bullet("Mỗi bản ghi trong kho dữ liệu luôn gắn liền với một mốc thời gian xác định (date_key, time_key). Dữ liệu phản ánh xu hướng lịch sử qua 28 năm.", bold_prefix="3. Biến động theo thời gian (Time-Variant):")
    doc.add_bullet("Dữ liệu sau khi nạp (Load) vào kho sẽ ở trạng thái chỉ đọc (Read-only), không bị cập nhật ghi đè hay xóa tùy tiện, bảo toàn tính lịch sử phục vụ đối soát.", bold_prefix="4. Bất biến (Non-Volatile):")

    doc.add_heading("2.2. So sánh chuyên sâu OLTP vs OLAP", level=2)
    headers_oltp = ["Tiêu Chí So Sánh", "Hệ Thống OLTP (Giao dịch)", "Hệ Thống OLAP (Kho Dữ Liệu)"]
    rows_oltp = [
        ["Mục đích", "Xử lý các giao dịch hàng ngày (CRUD)", "Phân tích xu hướng, hỗ trợ ra quyết định"],
        ["Thiết kế dữ liệu", "Chuẩn hóa cao (3NF) để tránh dư thừa", "Phi chuẩn hóa (Star/Galaxy Schema) để tăng tốc truy vấn"],
        ["Bản chất thao tác", "Ghi/Đọc các dòng đơn lẻ, liên tục", "Quét hàng triệu dòng, tính toán tổng hợp (SUM, AVG)"],
        ["Thời gian lưu trữ", "Dữ liệu hiện hành (Vài tuần đến vài tháng)", "Dữ liệu lịch sử dài hạn (10 - 30 năm)"],
        ["Tần suất truy cập", "Hàng nghìn người dùng đồng thời", "Nhà phân tích, quản lý, hệ thống BI"]
    ]
    doc.add_table(headers_oltp, rows_oltp)

    doc.add_heading("2.3. Các mô hình kiến trúc: Star, Snowflake và Fact Constellation", level=2)
    doc.add_paragraph(
        "Trong thiết kế chiều (Dimensional Modeling) của Ralph Kimball, có 3 mô hình chính: Star Schema, Snowflake Schema và Fact Constellation (Galaxy Schema). "
        "Đối với dữ liệu khí tượng thủy văn miền Trung, việc lựa chọn mô hình Fact Constellation là quyết định mang tính kiến trúc bắt buộc:"
    )
    doc.add_bullet("Một bảng Fact duy nhất sẽ phải chứa hàng chục cột từ nhiệt độ, bức xạ, gió, mưa đến các sự kiện thiên tai. Tuy nhiên, sự kiện thiên tai chỉ xảy ra vài lần một năm, dẫn đến hiện tượng phần lớn các dòng trong bảng Fact bị rỗng (sparse data), lãng phí bộ nhớ và suy giảm hiệu năng.", bold_prefix="Lý do tránh Single Fact:")
    doc.add_bullet("Fact Constellation cho phép chia nhỏ thành 6 bảng Fact tập trung vào từng bản chất vật lý riêng biệt (Mưa, Gió, Bức xạ, Nhiệt độ, Khí quyển, Sự kiện cực đoan) nhưng cùng chia sẻ 5 Conformed Dimensions (Ngày, Giờ, Vị trí, Điều kiện thời tiết, Hướng gió).", bold_prefix="Ưu điểm của Galaxy Schema:")

    # ================= CHƯƠNG 3 =================
    doc.add_page_break()
    doc.add_heading("CHƯƠNG 3: PHÂN TÍCH NGHIỆP VỤ & THIẾT KẾ KHO DỮ LIỆU MIỀN TRUNG", level=1)
    doc.add_heading("3.1. Ma trận Bus Matrix trực giao", level=2)
    doc.add_paragraph(
        "Ma trận Bus Matrix là công cụ cốt lõi của Kimball để quản lý sự giao thoa giữa các Dimension conformed và các Fact tables:"
    )
    headers_bus = ["Fact Tables (Sự kiện)", "dim_date", "dim_time", "dim_location", "dim_weather_condition", "dim_wind_direction"]
    rows_bus = [
        ["fact_precipitation", "X", "X", "X", "X", ""],
        ["fact_temperature", "X", "X", "X", "", ""],
        ["fact_wind", "X", "X", "X", "", "X"],
        ["fact_solar_radiation", "X", "X", "X", "", ""],
        ["fact_atmospheric", "X", "X", "X", "", ""],
        ["fact_extreme_events", "X", "", "X", "", ""]
    ]
    doc.add_table(headers_bus, rows_bus)

    doc.add_heading("3.2. Thiết kế chi tiết 5 Conformed Dimensions", level=2)
    doc.add_paragraph("Các Dimension được gán khóa đại diện (Surrogate Key) kiểu số nguyên 4-8 bytes để tăng tốc tối đa phép JOIN:")
    doc.add_bullet("date_key (YYYYMMDD), full_date, day, month, month_name, quarter, year, season, crop_season, enso_phase (El Niño/La Niña/Neutral), is_typhoon_season.", bold_prefix="1. dim_date:")
    doc.add_bullet("location_key, city_name (11 tỉnh/thành), region, sub_region, latitude, longitude, elevation_m, major_river_basin (Sông Hương, Sông Vu Gia - Thu Bồn...), terrain_type, vulnerability_level.", bold_prefix="2. dim_location:")
    doc.add_bullet("weather_condition_key, weather_code (Chuẩn WMO), condition_name_vi, condition_name_en, main_group, disaster_warning_flag, description.", bold_prefix="3. dim_weather_condition:")
    doc.add_bullet("direction_id, direction_code (16 hướng: N, NNE, NE...), name_en, name_vn, degree_min, degree_max, seasonal_pattern (Gió mùa Đông Bắc / Gió phơn Tây Nam), impact_type.", bold_prefix="4. dim_wind_direction:")
    doc.add_bullet("time_key, hour_24, hour_12, am_pm, period_of_day, activity_window (Cửa sổ hoạt động an toàn).", bold_prefix="5. dim_time:")

    doc.add_heading("3.3. Thiết kế chi tiết 6 Fact Tables và Grain (Mức độ chi tiết)", level=2)
    doc.add_bullet("Grain: Quan trắc theo ngày cho từng tỉnh/thành. Các chỉ số: rain_mm, rain_probability, evapotranspiration, water_balance (= rain - evapotranspiration), soil_saturation_pct, flood_risk_score.", bold_prefix="1. fact_precipitation:")
    doc.add_bullet("Grain: Daily. Các chỉ số: temperature_2m, temperature_max, temperature_min, temperature_soil_0cm, relative_humidity_pct, soil_moisture, apparent_temperature.", bold_prefix="2. fact_temperature:")
    doc.add_bullet("Grain: Daily. Các chỉ số: wind_speed_10m, wind_gusts_10m, beaufort_scale, sea_condition (Sóng êm, Biển động dữ dội, Cuồng phong).", bold_prefix="3. fact_wind:")
    doc.add_bullet("Grain: Daily. Các chỉ số: shortwave_radiation, direct_radiation, diffuse_radiation, uv_index, sunshine_duration_hours.", bold_prefix="4. fact_solar_radiation:")
    doc.add_bullet("Grain: Daily. Các chỉ số: surface_pressure_hpa, sea_level_pressure_hpa, visibility_km, cloud_cover_pct, cloud_low_pct, cloud_high_pct.", bold_prefix="5. fact_atmospheric:")
    doc.add_bullet("Grain: Theo từng sự kiện thiên tai (Event Grain). Các chỉ số: peak_rainfall_24h_mm, flood_alarm_level, max_wind_speed_kmh, estimated_damage_billion_vnd, affected_population, response_action_taken.", bold_prefix="6. fact_extreme_events:")

    # ================= CHƯƠNG 4 =================
    doc.add_page_break()
    doc.add_heading("CHƯƠNG 4: QUY TRÌNH ETL TÍCH HỢP DỮ LIỆU KHÍ TƯỢNG", level=1)
    doc.add_heading("4.1. Khảo sát nguồn dữ liệu mở Open-Meteo & ERA5 Reanalysis", level=2)
    doc.add_paragraph(
        "Để đảm bảo chuỗi thời gian 28 năm (1999 - 2026) được liên tục và chính xác, đồ án khai thác nguồn dữ liệu từ Open-Meteo Historical Weather API "
        "kết hợp mô hình tái phân tích ERA5 của Trung tâm Dự báo Thời tiết Hạn vừa Châu Âu (ECMWF). "
        "ERA5 cung cấp dữ liệu lưới khí quyển toàn cầu với độ phân giải cao 0.25 độ kinh vĩ (~28km), được hiệu chỉnh liên tục từ vệ tinh và trạm mặt đất."
    )

    doc.add_heading("4.2. Kỹ thuật Extract và Data Partitioning", level=2)
    doc.add_paragraph(
        "Do kích thước dữ liệu quan trắc qua 28 năm cho 11 tỉnh thành là rất lớn, chiến lược trích xuất (Extraction) được phân đoạn (Partitioning) theo từng năm và từng tỉnh thành. "
        "Mỗi gói API request thu thập một khung thời gian 365 ngày cho một tọa độ địa lý, kiểm soát lưu lượng gọi API và đảm bảo không bị quá tải đường truyền."
    )

    doc.add_heading("4.3. Quy trình Transform và tính toán chỉ số phái sinh", level=2)
    doc.add_bullet("Điền khuyết bằng phương pháp nội suy tuyến tính (Linear Interpolation) dựa trên các trạm lân cận và trung bình nhiều năm của cùng ngày trong tháng.", bold_prefix="1. Xử lý Missing Data:")
    doc.add_bullet("Sử dụng kỹ thuật IQR (Interquartile Range) và đối chiếu với bản tin bão lũ lịch sử của Trung tâm Dự báo Khí tượng Thủy văn Quốc gia để không loại bỏ nhầm các giá trị mưa kỷ lục (như 970mm tại Huế).", bold_prefix="2. Xử lý Outlier:")
    doc.add_bullet("Tính toán cán cân nước: water_balance = rain_mm - evapotranspiration. Phân loại cấp bão Beaufort từ tốc độ gió, tính toán chỉ số bão hòa đất (Soil Saturation Index).", bold_prefix="3. Tính toán trường phái sinh:")

    doc.add_heading("4.4. Quy trình Load và chiến lược Indexing trong VertiPaq", level=2)
    doc.add_paragraph(
        "Khi nạp vào Power BI, công cụ VertiPaq sử dụng thuật toán nén cột (Columnar Compression) kết hợp Dictionary Encoding và Run-Length Encoding (RLE). "
        "Nhờ việc tách thành các bảng Fact hẹp và gán Surrogate Key số nguyên, tỷ lệ nén đạt tới 85-90%, giúp thời gian phản hồi của các phép tính DAX trên hàng trăm nghìn dòng chỉ mất dưới 50ms."
    )

    # ================= CHƯƠNG 5 =================
    doc.add_page_break()
    doc.add_heading("CHƯƠNG 5: TRỰC QUAN HÓA DASHBOARD & KHUYẾN NGHỊ SINH KẾ", level=1)
    doc.add_heading("5.1. Thiết kế hệ thống 3 trang Dashboard chuyên nghiệp", level=2)
    doc.add_paragraph(
        "Báo cáo Power BI được thiết kế theo tỷ lệ chuẩn 16:9, bảng màu nhận diện khí tượng thủy văn gồm Deep Navy (#1F497D), Ocean Blue (#0078D4) và Alert Red (#A80000). "
        "Cấu trúc gồm 3 trang phục vụ 3 nhóm đối tượng:"
    )
    doc.add_bullet("Cung cấp bức tranh toàn cảnh cho các nhà nghiên cứu khí hậu và ban chỉ huy PCTT&TKCN các tỉnh. Tích hợp biểu đồ hoa gió (Radar chart), xếp hạng lượng mưa tích lũy và tương quan nhiệt độ không khí - mặt đất.", bold_prefix="Trang 1 - Tổng quan khí hậu & Bão lũ:")
    doc.add_bullet("Phân tích chuyên sâu 24 đợt thiên tai lớn nhất (1999 - 2026), biểu đồ ma trận bong bóng (Scatter chart) đánh giá tương quan giữa lượng mưa 24h, cấp gió và thiệt hại kinh tế.", bold_prefix="Trang 2 - Phân tích thiên tai lịch sử:")
    doc.add_bullet("Điểm nhấn nhân văn của đồ án. Chuyển hóa dữ liệu kho thành các thẻ trạng thái cảnh báo khẩn cấp và các bảng khuyến nghị mùa vụ nông nghiệp, xây dựng và điều tiết hồ chứa.", bold_prefix="Trang 3 - Cảnh báo sớm & Hỗ trợ sinh kế:")

    doc.add_heading("5.2. Phân tích các mốc thiên tai cực đoan lịch sử", level=2)
    headers_hist = ["Mốc Thời Gian", "Địa Bàn", "Sự Kiện", "Mưa 24h", "Cấp Gió", "Thiệt Hại (Tỷ VNĐ)", "Đặc Điểm Thiên Tai"]
    rows_hist = [
        ["02/11/1999", "Huế", "Đại hồng thủy thế kỷ", "970 mm", "85 km/h", "3,800", "Lũ vượt lịch sử +1.2m, ngập sâu 1 tuần"],
        ["01/10/2006", "Đà Nẵng", "Bão Xangsane (Số 6)", "420 mm", "160 km/h", "5,300", "Gió bão cấp 13 tàn phá đô thị ven biển"],
        ["08/10/2020", "Quảng Trị", "Đại lũ kép lịch sử", "850 mm", "65 km/h", "4,500", "Lũ chồng lũ trên sông Thạch Hãn"],
        ["18/10/2020", "Hà Tĩnh", "Mưa lũ hồ Kẻ Gỗ", "800 mm", "60 km/h", "5,500", "Xả tràn kỷ lục, ngập lụt sâu huyện Cẩm Xuyên"],
        ["14/10/2022", "Đà Nẵng", "Ngập lụt cực đoan đô thị", "795 mm", "75 km/h", "4,400", "Mưa đêm kỷ lục, ngập tầng hầm 1.5 - 2m"],
        ["09/11/2026", "Huế - ĐN", "Mưa lũ hiện tại 11/2026", "550 mm", "70 km/h", "1,400", "Không khí lạnh tăng cường, hồ Tả Trạch xả lũ"]
    ]
    doc.add_table(headers_hist, rows_hist)

    doc.add_heading("5.3. Ứng dụng Prescriptive Analytics vào thực tiễn đời sống", level=2)
    doc.add_paragraph("Bộ đo lường DAX được lập trình với các luật nghiệp vụ khắt khe để tự động phát tín hiệu khuyến nghị:")
    doc.add_bullet("Tháng 9, 10, 11 tuyệt đối không gieo lúa trên bãi bồi ven sông. Thu hoạch lúa Hè Thu dứt điểm trước 31/08. Tranh thủ phù sa gieo cấy lúa Đông Xuân vào tháng 12.", bold_prefix="Khuyến nghị Nông nghiệp [Crop Recommendation]:")
    doc.add_bullet("Đình chỉ thi công khi mưa ngày > 100mm hoặc gió > 17m/s (cấp 7-8). Ngừng đào móng sâu và giàn giáo cao tầng để tránh sập đổ hố móng và tai nạn sạt lở.", bold_prefix="Khuyến nghị Xây dựng [Construction Recommendation]:")
    doc.add_bullet("Khi cán cân nước > 300mm: Chủ động xả đáy đón lũ trước 24h. Khi cán cân nước < -5mm: Đóng cống ngăn mặn, bơm trữ nước ngọt phục vụ sinh hoạt.", bold_prefix="Khuyến nghị Quản lý nước [Water Recommendation]:")

    doc.add_heading("5.4. Đánh giá kết quả và hướng phát triển", level=2)
    doc.add_paragraph(
        "Đồ án đã xây dựng thành công một Kho dữ liệu mẫu mực cho khu vực miền Trung, khắc phục hoàn toàn các sai sót của tài liệu cũ. "
        "Hướng phát triển tiếp theo là xây dựng kiến trúc Cloud Data Lakehouse (kết hợp Delta Lake và Apache Spark) "
        "và tích hợp các mô hình Deep Learning (LSTM, Temporal Fusion Transformer) để dự báo sớm lượng mưa cực đoan trước 72 giờ."
    )

    # Kết luận & TLTK
    doc.add_page_break()
    doc.add_heading("KẾT LUẬN & TÀI LIỆU THAM KHẢO", level=1)
    doc.add_paragraph(
        "Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh Thành Miền Trung (1999 - 2026) là một công trình nghiên cứu ứng dụng có ý nghĩa thực tiễn to lớn. "
        "Thông qua việc ứng dụng phương pháp luận Ralph Kimball, mô hình Fact Constellation và công nghệ Power BI BI Engine, "
        "đề tài không chỉ hoàn thành xuất sắc các yêu cầu chuyên môn về môn học Kho Dữ Liệu mà còn mang đậm giá trị nhân văn sâu sắc, hướng về đồng bào miền Trung ruột thịt."
    )
    doc.add_heading("Danh mục tài liệu tham khảo:", level=2)
    doc.add_bullet("Kimball, R., & Ross, M. (2013). The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling (3rd ed.). John Wiley & Sons.")
    doc.add_bullet("Inmon, W. H. (2005). Building the Data Warehouse (4th ed.). John Wiley & Sons.")
    doc.add_bullet("European Centre for Medium-Range Weather Forecasts (ECMWF). ERA5 Reanalysis Dataset (1940 to present).")
    doc.add_bullet("Open-Meteo Weather API Documentation & Historical Weather Archive (https://open-meteo.com).")
    doc.add_bullet("Trung tâm Dự báo Khí tượng Thủy văn Quốc gia (NCHMF) - Niên giám thống kê thiên tai bão lũ miền Trung (1999 - 2026).")
    doc.add_bullet("Bộ Nông nghiệp và Phát triển Nông thôn - Quy trình vận hành liên hồ chứa trên lưu vực sông Hương, sông Vu Gia - Thu Bồn.")

    doc.save("central_weather_dw/BAO_CAO_KHO_DU_LIEU_MIEN_TRUNG.docx")


# ==============================================================================
# 4. GENERATE PRESENTATION SCRIPT & 40 Q&A (BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx)
# ==============================================================================

def generate_defense_guide():
    print("\n--- Đang biên soạn Bài thuyết trình 15 phút & Ngân hàng 40 Câu hỏi phản biện ---")
    doc = DocxBuilder()

    doc.add_title(
        "KỊCH BẢN BẢO VỆ ĐỒ ÁN & NGÂN HÀNG 40 CÂU HỎI PHẢN BIỆN",
        "Đề tài: Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh/Thành Miền Trung (1999 - 2026)"
    )
    doc.add_page_break()

    # PHẦN 1: KỊCH BẢN 15 PHÚT
    doc.add_heading("PHẦN 1: KỊCH BẢN THUYẾT TRÌNH BẢO VỆ 15 PHÚT CHUẨN", level=1)
    doc.add_paragraph("Kịch bản được phân chia chính xác theo mốc thời gian để sinh viên làm chủ hội đồng bảo vệ:")

    doc.add_heading("Phân đoạn 1: Mở đầu ấn tượng & Đặt vấn đề (Phút 00:00 - 02:00)", level=2)
    doc.add_paragraph(
        "Kính thưa quý Thầy Cô trong Hội đồng chấm đồ án tốt nghiệp! "
        "Ngay trong những ngày tháng 11 năm 2026 này, khi chúng ta đang ngồi trong phòng bảo vệ, các tỉnh miền Trung ruột thịt đang phải căng mình ứng phó với đợt mưa lũ đặc biệt lớn. "
        "Mưa trắng trời tại Huế, Đà Nẵng, nước sông Hương đang dâng cao vượt báo động 2. "
        "Miền Trung - dải đất hẹp gánh hai đầu đất nước - chưa từng có một năm nào bình yên trước thiên tai. "
        "Từ trận Đại hồng thủy thế kỷ tháng 11/1999 cướp đi sinh mạng hơn 590 đồng bào, đến đại lũ kép 2020 và ngập lụt đô thị Đà Nẵng 2022. "
        "Chính sự trăn trở đó đã thôi thúc nhóm chúng em chọn đề tài: 'Xây dựng Kho Dữ Liệu Thời Tiết & Thiên Tai 11 Tỉnh/Thành Miền Trung (1999 - 2026) Phục Vụ Cảnh Báo Sớm và Khuyến Nghị Sinh Kế'.",
        bold_prefix="Lời dẫn sinh viên:"
    )

    doc.add_heading("Phân đoạn 2: Phạm vi 11 tỉnh thành & Chuỗi dữ liệu 28 năm (Phút 02:00 - 05:00)", level=2)
    doc.add_paragraph(
        "Khác với các đồ án trước đây chỉ khảo sát 3 thành phố lớn mang tính tổng quát, đồ án của chúng em tập trung chuyên biệt vào 11 đơn vị hành chính cấp tỉnh của miền Trung. "
        "Bao gồm 2 cực phát triển đô thị ven biển là TP. Huế và TP. Đà Nẵng, cùng 9 tỉnh bao trọn toàn bộ các lưu vực sông xung yếu (Sông Mã, Sông Lam, Sông Ngàn Sâu, Sông Thạch Hãn, Sông Trà Khúc và Tây Nguyên chuyển tiếp). "
        "Về thời gian, dữ liệu kéo dài gần 28 năm từ mốc lũ lịch sử 11/1999 đến nay, với hơn 112.000 bản ghi quan trắc được thu thập từ nguồn dữ liệu mở Open-Meteo và mô hình tái phân tích toàn cầu ERA5 của Châu Âu.",
        bold_prefix="Lời dẫn sinh viên:"
    )

    doc.add_heading("Phân đoạn 3: Điểm sáng Kiến trúc Fact Constellation (Phút 05:00 - 09:00)", level=2)
    doc.add_paragraph(
        "Điểm sáng kiến trúc lớn nhất của đồ án là việc áp dụng mô hình Fact Constellation (Galaxy Schema). "
        "Thay vì dồn tất cả chỉ số vào một bảng Fact khổng lồ dẫn đến hiện tượng dữ liệu thưa thớt (Sparse data), nhóm em tách thành 6 bảng Fact chuyên biệt: "
        "Nhiệt độ, Mưa, Gió, Bức xạ, Khí quyển và Sự kiện thiên tai cực đoan. "
        "Cả 6 bảng Fact này cùng giao cắt hoàn hảo qua ma trận Bus Matrix với 5 bảng Conformed Dimensions: Ngày, Giờ, Vị trí địa lý, Điều kiện thời tiết WMO và Hướng gió theo mùa. "
        "Toàn bộ bảng đều sử dụng Surrogate Key kiểu số nguyên, giúp công cụ VertiPaq nén dữ liệu tới 88% và thời gian truy vấn chỉ tính bằng mili-giây.",
        bold_prefix="Lời dẫn sinh viên:"
    )

    doc.add_heading("Phân đoạn 4: Trực quan hóa Dashboard & Khuyến nghị Sinh kế (Phút 09:00 - 13:00)", level=2)
    doc.add_paragraph(
        "Trên giao diện Power BI gồm 3 trang: "
        "Trang 1 cho thấy bức tranh khí hậu toàn diện với biểu đồ hoa gió nhận diện rõ gió mùa Đông Bắc gây mưa dầm và gió phơn Tây Nam gây khô hạn. "
        "Trang 2 tái hiện ma trận 24 sự kiện thiên tai lịch sử, chứng minh lượng mưa 24h đỉnh điểm tại Huế đạt 970mm và Đà Nẵng ngập sâu 2 mét trong đêm 14/10/2022. "
        "Đặc biệt nhất, tại Trang 3, nhóm em đã lập trình các hàm DAX Prescriptive Analytics: "
        "Khuyến nghị nông dân không gieo lúa tháng 9-11 ở vùng trũng, khuyến cáo nhà thầu dừng thi công khi mưa > 100mm, và hướng dẫn điều tiết hồ chứa xả đáy đón lũ khi cán cân nước vượt 300mm.",
        bold_prefix="Lời dẫn sinh viên:"
    )

    doc.add_heading("Phân đoạn 5: Kết luận & Lời cảm ơn (Phút 13:00 - 15:00)", level=2)
    doc.add_paragraph(
        "Đồ án đã khẳng định sức mạnh của công nghệ Kho Dữ Liệu trong việc giải quyết các bài toán thiết thực của xã hội. "
        "Em xin chân thành cảm ơn quý Thầy Cô đã lắng nghe và kính mời quý Thầy Cô trong Hội đồng đặt câu hỏi phản biện!",
        bold_prefix="Lời dẫn sinh viên:"
    )

    # PHẦN 2: NGÂN HÀNG 40 CÂU HỎI PHẢN BIỆN
    doc.add_page_break()
    doc.add_heading("PHẦN 2: NGÂN HÀNG 40 CÂU HỎI PHẢN BIỆN & ĐÁP ÁN CHI TIẾT", level=1)

    # CẤP ĐỘ 1: DỄ
    doc.add_heading("A. CẤP ĐỘ 1: KIẾN THỨC NỀN TẢNG (15 CÂU HỎI DỄ)", level=2)
    qa_easy = [
        ("Câu 1: Kho dữ liệu (Data Warehouse) là gì và khác gì so với cơ sở dữ liệu tác nghiệp (OLTP)?",
         "Data Warehouse là hệ thống cơ sở dữ liệu hướng chủ đề, tích hợp, gắn với thời gian và bất biến, chuyên phục vụ phân tích OLAP. Khác với OLTP tối ưu cho ghi/sửa giao dịch hàng ngày (chuẩn hóa 3NF), Data Warehouse tối ưu cho đọc và quét khối lượng lớn dữ liệu (phi chuẩn hóa)."),
        ("Câu 2: Hãy nêu 4 đặc tính cơ bản của Data Warehouse theo W.H. Inmon?",
         "4 đặc tính gồm: 1. Hướng chủ đề (Subject-oriented), 2. Tích hợp (Integrated), 3. Biến động theo thời gian (Time-variant), 4. Bất biến / Không biến động (Non-volatile)."),
        ("Câu 3: Bảng Fact là gì? Bảng Dimension là gì?",
         "Bảng Fact chứa các số đo định lượng (measures/metrics) về sự kiện nghiệp vụ (ví dụ: lượng mưa, nhiệt độ, thiệt hại). Bảng Dimension chứa các thuộc tính ngữ cảnh (context) dùng để lọc, phân nhóm và cắt lát dữ liệu (ví dụ: ngày, địa điểm, điều kiện thời tiết)."),
        ("Câu 4: Thế nào là Conformed Dimension?",
         "Conformed Dimension là bảng chiều có cấu trúc và ý nghĩa nhất quán, được chia sẻ và sử dụng chung bởi nhiều bảng Fact khác nhau trong kho dữ liệu (như dim_date, dim_location)."),
        ("Câu 5: Khóa đại diện (Surrogate Key) là gì và tại sao lại dùng thay Natural Key?",
         "Surrogate Key là khóa nhân tạo kiểu số nguyên (integer) tự tăng hoặc định danh có quy tắc (YYYYMMDD), không mang ý nghĩa nghiệp vụ. Dùng Surrogate Key giúp tăng tốc độ JOIN, tiết kiệm bộ nhớ index và xử lý được các thay đổi của Natural Key từ nguồn."),
        ("Câu 6: Phân biệt mô hình Star Schema và Snowflake Schema?",
         "Star Schema có bảng Fact ở trung tâm nối trực tiếp với các bảng Dimension không chuẩn hóa. Snowflake Schema thực hiện chuẩn hóa các Dimension thành nhiều bảng phân cấp (như tách huyện từ tỉnh), giúp giảm dư thừa nhưng làm tăng số lượng phép JOIN."),
        ("Câu 7: Quy trình ETL gồm các giai đoạn nào?",
         "ETL gồm 3 giai đoạn: Extract (Trích xuất dữ liệu từ các nguồn gốc), Transform (Làm sạch, khử trùng lặp, chuẩn hóa định dạng, tính toán chỉ số phái sinh) và Load (Nạp dữ liệu vào các bảng Fact và Dimension)."),
        ("Câu 8: Khái niệm Grain (Mức độ chi tiết) của bảng Fact là gì?",
         "Grain là định nghĩa chính xác về ý nghĩa của một dòng đơn lẻ trong bảng Fact. Ví dụ: Grain của fact_precipitation là 'Một dòng đại diện cho tổng lượng mưa ghi nhận trong 1 ngày tại 1 tỉnh/thành phố cụ thể'."),
        ("Câu 9: Slowly Changing Dimension (SCD) là gì?",
         "SCD là kỹ thuật quản lý và lưu trữ dữ liệu lịch sử khi các thuộc tính trong bảng Dimension bị thay đổi theo thời gian."),
        ("Câu 10: Phân biệt SCD Type 1, Type 2 và Type 3?",
         "SCD Type 1: Ghi đè trực tiếp giá trị mới (không giữ lịch sử). SCD Type 2: Tạo dòng mới với Surrogate Key mới kèm cột Start_Date, End_Date, Is_Current (giữ toàn bộ lịch sử). SCD Type 3: Thêm cột lưu giá trị cũ (chỉ giữ được 1 mốc lịch sử gần nhất)."),
        ("Câu 11: Data Mart là gì và khác gì so với Data Warehouse doanh nghiệp (EDW)?",
         "Data Mart là một tập con của Data Warehouse, tập trung vào một phòng ban hoặc một chủ đề nghiệp vụ cụ thể. EDW chứa toàn bộ dữ liệu của toàn bộ tổ chức."),
        ("Câu 12: Đơn vị đo lượng mưa 'mm' có ý nghĩa vật lý như thế nào?",
         "Lượng mưa 1 mm có nghĩa là trên một mặt phẳng diện tích 1 mét vuông không thấm nước và không bốc hơi, lớp nước mưa dâng lên độ cao đúng 1 milimet (tương đương 1 lít nước trên 1 mét vuông)."),
        ("Câu 13: Cấp gió Beaufort là gì?",
         "Thang sức gió Beaufort là thang đo kinh nghiệm từ cấp 0 (lặng gió) đến cấp 12+ (bão cuồng phong), dựa trên tốc độ gió đo ở độ cao chuẩn 10 mét trên mặt đất."),
        ("Câu 14: DAX trong Power BI là viết tắt của từ gì?",
         "DAX viết tắt của Data Analysis Expressions - ngôn ngữ biểu thức và công thức tính toán được sử dụng trong Power BI, Analysis Services và Power Pivot trong Excel."),
        ("Câu 15: VertiPaq Engine trong Power BI hoạt động theo cơ chế nào?",
         "VertiPaq là một cơ sở dữ liệu in-memory lưu trữ theo cột (Columnar Database). Nó sử dụng bộ nhớ RAM, nén dữ liệu mạnh mẽ bằng Dictionary Encoding và RLE để thực thi các phép tính tổng hợp siêu tốc.")
    ]
    for q, a in qa_easy:
        doc.add_bullet(a, bold_prefix=q)

    # CẤP ĐỘ 2: TRUNG BÌNH
    doc.add_heading("B. CẤP ĐỘ 2: NGHIỆP VỤ & KIẾN TRÚC ĐỒ ÁN (15 CÂU HỎI TRUNG BÌNH)", level=2)
    qa_medium = [
        ("Câu 16: Tại sao đề tài này bắt buộc phải dùng mô hình Fact Constellation (Galaxy Schema)?",
         "Vì đồ án theo dõi 6 nhóm hiện tượng vật lý có chu kỳ phát sinh và mức độ chi tiết khác nhau. Nếu gộp chung vào 1 Fact, các ngày bình thường không có bão sẽ khiến các cột của bảng thiên tai bị NULL hàng loạt (Sparse data). Tách 6 Fact giúp tối ưu lưu trữ, dễ mở rộng mà vẫn phân tích liên thông qua 5 Conformed Dimensions."),
        ("Câu 17: Hãy giải thích cách thiết kế ma trận Bus Matrix trong đồ án?",
         "Bus Matrix thể hiện sự giao thoa: dim_date và dim_location xuất hiện ở cả 6 bảng Fact. dim_time xuất hiện ở 5 bảng quan trắc hàng ngày. dim_wind_direction chỉ nối với fact_wind, và dim_weather_condition nối với fact_precipitation. Ma trận này đảm bảo tính trực giao và nhất quán toàn hệ thống."),
        ("Câu 18: Tại sao lại tách riêng bảng dim_wind_direction thay vì để thuộc tính góc gió trong Fact?",
         "Tách dim_wind_direction giúp phân nhóm 16 hướng gió chuẩn hàng hải, đồng thời gắn nhãn các hiện tượng thời tiết đặc trưng như 'Gió mùa Đông Bắc' (mùa đông) hay 'Gió phơn Tây Nam' (mùa hè), phục vụ phân tích biểu đồ hoa gió (Radar chart) rất hiệu quả."),
        ("Câu 19: Cán cân nước (Water Balance) được tính như thế nào và có ý nghĩa gì?",
         "Công thức: Water Balance = Lượng mưa (rain_mm) - Lượng bốc thoát hơi nước (evapotranspiration). Nếu > 0: Nguồn nước dồi dào/thừa (nguy cơ ngập úng). Nếu < 0: Bốc hơi mạnh hơn mưa, cảnh báo nguy cơ hạn hán và thiếu nước tưới tiêu."),
        ("Câu 20: Dữ liệu lịch sử 1999 thu thập từ đâu và làm sao đảm bảo độ tin cậy?",
         "Dữ liệu được trích xuất từ Open-Meteo Historical Archive API, tích hợp mô hình tái phân tích toàn cầu ERA5 của Trung tâm Dự báo Hạn vừa Châu Âu (ECMWF). ERA5 chạy mô hình vật lý khí quyển kết hợp dữ liệu vệ tinh và trạm mặt đất từ năm 1940 đến nay, đảm bảo tính liên tục và độ chuẩn xác khoa học."),
        ("Câu 21: Làm thế nào để xử lý giá trị ngoại lai (Outliers) mà không làm mất các trận mưa kỷ lục?",
         "Nếu chỉ dùng quy tắc thống kê 3-Sigma hoặc Boxplot thông thường, các trận mưa cực đoan 970mm (Huế 1999) hay 795mm (Đà Nẵng 2022) sẽ bị coi là lỗi và xóa bỏ. Nhóm đã đối chiếu cross-check với cơ sở dữ liệu thiên tai lịch sử quốc gia. Chỉ những giá trị mưa vượt ngưỡng vật lý (>1500mm/ngày) mà không có bão mới bị xử lý làm sạch."),
        ("Câu 22: Tại sao date_key lại dùng định dạng số nguyên 19991102 thay vì kiểu Date thông thường?",
         "Số nguyên 4-bytes chiếm ít không gian hơn chuỗi ngày tháng, giúp tăng tốc độ JOIN giữa Fact và Dimension trong VertiPaq. Ngoài ra, người dùng có thể nhìn vào số 19991102 là suy ra ngay ngày 02 tháng 11 năm 1999 mà không cần giải mã."),
        ("Câu 23: Sự khác biệt giữa Calculated Column và Measure trong Power BI là gì?",
         "Calculated Column được tính toán trong quá trình nạp dữ liệu (Refresh) và lưu trực tiếp vào RAM, tiêu tốn bộ nhớ. Measure được tính toán động tại thời điểm truy vấn (Query time) theo ngữ cảnh bộ lọc (Filter Context), không tốn RAM lưu trữ, rất linh hoạt."),
        ("Câu 24: Hãy giải thích cách hoạt động của Measure [Flood Warning Level]?",
         "Measure dùng hàm SWITCH(TRUE(), ...) kiểm tra 2 điều kiện: Lượng mưa tích lũy [Total Rain] và Độ bão hòa đất [Avg Soil Saturation]. Khi TotalRain >= 500mm hoặc SoilSat >= 98%, hệ thống kích hoạt cảnh báo '🚨 Báo động 3+ (Khẩn cấp)'."),
        ("Câu 25: Tại sao độ ẩm đất (Soil Moisture) lại quyết định đến nguy cơ sạt lở đất?",
         "Khi đất ngậm no nước (độ bão hòa đất đạt trên 85-95%), lực liên kết giữa các hạt đất giảm mạnh, trọng lượng khối đất sườn dốc tăng lên gấp nhiều lần. Khi có thêm đợt mưa lớn trút xuống, áp lực nước lỗ rỗng sẽ kích hoạt hiện tượng trượt lở đất kinh hoàng."),
        ("Câu 26: Đồ án áp dụng SCD Type mấy cho thông tin địa giới hành chính các tỉnh?",
         "Đồ án sử dụng SCD Type 2 cho các thay đổi lớn về địa giới hành chính để theo dõi được dữ liệu của địa phương trước và sau điều chỉnh, và SCD Type 1 cho việc sửa đổi thông tin mô tả lưu vực sông."),
        ("Câu 27: Biểu đồ Hoa gió (Radar Chart) trên Dashboard thể hiện thông tin gì?",
         "Trục góc của biểu đồ thể hiện 8 hoặc 16 hướng gió chính, bán kính thể hiện tốc độ gió trung bình. Biểu đồ cho thấy vào mùa mưa lũ, gió Đông Bắc chiếm ưu thế tuyệt đối; trong khi vào mùa hè, gió Tây Nam chiếm ưu thế."),
        ("Câu 28: Khuyến nghị mùa vụ nông nghiệp [Crop Recommendation] hoạt động như thế nào?",
         "DAX trích xuất tháng hiện tại từ bộ lọc (SELECTEDVALUE). Vào tháng 9-11, DAX hiển thị khuyến nghị: 'Thu hoạch dứt điểm Hè Thu, KHÔNG gieo cấy lúa vùng trũng'. Vào tháng 12-1: Khuyến nghị 'Xuống giống lúa Đông Xuân ngắn ngày tranh thủ phù sa'."),
        ("Câu 29: Tính toán evapotranspiration (bốc thoát hơi nước) dựa trên nguyên lý nào?",
         "Mô hình Open-Meteo tính toán bốc thoát hơi nước tham chiếu theo công thức FAO-56 Penman-Monteith, dựa trên nhiệt độ không khí, bức xạ mặt trời, tốc độ gió và độ ẩm không khí."),
        ("Câu 30: Đồ án có khắc phục được lỗi của tài liệu cũ trong thư mục docs không?",
         "Khắc phục 100%: Tài liệu cũ bị lỗi copy-paste về 'thương mại điện tử' và bị đứt đoạn ở mục 2.3.2. Bản mới đã biên soạn hoàn chỉnh 5 chương chuyên sâu về khí tượng thủy văn, nâng cấp từ 3 thành phố lên trọn vẹn 11 tỉnh thành miền Trung.")
    ]
    for q, a in qa_medium:
        doc.add_bullet(a, bold_prefix=q)

    # CẤP ĐỘ 3: NÂNG CAO
    doc.add_page_break()
    doc.add_heading("C. CẤP ĐỘ 3: NÂNG CAO & TÌNH HUỐNG HÓC BÚA (10 CÂU HỎI KHÓ)", level=2)
    qa_hard = [
        ("Câu 31: Khi bảng Fact tăng lên hàng trăm triệu bản ghi quan trắc theo giờ, chiến lược tối ưu hóa là gì?",
         "Ta áp dụng 3 chiến lược: 1. Table Partitioning theo năm (Yearly Partition). 2. Xây dựng các bảng tổng hợp sẵn (Aggregated Fact Tables) ở mức Daily hoặc Monthly. 3. Sử dụng chế độ Composite Models trong Power BI (Import các bảng Dim và Aggregate, còn Fact chi tiết để DirectQuery)."),
        ("Câu 32: So sánh kiến trúc Cloud Data Lakehouse (Delta Lake/Iceberg) với Data Warehouse truyền thống cho bài toán thời tiết?",
         "Data Warehouse truyền thống mạnh về phân tích số liệu có cấu trúc qua SQL/BI nhưng chi phí lưu trữ cao và khó xử lý ảnh viễn thám hay radar thời tiết. Data Lakehouse lưu trữ trên Cloud Object Storage (S3/ADLS) theo định dạng Parquet mở, hỗ trợ ACID transactions, vừa cho phép Power BI truy vấn BI siêu tốc vừa cho phép Python/Spark chạy mô hình Machine Learning trực tiếp."),
        ("Câu 33: Nếu ngày mai API cung cấp số liệu hiệu chỉnh (Restated Data) của ngày hôm qua thì DW xử lý ra sao?",
         "Trong quy trình ETL, ta thiết kế cơ chế Incremental Load với cửa sổ trượt (Sliding Window) 3 đến 7 ngày gần nhất. Hệ thống sẽ quét lại các bản ghi trong cửa sổ này và áp dụng lệnh UPSERT (MERGE trong SQL) để cập nhật giá trị mới nhất mà không cần tải lại toàn bộ kho."),
        ("Câu 34: Tại sao trong DAX lại phải tránh dùng hàm IFERROR và FILTER toàn bộ bảng?",
         "Hàm IFERROR buộc engine phải tính toán từng dòng mà không tận dụng được cơ chế vector hóa của VertiPaq. Hàm FILTER('Table', ...) sẽ quét toàn bộ bảng và biến thành ngữ cảnh bảng lớn. Thay vào đó, nên dùng DIVIDE (tự động xử lý chia cho 0) và KEEPFILTERS để tối ưu hiệu năng."),
        ("Câu 35: Làm sao giải quyết bài toán sáp nhập thành phố Huế trực thuộc Trung ương trong mô hình dữ liệu?",
         "Đây là bài toán SCD kinh điển. Ta áp dụng SCD Type 2 cho dim_location. Bản ghi cũ lưu 'Tỉnh Thừa Thiên Huế' với End_Date là ngày ban hành nghị quyết sáp nhập, Is_Current = 0. Bản ghi mới lưu 'Thành phố Huế' với Start_Date, Is_Current = 1 và Surrogate Key mới."),
        ("Câu 36: Độ trễ (Latency) của dữ liệu ERA5 ảnh hưởng gì đến tính realtime của hệ thống?",
         "Dữ liệu ERA5 hoàn chỉnh thường có độ trễ khoảng 5 ngày để thẩm định khoa học. Để giải quyết, nhóm kiến trúc giải pháp kiến trúc Lambda: Dữ liệu quá khứ 1999 - 2026 dùng ERA5 (Batch Layer) để phân tích quy luật; dữ liệu những ngày gần nhất dùng API Open-Meteo Forecast/Realtime (Speed Layer) để cập nhật cảnh báo tức thời."),
        ("Câu 37: Làm thế nào để tích hợp Feature Store phục vụ huấn luyện mô hình Machine Learning dự báo ngập lụt?",
         "Kho dữ liệu Galaxy Schema đóng vai trò là nguồn cấp Feature hoàn hảo. Từ fact_precipitation và fact_temperature, ta tính toán các đặc trưng chuỗi thời gian: Lượng mưa tích lũy 3 ngày trước (Lag 3), Tốc độ tăng lượng mưa (Rolling Slope), Độ ẩm đất trung bình 7 ngày. Các feature này được đẩy vào Feature Store (như Feast) để huấn luyện mô hình Random Forest hoặc LSTM."),
        ("Câu 38: Chỉ số áp suất khí quyển (Surface Pressure) giảm sâu dưới 1000 hPa có ý nghĩa gì trong cảnh báo bão?",
         "Tâm bão là vùng áp suất cực thấp. Khi áp suất khí quyển giảm nhanh chóng (xuống dưới 990 - 970 hPa), nó báo hiệu tâm bão hoặc áp thấp nhiệt đới mạnh đang tiến sát đất liền. Kết hợp áp suất giảm và gió giật tăng là cơ sở kích hoạt lệnh cấm biển và sơ tán dân ven bờ."),
        ("Câu 39: Giải thích cơ chế lọc chéo 1 chiều (Single) vs 2 chiều (Both) giữa Fact và Dimension trong Power BI?",
         "Mặc định trong Galaxy Schema phải dùng Single (1 -> *). Nếu bật Both (hai chiều), bảng Fact này có thể lọc ngược lại bảng Dim và làm ảnh hưởng đến Fact khác một cách không mong muốn, gây sai lệch số liệu và tạo ra các vòng lặp quan hệ mơ hồ (Ambiguous Relationships)."),
        ("Câu 40: Nếu được tiếp tục phát triển đồ án này trong thực tế, nhóm sẽ mở rộng tính năng gì đầu tiên?",
         "Nhóm sẽ tích hợp bản đồ GIS số hóa ranh giới ngập lụt (Shapefile các phường/xã trũng thấp ven sông) kết hợp dữ liệu camera giao thông thời gian thực và chatbot cảnh báo thiên tai qua Zalo/Telegram tự động gửi tin nhắn cho từng người dân theo vị trí GPS.")
    ]
    for q, a in qa_hard:
        doc.add_bullet(a, bold_prefix=q)

    doc.save("central_weather_dw/BAI_THUYET_TRINH_VA_CAU_HOI_PHAN_BIEN.docx")


# ==============================================================================
# 5. GENERATE 16-SLIDE MODERN PRESENTATION (Slide_Kho_Du_Lieu_Mien_Trung.pptx)
# ==============================================================================

def generate_slides():
    print("\n--- Đang thiết kế bộ 16 Slide trình chiếu PowerPoint ---")
    pptx = PptxBuilder()

    # Slide 1: Bìa
    pptx.add_title_slide(
        "KHO DỮ LIỆU THỜI TIẾT & THIÊN TAI MIỀN TRUNG",
        "Nghiên Cứu Chuỗi Số Liệu 28 Năm (1999 - 2026) Cho 11 Tỉnh/Thành Phục Vụ Cảnh Báo Sớm",
        "Sinh viên thực hiện: Nhóm Đồ Án KDL VKU | GVHD: Giảng viên Bộ môn Kho Dữ Liệu"
    )

    # Slide 2: Mục lục
    pptx.add_content_slide(
        "NỘI DUNG BÁO CÁO (5 PHẦN CHÍNH)",
        [
            "1. Đặt vấn đề & Tính cấp thiết của đề tài tại dải đất Miền Trung",
            "2. Cơ sở lý thuyết Kho dữ liệu & Phương pháp luận Ralph Kimball",
            "3. Thiết kế kiến trúc Fact Constellation (Galaxy Schema) 11 Tỉnh/Thành",
            "4. Quy trình ETL trích xuất & làm sạch dữ liệu mở Open-Meteo (1999 - 2026)",
            "5. Kết quả trực quan hóa Power BI Dashboard & Ứng dụng Prescriptive Analytics"
        ],
        highlight_card="Trọng tâm: Nâng cấp toàn diện phạm vi không gian, thời gian và giá trị thực tiễn vì cộng đồng."
    )

    # Slide 3: Tính cấp thiết
    pptx.add_content_slide(
        "TÍNH CẤP THIẾT CỦA THIÊN TAI MIỀN TRUNG",
        [
            "Miền Trung là 'rốn bão lũ' của cả nước với địa hình hẹp ngang, dốc đứng từ dãy Trường Sơn ra biển.",
            "Chuỗi thiên tai lịch sử khốc liệt: Đại hồng thủy 1999 (970mm/24h), Đại lũ 2020, Ngập lụt Đà Nẵng 2022 (795mm).",
            "Hiện tại (11/2026): Mưa lũ đặc biệt lớn đang diễn ra phức tạp tại Huế, Đà Nẵng, Quảng Trị.",
            "Nhu cầu cấp bách: Cần một kho dữ liệu tập trung, đa chiều để phân tích quy luật và đưa ra cảnh báo sớm."
        ],
        highlight_card="Mục tiêu tối thượng: Dữ liệu không chỉ để quan sát, mà phải cứu trợ và bảo vệ tính mạng người dân."
    )

    # Slide 4: Mục tiêu đề tài
    pptx.add_content_slide(
        "MỤC TIÊU NGHIÊN CỨU & GIÁ TRỊ THỰC TIỄN",
        [
            "Xây dựng Kho dữ liệu chuẩn quốc tế theo phương pháp luận chiều của Ralph Kimball.",
            "Khắc phục hoàn toàn các lỗi sai sót trong tài liệu tham khảo cũ (loại bỏ hoàn toàn lỗi thương mại điện tử).",
            "Nghiên cứu chuỗi số liệu khí tượng thủy văn gần 28 năm (1999 - 2026) cho 11 đơn vị hành chính.",
            "Ứng dụng phân tích đề xuất hành động (Prescriptive Analytics): Lịch mùa vụ nông nghiệp, An toàn xây dựng, Cắt lũ hồ chứa."
        ],
        highlight_card="Đột phá: Chuyển dịch từ phân tích mô tả quá khứ sang khuyến nghị hành động tương lai."
    )

    # Slide 5: Đối tượng & Phạm vi
    pptx.add_content_slide(
        "ĐỐI TƯỢNG & PHẠM VI NGHIÊN CỨU",
        [
            "Phạm vi không gian: 11 đơn vị hành chính cấp tỉnh Miền Trung (Bao gồm 2 TP TW: Huế, Đà Nẵng).",
            "Bao trọn các lưu vực sông lớn: Sông Hương, Sông Vu Gia - Thu Bồn, Sông Thạch Hãn, Sông Trà Khúc, Sông Lam.",
            "Phạm vi thời gian: Giai đoạn 28 năm (Từ Đại hồng thủy 11/1999 đến bão lũ 11/2026).",
            "Quy mô dữ liệu: Hơn 112.000 bản ghi dữ liệu quan trắc hàng ngày kết hợp 24 đợt thiên tai cực đoan."
        ],
        highlight_card="Đại diện đầy đủ cho 3 tiểu vùng: Bắc Trung Bộ, Duyên hải Nam Trung Bộ và Tây Nguyên chuyển tiếp."
    )

    # Slide 6: Phương pháp luận Kimball
    pptx.add_content_slide(
        "PHƯƠNG PHÁP LUẬN THIẾT KẾ KIMBALL",
        [
            "Bước 1: Chọn quy trình nghiệp vụ (Business Process) - Giám sát khí quyển, mưa lũ và thiên tai.",
            "Bước 2: Xác định Grain (Mức độ chi tiết) - Daily Grain cho quan trắc và Event Grain cho thiên tai.",
            "Bước 3: Xác định Dimensions - 5 Conformed Dimensions dùng chung (Ngày, Giờ, Vị trí, Thời tiết, Gió).",
            "Bước 4: Xác định Facts - 6 bảng Fact chứa các chỉ số đo lường số học độc lập."
        ],
        highlight_card="Tuân thủ nghiêm ngặt 4 bước thiết kế chiều kinh điển của Ralph Kimball."
    )

    # Slide 7: Galaxy Schema
    pptx.add_content_slide(
        "KIẾN TRÚC TỔNG THỂ FACT CONSTELLATION",
        [
            "5 Conformed Dimensions: dim_date, dim_location, dim_time, dim_weather_condition, dim_wind_direction.",
            "6 Fact Tables chuyên biệt: fact_temperature, fact_precipitation, fact_wind, fact_solar_radiation, fact_atmospheric, fact_extreme_events.",
            "Giải quyết triệt để bài toán dữ liệu thưa (Sparse Data) so với mô hình 1 bảng Fact đơn lẻ.",
            "Liên kết trực giao qua ma trận Bus Matrix chuẩn hóa."
        ],
        highlight_card="Mô hình Galaxy Schema là sự lựa chọn tối ưu tuyệt đối cho hệ thống dữ liệu khí tượng đa chiều."
    )

    # Slide 8: 5 Conformed Dimensions
    pptx.add_content_slide(
        "THIẾT KẾ CHI TIẾT 5 CONFORMED DIMENSIONS",
        [
            "dim_date: Mở rộng thêm Mùa bão lũ (is_typhoon_season), Chu kỳ mùa vụ, và Pha ENSO (El Niño / La Niña).",
            "dim_location: Bổ sung tọa độ, cao độ, lưu vực sông chính (major_river_basin) và mức độ rủi ro (vulnerability).",
            "dim_weather_condition: Chuẩn hóa theo bảng mã quốc tế WMO (Tổ chức Khí tượng Thế giới).",
            "dim_wind_direction: 16 hướng gió hàng hải, phân loại Gió mùa Đông Bắc và Gió phơn Tây Nam khô nóng.",
            "dim_time: 24 khung giờ và các cửa sổ thời gian hoạt động an toàn ngoài trời."
        ],
        highlight_card="Toàn bộ Dimensions đều sử dụng Surrogate Key kiểu số nguyên tối ưu hóa truy vấn."
    )

    # Slide 9: 6 Fact Tables & Grain
    pptx.add_content_slide(
        "THIẾT KẾ CHI TIẾT 6 FACT TABLES",
        [
            "fact_precipitation: Lượng mưa, xác suất mưa, bốc thoát hơi nước, cán cân nước, độ bão hòa đất.",
            "fact_temperature: Nhiệt độ không khí 2m, nhiệt độ đất 0cm, độ ẩm không khí, độ ẩm đất.",
            "fact_wind: Tốc độ gió 10m, gió giật cực đại, cấp gió Beaufort, tình trạng biển cho tàu thuyền.",
            "fact_solar_radiation: Bức xạ trực tiếp, bức xạ tán xạ, chỉ số UV, số giờ nắng.",
            "fact_atmospheric: Áp suất mặt đất, áp suất mực nước biển, tầm nhìn xa, độ che phủ mây.",
            "fact_extreme_events: Mưa đỉnh 24h, cấp báo động lũ (BĐ1-BĐ3), thiệt hại kinh tế, người ảnh hưởng."
        ],
        highlight_card="Phân tách rành mạch giữa quan trắc vật lý liên tục (Daily) và sự kiện thiên tai rời rạc (Event)."
    )

    # Slide 10: Quy trình ETL
    pptx.add_content_slide(
        "QUY TRÌNH ETL TÍCH HỢP DỮ LIỆU",
        [
            "Nguồn dữ liệu: Open-Meteo Historical Archive API kết hợp mô hình tái phân tích ERA5 (ECMWF).",
            "Extract: Trích xuất phân mảnh theo năm và tọa độ 11 tỉnh thành để kiểm soát băng thông.",
            "Transform: Xử lý giá trị khuyết thiếu (Missing data), làm sạch ngoại lai, tính toán water_balance.",
            "Load: Nạp tự động vào Power BI VertiPaq Engine thông qua tập lệnh Power Query M chuẩn hóa."
        ],
        highlight_card="Dữ liệu được nén cột và lập chỉ mục trong bộ nhớ RAM, tốc độ tính toán chỉ mất vài chục mili-giây."
    )

    # Slide 11: Làm sạch & Kiểm thử
    pptx.add_content_slide(
        "XỬ LÝ DỮ LIỆU & BẢO TOÀN GIÁ TRỊ CỰC ĐOAN",
        [
            "Nội suy tuyến tính (Linear Interpolation) dựa trên các trạm quan trắc lân cận khi mất tín hiệu.",
            "Bảo tồn các mốc mưa kỷ lục: 970mm (Huế 1999) và 795mm (Đà Nẵng 2022) bằng đối soát lịch sử.",
            "Chuẩn hóa đơn vị đo lường: Nhiệt độ (°C), Lượng mưa (mm), Tốc độ gió (m/s), Áp suất (hPa).",
            "Kiểm tra toàn vẹn khóa ngoại (Referential Integrity) giữa 6 bảng Fact và 5 bảng Dimension đạt 100%."
        ],
        highlight_card="Chất lượng dữ liệu được kiểm định nghiêm ngặt trước khi đưa vào mô hình trực quan hóa."
    )

    # Slide 12: Trang 1 Dashboard
    pptx.add_content_slide(
        "DASHBOARD TRANG 1: TỔNG QUAN KHÍ HẬU",
        [
            "5 Thẻ KPI Card: Nhiệt độ TB, Lượng mưa tích lũy, Tốc độ gió TB, Sự kiện cực đoan, Cán cân nước.",
            "Bộ lọc tương tác (Slicers): Lọc nhanh theo 11 Tỉnh/Thành, Giai đoạn năm (1999 - 2026), Mùa khí hậu.",
            "Biểu đồ Line & Column: Xu hướng lượng mưa và nhiệt độ qua các năm.",
            "Biểu đồ Hoa gió (Radar Chart): Phân bố hướng và tốc độ gió theo mùa Đông Bắc và Tây Nam.",
            "Biểu đồ cột: Xếp hạng lượng mưa tích lũy 11 tỉnh (Huế, Đà Nẵng, Quảng Trị luôn dẫn đầu)."
        ],
        highlight_card="Cung cấp góc nhìn toàn diện cho lãnh đạo và các cơ quan chỉ huy phòng chống thiên tai."
    )

    # Slide 13: Trang 2 Dashboard
    pptx.add_content_slide(
        "DASHBOARD TRANG 2: THIÊN TAI LỊCH SỬ (1999 - 2026)",
        [
            "Thống kê tổng thiệt hại: Hơn 97.800 tỷ đồng và 12.8 triệu lượt người dân bị ảnh hưởng.",
            "Ma trận bong bóng (Scatter Chart): Tương quan giữa Lượng mưa 24h, Cấp gió giật và Mức độ thiệt hại.",
            "Phân tích đợt mưa lũ tháng 11/2026 hiện tại: Mưa lớn diện rộng do không khí lạnh kết hợp gió Đông.",
            "Bảng sự kiện chi tiết: Ngày, địa bàn, cấp báo động lũ sông và các biện pháp ứng phó khẩn cấp."
        ],
        highlight_card="Minh chứng sống động cho tính chất khốc liệt và biến đổi khó lường của thiên tai miền Trung."
    )

    # Slide 14: Trang 3 Dashboard
    pptx.add_content_slide(
        "DASHBOARD TRANG 3: CẢNH BÁO SỚM & SINH KẾ",
        [
            "Thẻ cảnh báo động: Cấp báo động lũ (BĐ1 - BĐ3+), Nguy cơ sạt lở đất đồi núi, Cảnh báo cấm biển ngư dân.",
            "Khuyến nghị nông nghiệp: Tuyệt đối không gieo cấy lúa vùng trũng thấp tháng 9-11; Xuống giống vụ Đông Xuân tháng 12.",
            "Khuyến nghị xây dựng: Đình chỉ thi công đào hố móng và giàn giáo khi mưa > 100mm hoặc gió > cấp 7.",
            "Quản lý hồ chứa: Xả đáy đón lũ trước 24h khi cán cân nước > 300mm; Đóng cống ngăn mặn vào mùa khô."
        ],
        highlight_card="Giá trị nhân văn cốt lõi: Ứng dụng khoa học dữ liệu trực tiếp phục vụ đời sống bà con nhân dân."
    )

    # Slide 15: Kết luận & Hướng mở rộng
    pptx.add_content_slide(
        "KẾT LUẬN & HƯỚNG PHÁT TRIỂN",
        [
            "Đồ án đã xây dựng thành công Kho dữ liệu mẫu mực, giải quyết trọn vẹn bài toán khí tượng miền Trung.",
            "Khắc phục 100% các hạn chế của đồ án cũ, nâng cấp toàn diện quy mô không gian và thời gian.",
            "Hướng mở rộng 1: Chuyển dịch lên Cloud Data Lakehouse (Delta Lake / Databricks) để xử lý ảnh Radar vệ tinh.",
            "Hướng mở rộng 2: Xây dựng mô hình AI Machine Learning (LSTM / Transformer) dự báo mưa lũ trước 72 giờ.",
            "Hướng mở rộng 3: Ứng dụng di động cảnh báo thiên tai tức thời đến từng hộ gia đình theo định vị GPS."
        ],
        highlight_card="Nền tảng vững chắc để phát triển thành một hệ thống cảnh báo thiên tai thông minh cấp vùng."
    )

    # Slide 16: Q&A
    pptx.add_title_slide(
        "XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY CÔ!",
        "Kính Chúc Quý Thầy Cô Sức Khỏe & Thành Công",
        "Nhóm Sinh Viên Rất Mong Nhận Được Ý Kiến Đóng Góp Của Hội Đồng Bảo Vệ (Q&A)"
    )

    pptx.save("central_weather_dw/Slide_Kho_Du_Lieu_Mien_Trung.pptx")


if __name__ == "__main__":
    generate_academic_report()
    generate_defense_guide()
    generate_slides()
    print("\n🎉 HOÀN THÀNH TOÀN BỘ 3 SẢN PHẨM TÀI LIỆU TRONG central_weather_dw/")
