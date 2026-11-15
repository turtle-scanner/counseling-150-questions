# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=True):
    font_names = [
        "malgunbd.ttf" if bold else "malgun.ttf",
        "gulim.ttc",
        "arialbd.ttf" if bold else "arial.ttf"
    ]
    for fn in font_names:
        p = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", fn)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def create_patent2_figure1():
    # 도 1: 저항 색띠형 6색 부동소수점 광 파장 매핑 표준 규격도
    W, H = 1920, 1080
    canvas = np.zeros((H, W, 3), dtype=np.uint8)

    # Dark blue-slate gradient
    top_c = np.array([28, 22, 16], dtype=np.float32)
    bot_c = np.array([14, 10, 8], dtype=np.float32)
    for y in range(H):
        alpha = y / H
        canvas[y, :] = ((1.0 - alpha) * top_c + alpha * bot_c).astype(np.uint8)

    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img, "RGBA")

    font_title = get_font(32, bold=True)
    font_sub_title = get_font(19, bold=False)
    font_sec = get_font(22, bold=True)
    font_badge = get_font(20, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)

    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)
    GREEN = (0, 230, 118)

    # Header
    draw.rounded_rectangle([60, 40, 1860, 130], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((90, 52), "【도 1】 저항 색띠형 6색 부동소수점 다파장 광 압축 매핑 표준 규격도", font=font_title, fill=WHITE)
    draw.text((92, 95), "Scientific Resistor-Color-Code Floating-Point 6-Band Optical Interconnect Protocol", font=font_sub_title, fill=GOLD)

    # Resistor Visualization Banner in center-top
    draw.rounded_rectangle([60, 150, 1860, 280], radius=10, fill=DARKER_CARD, outline=BORDER_CYAN, width=1)
    draw.text((85, 165), "■ 저항 색띠 부동소수점 광 링크 예시: [ + 2265 × 10¹ = +22,650 ] ➔ 단 1클럭 1펄스 전송!", font=font_sec, fill=CYAN)

    # 6 Color bands visualization
    band_x_start = 120
    band_spacing = 280
    bands_info = [
        ("제1 띠: 부호 (Sign)", "자외선: + (양수)\n적외선: - (음수)", (140, 70, 255), "λ_sign (+ / -)"),
        ("제2 띠: 유효숫자 1 (10³)", "빨강 = 2", (255, 50, 50), "λ2 (2000)"),
        ("제3 띠: 유효숫자 2 (10²)", "빨강 = 2", (255, 50, 50), "λ2 (200)"),
        ("제4 띠: 유효숫자 3 (10¹)", "파랑 = 6", (0, 150, 255), "λ6 (60)"),
        ("제5 띠: 유효숫자 4 (10⁰)", "노랑 = 5", (255, 225, 0), "λ5 (5)"),
        ("제6 띠: 지수 승수 (10ᴺ)", "갈색 = ×10¹ (승수)\n*파랑=×10⁶, 금=×10⁻¹", (160, 90, 45), "λ1 (×10¹)")
    ]

    for i, (b_title, b_sub, b_col, b_wl) in enumerate(bands_info):
        bx = band_x_start + i * band_spacing
        by = 205
        # Band Pill
        draw.rounded_rectangle([bx, by, bx + 240, by + 60], radius=8, fill=(20, 35, 50), outline=b_col, width=2)
        draw.rounded_rectangle([bx + 8, by + 8, bx + 45, by + 52], radius=4, fill=b_col)
        draw.text((bx + 55, by + 10), b_title, font=font_lbl, fill=WHITE)
        draw.text((bx + 55, by + 34), b_wl, font=font_code, fill=b_col)

    # 3 Detailed Table Columns: [Left: 유효숫자 0~9], [Center: 승수 Multiplier 10^-2 ~ 10^9], [Right: 핵심 보완 4대 기술]
    col_y = 310

    # 1. Left Table: 10대 기본 유효숫자 색상 (λ0 ~ λ9)
    draw.rounded_rectangle([60, col_y, 620, 1030], radius=10, fill=DARK_CARD, outline=BORDER_CYAN, width=1)
    draw.text((85, 330), "① 유효숫자 10대 색상 매핑 (0~9)", font=font_sec, fill=CYAN)
    
    digits = [
        ("0번", "검정", "λ0 (1270nm)", "능동 영(Active-Zero) 펄스", (60, 60, 60)),
        ("1번", "갈색", "λ1 (1290nm)", "기본 데이터 파장", (160, 90, 45)),
        ("2번", "빨강", "λ2 (1310nm)", "기본 데이터 파장", (255, 50, 50)),
        ("3번", "주황", "λ3 (1330nm)", "기본 데이터 파장", (255, 140, 0)),
        ("4번", "노랑", "λ4 (1350nm)", "기본 데이터 파장", (255, 225, 0)),
        ("5번", "초록", "λ5 (1370nm)", "기본 데이터 파장", (0, 230, 100)),
        ("6번", "파랑", "λ6 (1390nm)", "기본 데이터 파장", (0, 150, 255)),
        ("7번", "보라", "λ7 (1410nm)", "기본 데이터 파장", (180, 70, 255)),
        ("8번", "회색", "λ8 (1430nm)", "기본 데이터 파장", (180, 180, 180)),
        ("9번", "흰색", "λ9 (1450nm)", "기본 데이터 파장", (255, 255, 255))
    ]
    dy = 380
    for d_num, d_name, d_wl, d_note, d_rgb in digits:
        draw.rounded_rectangle([85, dy, 595, dy + 52], radius=6, fill=(15, 28, 42), outline=(40, 70, 100), width=1)
        draw.rectangle([95, dy + 10, 125, dy + 42], fill=d_rgb)
        draw.text((140, dy + 15), f"{d_num} [{d_name}]", font=font_lbl, fill=WHITE)
        draw.text((260, dy + 16), d_wl, font=font_code, fill=CYAN)
        draw.text((410, dy + 18), d_note, font=font_txt, fill=(180, 200, 220))
        dy += 62

    # 2. Center Table: 지수 승수(Multiplier) 매핑 (10^-2 ~ 10^+9)
    draw.rounded_rectangle([650, col_y, 1250, 1030], radius=10, fill=DARK_CARD, outline=BORDER_GOLD, width=1)
    draw.text((675, 330), "② 지수 승수(Multiplier) 매핑 체계", font=font_sec, fill=GOLD)

    multipliers = [
        ("은색 (Silver)", "× 10⁻² (0.01)", "λ_silv (1230nm)", "극미세 AI 가중치 소수점", (192, 192, 192)),
        ("금색 (Gold)", "× 10⁻¹ (0.1)", "λ_gold (1250nm)", "미세 가중치 소수점", (255, 215, 0)),
        ("검정 (Black)", "× 10⁰ (1배)", "λ0 (1270nm)", "정수 그대로 복원 (×1)", (80, 80, 80)),
        ("갈색 (Brown)", "× 10¹ (10배)", "λ1 (1290nm)", "십 단위 승산", (160, 90, 45)),
        ("빨강 (Red)", "× 10² (100배)", "λ2 (1310nm)", "백 단위 승산", (255, 50, 50)),
        ("주황 (Orange)", "× 10³ (1천배)", "λ3 (1330nm)", "킬로(k) 단위 승산", (255, 140, 0)),
        ("노랑 (Yellow)", "× 10⁴ (1만배)", "λ4 (1350nm)", "만 단위 승산", (255, 225, 0)),
        ("초록 (Green)", "× 10⁵ (10만배)", "λ5 (1370nm)", "십만 단위 승산", (0, 230, 100)),
        ("파랑 (Blue)", "× 10⁶ (100만배)", "λ6 (1390nm)", "메가(M) 단위 승산", (0, 150, 255)),
        ("흰색 (White)", "× 10⁹ (10억배)", "λ9 (1450nm)", "기가(G) 거대 스케일", (255, 255, 255))
    ]
    my = 380
    for m_col, m_val, m_wl, m_desc, m_rgb in multipliers:
        draw.rounded_rectangle([675, my, 1225, my + 52], radius=6, fill=(15, 28, 42), outline=(70, 60, 30), width=1)
        draw.rectangle([685, my + 10, 715, my + 42], fill=m_rgb)
        draw.text((730, my + 15), m_col, font=font_lbl, fill=WHITE)
        draw.text((880, my + 15), m_val, font=font_sec, fill=GOLD)
        draw.text((1040, my + 18), m_desc, font=font_txt, fill=(220, 220, 180))
        my += 62

    # 3. Right Column: 핵심 보완 4대 기술 카드
    draw.rounded_rectangle([1280, col_y, 1860, 1030], radius=10, fill=DARK_CARD, outline=GREEN, width=1)
    draw.text((1305, 330), "③ 특허 무결점 4대 핵심 보완 기술", font=font_sec, fill=GREEN)

    techs = [
        ("1. 물리적 $10ᴺ$ 즉시 게인 승산", 
         "승수 파장이 포토다이오드 증폭기 게인 단자에\n직접 인가되어, 광전 변환 순간 물리적으로\n$10^N$배 증폭 출력 (연산 딜레이 0초)", GREEN),
        ("2. 자가 온도 보상 (Athermal) 도파로", 
         "음의 열광학 계수(-dn/dT) 하이브리드 코팅으로\n칩 온도가 0℃~100℃로 상승해도 파장 간격\n0.001nm 무변형 영구 유지", (100, 200, 255)),
        ("3. 3차원 입체 복층 광 도로망 (3D DLW)", 
         "유리 기판 두께(100~500㎛)를 활용하여\n1층, 2층, 3층 나선형 복층으로 도파로를 매립,\n단일 패키지 내 수백 가닥 무간섭 병렬 전송", GOLD),
        ("4. 광학적 동적 셔플링 암호화 (ECC)", 
         "전자기 도청(EMI) 원천 차단 및 매 클럭마다\n파장 순서를 키 값으로 뒤섞어 하드웨어 해킹\n원천 방지 + 자가 오류 정정 부호 결합", (255, 120, 180))
    ]
    ty = 380
    for t_tit, t_desc, t_col in techs:
        draw.rounded_rectangle([1305, ty, 1835, ty + 140], radius=8, fill=DARKER_CARD, outline=t_col, width=1)
        draw.text((1325, ty + 14), t_tit, font=font_lbl, fill=t_col)
        draw.text((1325, ty + 46), t_desc, font=font_txt, fill=(210, 220, 230))
        ty += 155

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도1_저항색띠_부동소수점_매핑도.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 1 saved to: {out_p}")

def create_patent2_figure2():
    # 도 2: 저항 색띠형 부동소수점 광 인터커넥트 하드웨어 아키텍처 및 물리적 즉시 승산 시스템
    W, H = 1920, 1080
    canvas = np.zeros((H, W, 3), dtype=np.uint8)

    top_c = np.array([28, 22, 16], dtype=np.float32)
    bot_c = np.array([14, 10, 8], dtype=np.float32)
    for y in range(H):
        alpha = y / H
        canvas[y, :] = ((1.0 - alpha) * top_c + alpha * bot_c).astype(np.uint8)

    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img, "RGBA")

    font_title = get_font(32, bold=True)
    font_sub_title = get_font(19, bold=False)
    font_sec = get_font(22, bold=True)
    font_badge = get_font(20, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)

    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)
    GREEN = (0, 230, 118)

    # Header
    draw.rounded_rectangle([60, 40, 1860, 130], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((90, 52), "【도 2】 저항 색띠형 부동소수점 광 인터커넥트 하드웨어 및 물리적 즉시 승산(Gain) 시스템", font=font_title, fill=WHITE)
    draw.text((92, 95), "Hardware Architecture of Resistor-Code Floating-Point Interconnect with Instant Optical Gain Multiplier", font=font_sub_title, fill=CYAN)

    # Flow Box 1: [송신단 GPU / 10진 파장 인코더 (500)]
    draw.rounded_rectangle([60, 170, 520, 850], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    # Badge 500
    draw.rounded_rectangle([80, 190, 150, 225], radius=6, fill=CYAN)
    draw.text((90, 195), "500", font=font_badge, fill=(10, 10, 10))
    draw.text((165, 195), "부동소수점 송신 모듈 (Tx)", font=font_sec, fill=WHITE)

    tx_items = [
        ("부동소수점 데이터 입력", "(예: + 2265 × 10¹)", CYAN),
        ("510: 유효숫자-지수 분할기", "• 유효숫자: 2 2 6 5 분리\n• 지수 승수: 10¹ (갈색) 분리\n• 부호: + (자외선) 분리", WHITE),
        ("520: 마이크로 콤 광원", "초정밀 등간격 다파장 레이저", GOLD),
        ("530: 6채널 MRR 광변조기 어레이", "각 띠별 파장(λ_sign, λ2, λ2, λ6, λ5, λ_exp)을\n단 1클럭 내에 동시 변조하여 방출", (220, 220, 180))
    ]
    ty = 260
    for tit, sub, col in tx_items:
        draw.rounded_rectangle([80, ty, 500, ty + 120], radius=8, fill=DARKER_CARD, outline=(40, 70, 100), width=1)
        draw.text((95, ty + 12), tit, font=font_lbl, fill=col)
        draw.text((95, ty + 42), sub, font=font_txt, fill=(180, 200, 220))
        ty += 140

    # Flow Box 2: [유리 코어 기판 & 3D 광 도파로 (600)]
    draw.rounded_rectangle([560, 170, 1260, 850], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    # Badge 600
    draw.rounded_rectangle([580, 190, 650, 225], radius=6, fill=GOLD)
    draw.text((590, 195), "600", font=font_badge, fill=(10, 10, 10))
    draw.text((665, 195), "초평탄 유리 코어 기판 (Glass Core Substrate)", font=font_sec, fill=WHITE)

    # 3D Optical Waveguide with glowing 6-color rainbow beam inside
    draw.rounded_rectangle([590, 260, 1230, 480], radius=10, fill=(12, 20, 32), outline=BORDER_GOLD, width=1)
    draw.text((610, 275), "610: 3차원 자가 온도 보상(Athermal) 내장 광 도파로", font=font_lbl, fill=GOLD)
    draw.text((610, 305), "• 6색 펄스 동시 도파 (빛의 속도 300,000 km/s 직결)\n• 음의 열광학(-dn/dT) 코팅으로 85℃ 고열에도 파장 무간섭 유지", font=font_txt, fill=(200, 230, 250))

    # Draw rainbow pulse beam
    beam_colors = [(140, 70, 255), (255, 50, 50), (255, 50, 50), (0, 150, 255), (255, 225, 0), (160, 90, 45)]
    beam_names = ["λ_sign (+)", "λ2 (2)", "λ2 (2)", "λ6 (6)", "λ5 (5)", "λ_exp (×10¹)"]
    by = 380
    for idx, (b_col, b_nm) in enumerate(zip(beam_colors, beam_names)):
        draw.line([(620, by + idx * 14), (1200, by + idx * 14)], fill=b_col, width=4)
        draw.text((630 + idx * 95, by + 90), b_nm, font=font_code, fill=b_col)

    # Box 2 Lower: 620 AWG Prism demultiplexer
    draw.rounded_rectangle([590, 510, 1230, 820], radius=10, fill=DARKER_CARD, outline=CYAN, width=1)
    draw.text((610, 525), "620: 고분해능 AWG 광학 분광기 (Optical De-multiplexer)", font=font_lbl, fill=CYAN)
    draw.text((610, 555), "단일 유리 도파로로 진입한 6색 펄스를 각 채널별로 100% 무손실 물리적 분기", font=font_txt, fill=(180, 220, 240))

    # Demux branching lines
    for i, col in enumerate(beam_colors):
        py = 620 + i * 30
        draw.line([(630, 590), (750, py), (1210, py)], fill=col, width=3)
        draw.ellipse([1207, py - 3, 1213, py + 3], fill=WHITE)

    # Flow Box 3: [수신단 디코더 & 물리적 즉시 승산기 (700)]
    draw.rounded_rectangle([1300, 170, 1860, 850], radius=12, fill=DARK_CARD, outline=GREEN, width=2)
    # Badge 700
    draw.rounded_rectangle([1320, 190, 1390, 225], radius=6, fill=GREEN)
    draw.text((1330, 195), "700", font=font_badge, fill=(10, 10, 10))
    draw.text((1405, 195), "수신 및 물리적 즉시 승산 모듈", font=font_sec, fill=WHITE)

    rx_items = [
        ("710: 초고속 포토다이오드 어레이", "유효숫자 파장(2265) 광전 변환", WHITE),
        ("720: 광학 제어 게인 승산기(Gain Multiplier)", "★ 핵심: 지수 파장(λ_exp)이 증폭기 전압을 직접 제어하여\n광전 변환 순간 물리적으로 10¹배 즉시 뻥튀기 출력!", GOLD),
        ("730: 부호 및 소수점 정렬기", "+ 부호 부여 및 최종 부동소수점 데이터 복원", CYAN),
        ("HBM4 / GPU 연산 코어로 직결", "결과: +22,650 단 1클럭 내 완성!", GREEN)
    ]
    ry = 260
    for tit, sub, col in rx_items:
        draw.rounded_rectangle([1320, ry, 1840, ry + 120], radius=8, fill=DARKER_CARD, outline=(30, 70, 50), width=1)
        draw.text((1335, ry + 12), tit, font=font_lbl, fill=col)
        draw.text((1335, ry + 42), sub, font=font_txt, fill=(200, 220, 210))
        ry += 140

    # Bottom Master Status Card
    draw.rounded_rectangle([60, 880, 1860, 1030], radius=10, fill=DARK_CARD, outline=BORDER_GOLD, width=1)
    summary_txt = (
        "【핵심 기술 총결집】 저항 색띠(유효숫자 + 10ᴺ 승수) ➔ 1클럭 동시 펄스 방출 ➔ 자가 온도 보상(Athermal) 유리 도파로 전파 ➔ "
        "AWG 광학 분광 ➔ 지수 파장이 증폭기 게인을 직접 물리적으로 제어하여 단 1클럭 만에 거대 부동소수점 복원 및 전송 완료!"
    )
    draw.text((85, 895), "■ 주식회사 세이프티온 (SAFETYON) ┃ 저항 색띠형 10진 지수 부동소수점 광 인터커넥트 시스템", font=font_sec, fill=GOLD)
    draw.text((85, 935), summary_txt, font=font_lbl, fill=(220, 240, 255))

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도2_하드웨어_아키텍처.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 2 saved to: {out_p}")

if __name__ == "__main__":
    create_patent2_figure1()
    create_patent2_figure2()
