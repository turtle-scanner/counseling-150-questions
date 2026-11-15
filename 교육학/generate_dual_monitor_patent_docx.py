# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_dual_monitor_patent_docx():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    style = doc.styles['Normal']
    font = style.font
    font.name = '맑은 고딕'
    font.size = Pt(10)
    font.color.rgb = RGBColor(30, 30, 30)

    # Title Banner Table
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl.rows[0].cells[0]
    c.width = Inches(6.5)
    set_cell_background(c, "0F2846")
    p_hdr = c.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_hdr.add_run("특 허 출 원 명 세 서 [바른자세 듀얼·트리플 2.0]\n")
    r1.font.name = '맑은 고딕'
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0, 229, 255) # Cyan

    r2 = p_hdr.add_run("주식회사 세이프티온 (SAFETYON CO., LTD.) ┃ 대표이사 변귀섭")
    r2.font.name = '맑은 고딕'
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(220, 235, 245)

    doc.add_paragraph()

    def add_sec(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 80, 160)
        return p

    def add_p(text, indent=True):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.25
        if indent:
            p.paragraph_format.first_line_indent = Pt(10)
        r = p.add_run(text)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(10)
        return p

    # 1. 서지사항
    add_sec("【서지사항】")
    add_p("【출원인】 주식회사 세이프티온 (대표이사 변귀섭)", indent=False)
    add_p("【발명자】 변귀섭", indent=False)
    add_p("【발명의 명칭】 바른자세 시선 유지형 상하 슬라이딩 리프트 및 마그네틱 탈부착 윙을 구비한 가변 적층식 듀얼 및 트리플 노트북 모니터 시스템 및 그 제어 방법\n"
          "(VARIABLE STACKED DUAL AND TRIPLE LAPTOP MONITOR SYSTEM WITH POSTURE-CORRECTING EYE-LEVEL SLIDING LIFT AND MAGNETIC DETACHABLE WINGS AND CONTROL METHOD THEREOF)", indent=False)

    # 2. 기술분야
    add_sec("【기술분야】")
    add_p("본 발명은 휴대용 컴퓨터 및 다중 디스플레이 장치에 관한 것으로, 구체적으로는 평상시 단일 노트북으로 초경량 휴대하다가 거치 시 상단 제2 모니터가 사용자의 안구 수평 시선(Eye-Level) 높이까지 무중력 감각으로 수직 솟아오르고, 필요 시 좌우에 윙(Wing) 형태의 제3 모니터가 마그네틱 포고핀(Pogo-Pin)으로 케이블 없이 0.1초 만에 결합되어 3면 입체 파노라마 작업 환경을 구축함과 동시에, AI 웹캠을 통해 사용자의 경추 굴곡 각도를 실시간 분석하여 거북목을 능동 방지하는 바른자세 시선 유지형 가변 적층식 듀얼 및 트리플 노트북 모니터 시스템 및 그 제어 방법에 관한 것이다.")

    # 3. 배경기술
    add_sec("【배경기술】")
    add_p("재택근무 및 원격 프로그래밍, 전문 문서 작업이 일상화되면서 노트북의 작은 단일 화면에 대한 답답함을 해소하기 위해 다중 모니터를 결합한 제품들이 개발되고 있다. 그러나 종래의 듀얼 스크린 노트북(예: 단순 180도 펼침 방식이나 키보드 상단 보조 스크린 탑재형)은 모니터 화면의 중심점이 사용자의 수평 시선보다 20cm 내지 30cm 이상 아래에 머무를 수밖에 없는 구조적 한계가 존재하였다.")
    add_p("이로 인해 사용자는 장시간 작업 시 고개를 45도 내지 60도 이상 아래로 숙이게 되며, 이는 경추(목뼈)에 약 20kg 이상의 과도한 하중을 지속적으로 가하여 거북목 증후군, 목 디스크, 만성 어깨 결림 등의 심각한 근골격계 질환을 필연적으로 유발한다.")
    add_p("나아가 종래의 다중 모니터 장치는 보조 화면을 부착할 때마다 복잡한 전원 케이블 및 HDMI/Type-C 영상선을 치렁치렁 연결해야 하는 극심한 사용상 번거로움이 있었고, 항시 결합된 상태로 휴대할 경우 2.5kg 이상의 과도한 무게로 인해 휴대용 노트북 본연의 이동성을 완전히 상실하는 치명적인 결함이 있었다.")

    # 4. 발명의 내용
    add_sec("【발명의 내용】")
    add_p("【해결하고자 하는 과제】", indent=False)
    add_p("본 발명이 해결하고자 하는 주된 과제는, 상단 모니터가 사용자의 눈높이(Eye-Level) 수평선에 정확히 일치하도록 수직 상방으로 15cm 내지 25cm 부드럽게 솟아오르는 자가 평형(Zero-Gravity) 슬라이딩 리프트 기구를 제공하여, 작업 중 경추 꺾임각을 0도로 영구 유지함으로써 거북목을 원천 방지하는 데 있다.")
    add_p("본 발명이 해결하고자 하는 다른 과제는, 평상시에는 1.1kg대의 단일 초경량 노트북으로 휴대하고, 필요 시 좌우 윙(Wing) 모니터가 네오디뮴 자석 및 포고핀 어레이에 의해 선 연결 없이 0.1초 만에 원터치 결합되는 초슬림 모듈형 트리플(트리얼) 파노라마 워크스테이션을 제공하는 데 있다.")
    add_p("본 발명이 해결하고자 하는 또 다른 과제는, 상단 베젤의 초소형 AI 카메라를 통해 사용자의 시선과 목선 벡터를 실시간 추적하고, 사용자가 부지불식간에 고개를 숙일 경우 상단 모니터로 시선을 유도하거나 화면 틸트 각도를 미세 자동 보정하는 인공지능 기반 바른자세 헬스케어 피드백 시스템을 제공하는 데 있다.")

    add_p("【과제의 해결 수단】", indent=False)
    add_p("상기 과제를 해결하기 위한 본 발명의 바른자세 듀얼 및 트리플 노트북 모니터 시스템은,\n"
          "본체 키보드부 상단에 힌지 결합된 제1 메인 모니터;\n"
          "상기 제1 메인 모니터의 배면에 내장된 가이드 레일 및 토크 스프링을 구비하여, 사용자의 정면 수평 시선 높이에 대응하여 수직 상방으로 15cm 내지 25cm 슬라이딩 승강 가능한 자가 평형(Zero-Gravity) 리프트 기구;\n"
          "상기 리프트 기구의 상단에 결합되어 사용자의 안구 수평선과 정면 1:1 대향하는 제2 상단 메인 모니터; 및\n"
          "상기 제2 상단 메인 모니터의 좌우 측면에 네오디뮴 자석 및 전원·영상 복합 포고핀(Pogo-Pin) 어레이로 케이블리스 탈부착되어, 180도 내측 오목 파노라마 시야각을 형성하는 제3 좌우 윙(Wing) 모니터;\n"
          "를 포함하는 것을 특징으로 한다.")

    add_p("【발명의 효과】", indent=False)
    add_p("본 발명에 따르면 첫째, 상단 제2 모니터가 수평 안구 시선과 정확히 일치하므로 고개를 숙이지 않고 척추를 꼿꼿이 세운 상태에서 장시간 코딩 및 문서 작업이 가능하여 거북목 발병률을 90% 이상 예방한다.")
    add_p("둘째, 좌우 윙 모니터가 마그네틱 포고핀으로 선 없이 0.1초 만에 결합되어 코딩창, 기획문서, 화상회의창의 3면 입체 파노라마 작업 공간을 즉시 구현한다.")
    add_p("셋째, 모듈형 분리 구조로 외출 시에는 1.1kg의 단일 노트북으로 가볍게 휴대할 수 있어 최고의 이동성과 생산성을 동시에 만족한다.")

    # 5. 도면의 간단한 설명 (도 1 ~ 도 4)
    add_sec("【도면의 간단한 설명】")
    add_p("도 1은 본 발명의 일 실시예에 따른 바른자세 시선 유지형 상하 슬라이딩 리프트 듀얼 모니터 전개 및 시야각 비교도이다.", indent=False)
    add_p("도 2는 본 발명의 일 실시예에 따른 트리플(트리얼) 3면 입체 파노라마 전개 및 마그네틱 윙(Wing) 확장 구조도이다.", indent=False)
    add_p("도 3은 본 발명의 일 실시예에 따른 자가 평형(Zero-Gravity) 슬라이딩 힌지 기구 및 마그네틱 포고핀 결합 단면도이다.", indent=False)
    add_p("도 4는 본 발명의 일 실시예에 따른 AI 시선 및 경추 꺾임각 감지 기반 바른자세 피드백 제어 시스템 블록도이다.", indent=False)

    # 6. 부호의 설명
    add_sec("【부호의 설명】")
    add_p("100: 제1 메인 모니터 (하단)", indent=False)
    add_p("200: 자가 평형(Zero-Gravity) 슬라이딩 리프트 기구", indent=False)
    add_p("210: 정하중 토크 스프링 (모니터 자중 상쇄 밸런서)", indent=False)
    add_p("220: 미세 마찰 브레이크 패드", indent=False)
    add_p("300: 제2 상단 메인 모니터 (수평 시선 직결 작업창)", indent=False)
    add_p("400L, 400R: 제3 좌우 윙(Wing) 모니터 (트리플 확장용)", indent=False)
    add_p("500: 마그네틱 포고핀(Pogo-Pin) 무선 결합 조인트", indent=False)
    add_p("810: 초소형 AI 웹캠", indent=False)
    add_p("820: 경추 굴곡각 판별 엔진", indent=False)
    add_p("830: 바른자세 복원 피드백 제어기", indent=False)

    # 7. 특허청구범위 (압축 5대 청구항)
    add_sec("【특허청구범위】")

    claims = [
        ("【청구항 1】 (독립항: 슬라이딩 리프트 및 마그네틱 포고핀 결합 시스템)",
         "본체 키보드부 상단에 힌지 결합된 제1 메인 모니터;\n"
         "상기 제1 메인 모니터의 배면에 실장된 가이드 레일 및 토크 스프링을 구비하여, 사용자의 정면 안구 수평 시선(Eye-Level) 높이에 대응하여 수직 상방으로 슬라이딩 승강 가능한 자가 평형(Zero-Gravity) 리프트 기구;\n"
         "상기 리프트 기구의 상단에 결합되어 수직 15cm 내지 25cm 상승 전개되는 제2 상단 메인 모니터; 및\n"
         "상기 제2 상단 메인 모니터의 좌우 측면에 네오디뮴 영구자석 및 디스플레이포트(DP) 전송용 포고핀(Pogo-Pin) 어레이로 케이블리스 탈부착되어 3면 입체 파노라마 작업 영역을 형성하는 제3 윙(Wing) 모니터;\n"
         "를 포함하는 것을 특징으로 하는 바른자세 가변 적층식 듀얼 및 트리플 노트북 모니터 시스템."),

        ("【청구항 2】 (종속항: 자가 평형 힌지 기구)",
         "제1항에 있어서,\n"
         "상기 자가 평형 리프트 기구는 상기 제2 상단 메인 모니터의 자중(Gravity)과 1:1로 대향하는 정하중 태엽 스프링 및 미세 마찰 패드를 포함하여,\n"
         "외력 인가 시 부드럽게 승강하고 외력 해제 시 별도의 잠금 레버 조작 없이 임의의 높이에서 처짐 없이 자가 유지 고정되는 것을 특징으로 하는 모니터 시스템."),

        ("【청구항 3】 (종속항: 마그네틱 포고핀 원터치 무선 결합 구조)",
         "제1항에 있어서,\n"
         "상기 제3 윙 모니터의 결합면에는 자극(N극, S극)이 교대 배치된 마그네틱 가이드 및 스프링 탄성 포고핀 단자가 구비되어,\n"
         "근접 시 자력에 의해 자동으로 중심 정렬 결합됨과 동시에 단일 접촉면을 통해 직류 구동 전원 및 고해상도 비디오 신호가 동시 직결 공급되는 것을 특징으로 하는 모니터 시스템."),

        ("【청구항 4】 (종속항: AI 경추 꺾임각 감지 및 능동 피드백 제어)",
         "제1항에 있어서,\n"
         "상기 제2 상단 메인 모니터 상단 베젤에 내장된 카메라를 통해 사용자의 얼굴 특징점 및 어깨선 벡터를 추출하여 경추 굴곡 각도를 실시간 연산하는 AI 자세 분석 모듈; 및\n"
         "상기 경추 굴곡 각도가 기준치를 초과하여 고개가 아래로 숙여진 것으로 판정된 경우, 상기 제2 상단 메인 모니터로 시선을 유도하는 팝업을 발생시키거나 상기 제1 메인 모니터의 밝기를 감쇄시키는 자세 교정 제어부;\n"
         "를 더 포함하는 것을 특징으로 하는 모니터 시스템."),

        ("【청구항 5】 (방법 독립항: 가변 전개 및 동적 제어 방법)",
         "가변 적층식 듀얼 및 트리플 모니터를 제어하는 방법에 있어서,\n"
         "(a) 상단 제2 모니터가 자가 평형 리프트 기구를 통해 수직 상승하여 안구 수평선 높이로 전개되는 단계;\n"
         "(b) 제3 윙 모니터가 마그네틱 포고핀 단자에 자력 결합 시 하드웨어 연결을 자동 감지하여 다중 디스플레이 해상도를 3면 파노라마로 자동 확장 구성하는 단계; 및\n"
         "(c) 카메라 영상 기반으로 사용자의 시선 높이 및 거북목 각도를 실시간 추적하여 디스플레이 위치 및 시선 유도 인터페이스를 동적 제어하는 단계;\n"
         "를 포함하는 것을 특징으로 하는 바른자세 듀얼 및 트리플 모니터 제어 방법.")
    ]

    for c_tit, c_body in claims:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(c_tit)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 50, 120)
        add_p(c_body, indent=False)

    # 8. 요약서 및 대표도
    doc.add_page_break()
    add_sec("【요약서】")
    add_p("【요약】", indent=False)
    add_p("본 발명은 장시간 노트북 작업 시 고개를 숙임으로써 발생하는 거북목 및 목 디스크를 원천 예방하기 위한 바른자세 시선 유지형 상하 슬라이딩 리프트 듀얼 및 트리플 노트북 모니터 시스템에 관한 것이다.\n\n"
          "본 발명은 하단 제1 모니터 배면의 자가 평형 리프트 기구를 통해 제2 상단 모니터가 사용자의 안구 수평선(Eye-Level) 높이로 15~25cm 수직 솟아오르고, 필요 시 좌우에 제3 윙(Wing) 모니터가 마그네틱 포고핀으로 케이블 없이 0.1초 만에 결합되어 3면 입체 파노라마 작업 환경을 구축한다. 나아가 AI 웹캠을 통해 사용자의 목 꺾임 각도를 실시간 감지하여 바른 척추 자세를 유도한다.\n\n"
          "본 발명에 따르면, 평상시에는 1.1kg 단일 노트북으로 가볍게 휴대하다가 거치 시 완벽한 인체공학 3면 워크스테이션으로 변신하여 거북목 예방과 작업 생산성 극대화를 동시에 달성한다.")

    add_p("【대표도】", indent=False)
    p_fig = doc.add_paragraph()
    p_fig.paragraph_format.space_before = Pt(6)
    p_fig.paragraph_format.space_after = Pt(8)
    p_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_f = p_fig.add_run("도 2\n")
    r_f.font.name = '맑은 고딕'
    r_f.font.size = Pt(11)
    r_f.font.bold = True

    fig2_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도2_트리플_파노라마.png'
    if os.path.exists(fig2_path):
        doc.add_picture(fig2_path, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_cap.add_run("【도 2】 트리플(트리얼) 3면 입체 파노라마 전개 및 마그네틱 윙(Wing) 확장 구조도")
        r_c.font.name = '맑은 고딕'
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(100, 100, 100)

    # 9. 도면 전체 모음 (도 1 ~ 도 4)
    doc.add_page_break()
    add_sec("【도면】")

    figures_list = [
        ("【도 1】 바른자세 시선 유지형 상하 슬라이딩 리프트 듀얼 모니터 전개 및 시야각 비교도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도1_듀얼리프트_시야각.png', 6.2),
        ("【도 2】 트리플(트리얼) 3면 입체 파노라마 전개 및 마그네틱 윙(Wing) 확장 구조도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도2_트리플_파노라마.png', 6.2),
        ("【도 3】 자가 평형(Zero-Gravity) 슬라이딩 힌지 기구 및 마그네틱 포고핀 결합 단면도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도3_힌지_포고핀.png', 6.2),
        ("【도 4】 AI 시선 및 경추 꺾임각 감지 기반 바른자세 피드백 제어 시스템 블록도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도4_AI제어흐름도.png', 6.2)
    ]

    for title, img_path, w_inch in figures_list:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_before = Pt(14)
        p_t.paragraph_format.space_after = Pt(6)
        p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_t = p_t.add_run(title)
        r_t.font.name = '맑은 고딕'
        r_t.font.size = Pt(10.5)
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(20, 60, 100)

        if os.path.exists(img_path):
            doc.add_picture(img_path, width=Inches(w_inch))

    out_docx = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_듀얼_트리플_모니터_2.0.docx'
    doc.save(out_docx)
    print(f"Created complete Patent DOCX at: {out_docx}")

if __name__ == "__main__":
    create_dual_monitor_patent_docx()
