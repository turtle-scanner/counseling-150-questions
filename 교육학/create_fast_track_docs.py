import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# 한글 폰트 등록
font_path = "C:/Windows/Fonts/malgun.ttf"
font_bold_path = "C:/Windows/Fonts/malgunbd.ttf"
pdfmetrics.registerFont(TTFont("Malgun", font_path))
pdfmetrics.registerFont(TTFont("MalgunBold", font_bold_path))

desktop_dir = r"C:\Users\LENOVO\Desktop"
pdf_path = os.path.join(desktop_dir, "우선심사신청설명서_초고속_변귀섭.pdf")
docx_path = os.path.join(desktop_dir, "우선심사신청설명서_초고속_변귀섭.docx")

# 1. PDF 생성
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=45,
    rightMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Normal"],
    fontName="MalgunBold",
    fontSize=18,
    leading=24,
    alignment=1,
    textColor=colors.HexColor("#1A237E")
)
sub_style = ParagraphStyle(
    "SubStyle",
    parent=styles["Normal"],
    fontName="MalgunBold",
    fontSize=13,
    leading=18,
    textColor=colors.HexColor("#0D47A1")
)
body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["Normal"],
    fontName="Malgun",
    fontSize=10,
    leading=16,
    textColor=colors.HexColor("#212121")
)
bold_body = ParagraphStyle(
    "BoldBody",
    parent=styles["Normal"],
    fontName="MalgunBold",
    fontSize=10,
    leading=16,
    textColor=colors.HexColor("#212121")
)

story = []
story.append(Spacer(1, 10))
story.append(Paragraph("우 선 심 사 신 청 설 명 서 (초고속)", title_style))
story.append(Spacer(1, 15))

# 기본 서지사항 표
table_data = [
    [Paragraph("<b>출 원 번 호</b>", bold_body), Paragraph("10-2026-0205329 (출원일자: 2026.10.22)", body_style)],
    [Paragraph("<b>발 명 의 명 칭</b>", bold_body), Paragraph("개인 맞춤형 동적 베이스라인 생체 및 음성 분석, 이개강 전도성 실리콘 전극 기반 뇌신경 자극 및 능동적 탈숙고 유한상태기계 폐루프 제어를 구비한 디지털 치료 시스템 및 이의 제어 방법", body_style)],
    [Paragraph("<b>출   원   인</b>", bold_body), Paragraph("변귀섭 (특허고객번호: 4-2020-055266-0)", body_style)],
    [Paragraph("<b>첨단특허분류</b>", bold_body), Paragraph("<b>A61B 5/4836</b> (특허청 공식 부여 국가 첨단기술 분류)", bold_body)],
    [Paragraph("<b>신 청 구 분</b>", bold_body), Paragraph("국가 첨단기술 특허분류 부여에 따른 <b>초고속 우선심사</b>", bold_body)]
]
t = Table(table_data, colWidths=[110, 395])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F5F7FA")),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#B0BEC5")),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 15))

# 1. 신청 취지
story.append(Paragraph("1. 신청의 취지", sub_style))
story.append(Spacer(1, 5))
story.append(Paragraph("본 특허출원(제10-2026-0205329호)은 대한민국 특허청(지식재산처)으로부터 공식 <b>첨단기술 특허분류(A61B 5/4836)</b>를 부여받은 출원으로서, 「특허법」 제61조 및 「특허·실용신안 우선심사의 신청에 관한 고시」에 따라 조속한 권리 확정 및 산업적 조기 실용화를 위하여 <b>초고속 우선심사를 신청</b>합니다.", body_style))
story.append(Spacer(1, 12))

# 2. 신청 이유 (첨단기술 분류 부여)
story.append(Paragraph("2. 우선심사 신청 이유 (국가 첨단기술 분류 근거)", sub_style))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>가. 특허청 첨단기술 특허분류(A61B 5/4836) 공식 부여</b><br/>"
                       "본 출원인은 2026년 11월 4일 특허청으로부터 「첨단기술 특허분류로 초고속심사 및 우선심사신청이 가능한 특허분류 A61B 5/4836가 부여되었습니다」라는 공식 심사안내 통지를 수신하였습니다. 이에 따라 관련 법령상 초고속 우선심사 대상 요건을 완벽하게 충족하고 있습니다.", body_style))
story.append(Spacer(1, 8))

# 3. 기술적 특징 및 첨단성
story.append(Paragraph("3. 발명의 구체적 기술 특징 및 첨단성", sub_style))
story.append(Spacer(1, 5))
p_tech = (
    "<b>가. 다중 생체 신호 및 음성 바이오마커 기반 실시간 위기 감지</b><br/>"
    "본 발명은 사용자의 광용적맥파(PPG), 심박변이도(HRV), 피부전기활동(EDA) 및 음성 주파수 지표를 융합하여 개인 맞춤형 동적 베이스라인을 구축하고, 급성 심리적 공황 및 위기 징후를 극초기에 감지합니다.<br/><br/>"
    "<b>나. 비침습적 이개강 전도성 실리콘 전극 기반 미주신경 자극(tVNS)</b><br/>"
    "귀 안쪽 이개강(Concha)에 안전하게 밀착되는 고유연 전도성 실리콘 전극을 통해 부작용 없이 미주신경을 정밀 전기 자극하여 부교감신경계를 신속히 활성화합니다.<br/><br/>"
    "<b>다. 능동적 탈숙고(Dereflection) 유한상태기계(FSM) 폐루프 제어</b><br/>"
    "내담자의 병리적 반추(Rumination)를 즉각 중단시키는 탈숙고(Dereflection) 인지 알고리즘을 하드웨어 자극 강도와 실시간 연동하는 폐루프(Closed-loop) 유한상태기계를 탑재하여 치료 효과를 극대화한 차세대 디지털 치료 시스템(DTx)입니다."
)
story.append(Paragraph(p_tech, body_style))
story.append(Spacer(1, 12))

