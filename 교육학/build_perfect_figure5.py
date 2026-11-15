# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def build_perfect_figure5():
    W, H = 1920, 1080
    canvas = np.zeros((H, W, 3), dtype=np.uint8)

    # 1. Dark high-tech navy gradient background
    top_col = np.array([28, 20, 14], dtype=np.float32) # BGR
    bot_col = np.array([16, 12, 8], dtype=np.float32)
    for y in range(H):
        alpha = y / H
        col = (1.0 - alpha) * top_col + alpha * bot_col
        canvas[y, :] = col.astype(np.uint8)

    # Convert to PIL
    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img, "RGBA")

    # Font helper
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

    font_title = get_font(32, bold=True)
    font_sub_title = get_font(20, bold=False)
    font_box_header = get_font(22, bold=True)
    font_badge = get_font(20, bold=True)
    font_label = get_font(18, bold=True)
    font_desc = get_font(16, bold=False)
    font_code = get_font(15, bold=True)

    # Colors
    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    DARKer_CARD = (6, 14, 24, 250)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)
    GREEN = (0, 230, 118)

    # 10 Wavelength definition (Color Code 0~9)
    # 0: 검정, 1: 갈색, 2: 빨강, 3: 주황, 4: 노랑, 5: 초록, 6: 파랑, 7: 보라, 8: 회색, 9: 흰색
    colors_10 = [
        {"num": 0, "name": "검정", "wl": "λ0 (1270nm)", "rgb": (80, 80, 80), "box_rgb": (30, 30, 30), "text_rgb": (220, 220, 220)},
        {"num": 1, "name": "갈색", "wl": "λ1 (1290nm)", "rgb": (160, 90, 45), "box_rgb": (130, 70, 30), "text_rgb": (255, 255, 255)},
        {"num": 2, "name": "빨강", "wl": "λ2 (1310nm)", "rgb": (255, 50, 50), "box_rgb": (180, 20, 20), "text_rgb": (255, 255, 255)},
        {"num": 3, "name": "주황", "wl": "λ3 (1330nm)", "rgb": (255, 140, 0), "box_rgb": (210, 100, 0), "text_rgb": (255, 255, 255)},
        {"num": 4, "name": "노랑", "wl": "λ4 (1350nm)", "rgb": (255, 225, 0), "box_rgb": (190, 170, 0), "text_rgb": (20, 20, 20)},
        {"num": 5, "name": "초록", "wl": "λ5 (1370nm)", "rgb": (0, 230, 100), "box_rgb": (0, 140, 60), "text_rgb": (255, 255, 255)},
        {"num": 6, "name": "파랑", "wl": "λ6 (1390nm)", "rgb": (0, 150, 255), "box_rgb": (0, 90, 180), "text_rgb": (255, 255, 255)},
        {"num": 7, "name": "보라", "wl": "λ7 (1410nm)", "rgb": (180, 70, 255), "box_rgb": (120, 40, 190), "text_rgb": (255, 255, 255)},
        {"num": 8, "name": "회색", "wl": "λ8 (1430nm)", "rgb": (170, 180, 190), "box_rgb": (120, 130, 140), "text_rgb": (20, 20, 20)},
        {"num": 9, "name": "흰색", "wl": "λ9 (1450nm)", "rgb": (255, 255, 255), "box_rgb": (230, 230, 230), "text_rgb": (20, 20, 20)}
    ]

    # A. Top Header
    draw.rounded_rectangle([60, 40, 1860, 130], radius=12, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((90, 52), "【도 5】 10진 파장 수신 모듈(400)의 어레이 도파로 회절격자(AWG) 및 디코더 구조도", font=font_title, fill=WHITE)
    draw.text((92, 95), "Arrayed Waveguide Grating (AWG) De-multiplexer & Photodiode Array Decimal Decoding Architecture", font=font_sub_title, fill=CYAN)

    # B. Master Flow Indicator Bar (Top step indicator)
    step_y = 150
    steps = [
        ("1. 다파장 광 입력", "λ0~λ9 혼합광 진입", 60, 440, CYAN),
        ("2. 1차 광분배 (스타커플러 1)", "자유전파영역 빛 확산", 470, 850, (100, 180, 255)),
        ("3. 어레이 도파로 위상지연 (AWG)", "길이 차이(ΔL)로 위상 분리", 880, 1260, GOLD),
        ("4. 2차 파장 분광 (스타커플러 2)", "간섭 효과로 10개 파장 결상", 1290, 1540, (255, 120, 80)),
        ("5. 10채널 PD & 디코딩", "빛 ➔ 전기 신호 ➔ 10진 복원", 1570, 1860, GREEN)
    ]
    for s_title, s_desc, x1, x2, s_col in steps:
        draw.rounded_rectangle([x1, step_y, x2, step_y + 45], radius=6, fill=(12, 28, 45, 220), outline=s_col, width=1)
        draw.text((x1 + 12, step_y + 6), s_title, font=font_label, fill=s_col)
        draw.text((x1 + 12, step_y + 26), s_desc, font=font_desc, fill=(180, 200, 220))

    # C. Main Drawing Area: [Y: 220 ~ 1000]

    # =========================================================================
    # 1. INPUT WAVEGUIDE: [210: 유리 내장형 3D 광 도파로]
    # =========================================================================
    input_x_start = 60
    input_x_end = 260
    input_y = 590

    # Draw multi-color glowing rainbow bus line
    bus_thickness = 18
    # Rainbow stacked lines to show multiple wavelengths combined
    for i, col_info in enumerate(colors_10):
        y_offset = int((i - 4.5) * 2.2)
        draw.line([(input_x_start, input_y + y_offset), (input_x_end, input_y + y_offset)], fill=col_info["rgb"], width=2)

    # Input Callout Box
    draw.rounded_rectangle([60, 420, 260, 520], radius=8, fill=DARKer_CARD, outline=BORDER_CYAN, width=2)
    # Badge 210
    draw.rounded_rectangle([75, 432, 135, 462], radius=4, fill=CYAN)
    draw.text((82, 436), "210", font=font_badge, fill=(10, 10, 10))
    draw.text((145, 436), "광 도파로", font=font_label, fill=WHITE)
    draw.text((75, 470), "다파장 혼합 광신호\n(10대 파장 λ0~λ9)", font=font_desc, fill=(180, 220, 240))
    draw.line([(160, 520), (160, 580)], fill=CYAN, width=2)
    draw.ellipse([157, 577, 163, 583], fill=WHITE)

    # Arrow indicating beam direction
    draw.polygon([(input_x_end - 15, input_y - 12), (input_x_end, input_y), (input_x_end - 15, input_y + 12)], fill=WHITE)

    # =========================================================================
    # 2. STAR COUPLER 1 (입력측 자유전파영역 FPR 1 / 입사 스타커플러)
    # =========================================================================
    # Trapezoid shape spreading the light
    c1_left_x = 260
    c1_right_x = 450
    c1_top_y = 360
    c1_bot_y = 820
    c1_in_top = input_y - 25
    c1_in_bot = input_y + 25

    star1_poly = [
        (c1_left_x, c1_in_top),
        (c1_right_x, c1_top_y),
        (c1_right_x, c1_bot_y),
        (c1_left_x, c1_in_bot)
    ]
    draw.polygon(star1_poly, fill=(20, 60, 110, 230), outline=CYAN, width=2)

    # Draw internal diverging light rays inside FPR 1
    for i in range(11):
        target_y_c1 = c1_top_y + (c1_bot_y - c1_top_y) * (i / 10.0)
        draw.line([(c1_left_x, input_y), (c1_right_x, target_y_c1)], fill=(100, 200, 255, 120), width=1)

    # Star Coupler 1 Label
    draw.text((280, 570), "제1 스타커플러\n(입력 FPR 1)", font=font_label, fill=WHITE)
    draw.text((280, 615), "빛 균일 확산 분배", font=font_desc, fill=(180, 220, 240))

    # =========================================================================
    # 3. ARRAYED WAVEGUIDES (410: 어레이 도파로 회절격자 위상 지연 경로)
    # =========================================================================
    # 10 curved waveguides with incrementing lengths (ΔL)
    # Connecting c1_right_x to c2_left_x
    c2_left_x = 940
    c2_right_x = 1120
    c2_top_y = 360
    c2_bot_y = 820

    awg_num_paths = 10
    for i in range(awg_num_paths):
        y_start = c1_top_y + (c1_bot_y - c1_top_y) * (i / 9.0)
        y_end = c2_top_y + (c2_bot_y - c2_top_y) * (i / 9.0)
        
        # Arching curve height increases as index increases (Length difference ΔL)
        # Higher curves travel longer distance!
        arch_height = 80 + i * 28
        mid_x = (c1_right_x + c2_left_x) // 2

        # Draw a beautiful smooth cubic bezier curve
        # P0=(c1_right_x, y_start), P1=(c1_right_x+100, y_start - arch_height), P2=(c2_left_x-100, y_end - arch_height), P3=(c2_left_x, y_end)
        pts = []
        for t_step in range(41):
            t = t_step / 40.0
            bx = (1-t)**3 * c1_right_x + 3*(1-t)**2*t * (c1_right_x + 120) + 3*(1-t)*t**2 * (c2_left_x - 120) + t**3 * c2_left_x
            by = (1-t)**3 * y_start + 3*(1-t)**2*t * (y_start - arch_height) + 3*(1-t)*t**2 * (y_end - arch_height) + t**3 * y_end
            pts.append((bx, by))
        
        # Draw curve with high-tech glowing style
        col_curve = (0, 220, 180, 230) if i % 2 == 0 else (0, 180, 240, 230)
        draw.line(pts, fill=col_curve, width=3)

    # AWG Master Callout Box
    draw.rounded_rectangle([520, 230, 880, 340], radius=8, fill=DARKer_CARD, outline=BORDER_GOLD, width=2)
    # Badge 410
    draw.rounded_rectangle([535, 242, 595, 272], radius=4, fill=GOLD)
    draw.text((542, 246), "410", font=font_badge, fill=(10, 10, 10))
    draw.text((605, 246), "어레이 도파로 회절격자 (AWG)", font=font_label, fill=WHITE)
    draw.text((535, 280), "• 경로별 광도파로 길이 차이: ΔL 고정\n• 파장(λ)에 따른 위상 지연차(Phase Shift) 발생\n• 10개 파장의 보강 간섭 각도 정밀 제어", font=font_desc, fill=(230, 230, 200))

    # =========================================================================
    # 4. STAR COUPLER 2 (출력측 자유전파영역 FPR 2 / 집속 스타커플러)
    # =========================================================================
    star2_poly = [
        (c2_left_x, c2_top_y),
        (c2_right_x, 420),
        (c2_right_x, 760),
        (c2_left_x, c2_bot_y)
    ]
    draw.polygon(star2_poly, fill=(20, 60, 110, 230), outline=CYAN, width=2)

    # Converging light rays inside FPR 2 showing chromatic dispersion
    for i in range(10):
        y_start_c2 = c2_top_y + (c2_bot_y - c2_top_y) * (i / 9.0)
        out_y = 440 + i * 32
        draw.line([(c2_left_x, y_start_c2), (c2_right_x, out_y)], fill=colors_10[i]["rgb"], width=1)

    draw.text((960, 560), "제2 스타커플러\n(출력 FPR 2)", font=font_label, fill=WHITE)
    draw.text((960, 605), "위상 간섭 분광", font=font_desc, fill=(180, 220, 240))

    # =========================================================================
    # 5. DEMULTIPLEXED 10 CHANNELS (λ0 ~ λ9) & PHOTODIODE ARRAY (420)
    # =========================================================================
    pd_box_x = 1320
    pd_box_w = 160
    pd_h = 30
    pd_spacing = 42
    start_pd_y = 310

    # Draw individual colored beam lines from Coupler 2 to Photodiode Array
    for i, col in enumerate(colors_10):
        curr_y = start_pd_y + i * pd_spacing
        source_y = 440 + int(i * 31.0)
        
        # S-curve light line
        p_line = [
            (c2_right_x, source_y),
            (c2_right_x + 60, source_y),
            (pd_box_x - 60, curr_y + pd_h // 2),
            (pd_box_x, curr_y + pd_h // 2)
        ]
        draw.line(p_line, fill=col["rgb"], width=3)
        # Glowing dot at PD entrance
        draw.ellipse([pd_box_x - 5, curr_y + pd_h // 2 - 4, pd_box_x + 3, curr_y + pd_h // 2 + 4], fill=col["rgb"])

        # Photodiode Chip Box
        draw.rounded_rectangle([pd_box_x, curr_y, pd_box_x + pd_box_w, curr_y + pd_h], radius=5, fill=col["box_rgb"], outline=col["rgb"], width=2)
        # PD text
        draw.text((pd_box_x + 8, curr_y + 4), f"PD{i} : {col['wl']}", font=font_code, fill=col["text_rgb"])

    # 420 Header Box for PD Array
    draw.rounded_rectangle([1320, 230, 1480, 290], radius=6, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    # Badge 420
    draw.rounded_rectangle([1328, 238, 1378, 268], radius=4, fill=GOLD)
    draw.text((1334, 242), "420", font=font_badge, fill=(10, 10, 10))
    draw.text((1388, 244), "PD 어레이", font=font_label, fill=WHITE)
    draw.text((1332, 272), "10채널 고속 광전변환", font=font_desc, fill=(220, 220, 180))

    # =========================================================================
    # 6. ELECTRICAL CONNECTORS & 10-DECIMAL DECODER (430)
    # =========================================================================
    decoder_x = 1580
    decoder_y = 260
    decoder_w = 280
    decoder_h = 750

    # Draw electrical copper interconnect lines from each PD to Decoder
    for i, col in enumerate(colors_10):
        curr_y = start_pd_y + i * pd_spacing + pd_h // 2
        wire_y = 350 + i * 36
        draw.line([(pd_box_x + pd_box_w, curr_y), (pd_box_x + pd_box_w + 30, curr_y), (decoder_x - 30, wire_y), (decoder_x, wire_y)], fill=(255, 180, 50), width=2)
        # Tiny terminal pad
        draw.rectangle([decoder_x - 3, wire_y - 2, decoder_x + 3, wire_y + 2], fill=GOLD)

    # 430 Decoder Main Chassis Box
    draw.rounded_rectangle([decoder_x, decoder_y, decoder_x + decoder_w, decoder_y + decoder_h], radius=12, fill=DARKer_CARD, outline=GREEN, width=3)

    # Badge 430
    draw.rounded_rectangle([decoder_x + 20, decoder_y + 20, decoder_x + 85, decoder_y + 55], radius=6, fill=GREEN)
    draw.text((decoder_x + 28, decoder_y + 24), "430", font=font_badge, fill=(10, 10, 10))
    draw.text((decoder_x + 95, decoder_y + 26), "10진 데이터 디코더", font=font_box_header, fill=WHITE)

    # Decoder internal functional list
    dec_info_y = decoder_y + 80
    draw.line([(decoder_x + 15, dec_info_y), (decoder_x + decoder_w - 15, dec_info_y)], fill=(0, 180, 90, 150), width=1)

    desc_lines = [
        ("수신 처리 기능", font_label, GREEN),
        ("① 10개 파장 감지 판별", font_desc, WHITE),
        ("② 심볼 룩업테이블(LUT) 역변환", font_desc, WHITE),
        ("③ 0~9 10진수 즉시 복원", font_desc, (255, 230, 100)),
        ("④ 2진 비트 병렬 출력 (1클럭)", font_desc, WHITE),
        ("", font_desc, WHITE),
        ("매핑 복원표 (1:1 복원)", font_label, CYAN),
        ("• λ0 감지 ➔ 숫자 '0' 복원", font_desc, (220, 220, 220)),
        ("• λ1 감지 ➔ 숫자 '1' 복원", font_desc, (220, 220, 220)),
        ("• λ2 감지 ➔ 숫자 '2' 복원", font_desc, (220, 220, 220)),
        ("• λ3 감지 ➔ 숫자 '3' 복원", font_desc, (220, 220, 220)),
        ("• λ4 감지 ➔ 숫자 '4' 복원", font_desc, (220, 220, 220)),
        ("• λ5 감지 ➔ 숫자 '5' 복원", font_desc, (220, 220, 220)),
        ("• λ6 감지 ➔ 숫자 '6' 복원", font_desc, (220, 220, 220)),
        ("• λ7 감지 ➔ 숫자 '7' 복원", font_desc, (220, 220, 220)),
        ("• λ8 감지 ➔ 숫자 '8' 복원", font_desc, (220, 220, 220)),
        ("• λ9 감지 ➔ 숫자 '9' 복원", font_desc, (220, 220, 220)),
        ("", font_desc, WHITE),
        ("차세대 HBM4 메모리로", font_label, GOLD),
        ("초고속 비동기 직결 전송!", font_desc, (255, 255, 255))
    ]

    cur_ty = dec_info_y + 15
    for txt, f_type, col in desc_lines:
        if txt == "":
            cur_ty += 8
            continue
        draw.text((decoder_x + 20, cur_ty), txt, font=f_type, fill=col)
        cur_ty += 24

    # Bottom Master Status Card
    draw.rounded_rectangle([60, 950, 1860, 1040], radius=10, fill=DARK_CARD, outline=BORDER_CYAN, width=1)
    status_summary = (
        "【핵심 동작 원리 요약】 단일 도파로(210)로 입력된 10대 파장 혼합광 ➔ 제1 스타커플러가 부채꼴 확산 ➔ "
        "어레이 도파로(410)가 길이 차이(ΔL)를 주어 파장별 위상차 생성 ➔ 제2 스타커플러에서 간섭 분광되어 10개 출력단으로 분리 ➔ "
        "10채널 PD 어레이(420)가 수광 ➔ 디코더(430)가 단 1클럭 내에 10진수(0~9)로 완벽 복원!"
    )
    draw.text((85, 965), "■ 400: 10진 파장 수신 모듈 (Rx) 핵심 아키텍처", font=font_label, fill=GOLD)
    draw.text((85, 995), status_summary, font=font_desc, fill=(200, 230, 250))

    # Save output files
    out_png = r'C:\Users\LENOVO\Desktop\세이프티온_특허_도5_수신단_AWG디멀티플렉서.png'
    pil_img.save(out_png, "PNG", quality=100)
    print(f"Successfully generated perfect clear Figure 5 at:\n  {out_png}")

if __name__ == "__main__":
    build_perfect_figure5()
