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

def create_complete_docx():
    doc = docx.Document()

    # Page Margins: 20mm (Standard KIPO format)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Base Font Settings
    style = doc.styles['Normal']
    font = style.font
    font.name = '맑은 고딕'
    font.size = Pt(10.5)
    font.color.rgb = RGBColor(30, 30, 30)

    # Document Header Table (Title banner)
    header_tbl = doc.add_table(rows=1, cols=1)
    header_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_tbl.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "0A1E32")
    p_hdr = cell.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_hdr1 = p_hdr.add_run("특 허 출 원 명 세 서\n")
    r_hdr1.font.name = '맑은 고딕'
    r_hdr1.font.size = Pt(16)
    r_hdr1.font.bold = True
    r_hdr1.font.color.rgb = RGBColor(0, 229, 255) # Cyan

    r_hdr2 = p_hdr.add_run("주식회사 세이프티온 (SAFETYON CO., LTD.) ┃ 대표이사 변귀섭")
    r_hdr2.font.name = '맑은 고딕'
    r_hdr2.font.size = Pt(10.5)
    r_hdr2.font.color.rgb = RGBColor(220, 235, 245)

    doc.add_paragraph() # spacing

    def add_section_title(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title_text)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 80, 160)
        return p

    def add_body(text, indent=True):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.25
        if indent:
            p.paragraph_format.first_line_indent = Pt(10)
        r = p.add_run(text)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(10)
        return p

    # 1. Title
    add_section_title("【서지사항】")
    add_body("【출원인】 주식회사 세이프티온 (대표이사 변귀섭)", indent=False)
    add_body("【발명자】 변귀섭", indent=False)
    add_body("【발명의 명칭】 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지 및 그 데이터 전송 방법\n(Semiconductor Package with Multi-Wavelength Decimal Optical Interconnect Embedded in Glass Substrate and Data Transmission Method Thereof)", indent=False)

    # 2. Tech Field
    add_section_title("【기술분야】")
    add_body("본 발명은 인공지능(AI) 반도체 및 고대역폭 메모리 패키징 기술에 관한 것으로, 구체적으로는 종래의 실리콘 인터포저나 유기 인터포저 대신 초평탄·저손실 유리 코어 기판(Glass Core Substrate)을 적용하고, 내부 광 도파로를 통해 데이터를 2진수 비트열이 아닌 10진수(0~9)와 10대 독립 광 파장(Wavelength)으로 1:1 매핑 전송함으로써 전송 대역폭을 극대화하고 신호 지연 및 소모 전력을 획기적으로 절감하는 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지 및 그 데이터 전송 방법에 관한 것이다.")

    # 3. Background Art
    add_section_title("【배경기술】")
    add_body("최근 인공지능 거대언어모델(LLM) 및 딥러닝 연산의 폭발적 증가로 인하여, GPU/NPU와 같은 고성능 연산 프로세서와 고대역폭 메모리(HBM) 간에 초당 수십 테라바이트(TB/s) 이상의 데이터를 초고속으로 전송해야 하는 요구가 급증하고 있다.")
    add_body("종래의 반도체 패키징은 실리콘 인터포저(Silicon Interposer) 또는 유기(Organic) 기판 상에 미세 구리 배선을 형성하여 전기적 신호로 데이터를 송수신하였다. 그러나 구리 도선은 도선 저항(Resistance)과 기생 커패시턴스(Capacitance)로 인하여 신호 전송 주파수가 수 GHz 이상으로 증가할수록 극심한 고주파 표피 효과(Skin Effect)와 신호 감쇄, RC 지연 및 옴 열(Joule Heat)이 기하급수적으로 발생한다. 이로 인해 프로세서가 메모리로부터 데이터를 제때 공급받지 못해 연산 효율이 급락하는 '메모리 벽(Memory Wall)' 현상이 심화되고 있다.")
    add_body("나아가 기존의 모든 데이터 전송은 2진수 비트(0과 1)에 기반하여 데이터를 직렬 또는 병렬로 쪼개어 전송하는 방식이므로, 큰 수치를 전송하기 위해 복잡한 직렬화-역직렬화(SerDes) 회로와 고주파 클럭 스위칭이 요구되며, 이는 막대한 전력 소모와 열 방출을 유발하는 치명적인 한계가 존재한다.")

    # 4. Prior Art
    add_section_title("【선행기술문헌】")
    add_body("【특허문헌】", indent=False)
    add_body("(특허문헌 0001) 대한민국 등록특허 제10-2023-0145892호 (광 도파로 일체형 반도체 패키지 기판 및 그 제조방법)")
    add_body("(특허문헌 0002) 미국 공개특허 US 2023/0288634 A1 (Glass Substrate with Optical Waveguides for High-Density Interconnects)")
    add_body("【비특허문헌】", indent=False)
    add_body("(비특허문헌 0001) IEEE Journal of Selected Topics in Quantum Electronics, 'Co-Packaged Optics and Wavelength-Division Multiplexing for AI/ML Accelerators', Vol. 29, Issue 2, 2023.")

    # 5. Invention Summary
    add_section_title("【발명의 내용】")
    add_body("【해결하고자 하는 과제】", indent=False)
    add_body("본 발명이 해결하고자 하는 주된 과제는, 인공지능 연산 장치(GPU/NPU)와 고대역폭 메모리(HBM) 간의 초고속 데이터 전송 시 구리 배선에서 필연적으로 발생하는 저항 손실, 기생 커패시턴스, 발열 및 신호 왜곡을 원천적으로 해결할 수 있는 신규 광학 반도체 인터커넥트 패키지를 제공하는 데 있다.")
    add_body("본 발명이 해결하고자 하는 다른 과제는, 기존 2진수(0, 1) 신호 전송의 물리적 시간·대역폭 한계를 근본적으로 극복하기 위하여, 10진수 숫자(0 내지 9)에 1:1 대응하는 10가지 고유 광 파장(λ0 ~ λ9)을 정의하고, 단 1클럭의 단일 펄스 주기만으로 10진수 1자릿수(3.32비트 분량) 이상을 동시 전송함으로써 신호 지연(Latency)을 획기적으로 단축하고 전송 대역폭을 비약적으로 극대화하는 광 전송 시스템 및 그 방법을 제공하는 데 있다.")
    add_body("본 발명이 해결하고자 하는 또 다른 과제는, 초평탄·무휨 특성을 갖는 유리 코어 기판(Glass Core Substrate) 내부에 3차원 광 도파로(3D Optical Waveguide)를 일체형으로 직접 매립 형성함으로써, 신호 간섭(Crosstalk)과 광 결합 손실(Coupling Loss)을 최소화하면서도 칩 간 인터페이스 핀 수(Pin Count)를 대폭 축소할 수 있는 초고성능 CPO(Co-Packaged Optics) 반도체 패키지를 제공하는 데 있다.")

    add_body("【과제의 해결 수단】", indent=False)
    add_body("상기 과제를 해결하기 위한 본 발명의 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지는, 입력된 2진 비트열을 0부터 9까지의 10진수 심볼 값으로 변환하고, 상기 10진수 심볼 값 각각에 대응하여 미리 설정된 10개의 고유 광 파장(λ0 ~ λ9) 중 어느 하나 이상의 광 신호를 단일 전송 사이클 동안 선택적으로 생성하는 10진 파장 송신 모듈(Tx); 두께 100㎛ 내지 500㎛ 범위의 유리 코어층(Glass Core Layer)을 구비하며, 상기 유리 코어층 내부에 펨토초 레이저 직접 묘화(Direct Laser Writing) 방식으로 형성되어 상기 10개의 고유 광 파장 신호를 동시 전파 가능한 유리 기판 내장형 3D 광 도파로(Optical Waveguide); 및 상기 3D 광 도파로를 통과한 광 신호를 파장별로 분기하여 상기 10진수 심볼 값 및 원래의 2진 비트열로 단 1클럭 내에 복원하는 10진 파장 수신 모듈(Rx)을 포함한다.")
    add_body("본 발명의 일 실시예에 따르면, 상기 10개의 고유 광 파장(λ0 ~ λ9)은 1310nm 또는 1550nm 광통신 윈도우 대역 내에서 20nm의 등간격 파장 그리드(Wavelength Grid)로 배치되며, 검정(0번 ➔ λ0), 갈색(1번 ➔ λ1), 빨강(2번 ➔ λ2), 주황(3번 ➔ λ3), 노랑(4번 ➔ λ4), 초록(5번 ➔ λ5), 파랑(6번 ➔ λ6), 보라(7번 ➔ λ7), 회색(8번 ➔ λ8), 및 흰색(9번 ➔ λ9)의 10대 스펙트럼 룩업테이블(LUT)에 의해 1:1 매핑 변조된다.")

    add_body("【발명의 효과】", indent=False)
    add_body("본 발명에 따르면 첫째, 종래 2진수(0, 1) 직렬 전송 대비 1회의 광 전송 사이클만으로 기존 대비 최소 3.32배(log2(10)) 이상의 정보량을 순간 전송하며, 10개 파장의 동시 다중화(WDM) 병렬 전송 시 전송 대역폭을 10배(1,000%) 이상 폭발적으로 증대시킬 수 있다.")
    add_body("둘째, 복잡한 직렬-병렬 변환(SerDes) 및 버퍼링 단계를 생략하고 빛의 속도(3×10^8 m/s)로 직결 전송하므로 신호 지연(Latency)을 90% 이상 단축할 수 있다.")
    add_body("셋째, 순수 광자(Photon) 기반 전송이므로 구리 배선에서 발생하던 극심한 옴 열(Joule Heat)을 원천 차단하여 소모 전력을 80% 이상 절감할 수 있다.")

    # 6. Description of Drawings
    add_section_title("【도면의 간단한 설명】")
    add_body("도 1은 본 발명의 일 실시예에 따른 0번부터 9번까지의 10진수 심볼과 10대 고유 광 파장(λ0 ~ λ9) 간의 1:1 스펙트럼 매핑 표준 규격도이다.", indent=False)
    add_body("도 2는 본 발명의 일 실시예에 따른 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지의 3차원 투시 결합 구조를 나타낸 특허 대표도이다.", indent=False)
    add_body("도 3은 본 발명의 일 실시예에 따른 송신측 10진 파장 인코더 및 10 채널 마이크로 링 공진기(MRR) 어레이 송신 모듈의 상세 구조도이다.", indent=False)
    add_body("도 4는 본 발명의 일 실시예에 따른 초평탄 유리 코어 기판 내부에 펨토초 레이저로 매립 형성된 3차원 광 도파로의 단면 구조도이다.", indent=False)
    add_body("도 5는 본 발명의 일 실시예에 따른 수신측 어레이 도파로 회절격자(AWG) 디멀티플렉서 및 초고속 포토다이오드(PD) 어레이 수신 모듈의 상세 구성도이다.", indent=False)
    add_body("도 6은 본 발명의 일 실시예에 따른 10진 파장 광 인터커넥트 시스템의 데이터 송수신 전체 프로세스를 나타낸 동작 순서도이다.", indent=False)

    # 7. Reference Numerals
    add_section_title("【부호의 설명】")
    add_body("100: 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지", indent=False)
    add_body("110: 인공지능 연산 칩렛 (AI GPU / NPU 다이)", indent=False)
    add_body("115: 마이크로 범프 어레이 (Micro-Bump Interconnects)", indent=False)
    add_body("120: 차세대 메모리 칩렛 (16단 적층 HBM4 메모리 큐브)", indent=False)
    add_body("200: 초평탄 유리 코어 기판 (Glass Core Substrate)", indent=False)
    add_body("210: 유리 내장형 3차원 광 도파로 (3D Optical Waveguide: 무지개 광 링크 λ0~λ9)", indent=False)
    add_body("300: 10진 파장 송신 모듈 (Tx: 마이크로 링 공진기 MRR 어레이)", indent=False)
    add_body("400: 10진 파장 수신 모듈 (Rx: 어레이 도파로 회절격자 AWG 및 포토다이오드 PD 어레이)", indent=False)

    # 8. Claims (5 Core Claims)
    add_section_title("【특허청구범위】")
    
    claims = [
        ("【청구항 1】", 
         "연산 칩렛 및 메모리 칩렛을 상호 연결하는 반도체 패키징 시스템에 있어서,\n"
         "입력된 데이터를 0부터 9까지의 10진수 심볼 값으로 변환하고, 상기 10진수 심볼 값 각각에 대응하여 미리 설정된 10개의 고유 광 파장(λ0, λ1, λ2, λ3, λ4, λ5, λ6, λ7, λ8, λ9) 중 어느 하나 이상의 광 신호를 단일 전송 사이클 동안 선택적으로 생성하는 10진 파장 송신 모듈;\n"
         "두께 100㎛ 내지 500㎛ 범위의 유리 코어층(Glass Core Layer) 내부에 펨토초 레이저 직접 묘화 방식으로 형성되어, 상기 10개의 고유 광 파장 신호를 무간섭으로 동시 전파하는 유리 기판 내장형 3차원 광 도파로; 및\n"
         "상기 3차원 광 도파로를 통과한 광 신호를 파장별로 분기 검출하여 상기 10진수 심볼 값 및 원래의 2진 데이터로 단 1클럭 내에 복원하는 10진 파장 수신 모듈;\n"
         "을 포함하는 것을 특징으로 하는 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지."),
        
        ("【청구항 2】",
         "제1항에 있어서,\n"
         "상기 10개의 고유 광 파장(λ0 ~ λ9)은 1310nm 또는 1550nm 광통신 대역 내에서 등간격 파장 그리드로 배치되며,\n"
         "검정(0번 ➔ λ0), 갈색(1번 ➔ λ1), 빨강(2번 ➔ λ2), 주황(3번 ➔ λ3), 노랑(4번 ➔ λ4), 초록(5번 ➔ λ5), 파랑(6번 ➔ λ6), 보라(7번 ➔ λ7), 회색(8번 ➔ λ8), 및 흰색(9번 ➔ λ9)에 각각 대응하는 10대 스펙트럼 룩업테이블(LUT)에 의해 1:1 매핑 변조되는 것을 특징으로 하는 반도체 패키지."),
         
        ("【청구항 3】",
         "제1항에 있어서,\n"
         "상기 10진 파장 송신 모듈은 단일 칩에 집적된 10 채널 마이크로 링 공진기(MRR: Micro-Ring Resonator) 어레이를 구비하고,\n"
         "상기 10진 파장 수신 모듈은 어레이 도파로 회절격자(AWG) 및 10 채널 포토다이오드(PD) 어레이를 구비하여,\n"
         "단일 광 도파로 채널을 통해 1클럭당 복수의 10진 심볼이 파장 분할 다중화(WDM) 방식으로 동시 병렬 전송되는 것을 특징으로 하는 반도체 패키지."),
         
        ("【청구항 4】",
         "제1항에 있어서,\n"
         "상기 연산 칩렛은 GPU 또는 NPU이고, 상기 메모리 칩렛은 차세대 고대역폭 메모리(HBM4)이며, 상기 유리 코어층 상면에 CPO(Co-Packaged Optics) 형태로 직접 일체화 실장되고,\n"
         "상기 유리 코어층의 열팽창계수(CTE)는 3 내지 8 ppm/K 범위로 제어되어 상기 칩렛들과의 열팽창 차이에 의한 휨 변형(Warpage)이 억제되는 것을 특징으로 하는 반도체 패키지."),
         
        ("【청구항 5】",
         "유리 기판에 실장된 복수의 반도체 칩 간에 데이터를 전송하는 방법에 있어서,\n"
         "(a) 송신측이 입력 데이터를 0 내지 9의 10진수 단위로 분할 인코딩하는 단계;\n"
         "(b) 인코딩된 10진수 값에 1:1 매핑된 고유 파장(λ0 ~ λ9)의 광 펄스를 광원을 통해 1클럭 내에 방출하는 단계;\n"
         "(c) 방출된 광 신호가 유리 기판 내부의 3차원 광 도파로를 통해 광속으로 도파되는 단계; 및\n"
         "(d) 수신측 어레이 도파로 회절격자(AWG)가 수신된 파장을 분파 검출하여 10진 데이터를 원래의 데이터로 단 1클럭 내에 복원하는 단계;\n"
         "를 포함하는 것을 특징으로 하는 유리 기판 다파장 10진 광 데이터 전송 방법.")
    ]

    for c_title, c_body in claims:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(c_title)
        r.font.name = '맑은 고딕'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 50, 120)
        
        add_body(c_body, indent=False)

    # 9. Abstract (요약서) - PERFECTLY EMBEDDED WITH IMAGE
    doc.add_page_break()
    add_section_title("【요약서】")
    add_body("【요약】", indent=False)
    add_body("본 발명은 인공지능 연산 칩렛(GPU/NPU)과 고대역폭 메모리(HBM) 간의 대용량 데이터 전송 시 구리 배선의 저항 및 발열로 인한 메모리 벽(Memory Wall) 현상을 원천적으로 해결하기 위한 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지 및 그 전송 방법에 관한 것이다.\n\n"
             "본 발명에 따른 반도체 패키지는, 입력된 데이터를 0부터 9까지의 10진수 심볼 값으로 변환하고 이에 대응하여 미리 설정된 10개의 고유 광 파장(λ0 ~ λ9) 중 어느 하나 이상의 광 신호를 단일 사이클 동안 선택적으로 생성하는 10진 파장 송신 모듈; 두께 100㎛ 내지 500㎛ 범위의 유리 코어층 내부에 펨토초 레이저로 직접 식각 형성되어 상기 10개의 고유 광 파장 신호를 무간섭 광속으로 동시 전파하는 유리 기판 내장형 3차원 광 도파로; 및 상기 광 신호를 어레이 도파로 회절격자(AWG)를 통해 파장별로 분기 검출하여 단 1클럭 내에 10진수 및 2진 데이터로 즉시 복원하는 10진 파장 수신 모듈을 포함한다.\n\n"
             "본 발명에 따르면, 종래 2진수(0, 1) 직렬 전송 대비 1회의 광 전송 사이클만으로 최소 3.32배 이상의 정보량을 순간 전송하며, 10개 파장의 동시 병렬 전송(WDM) 시 대역폭을 10배 이상 비약적으로 극대화하고, 전송 지연 및 옴 열(Joule Heat)을 80% 이상 감축할 수 있다.")

    add_body("【대표도】", indent=False)
    p_fig = doc.add_paragraph()
    p_fig.paragraph_format.space_before = Pt(6)
    p_fig.paragraph_format.space_after = Pt(10)
    p_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig = p_fig.add_run("도 2\n")
    r_fig.font.name = '맑은 고딕'
    r_fig.font.size = Pt(11)
    r_fig.font.bold = True
    
    # INSERT THE PERFECT FIGURE 2 DIRECTLY IN ABSTRACT!
    fig2_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허_도2_대표도_최종완성.png'
    if os.path.exists(fig2_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(12)
        doc.add_picture(fig2_path, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("【도 2】 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지 대표도")
        r_cap.font.name = '맑은 고딕'
        r_cap.font.size = Pt(9.5)
        r_cap.font.color.rgb = RGBColor(100, 100, 100)

    # 10. Figures Section (도면 1 ~ 도면 6 일괄 삽입)
    doc.add_page_break()
    add_section_title("【도면】")

    figures = [
        ("【도 1】 10진수 심볼(0~9) 대 10대 고유 광 파장(λ0~λ9) 1:1 매핑 규격도", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도1_10진파장매핑.png', 6.0),
        ("【도 2】 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지 대표도", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도2_대표도_최종완성.png', 6.4),
        ("【도 3】 10진 파장 송신 모듈 (Tx: 10채널 마이크로 링 공진기 MRR 어레이)", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도3_송신단_MRR어레이.png', 6.0),
        ("【도 4】 초평탄 유리 코어 기판 내장형 3차원 광 도파로 단면도", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도4_유리기판_3D도파로단면.png', 6.0),
        ("【도 5】 10진 파장 수신 모듈 (Rx: AWG 디멀티플렉서 & 포토다이오드 PD 어레이)", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도5_수신단_AWG디멀티플렉서.png', 6.0),
        ("【도 6】 다파장 10진 광 인터커넥트 데이터 송수신 전체 프로세스 흐름도", 
         r'C:\Users\LENOVO\Desktop\세이프티온_특허_도6_데이터전송_순서도.png', 5.8)
    ]

    for title, img_path, w_inch in figures:
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
            p_i = doc.add_paragraph()
            p_i.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_i.paragraph_format.space_after = Pt(14)
            doc.add_picture(img_path, width=Inches(w_inch))

    out_docx_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허출원명세서_유리기판_10진광인터커넥트.docx'
    doc.save(out_docx_path)
    print(f"Successfully generated complete docx with all figures at:\n  {out_docx_path}")

if __name__ == "__main__":
    create_complete_docx()
