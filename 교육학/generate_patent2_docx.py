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

def create_patent2_docx():
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
    set_cell_background(c, "0A1E32")
    p_hdr = c.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_hdr.add_run("특 허 출 원 명 세 서 [특허 제2탄]\n")
    r1.font.name = '맑은 고딕'
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(255, 215, 0) # Gold

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
    add_p("【발명의 명칭】 유리 기판 광 인터커넥트 기반의 저항 색띠형 유효숫자 및 지수 승수 다파장 부동소수점 광 데이터 압축 전송 반도체 패키지 및 그 방법\n"
          "(Semiconductor Package for Compressive Floating-Point Optical Interconnect Based on Resistor-Color-Code Significand and Exponential Multiplier in Glass Substrate and Method Thereof)", indent=False)

    # 2. 기술분야
    add_sec("【기술분야】")
    add_p("본 발명은 인공지능(AI) 반도체 및 초고속 광 인터커넥트 패키징 기술에 관한 것으로, 구체적으로는 초평탄 유리 코어 기판(Glass Core Substrate)에 저항 색띠(Resistor Color Code)의 유효숫자 판별 및 승수(Multiplier, 10^N) 원리를 적용하여, 복수의 광 파장 중 선행 파장 군을 유효숫자로 매핑하고 후행 파장을 10진 지수 승수로 매핑함으로써, 우주적 스케일의 거대 정수부터 미세 AI 가중치 소수점까지의 모든 부동소수점 데이터를 단 1클럭 사이클 내에 초압축 전송하고, 수신단에서 포토다이오드의 물리적 게인(Gain)을 제어하여 소프트웨어 연산 지연 없이 실시간 아날로그 복원하는 저항 색띠형 부동소수점 광 데이터 압축 전송 반도체 패키지 및 그 방법에 관한 것이다.")

    # 3. 배경기술
    add_sec("【배경기술】")
    add_p("현대 인공지능(AI) 딥러닝 및 거대언어모델(LLM) 연산의 95% 이상은 IEEE 754 표준에 따른 FP32, FP16, FP8, BF16 등의 부동소수점(Floating-Point) 실수 데이터를 기반으로 수행된다. 부동소수점 데이터는 부호(Sign), 가수(Significand/Mantissa, 유효숫자), 및 지수(Exponent)의 3가지 요소로 구성된다.")
    add_p("그러나 종래의 반도체 인터커넥트는 부동소수점 실수를 전송하기 위해 데이터를 2진수 비트열로 잘게 쪼개어 수십 가닥의 구리 배선이나 고주파 직렬화(SerDes) 회로를 통해 전송하였다. 이로 인해 수십 GHz에 달하는 고주파 스위칭 발열, 신호 왜곡, RC 지연, 그리고 막대한 전력 소모가 발생하여 '메모리 벽(Memory Wall)' 현상이 극에 달하고 있다.")
    add_p("또한, 기존의 파장 분할 다중화(WDM) 광통신 기술은 단순히 파장별로 2진수 비트를 독립 전송하는 파이프라인 확장에 불과하여, 부동소수점 데이터가 갖는 자릿수와 지수적 특성을 광학적으로 직접 압축하거나 처리하지 못하는 한계가 존재하였다.")

    # 4. 발명의 내용
    add_sec("【발명의 내용】")
    add_p("【해결하고자 하는 과제】", indent=False)
    add_p("본 발명이 해결하고자 하는 주된 과제는, 전자공학의 저항 색띠(Resistor Color Code) 원리를 광 인터커넥트에 융합하여, 복수의 광 파장 조합만으로 방대한 부동소수점 실수를 단 5~6개의 광 펄스로 초압축하여 단 1클럭 내에 전송할 수 있는 신규 광학 반도체 패키지를 제공하는 데 있다.")
    add_p("본 발명이 해결하고자 하는 다른 과제는, 수신단에서 소프트웨어적인 디지털 연산 디코딩 단계를 생략하고, 수신된 지수 파장이 포토다이오드 증폭기의 게인(Gain) 단자를 직접 물리적으로 제어함으로써 광전 변환 순간 10^N배 즉시 증폭되는 무지연(Zero-Latency) 아날로그 승산 하드웨어를 제공하는 데 있다.")
    add_p("본 발명이 해결하고자 하는 또 다른 과제는, 검정색(0번) 파장의 신호 유무 오인을 방지하는 능동 영 펄스(Active-Zero Pulse) 메커니즘, 칩 발열 시에도 파장 간격을 영구 보존하는 자가 온도 보상(Athermal) 도파로, 입체적 복층 광 도로망을 구성하는 3D 다층 나선형 도파로, 및 광학적 동적 셔플링 암호화(ECC) 기술을 융합하여 완벽한 산업적 신뢰성을 보장하는 데 있다.")

    add_p("【과제의 해결 수단】", indent=False)
    add_p("상기 과제를 해결하기 위한 본 발명의 저항 색띠형 부동소수점 광 데이터 압축 전송 반도체 패키지는,\n"
          "입력된 부동소수점 데이터의 부호 및 유효숫자를 검정(0)부터 흰색(9)에 대응하는 복수의 고유 광 파장(λ0 ~ λ9)으로 매핑 변조하는 유효숫자 광 송신부;\n"
          "상기 부동소수점 데이터의 10진 지수 거듭제곱 승수(Multiplier, 10^N)를 은색(10^-2), 금색(10^-1), 검정(10^0) 내지 흰색(10^9)에 1:1 대응하는 단일의 지수 파장(λ_exp)으로 매핑 변조하는 지수 광 송신부;\n"
          "초평탄 유리 코어 기판(Glass Core Substrate) 내부에 펨토초 레이저로 형성되어, 상기 유효숫자 광 펄스들과 상기 지수 광 펄스를 단일 전송 사이클 동안 동시 도파하는 자가 온도 보상형 3차원 광 도파로; 및\n"
          "상기 3차원 광 도파로를 통과한 광 신호를 파장별로 분기하여 상기 지수 파장에 기초하여 상기 유효숫자의 자릿수를 단 1클럭 내에 복원하는 광학 수신 및 승산 모듈;\n"
          "을 포함하는 것을 특징으로 한다.")

    add_p("【발명의 효과】", indent=False)
    add_p("본 발명에 따르면 첫째, 기존 2진수 대비 데이터 전송 파장 및 핀 수를 50% 이상 절감하면서도, 0부터 수조 단위에 이르는 초거대 부동소수점 실수를 단 1클럭 펄스로 순간 전송할 수 있다.")
    add_p("둘째, 지수 승수 파장이 수신단 광전 증폭기의 물리적 게인을 직접 제어하므로, 디지털 연산 지연 시간(Latency)이 '0초'인 혁신적 실시간 아날로그 승산이 구현된다.")
    add_p("셋째, 자가 온도 보상 코팅을 통해 85℃ 이상의 가혹한 고열 환경에서도 0.001nm의 파장 안정성을 영구 유지한다.")

    # 5. 도면의 간단한 설명
    add_sec("【도면의 간단한 설명】")
    add_p("도 1은 본 발명의 일 실시예에 따른 저항 색띠형 6색 부동소수점 다파장 광 압축 매핑 표준 규격도이다.", indent=False)
    add_p("도 2는 본 발명의 일 실시예에 따른 저항 색띠형 부동소수점 광 인터커넥트 하드웨어 아키텍처 및 물리적 즉시 승산 시스템 구조도이다.", indent=False)

    # 6. 부호의 설명
    add_sec("【부호의 설명】")
    add_p("500: 부동소수점 광 송신 모듈 (Tx)", indent=False)
    add_p("510: 유효숫자-지수 분할기 (Significand-Exponent Splitter)", indent=False)
    add_p("520: 마이크로 콤 광원 (Micro-Comb Laser)", indent=False)
    add_p("530: 6채널 MRR 광변조기 어레이", indent=False)
    add_p("600: 초평탄 유리 코어 기판 (Glass Core Substrate)", indent=False)
    add_p("610: 자가 온도 보상(Athermal) 3차원 내장 광 도파로", indent=False)
    add_p("620: 고분해능 AWG 광학 분광기 (Optical De-multiplexer)", indent=False)
    add_p("700: 수신 및 물리적 즉시 승산 모듈 (Rx & Gain Multiplier)", indent=False)
    add_p("710: 초고속 포토다이오드 어레이 (Photodiode Array)", indent=False)
    add_p("720: 광학 제어 게인 승산기 (Optical Gain Multiplier)", indent=False)
    add_p("730: 부호 및 소수점 정렬기", indent=False)

    # 7. 특허청구범위 (압축 5대 청구항)
    add_sec("【특허청구범위】")

    claims = [
        ("【청구항 1】 (독립항: 저항 색띠형 부동소수점 광 인터커넥트 시스템)",
         "연산 칩렛 및 메모리 칩렛을 상호 연결하는 반도체 패키징 시스템에 있어서,\n"
         "입력된 부동소수점 데이터의 부호 및 유효숫자를 검정(0)부터 흰색(9)에 대응하는 복수의 고유 광 파장(λ0 ~ λ9)으로 매핑 변조하는 유효숫자 광 송신 모듈;\n"
         "상기 부동소수점 데이터의 10진 지수 거듭제곱 승수(Multiplier, 10^N)를 은색(10^-2), 금색(10^-1), 검정(10^0) 내지 흰색(10^9)에 대응하는 단일의 지수 파장(λ_exp)으로 매핑 변조하는 지수 광 송신 모듈;\n"
         "초평탄 유리 코어 기판(Glass Core Substrate) 내부에 형성되어, 상기 유효숫자 광 펄스들과 상기 지수 광 펄스를 단일 전송 사이클 동안 동시 도파하는 유리 기판 내장형 3차원 광 도파로; 및\n"
         "상기 3차원 광 도파로를 통과한 광 신호를 파장별로 분기하여 상기 지수 파장에 기초하여 상기 유효숫자의 자릿수를 단 1클럭 내에 복원하는 광학 수신 모듈;\n"
         "을 포함하는 것을 특징으로 하는 저항 색띠형 10진 지수 부동소수점 광 데이터 압축 전송 반도체 패키지."),

        ("【청구항 2】 (종속항: 물리적 게인 제어 즉시 아날로그 승산 하드웨어)",
         "제1항에 있어서,\n"
         "상기 광학 수신 모듈은 복수의 포토다이오드 및 가변 이득 증폭기(VGA)를 구비하며,\n"
         "상기 지수 파장(λ_exp)에 대응하는 수광 광전류가 상기 가변 이득 증폭기의 게인(Gain) 단자에 직접 인가되어, 상기 유효숫자 광 신호가 전기 신호로 변환되는 순간 물리적 하드웨어에 의해 자동으로 10^N배 승산 출력되는 것을 특징으로 하는 반도체 패키지."),

        ("【청구항 3】 (종속항: 자가 온도 보상형 무변형 광 도파로)",
         "제1항에 있어서,\n"
         "상기 유리 기판 내장형 3차원 광 도파로는 코어 외주면에 음의 열광학 계수(-dn/dT)를 갖는 클래딩층이 코팅되어,\n"
         "0℃ 내지 100℃의 패키지 온도 변화 범위 내에서 상기 광 파장들의 중심 파장 드리프트가 0.005nm 이하로 자동 보상 억제되는 것을 특징으로 하는 반도체 패키지."),

        ("【청구항 4】 (종속항: 능동 영 펄스 및 광학적 동적 암호화 셔플링)",
         "제1항에 있어서,\n"
         "상기 유효숫자 광 송신 모듈은 검정색(0번) 유효숫자 전송 시 무발광 상태와 구별하기 위한 기준 능동 영(Active-Zero) 펄스를 방출하고,\n"
         "전송 사이클마다 미리 공유된 암호화 키에 기초하여 파장 매핑 순서를 동적으로 뒤섞어 하드웨어 도청을 차단하는 광학 셔플링 암호화부를 더 포함하는 것을 특징으로 하는 반도체 패키지."),

        ("【청구항 5】 (방법 독립항: 저항 색띠형 광 압축 전송 방법)",
         "유리 기판에 실장된 반도체 칩 간에 부동소수점 데이터를 전송하는 방법에 있어서,\n"
         "(a) 송신측이 부동소수점 데이터를 부호, 유효숫자, 및 10진 지수 승수로 분할하는 단계;\n"
         "(b) 상기 유효숫자를 검정(0) 내지 흰색(9) 파장으로 매핑하고, 상기 지수 승수를 10^-2 내지 10^9 파장으로 매핑하여 단 1클럭 펄스로 방출하는 단계;\n"
         "(c) 방출된 광 펄스 군이 유리 기판 내부의 3차원 광 도파로를 통해 무간섭 광속으로 도파되는 단계; 및\n"
         "(d) 수신측 어레이 도파로 회절격자(AWG)가 파장별로 분기하고, 수신된 지수 파장으로 수광 증폭기의 게인을 직접 제어하여 부동소수점 데이터를 단 1클럭 내에 복원 출력하는 단계;\n"
         "를 포함하는 것을 특징으로 하는 저항 색띠형 부동소수점 광 데이터 압축 전송 방법.")
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
    add_p("본 발명은 인공지능(AI) 반도체에서 방대한 부동소수점(Floating-Point) 데이터를 전송할 때 구리 배선의 발열 및 대역폭 한계를 원천 극복하기 위한 저항 색띠형 10진 지수 부동소수점 광 데이터 압축 전송 반도체 패키지 및 그 방법에 관한 것이다.\n\n"
          "본 발명은 저항 색띠의 유효숫자 및 10^N 승수 원리를 결합하여, 유효숫자는 0~9 파장(λ0~λ9)으로 매핑하고 지수 승수는 10^-2부터 10^9 파장(λ_exp)으로 매핑하여 단 1클럭 1펄스로 동시 방출한다. 초평탄 유리 기판 내장형 3차원 자가 온도 보상 도파로를 통해 빛의 속도로 도파된 광 신호는 수신단 AWG에서 분광된 후, 지수 파장이 포토다이오드 증폭기의 물리적 게인(Gain)을 직접 제어하여 연산 지연 없이 실시간 아날로그 승산 복원된다.\n\n"
          "본 발명에 따르면, 전송 파장 수를 50% 절감하면서도 0부터 수조 단위의 부동소수점을 1클럭에 전송하고 전력 소모를 80% 이상 절감하는 혁신적 효과를 달성한다.")

    add_p("【대표도】", indent=False)
    p_fig = doc.add_paragraph()
    p_fig.paragraph_format.space_before = Pt(6)
    p_fig.paragraph_format.space_after = Pt(8)
    p_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_f = p_fig.add_run("도 2\n")
    r_f.font.name = '맑은 고딕'
    r_f.font.size = Pt(11)
    r_f.font.bold = True

    fig2_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도2_하드웨어_아키텍처.png'
    if os.path.exists(fig2_path):
        doc.add_picture(fig2_path, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_cap.add_run("【도 2】 저항 색띠형 부동소수점 광 인터커넥트 하드웨어 및 물리적 즉시 승산(Gain) 시스템")
        r_c.font.name = '맑은 고딕'
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(100, 100, 100)

    # 9. 도면 섹션
    doc.add_page_break()
    add_sec("【도면】")

    figs = [
        ("【도 1】 저항 색띠형 6색 부동소수점 다파장 광 압축 매핑 표준 규격도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도1_저항색띠_부동소수점_매핑도.png', 6.2),
        ("【도 2】 저항 색띠형 부동소수점 광 인터커넥트 하드웨어 및 물리적 즉시 승산 시스템 구조도",
         r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도2_하드웨어_아키텍처.png', 6.2)
    ]

    for title, img_path, w_inch in figs:
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

    out_docx = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_저항색띠_부동소수점_유리기판_광인터커넥트.docx'
    doc.save(out_docx)
    print(f"Patent 2 DOCX created at: {out_docx}")

if __name__ == "__main__":
    create_patent2_docx()
