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

    font_title = get_font(30, bold=True)
    font_sub_title = get_font(18, bold=False)

    draw.rounded_rectangle([60, 40, 1860, 130], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((90, 52), f"【도 {fig_no}】 {title_ko}", font=font_title, fill=WHITE)
    draw.text((92, 95), title_en, font=font_sub_title, fill=CYAN)

    return pil_img, draw

# 도 1: 상하 듀얼 시선 리프트(Eye-Level Elevation) 및 바른자세 인체공학 구조도
def create_dual_monitor_fig1():
    pil_img, draw = create_base_canvas(
        "바른자세 시선 유지형 상하 슬라이딩 리프트 듀얼 모니터 전개 및 시야각 비교도",
        "Eye-Level Elevation Dual Monitor Deployment and Ergonomic Posture Comparison",
        1
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    RED = (255, 80, 80)
    GREEN = (0, 230, 118)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_badge = get_font(20, bold=True)

    # Left: 종래 일반 노트북 (거북목 유발)
    draw.rounded_rectangle([60, 170, 780, 980], radius=12, fill=DARK_CARD, outline=RED, width=2)
    draw.text((85, 195), "■ 종래 일반 노트북: 심각한 거북목 및 목 디스크 유발", font=font_sec, fill=RED)
    
    # Graphic: Person looking down at laptop
    draw.ellipse([260, 310, 340, 390], fill=(220, 180, 140), outline=WHITE, width=2) # Head
    draw.text((275, 340), "사용자", font=font_lbl, fill=(10, 10, 10))
    # Bent neck
    draw.line([(300, 390), (330, 460)], fill=RED, width=8)
    draw.text((345, 415), "목 꺾임각: 45°~60° (경추 하중 27kg!)", font=font_lbl, fill=RED)

    # Conventional Laptop
    draw.line([(220, 680), (450, 680)], fill=(120, 130, 140), width=10) # Base
    draw.line([(450, 680), (520, 520)], fill=(80, 150, 200), width=8) # Single Screen
    draw.text((430, 560), "단일 화면\n(시선 하향 쏠림)", font=font_txt, fill=WHITE)

    draw.rounded_rectangle([85, 750, 755, 950], radius=8, fill=DARKER_CARD, outline=RED, width=1)
    draw.text((105, 765), "종래 기술의 치명적 한계", font=font_lbl, fill=RED)
    draw.text((105, 800), "• 모니터 화면 중심이 사용자의 시선보다 20~30cm 아래에 위치\n• 장시간 작업 시 경추 굴곡으로 인한 거북목 및 만성 통증 발생\n• 화면 분할 시 작업 영역 협소 및 업무 효율성 급락", font=font_txt, fill=(220, 220, 220))

    # Right: 본 발명의 바른자세 상하 슬라이딩 듀얼 모니터 (2.0)
    draw.rounded_rectangle([840, 170, 1860, 980], radius=12, fill=DARK_CARD, outline=GREEN, width=2)
    draw.text((865, 195), "■ 본 발명: 시선 수평 유지(Eye-Level) 슬라이딩 리프트 듀얼 모니터 (2.0)", font=font_sec, fill=GREEN)

    # Graphic: Straight posture
    draw.ellipse([1040, 300, 1120, 380], fill=(220, 180, 140), outline=WHITE, width=2) # Head
    draw.text((1055, 330), "사용자", font=font_lbl, fill=(10, 10, 10))
    # Straight neck
    draw.line([(1080, 380), (1080, 470)], fill=GREEN, width=8)
    draw.text((1095, 415), "목 꺾임각: 0° (바른 척추 자세 유지)", font=font_lbl, fill=GREEN)

    # Eye sight line straight ahead
    draw.line([(1120, 340), (1380, 340)], fill=CYAN, width=3)
    draw.polygon([(1370, 332), (1390, 340), (1370, 348)], fill=CYAN)
    draw.text((1180, 310), "수평 시선 정면 일치 (Eye-Level 0°)", font=font_lbl, fill=CYAN)

    # Laptop Base
    draw.line([(1200, 680), (1450, 680)], fill=(120, 130, 140), width=10)
    # Lower Monitor (1st)
    draw.line([(1450, 680), (1500, 520)], fill=(0, 180, 240), width=8)
    draw.text((1515, 560), "100: 제1 메인 모니터 (하단)", font=font_lbl, fill=CYAN)

    # Telescopic / Sliding Elevation Link (200)
    draw.line([(1500, 520), (1500, 280)], fill=GOLD, width=6)
    draw.text((1515, 420), "200: 슬라이딩 리프트 기구 (수직 15~25cm 상승)", font=font_lbl, fill=GOLD)

    # Upper Monitor (2nd) - Raised to Eye Level!
    draw.line([(1500, 380), (1500, 220)], fill=GREEN, width=10)
    draw.text((1515, 270), "300: 제2 상단 리프트 모니터 (수평 시선 직결)", font=font_sec, fill=GREEN)

    draw.rounded_rectangle([865, 750, 1835, 950], radius=8, fill=DARKER_CARD, outline=GREEN, width=1)
    draw.text((885, 765), "본 발명 2.0의 혁신적 특장점", font=font_lbl, fill=GREEN)
    draw.text((885, 800), "• 하단 제1 모니터(100)는 문서/도구창, 상단 제2 모니터(300)는 정면 수평 시선 작업창 전담\n• 내장 토크 밸런서(스프링 기구)로 손가락 하나로 밀어 올리면 원하는 높이에 무중력 자가 고정\n• 거북목 발병률 90% 이상 예방 및 코딩/문서/디자인 작업 효율 250% 폭증", font=font_txt, fill=WHITE)

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도1_듀얼리프트_시야각.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 1 saved: {out_p}")

# 도 2: 트리플(트리얼) 3면 입체 파노라마 전개 구조도 (상단 리프트 + 좌우 윙 확장)
def create_dual_monitor_fig2():
    pil_img, draw = create_base_canvas(
        "트리플(트리얼) 3면 입체 파노라마 전개 및 마그네틱 윙(Wing) 확장 구조도",
        "Triple Panoramic Screen Expansion with Upper Lift and Magnetic Detachable Wings",
        2
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    GREEN = (0, 230, 118)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_badge = get_font(20, bold=True)

    # Main 3-Screen Panoramic Layout Box
    draw.rounded_rectangle([60, 170, 1860, 980], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((85, 195), "■ 트리플(트리얼) 3면 180° 곡면 파노라마 시야각 구축 구조", font=font_sec, fill=GOLD)

    # 1. Lower Laptop Base & 1st Monitor (Bottom Center)
    base_x, base_y = 760, 680
    draw.rounded_rectangle([base_x, base_y, base_x + 400, base_y + 160], radius=8, fill=(35, 45, 60), outline=(100, 130, 160), width=2)
    draw.text((base_x + 130, base_y + 60), "노트북 본체 (키보드부)", font=font_lbl, fill=WHITE)

    # Lower 1st Screen (100)
    draw.rounded_rectangle([base_x + 10, base_y - 200, base_x + 390, base_y - 10], radius=8, fill=(15, 30, 50), outline=CYAN, width=3)
    draw.text((base_x + 60, base_y - 120), "100: 제1 메인 모니터 (16:10 QHD)\n(키보드 연결부 / 문서·도구)", font=font_lbl, fill=CYAN)

    # 2. Upper 2nd Center Screen (300) - Raised high!
    top_x, top_y = base_x + 10, base_y - 460
    draw.rounded_rectangle([top_x, top_y, top_x + 380, top_y + 230], radius=8, fill=(12, 40, 30), outline=GREEN, width=3)
    draw.text((top_x + 45, top_y + 90), "300: 제2 상단 메인 모니터\n(안구 수평 시선 / 메인 작업창)", font=font_sec, fill=GREEN)

    # 3. Left Wing 3rd Screen (400L) - Angled inward
    left_x, left_y = top_x - 420, top_y + 20
    draw.rounded_rectangle([left_x, left_y, left_x + 390, left_y + 220], radius=8, fill=(30, 25, 45), outline=GOLD, width=2)
    draw.text((left_x + 35, left_y + 80), "400L: 좌측 윙 모니터 (3rd)\n(참조자료 / 웹브라우저)", font=font_lbl, fill=GOLD)
    # Magnetic Pogo-Pin Joint Left
    draw.rounded_rectangle([left_x + 385, left_y + 70, left_x + 415, left_y + 150], radius=4, fill=GOLD)
    draw.text((left_x + 330, left_y + 160), "500: 마그네틱 포고핀 결합", font=font_txt, fill=GOLD)

    # 4. Right Wing 3rd Screen (400R) - Angled inward
    right_x, right_y = top_x + 410, top_y + 20
    draw.rounded_rectangle([right_x, right_y, right_x + 390, right_y + 220], radius=8, fill=(30, 25, 45), outline=GOLD, width=2)
    draw.text((right_x + 45, right_y + 80), "400R: 우측 윙 모니터 (3rd)\n(메신저 / 주식차트 / 모니터링)", font=font_lbl, fill=GOLD)
    # Magnetic Pogo-Pin Joint Right
    draw.rounded_rectangle([right_x - 25, right_y + 70, right_x + 5, right_y + 150], radius=4, fill=GOLD)
    draw.text((right_x + 10, right_y + 160), "500: 마그네틱 포고핀 결합", font=font_txt, fill=GOLD)

    # Connecting guidelines
    draw.line([(left_x + 390, left_y + 110), (top_x, top_y + 110)], fill=GOLD, width=4)
    draw.line([(top_x + 380, top_y + 110), (right_x, right_y + 110)], fill=GOLD, width=4)

    # Bottom Description Box
    draw.rounded_rectangle([85, 860, 1835, 960], radius=8, fill=DARKER_CARD, outline=BORDER_CYAN, width=1)
    desc_txt = (
        "【트리플(트리얼) 가변 모드 요약】 평상시에는 1.1kg 단일 노트북 휴대 ➔ 거치 시 상단 제2 모니터(300)가 시선 높이로 솟아오름 ➔ "
        "필요 시 좌우 윙 모니터(400L, 400R)가 자석(500)으로 0.1초 만에 탈부착되어 선 없는 3면 몰입형 파노라마 워크스테이션 완성!"
    )
    draw.text((105, 875), "■ 2.0 트리플(트리얼) 가변 확장 메커니즘", font=font_lbl, fill=GOLD)
    draw.text((105, 908), desc_txt, font=font_txt, fill=(220, 235, 250))

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도2_트리플_파노라마.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 2 saved: {out_p}")

# 도 3: 자가 평형(Zero-Gravity) 스프링 힌지 및 마그네틱 포고핀 탈부착 상세 기구도
def create_dual_monitor_fig3():
    pil_img, draw = create_base_canvas(
        "자가 평형(Zero-Gravity) 슬라이딩 힌지 기구 및 마그네틱 포고핀 결합 단면도",
        "Zero-Gravity Spring Hinge Elevation Mechanism & Magnetic Pogo-Pin Detachable Joint",
        3
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    GREEN = (0, 230, 118)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)
    font_code = get_font(16, bold=True)

    # Left: Zero-Gravity Hinge Mechanism
    draw.rounded_rectangle([60, 170, 920, 980], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((85, 195), "200: 자가 평형(Zero-Gravity) 슬라이딩 리프트 힌지", font=font_sec, fill=CYAN)

    # Draw Telescopic slider track
    draw.rounded_rectangle([180, 260, 320, 720], radius=10, fill=(25, 35, 50), outline=CYAN, width=2)
    draw.text((195, 280), "가이드 레일", font=font_lbl, fill=WHITE)

    # Internal spring mechanism
    sy_start = 330
    for i in range(10):
        sy = sy_start + i * 32
        draw.line([(220, sy), (280, sy + 16)], fill=GOLD, width=4)
        draw.line([(280, sy + 16), (220, sy + 32)], fill=GOLD, width=4)
    draw.text((345, 450), "210: 정하중 태엽/가스 스프링\n(모니터 자중과 1:1 평형)", font=font_lbl, fill=GOLD)

    # Friction Brake Pad
    draw.rounded_rectangle([190, 620, 310, 660], radius=4, fill=(180, 50, 50))
    draw.text((345, 630), "220: 미세 마찰 브레이크 패드\n(원하는 높이에서 정지)", font=font_lbl, fill=(255, 150, 150))

    draw.rounded_rectangle([85, 760, 895, 950], radius=8, fill=DARKER_CARD, outline=BORDER_CYAN, width=1)
    draw.text((105, 775), "무중력 리프트 기구 원리", font=font_lbl, fill=CYAN)
    draw.text((105, 810), "• 상단 모니터(약 450g)의 중력 방향 하중을 내부 토크 스프링이 1:1로 상쇄\n• 손가락 하나로 밀어 올리면 부드럽게 상승하고, 손을 떼는 즉시 그 자리에 고정\n• 케이블이 레일 내부 플렉시블 FPCB로 매립되어 단선 및 외관 돌출 완전 배제", font=font_txt, fill=WHITE)

    # Right: Magnetic Pogo-Pin Detachable Joint (500)
    draw.rounded_rectangle([960, 170, 1860, 980], radius=12, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((985, 195), "500: 마그네틱 포고핀(Pogo-Pin) 케이블리스 결합 구조", font=font_sec, fill=GOLD)

    # Female side (Main Screen edge)
    draw.rounded_rectangle([1050, 280, 1280, 680], radius=12, fill=(20, 35, 55), outline=CYAN, width=2)
    draw.text((1070, 300), "메인 모니터 측면", font=font_lbl, fill=CYAN)

    # Male side (Wing Screen edge)
    draw.rounded_rectangle([1450, 280, 1680, 680], radius=12, fill=(35, 30, 55), outline=GOLD, width=2)
    draw.text((1470, 300), "윙 모니터 측면", font=font_lbl, fill=GOLD)

    # Neodymium Magnets
    draw.rounded_rectangle([1220, 360, 1270, 420], radius=4, fill=(200, 50, 50)) # N pole
    draw.text((1235, 385), "N", font=font_lbl, fill=WHITE)
    draw.rounded_rectangle([1460, 360, 1510, 420], radius=4, fill=(50, 80, 200)) # S pole
    draw.text((1475, 385), "S", font=font_lbl, fill=WHITE)
    draw.text((1290, 390), "강력 네오디뮴 자석 결합", font=font_lbl, fill=GOLD)

    # Pogo Pins (Spring Loaded Pins)
    for p_idx in range(5):
        py = 460 + p_idx * 35
        # Pin
        draw.line([(1250, py), (1470, py)], fill=GOLD, width=6)
        draw.ellipse([1465, py - 5, 1475, py + 5], fill=WHITE)
    draw.text((1290, 530), "금도금 포고핀 어레이\n(전원 20V + DP 영상 직결)", font=font_code, fill=GREEN)

    draw.rounded_rectangle([985, 760, 1835, 950], radius=8, fill=DARKER_CARD, outline=BORDER_GOLD, width=1)
    draw.text((1005, 775), "선 없는(Cableless) 원터치 결합의 효과", font=font_lbl, fill=GOLD)
    draw.text((1005, 810), "• 지저분한 HDMI/C타입 케이블 연결 없이 0.1초 만에 자석으로 '착' 달라붙음\n• 포고핀 단자를 통해 디스플레이포트(DP Alt-Mode) 고해상도 신호와 전원 동시 공급\n• 필요 없을 땐 가볍게 떼어내어 파우치에 쏙 들어가는 완벽한 모듈형 구조", font=font_txt, fill=WHITE)

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도3_힌지_포고핀.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 3 saved: {out_p}")

# 도 4: AI 거북목 감지 웹캠 연동 및 자동 각도/피드백 제어 블록도
def create_dual_monitor_fig4():
    pil_img, draw = create_base_canvas(
        "AI 시선 및 경추 꺾임각 감지 기반 바른자세 피드백 제어 시스템 블록도",
        "AI-Based Cervical Spine Angle Detection and Posture-Correction Feedback Architecture",
        4
    )
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    GREEN = (0, 230, 118)
    DARK_CARD = (10, 24, 38, 240)
    DARKER_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)

    font_sec = get_font(22, bold=True)
    font_lbl = get_font(18, bold=True)
    font_txt = get_font(15, bold=False)

    steps = [
        ("810: 상단 베젤 초소형 AI 웹캠", "사용자 얼굴 윤곽(Face Mesh) 및 안구 홍채 위치 실시간 감지", CYAN),
        ("820: 경추 굴곡각 판별 엔진", "사용자 귀-어깨-목선 벡터 분석 ➔ 거북목 각도(>15°) 초과 판정", (100, 200, 255)),
        ("830: 바른자세 복원 피드백 제어기", "• 1단계: 상단 메인 화면(300)으로 시선 유도 팝업 발송\n• 2단계: 하단 모니터 밝기 미세 감쇄 ➔ 고개 자연 상승 유도\n• 3단계: 미세 엑추에이터 제어로 상단 모니터 틸트각 자동 상향", GOLD),
        ("840: 자세 개선 리포트 & 건강 데이터 동기화", "일일 바른자세 유지 시간(%) 기록 및 스마트워치/헬스케어 앱 연동", GREEN)
    ]

    sy = 190
    box_w = 1200
    box_h = 130
    start_x = 360

    for i, (s_tit, s_desc, s_col) in enumerate(steps):
        draw.rounded_rectangle([start_x, sy, start_x + box_w, sy + box_h], radius=10, fill=DARK_CARD, outline=s_col, width=2)
        # Badge
        draw.rounded_rectangle([start_x + 15, sy + 15, start_x + 95, sy + 55], radius=6, fill=s_col)
        draw.text((start_x + 22, sy + 22), f"단계 {i+1}", font=font_lbl, fill=(10, 10, 10))
        draw.text((start_x + 115, sy + 20), s_tit, font=font_sec, fill=WHITE)
        draw.text((start_x + 115, sy + 60), s_desc, font=font_txt, fill=(210, 230, 245))

        if i < len(steps) - 1:
            arrow_y = sy + box_h
            draw.line([(start_x + box_w // 2, arrow_y), (start_x + box_w // 2, arrow_y + 40)], fill=GOLD, width=3)
            draw.polygon([(start_x + box_w // 2 - 8, arrow_y + 28), (start_x + box_w // 2 + 8, arrow_y + 28), (start_x + box_w // 2, arrow_y + 40)], fill=GOLD)
        sy += 175

    out_p = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도4_AI제어흐름도.png'
    pil_img.save(out_p, "PNG", quality=100)
    print(f"Figure 4 saved: {out_p}")

if __name__ == "__main__":
    create_dual_monitor_fig1()
    create_dual_monitor_fig2()
    create_dual_monitor_fig3()
    create_dual_monitor_fig4()
