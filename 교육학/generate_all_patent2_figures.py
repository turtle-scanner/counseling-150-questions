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

def create_base_canvas(title_ko, title_en, fig_no):
    W, H = 1920, 1080
    canvas = np.zeros((H, W, 3), dtype=np.uint8)
    top_c = np.array([28, 22, 16], dtype=np.float32)
    bot_c = np.array([14, 10, 8], dtype=np.float32)
    for y in range(H):
        alpha = y / H
        canvas[y, :] = ((1.0 - alpha) * top_c + alpha * bot_c).astype(np.uint8)

    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img, "RGBA")

    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    BORDER_CYAN = (0, 180, 220, 255)

    font_title = get_font(32, bold=True)
    font_sub_title = get_font(19, bold=False)

    draw.rounded_rectangle([60, 40, 1860, 130], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((90, 52), f"【도 {fig_no}】 {title_ko}", font=font_title, fill=WHITE)
    draw.text((92, 95), title_en, font=font_sub_title, fill=CYAN)

    return pil_img, draw

# 도 3: 송신단 유효숫자-지수 분할기 및 6채널 MRR 광변조기 송신 모듈 상세 구조도
def create_figure3():
    pil_img, draw = create_base_canvas(
        "부동소수점 송신 모듈(500)의 유효숫자-지수 분할기 및 6채널 MRR 광변조기 상세 구조도",
        "Significand-Exponent Splitter and 6-Channel Micro-Ring Resonator Transmitter Architecture",
        3
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_GOLD = (255, 190, 40, 255)
    BORDER_CYAN = (0, 180, 220, 255)
    GREEN = (0, 230, 118)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)
    font_badge = get_font(20, bold=True)

    # 1. Left Input Block: GPU/NPU Data In
    draw.rounded_rectangle([60, 170, 440, 850], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((85, 195), "510: 유효숫자-지수 분할기", font=font_sec, fill=CYAN)
    draw.text((85, 230), "GPU/NPU 부동소수점 데이터 입력", font=font_lbl, fill=WHITE)

    sample_box_y = 280
    draw.rounded_rectangle([85, sample_box_y, 415, sample_box_y + 110], radius=8, fill=DARKER_CARD, outline=GOLD, width=1)
    draw.text((105, sample_box_y + 15), "입력 데이터 샘플: + 22650", font=font_lbl, fill=GOLD)
    draw.text((105, sample_box_y + 45), "➔ 부호: [ + ] (양수)\n➔ 유효숫자: [ 2 2 6 5 ] (4자리)\n➔ 지수 승수: [ × 10¹ ] (갈색)", font=font_txt, fill=WHITE)

    split_items = [
        ("채널 1 (부호)", "λ_sign (자외선/적외선)", (140, 70, 255)),
        ("채널 2 (천단위)", "λ2 (빨강: 2)", (255, 50, 50)),
        ("채널 3 (백단위)", "λ2 (빨강: 2)", (255, 50, 50)),
        ("채널 4 (십단위)", "λ6 (파랑: 6)", (0, 150, 255)),
        ("채널 5 (일단위)", "λ5 (노랑: 5)", (255, 225, 0)),
        ("채널 6 (지수)", "λ_exp (갈색: 10¹)", (160, 90, 45))
    ]
    sy = 420
    for ch_name, ch_val, ch_col in split_items:
        draw.rounded_rectangle([85, sy, 415, sy + 58], radius=6, fill=DARKER_CARD, outline=ch_col, width=1)
        draw.rectangle([95, sy + 12, 120, sy + 46], fill=ch_col)
        draw.text((135, sy + 10), ch_name, font=font_lbl, fill=WHITE)
        draw.text((135, sy + 32), ch_val, font=font_code, fill=ch_col)
        sy += 70

    # 2. Center Block: 520 Micro-comb laser & 530 6-Channel MRR Array
    draw.rounded_rectangle([480, 170, 1380, 850], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    # Badge 530
    draw.rounded_rectangle([505, 190, 575, 225], radius=6, fill=GOLD)
    draw.text((515, 195), "530", font=font_badge, fill=(10, 10, 10))
    draw.text((590, 195), "6채널 마이크로 링 공진기 (MRR) 광변조기 어레이", font=font_sec, fill=WHITE)

    # Laser Source (520)
    draw.rounded_rectangle([510, 260, 780, 360], radius=8, fill=DARKER_CARD, outline=CYAN, width=1)
    draw.text((530, 275), "520: 마이크로 주파수 콤 광원", font=font_lbl, fill=CYAN)
    draw.text((530, 305), "• 초등간격 다파장 레이저 동시 공급\n• 고안정성 기준 주파수 빗(Comb)", font=font_txt, fill=(200, 220, 240))

    # Bus waveguide connecting laser through MRR rings
    bus_y = 520
    draw.line([(780, 310), (840, 310), (840, bus_y), (1350, bus_y)], fill=WHITE, width=4)
    draw.text((860, bus_y - 25), "마스터 광 버스 도파로 (Master Optical Bus)", font=font_lbl, fill=WHITE)

    # 6 MRR Rings
    ring_x_start = 900
    ring_spacing = 75
    for i, (ch_name, ch_val, ch_col) in enumerate(split_items):
        rx = ring_x_start + i * ring_spacing
        ry = bus_y + 45
        # Ring circle
        draw.ellipse([rx - 25, ry - 25, rx + 25, ry + 25], outline=ch_col, width=4)
        draw.text((rx - 15, ry - 10), f"R{i+1}", font=font_code, fill=ch_col)
        # Drop line from Splitter to Ring (electrical modulation wire)
        draw.line([(415, 450 + i * 70), (rx, ry + 30)], fill=ch_col, width=2)
        draw.ellipse([rx - 4, ry + 26, rx + 4, ry + 34], fill=WHITE)

    draw.text((880, 720), "■ 개별 마이크로 링 공진기(MRR)의 전압 인가에 따른 1클럭 동시 파장 변조", font=font_lbl, fill=GOLD)
    draw.text((880, 755), "• 6개 파장이 간섭 없이 단 1개의 버스 도파로에 1클럭 펄스로 다중화(WDM) 합성", font=font_txt, fill=(220, 230, 250))

    # 3. Right Output: Multiplexed Output to Glass Substrate (600)
    draw.rounded_rectangle([1420, 170, 1860, 850], radius=12, fill=DARK_CARD, outline=GREEN, width=2)
    draw.text((1445, 195), "600: 유리 기판 도파로 연결단", font=font_sec, fill=GREEN)

    draw.line([(1350, bus_y), (1440, bus_y)], fill=WHITE, width=6)
    # Output rainbow beam bundle
    for i, (_, _, ch_col) in enumerate(split_items):
        draw.line([(1440, bus_y + (i - 2.5) * 6), (1830, bus_y + (i - 2.5) * 6)], fill=ch_col, width=3)

    draw.rounded_rectangle([1445, 620, 1835, 810], radius=8, fill=DARKER_CARD, outline=GREEN, width=1)
    draw.text((1465, 640), "단일 광 도파로 동시 방출", font=font_lbl, fill=GREEN)
    draw.text((1465, 675), "• 6색 복합 펄스 동시 도파\n• 지연 시간 0.0001ns 미만\n• 2진수 대비 대역폭 10배 폭증\n• 고주파 스위칭 발열 80% 절감", font=font_txt, fill=WHITE)

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도3_송신단_MRR어레이.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 3 saved: {out_p}")

# 도 4: 초평탄 유리 코어 기판 내 자가 온도 보상(Athermal) 3차원 다층 나선형 도파로 단면도
def create_figure4():
    pil_img, draw = create_base_canvas(
        "초평탄 유리 코어 기판(600) 내 자가 온도 보상(Athermal) 3차원 입체 도파로 단면도",
        "Cross-Sectional View of 3D Athermal Waveguide and Multilayer Optical Routing Network",
        4
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_GOLD = (255, 190, 40, 255)
    BORDER_CYAN = (0, 180, 220, 255)
    GREEN = (0, 230, 118)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)

    # Left: Athermal Single Waveguide Detail
    draw.rounded_rectangle([60, 170, 920, 850], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((85, 195), "610: 자가 온도 보상 (Athermal) 도파로 코어 단면", font=font_sec, fill=CYAN)

    # Draw Glass Core Block
    draw.rounded_rectangle([120, 260, 860, 680], radius=16, fill=(18, 32, 50), outline=(0, 150, 220), width=2)
    draw.text((140, 280), "초평탄 유리 코어층 (Glass Core: n = 1.52, 두께 300㎛)", font=font_lbl, fill=WHITE)

    # Waveguide Core & Cladding
    cx, cy = 490, 470
    # Negative dn/dT Cladding ring
    draw.ellipse([cx - 140, cy - 140, cx + 140, cy + 140], fill=(30, 70, 90), outline=GOLD, width=3)
    draw.text((cx - 120, cy - 165), "음의 열광학(-dn/dT) 하이브리드 클래딩층", font=font_lbl, fill=GOLD)

    # Core
    draw.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], fill=(0, 229, 255, 220), outline=WHITE, width=2)
    draw.text((cx - 35, cy - 10), "광 코어\n(Core)", font=font_lbl, fill=(10, 10, 10))

    # Formula Card at bottom
    draw.rounded_rectangle([120, 710, 860, 820], radius=8, fill=DARKER_CARD, outline=BORDER_CYAN, width=1)
    draw.text((140, 725), "온도 보상 원리: dλ/dT = (λ/n) · (dn/dT_core + dn/dT_clad) ≈ 0", font=font_code, fill=CYAN)
    draw.text((140, 760), "• 칩 온도 0℃ ➔ 100℃ 상승 시 유리의 양(+)의 굴절률 변화를 클래딩의 음(-)의\n  열광학 효과로 완전 상쇄하여 중심 파장 드리프트 0.005nm 이하 영구 고정!", font=font_txt, fill=(210, 230, 250))

    # Right: Multilayer 3D Helix Routing Network
    draw.rounded_rectangle([960, 170, 1860, 850], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((985, 195), "3차원 입체 복층 광 도로망 (3D Multilayer Optical Network)", font=font_sec, fill=GOLD)

    # 3 Layers in Glass
    layer_names = ["상층 광 도파로층 (Layer 3)", "중간 광 도파로층 (Layer 2)", "하층 광 도파로층 (Layer 1)"]
    ly_start = 280
    for idx, l_name in enumerate(layer_names):
        ly = ly_start + idx * 160
        draw.rounded_rectangle([1000, ly, 1820, ly + 130], radius=10, fill=DARKER_CARD, outline=(60, 90, 120), width=1)
        draw.text((1020, ly + 15), l_name, font=font_lbl, fill=WHITE)
        
        # Parallel waveguides inside each layer
        for w_idx in range(6):
            wx = 1040 + w_idx * 125
            draw.line([(wx, ly + 65), (wx + 90, ly + 65)], fill=CYAN if idx % 2 == 0 else GOLD, width=4)
            draw.ellipse([wx + 40, ly + 60, wx + 50, ly + 70], fill=WHITE)
        draw.text((1020, ly + 95), "수백 가닥의 무지개 광 도로가 위아래로 무간섭 교차 전송!", font=font_txt, fill=(180, 200, 220))

    draw.rounded_rectangle([1000, 770, 1820, 830], radius=6, fill=(15, 30, 45), outline=GREEN, width=1)
    draw.text((1020, 790), "■ 초평탄 유리 기판(CTE 3~8 ppm/K) 적용으로 대면적 패키지 휨 변형(Warpage) 영구 억제", font=font_lbl, fill=GREEN)

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도4_유리기판_3D도파로단면.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 4 saved: {out_p}")

# 도 5: 수신단 AWG 광학 분광기 및 포토다이오드 게인 단자 직결 물리적 10^N 아날로그 승산 회로도
def create_figure5():
    pil_img, draw = create_base_canvas(
        "수신단 AWG 광학 분광기 및 포토다이오드 게인 단자 직결 물리적 10ᴺ 아날로그 승산 회로도",
        "Optical De-multiplexer & Instant Analog Hardware Gain Multiplier Architecture",
        5
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_GOLD = (255, 190, 40, 255)
    BORDER_CYAN = (0, 180, 220, 255)
    GREEN = (0, 230, 118)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)

    # Left: 620 AWG Prism demultiplexer
    draw.rounded_rectangle([60, 170, 680, 850], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((85, 195), "620: AWG 광학 파장 분광기", font=font_sec, fill=CYAN)
    draw.text((85, 230), "6색 복합 펄스를 무손실 파장별 분기", font=font_lbl, fill=WHITE)

    # AWG Prism Graphic
    draw.polygon([(120, 480), (350, 320), (350, 680), (120, 520)], fill=(20, 50, 90), outline=CYAN, width=2)
    draw.text((170, 490), "AWG 분광기\n(Prism)", font=font_lbl, fill=WHITE)

    out_branches = [
        ("λ_sign (+)", (140, 70, 255), 340),
        ("λ2 (2: 천)", (255, 50, 50), 400),
        ("λ2 (2: 백)", (255, 50, 50), 460),
        ("λ6 (6: 십)", (0, 150, 255), 520),
        ("λ5 (5: 일)", (255, 225, 0), 580),
        ("λ_exp (10¹: 갈)", (160, 90, 45), 650)
    ]
    for b_nm, b_col, b_y in out_branches:
        draw.line([(350, 500), (450, b_y), (650, b_y)], fill=b_col, width=3)
        draw.text((470, b_y - 20), b_nm, font=font_code, fill=b_col)

    # Right: 700 Instant Analog Gain Multiplier Circuit
    draw.rounded_rectangle([720, 170, 1860, 850], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((745, 195), "700: 수신 및 물리적 즉시 승산(Gain) 하드웨어 시스템", font=font_sec, fill=GOLD)

    # 1. PD Array for Significand
    draw.rounded_rectangle([750, 270, 1150, 630], radius=10, fill=DARKER_CARD, outline=CYAN, width=1)
    draw.text((770, 285), "710: 초고속 포토다이오드 (PD) 어레이", font=font_lbl, fill=CYAN)
    draw.text((770, 315), "유효숫자 파장 입사 ➔ 광전 변환 전기 신호(2265) 생성", font=font_txt, fill=WHITE)

    for i in range(4):
        pdy = 370 + i * 55
        draw.rounded_rectangle([770, pdy, 1120, pdy + 45], radius=6, fill=(15, 30, 45), outline=(0, 180, 220), width=1)
        draw.text((785, pdy + 12), f"PD {i+1} : 유효숫자 채널 ➔ 전류 신호(I_{i+1})", font=font_code, fill=WHITE)

    # 2. Crucial Gain Multiplier (720)
    draw.rounded_rectangle([1220, 270, 1820, 630], radius=10, fill=DARKER_CARD, outline=BORDER_GOLD, width=2)
    draw.text((1240, 285), "720: 가변 이득 증폭기 (VGA) & 물리적 게인 승산기", font=font_sec, fill=GOLD)
    draw.text((1240, 320), "★ 핵심 메커니즘: 소프트웨어 디코딩 회로 완전 배제!", font=font_lbl, fill=GREEN)

    # Draw connection from λ_exp to Gain terminal
    draw.line([(650, 650), (1240, 650), (1240, 480)], fill=(160, 90, 45), width=4)
    draw.text((1255, 610), "지수 파장(λ_exp) 광전류 ➔ VGA 게인 단자 직결!", font=font_lbl, fill=GOLD)

    # Amplifier Triangle Icon
    tri_pts = [(1350, 400), (1480, 460), (1350, 520)]
    draw.polygon(tri_pts, fill=(40, 30, 15), outline=GOLD, width=3)
    draw.text((1365, 445), "× 10ᴺ", font=font_sec, fill=GOLD)

    # Gain Output
    draw.line([(1480, 460), (1780, 460)], fill=GREEN, width=4)
    draw.text((1520, 425), "물리적 즉시 승산 출력", font=font_lbl, fill=GREEN)
    draw.text((1520, 475), "출력값: 2265 × 10¹ = 22,650", font=font_sec, fill=WHITE)

    # Status Card
    draw.rounded_rectangle([750, 670, 1820, 820], radius=8, fill=(10, 20, 32), outline=GREEN, width=1)
    draw.text((770, 690), "■ 수신단 지연 시간(Latency) 혁신: 사실상 0.00000초 달성!", font=font_lbl, fill=GREEN)
    draw.text((770, 725), "• 기존: 2진수 비트 수신 ➔ 시프트 레지스터 ➔ ALU 부동소수점 정규화 ➔ 수십 클럭 소요\n• 본 발명: 빛이 센서에 닿는 찰나에 증폭기 이득(Gain)이 물리적으로 10^N배로 뻥튀기되어 즉시 출력!", font=font_txt, fill=(220, 240, 255))

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도5_수신단_물리적승산회로.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 5 saved: {out_p}")

# 도 6: 저항 색띠형 부동소수점 데이터 압축 전송 전체 프로세스 흐름 순서도 (Flowchart)
def create_figure6():
    pil_img, draw = create_base_canvas(
        "저항 색띠형 부동소수점 광 데이터 압축 전송 전체 프로세스 흐름 순서도",
        "End-to-End Operational Flowchart of Compressive Optical Floating-Point Interconnect",
        6
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_GOLD = (255, 190, 40, 255)
    BORDER_CYAN = (0, 180, 220, 255)
    GREEN = (0, 230, 118)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)

    flow_steps = [
        ("S100: 부동소수점 데이터 입력 및 저항 색띠 분할",
         "연산 칩렛(GPU/NPU)으로부터 부동소수점 실수 데이터를 입력받아,\n부호(Sign), 유효숫자(Significand 4자리), 및 10진 지수 승수(10^N)로 분할", CYAN),
        ("S200: 6색 독립 고유 파장 1:1 매핑 변조",
         "부호(λ_sign), 유효숫자(검0~흰9 ➔ λ0~λ9), 및 지수 승수(은10^-2~흰10^9 ➔ λ_exp)로\n1:1 매핑하고 6채널 MRR 광변조기를 통해 단 1클럭 펄스로 동시 변조", (100, 200, 255)),
        ("S300: 자가 온도 보상형 유리 기판 3D 도파로 광속 도파",
         "유리 코어 기판 내부의 3차원 도파로를 통해 6색 복합 펄스가 무간섭 광속(30만 km/s)으로 도파되며,\n음의 열광학 코팅(-dn/dT)으로 고열 환경에서도 파장 무변형 유지", GOLD),
        ("S400: AWG 광학 분광기를 통한 무손실 파장 분기",
         "수신측 고분해능 AWG(프리즘)를 통해 6색 펄스가 각각의 고유 파장별로\n100% 무손실 물리적 공간 분기", (255, 150, 80)),
        ("S500: 지수 파장의 물리적 게인 제어 아날로그 즉시 승산",
         "지수 파장(λ_exp)의 광전류가 가변 이득 증폭기(VGA) 게인 단자에 직접 인가되어,\n유효숫자 신호를 물리적 하드웨어 법칙에 의해 단 1클럭 내에 10^N배 즉시 증폭 복원", GREEN),
        ("S600: 최종 부동소수점 데이터 메모리(HBM4) 직결 저장",
         "복원된 고정밀 부동소수점 데이터가 초저지연(Zero-Latency)으로 HBM4 메모리로 직결 입력 완료", WHITE)
    ]

    sy = 170
    box_w = 1200
    box_h = 100
    start_x = 360

    for i, (s_tit, s_desc, s_col) in enumerate(flow_steps):
        # Step Card
        draw.rounded_rectangle([start_x, sy, start_x + box_w, sy + box_h], radius=10, fill=DARK_CARD, outline=s_col, width=2)
        # Step Badge
        draw.rounded_rectangle([start_x + 15, sy + 15, start_x + 95, sy + 50], radius=6, fill=s_col)
        draw.text((start_x + 22, sy + 20), f"단계 {i+1}", font=font_lbl, fill=(10, 10, 10))
        draw.text((start_x + 115, sy + 20), s_tit, font=font_lbl, fill=WHITE)
        draw.text((start_x + 115, sy + 52), s_desc, font=font_txt, fill=(200, 220, 240))

        # Down arrow between steps
        if i < len(flow_steps) - 1:
            arrow_y = sy + box_h
            draw.line([(start_x + box_w // 2, arrow_y), (start_x + box_w // 2, arrow_y + 35)], fill=GOLD, width=3)
            draw.polygon([(start_x + box_w // 2 - 8, arrow_y + 25), (start_x + box_w // 2 + 8, arrow_y + 25), (start_x + box_w // 2, arrow_y + 35)], fill=GOLD)
        sy += 138

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허2탄_도6_데이터전송_순서도.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 6 saved: {out_p}")

if __name__ == "__main__":
    create_figure3()
    create_figure4()
    create_figure5()
    create_figure6()