# 4. 결론
story.append(Paragraph("4. 맺음말", sub_style))
story.append(Spacer(1, 5))
story.append(Paragraph("본 발명은 국가 미래 신성장 동력인 디지털 헬스케어 및 전자약 분야의 원천 기술로서, 특허청이 인정한 첨단기술 분류에 부합하므로 신속한 권리화 및 조기 상용화를 위해 본원발명에 대하여 <b>초고속 우선심사를 조속히 결정하여 주시기를 간곡히 요청</b>드립니다.", body_style))
story.append(Spacer(1, 20))

# 날짜 및 서명
story.append(Paragraph("2026년 11월 04일", bold_body))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>출 원 인 :  변  귀  섭  (인)</b>", bold_body))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>특  허  청  장  귀하</b>", bold_body))

doc.build(story)

# 2. DOCX 생성
doc_word = Document()
for section in doc_word.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

h1 = doc_word.add_heading("우 선 심 사 신 청 설 명 서 (초고속)", level=1)
h1.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.style.font.name = "맑은 고딕"
h1.style.font.size = Pt(18)
h1.style.font.bold = True
h1.style.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

p_meta = doc_word.add_paragraph()
p_meta.add_run("1. 출원번호 : 10-2026-0205329 (출원일자: 2026.10.22)\n").bold = True
p_meta.add_run("2. 발명의 명칭 : 개인 맞춤형 동적 베이스라인 생체 및 음성 분석, 이개강 전도성 실리콘 전극 기반 뇌신경 자극 및 능동적 탈숙고 유한상태기계 폐루프 제어를 구비한 디지털 치료 시스템 및 이의 제어 방법\n")
p_meta.add_run("3. 출 원 인 : 변귀섭 (특허고객번호: 4-2020-055266-0)\n")
p_meta.add_run("4. 첨단특허분류 : A61B 5/4836 (특허청 공식 부여 국가 첨단기술)\n").bold = True
p_meta.add_run("5. 신청구분 : 초고속 우선심사\n").bold = True

doc_word.add_heading("1. 신청의 취지", level=2)
doc_word.add_paragraph(
    "본 특허출원(제10-2026-0205329호)은 특허청으로부터 공식 첨단기술 특허분류(A61B 5/4836)를 부여받은 출원으로서, "
    "「특허법」 제61조 및 「특허·실용신안 우선심사의 신청에 관한 고시」에 의거하여 조속한 권리 확정 및 산업적 조기 실용화를 위하여 초고속 우선심사를 신청합니다."
)

doc_word.add_heading("2. 우선심사 신청 이유 (국가 첨단기술 분류 근거)", level=2)
doc_word.add_paragraph(
    "본 출원인은 2026년 11월 4일 특허청으로부터 「첨단기술 특허분류로 초고속심사 및 우선심사신청이 가능한 특허분류 A61B 5/4836가 부여되었습니다」라는 공식 심사안내 통지를 수신하였습니다. "
    "이에 따라 관련 법령상 초고속 우선심사 대상 요건을 완벽하게 충족하고 있습니다."
)

doc_word.add_heading("3. 발명의 구체적 기술 특징 및 첨단성", level=2)
doc_word.add_paragraph(
    "가. 다중 생체 신호 및 음성 바이오마커 기반 실시간 위기 감지:\n"
    "사용자의 PPG, HRV, EDA 및 음성 지표를 융합하여 개인 맞춤형 동적 베이스라인을 구축하고, 급성 심리적 위기 징후를 극초기에 감지합니다.\n\n"
    "나. 비침습적 이개강 전도성 실리콘 전극 기반 미주신경 자극(tVNS):\n"
    "귀 안쪽 이개강(Concha)에 안전하게 밀착되는 고유연 전도성 실리콘 전극을 통해 부작용 없이 미주신경을 정밀 전기 자극하여 부교감신경계를 신속히 활성화합니다.\n\n"
    "다. 능동적 탈숙고(Dereflection) 유한상태기계(FSM) 폐루프 제어:\n"
    "내담자의 병리적 반추(Rumination)를 즉각 중단시키는 탈숙고(Dereflection) 인지 알고리즘을 하드웨어 자극 강도와 실시간 연동하는 폐루프 유한상태기계를 탑재한 차세대 디지털 치료 시스템(DTx)입니다."
)

doc_word.add_heading("4. 맺음말", level=2)
doc_word.add_paragraph(
    "본 발명은 국가 미래 신성장 동력인 디지털 헬스케어 및 전자약 분야의 원천 기술로서, 특허청이 공인한 첨단기술 분류가 부여된 출원이므로 신속한 권리화 및 조기 상용화를 위해 본원발명에 대하여 초고속 우선심사를 조속히 결정하여 주시기를 간곡히 요청드립니다."
)

p_sign = doc_word.add_paragraph()
p_sign.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sign.add_run("\n2026년 11월 04일\n\n출 원 인 :   변   귀   섭   (인)\n\n특  허  청  장   귀하\n").bold = True

doc_word.save(docx_path)
print("Files created successfully on Desktop!")
