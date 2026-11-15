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

def create_figure5_pure_korean_3d():
    src_img_path = r'C:\Users\LENOVO\.gemini\antigravity\brain\974899d5-e6b1-45e5-8370-d95de83d7e11\ergonomic_multi_display_laptop_workstation_v2_1793436869048.jpg'
    
    with open(src_img_path, 'rb') as f:
        bytes_data = bytearray(f.read())
    numpy_array = np.asarray(bytes_data, dtype=np.uint8)
    orig_bgr = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    h_orig, w_orig, _ = orig_bgr.shape

    CANVAS_W, CANVAS_H = 1920, 1080
    canvas = np.zeros((CANVAS_H, CANVAS_W, 3), dtype=np.uint8)

    # Smooth dark tech studio gradient background
    top_col = np.array([24, 18, 14], dtype=np.float32)
    bot_col = np.array([12, 10, 8], dtype=np.float32)
    for y in range(CANVAS_H):
        alpha = y / CANVAS_H
        canvas[y, :] = ((1.0 - alpha) * top_col + alpha * bot_col).astype(np.uint8)

    # Scale 3D graphic into center (target width 1300)
    scale = 1300.0 / float(w_orig)
    target_w = int(w_orig * scale)
    target_h = int(h_orig * scale)
    scaled_bgr = cv2.resize(orig_bgr, (target_w, target_h), interpolation=cv2.INTER_LANCZOS4)

    start_x = (CANVAS_W - target_w) // 2
    start_y = 150

    # Seamless edge blending
    blend_mask = np.ones((target_h, target_w), dtype=np.float32)
    margin = 55
    for i in range(margin):
        factor = i / float(margin)
        blend_mask[i, :] = np.minimum(blend_mask[i, :], factor)
        blend_mask[target_h - 1 - i, :] = np.minimum(blend_mask[target_h - 1 - i, :], factor)
        blend_mask[:, i] = np.minimum(blend_mask[:, i], factor)
        blend_mask[:, target_w - 1 - i] = np.minimum(blend_mask[:, target_w - 1 - i], factor)

    blend_mask_3c = np.repeat(blend_mask[:, :, np.newaxis], 3, axis=2)
    roi_canvas = canvas[start_y:start_y+target_h, start_x:start_x+target_w].astype(np.float32)
    blended = scaled_bgr.astype(np.float32) * blend_mask_3c + roi_canvas * (1.0 - blend_mask_3c)
    canvas[start_y:start_y+target_h, start_x:start_x+target_w] = np.clip(blended, 0, 255).astype(np.uint8)

    # Draw Patent Annotations (100% Pure Korean, ZERO English!)
    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img, "RGBA")

    font_title = get_font(30, bold=True)
    font_badge = get_font(21, bold=True)
    font_label = get_font(19, bold=True)
    font_sub = get_font(15, bold=False)

    WHITE = (255, 255, 255)
    CYAN = (0, 229, 255)
    GOLD = (255, 215, 0)
    DARK_CARD = (10, 24, 38, 240)
    BORDER_CYAN = (0, 180, 220, 255)
    BORDER_GOLD = (255, 190, 40, 255)

    # A. Header / Title Box (Top-Left)
    draw.rounded_rectangle([50, 45, 340, 110], radius=10, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
    draw.text((75, 58), "【도 5】 (3차원 외관도)", font=font_title, fill=WHITE)

    # B. Top Master Title Box (100% Pure Korean)
    box_100_x1, box_100_y1 = 380, 45
    box_100_x2, box_100_y2 = 1860, 110
    draw.rounded_rectangle([box_100_x1, box_100_y1, box_100_x2, box_100_y2], radius=10, fill=DARK_CARD, outline=BORDER_GOLD, width=2)
    draw.text((box_100_x1 + 30, box_100_y1 + 18), "바른자세 시선 유지형 상하 슬라이딩 리프트 듀얼 및 트리플 가변 노트북 시스템", font=font_title, fill=GOLD)

    # Helper function to draw leader line with pin anchor
    def draw_leader(x_text, y_text, x_target, y_target, color=CYAN, is_left=True):
        if is_left:
            elbow_x = x_text + 20
            draw.line([(x_text, y_text), (elbow_x, y_text), (x_target, y_target)], fill=color, width=2)
        else:
            elbow_x = x_text - 20
            draw.line([(x_text, y_text), (elbow_x, y_text), (x_target, y_target)], fill=color, width=2)
        
        r = 6
        draw.ellipse([x_target-r, y_target-r, x_target+r, y_target+r], outline=color, width=2)
        draw.ellipse([x_target-3, y_target-3, x_target+3, y_target+3], fill=WHITE)

    # Function to draw callout card (Zero English!)
    def draw_callout(x, y, w_box, h_box, num_str, title_str, sub_str, target_xy, is_left=True, is_gold=False):
        border_col = BORDER_GOLD if is_gold else BORDER_CYAN
        badge_bg = GOLD if is_gold else CYAN
        badge_fg = (10, 10, 10)
        line_col = GOLD if is_gold else CYAN

        draw.rounded_rectangle([x, y, x + w_box, y + h_box], radius=8, fill=DARK_CARD, outline=border_col, width=2)

        badge_w = 68
        badge_h = 32
        draw.rounded_rectangle([x + 10, y + 10, x + 10 + badge_w, y + 10 + badge_h], radius=6, fill=badge_bg)
        draw.text((x + 18, y + 13), num_str, font=font_badge, fill=badge_fg)

        draw.text((x + 88, y + 14), title_str, font=font_label, fill=WHITE)
        if sub_str:
            draw.text((x + 88, y + 42), sub_str, font=font_sub, fill=(180, 210, 230))

        if is_left:
            conn_x = x + w_box
            conn_y = y + h_box // 2
        else:
            conn_x = x
            conn_y = y + h_box // 2
        
        draw_leader(conn_x, conn_y, target_xy[0], target_xy[1], color=line_col, is_left=is_left)

    # -------------------------------------------------------------------------
    # LEFT CALLOUTS (50px ~ 460px margin, NEVER TRUNCATED!)
    # -------------------------------------------------------------------------
    # 400L: 좌측 윙 모니터
    target_400l = (start_x + int(target_w * 0.28), start_y + int(target_h * 0.35))
    draw_callout(
        x=50, y=210, w_box=420, h_box=72,
        num_str="400L",
        title_str="제3 좌측 윙 모니터",
        sub_str="(참조 문서 및 90도 세로 회전 모드)",
        target_xy=target_400l,
        is_left=True
    )

    # 100: 제1 메인 모니터 (하단)
    target_100 = (start_x + int(target_w * 0.48), start_y + int(target_h * 0.58))
    draw_callout(
        x=50, y=430, w_box=420, h_box=72,
        num_str="100",
        title_str="제1 메인 모니터 (하단)",
        sub_str="(키보드 상단 틸트 및 펜 필기창)",
        target_xy=target_100,
        is_left=True,
        is_gold=True
    )

    # 900: 카운터밸런스 킥스탠드
    target_900 = (start_x + int(target_w * 0.45), start_y + int(target_h * 0.85))
    draw_callout(
        x=50, y=650, w_box=420, h_box=72,
        num_str="900",
        title_str="무게중심 자가평형 지지대",
        sub_str="(15도 인체공학 타이핑 틸트 지지)",
        target_xy=target_900,
        is_left=True
    )

    # -------------------------------------------------------------------------
    # RIGHT CALLOUTS (1440px ~ 1870px margin, NEVER TRUNCATED!)
    # -------------------------------------------------------------------------
    # 810: 인공지능 시선 웹캠
    target_810 = (start_x + int(target_w * 0.52), start_y + int(target_h * 0.18))
    draw_callout(
        x=1440, y=190, w_box=430, h_box=72,
        num_str="810",
        title_str="초소형 인공지능 시선 카메라",
        sub_str="(경추 꺾임각 실시간 감지 및 거북목 방지)",
        target_xy=target_810,
        is_left=False,
        is_gold=True
    )

    # 300: 제2 상단 메인 모니터
    target_300 = (start_x + int(target_w * 0.53), start_y + int(target_h * 0.32))
    draw_callout(
        x=1440, y=390, w_box=430, h_box=72,
        num_str="300",
        title_str="제2 상단 메인 모니터",
        sub_str="(안구 수평 시선 직결 및 목 꺾임각 0도)",
        target_xy=target_300,
        is_left=False
    )

    # 200: 무중력 슬라이딩 리프트 힌지
    target_200 = (start_x + int(target_w * 0.51), start_y + int(target_h * 0.48))
    draw_callout(
        x=1440, y=590, w_box=430, h_box=72,
        num_str="200",
        title_str="무중력 슬라이딩 리프트 힌지",
        sub_str="(토크 스프링 자가 평형 및 20cm 수직 상승)",
        target_xy=target_200,
        is_left=False,
        is_gold=True
    )

    # 400R / 500: 우측 윙 모니터 및 자석 결합부
    target_400r = (start_x + int(target_w * 0.75), start_y + int(target_h * 0.35))
    draw_callout(
        x=1440, y=790, w_box=430, h_box=72,
        num_str="400R",
        title_str="제3 우측 윙 모니터 [500]",
        sub_str="(자석 접점 연결로 선 없는 0.1초 원터치 결합)",
        target_xy=target_400r,
        is_left=False
    )

    # Bottom Status Footer Bar
    draw.rounded_rectangle([440, 990, 1480, 1050], radius=8, fill=(8, 16, 25, 240), outline=(0, 120, 180, 180), width=1)
    footer_text = "주식회사 세이프티온 (SAFETYON) ┃ 바른자세 듀얼 및 트리플 가변 노트북 시스템 3차원 외관도"
    draw.text((470, 1008), footer_text, font=font_sub, fill=(150, 190, 220))

    # Save final masterpiece images
    out_png = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도5_3D외관도_최종.png'
    out_jpg = r'C:\Users\LENOVO\Desktop\세이프티온_특허_바른자세_도5_3D외관도_최종.jpg'

    pil_img.save(out_png, "PNG", quality=100)
    pil_img.convert("RGB").save(out_jpg, "JPEG", quality=98)
    print(f"Figure 5 100% Pure Korean created successfully:\n  {out_png}\n  {out_jpg}")

if __name__ == "__main__":
    create_figure5_pure_korean_3d()
