# -*- coding: utf-8 -*-
import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def imread_kr(path):
    with open(path, 'rb') as f:
        bytes_data = bytearray(f.read())
    numpy_array = np.asarray(bytes_data, dtype=np.uint8)
    return cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)

def imwrite_kr(path, img):
    ext = os.path.splitext(path)[1]
    ret, buf = cv2.imencode(ext, img)
    with open(path, 'wb') as f:
        f.write(buf.tobytes())

# Path to original user image
user_img_path = r'C:\Users\LENOVO\.gemini\antigravity\brain\974899d5-e6b1-45e5-8370-d95de83d7e11\.user_uploaded\media_1793421285402_10e104f1.jpg'
orig_img = imread_kr(user_img_path)
h, w, c = orig_img.shape
print(f"Original image size: {w}x{h}")

# 1. Precise masking and inpainting of English texts & guide lines
# We identify the text and line regions
gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
mask = np.zeros((h, w), dtype=np.uint8)

boxes = [
    # Top-left GPU English texts & lines
    (20, 75, 275, 205),
    # Top-center Glass waveguide text & line
    (220, 30, 430, 115),
    # Top-center-right circuitry text & line
    (530, 20, 710, 95),
    # Top-right 16-layer HBM4 text & lines
    (750, 30, 1010, 135),
    # Mid-right 16 distinct silicon layers text & line
    (820, 135, 1010, 210),
    # Right dimension indicator (8LL/11N)
    (870, 210, 950, 290),
    # Right edge line
    (840, 265, 925, 325),
    # Bottom-right Glass core text & line
    (730, 330, 1010, 420),
    # Bottom-right Photonic link text & line
    (640, 410, 920, 480),
    # Bottom-center Embedded circuitry text & line
    (560, 465, 780, 525),
    # Bottom-left Micro-bump text & lines
    (20, 325, 240, 390),
    # Bottom-left 2D schematic diagram (HIL, GPU, DIE, SIS)
    (15, 385, 240, 555),
    # Lower-left diagonal guideline
    (75, 250, 150, 330),
    # Bottom dimension guideline
    (420, 495, 540, 545)
]

for (x1, y1, x2, y2) in boxes:
    roi_gray = gray[y1:y2, x1:x2]
    # Local median background
    bg_val = np.median(roi_gray)
    # Bright text/lines
    thresh = (roi_gray > (bg_val + 10)).astype(np.uint8) * 255
    # Morphological dilation to thoroughly cover antialiased fringes
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    mask[y1:y2, x1:x2] = thresh

# Inpaint with generous radius
clean_bgr = cv2.inpaint(orig_img, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)

# For areas like bottom-left 2D schematic and upper text, do a subtle secondary pass with blur-blend to eliminate any faint residual text
for (x1, y1, x2, y2) in boxes:
    roi = clean_bgr[y1:y2, x1:x2]
    # gentle bilateral filter on the background patches
    clean_bgr[y1:y2, x1:x2] = cv2.bilateralFilter(roi, d=9, sigmaColor=35, sigmaSpace=35)

print("Text removal and inpainting completed.")

# 2. Expand Canvas to Full HD 1920 x 1080 Wide (Prevent any text truncation!)
CANVAS_W, CANVAS_H = 1920, 1080
canvas = np.zeros((CANVAS_H, CANVAS_W, 3), dtype=np.uint8)

# Sample background color gradient from original image edges
top_bg = np.median(clean_bgr[0:30, :], axis=(0, 1))
bottom_bg = np.median(clean_bgr[h-30:h, :], axis=(0, 1))
left_bg = np.median(clean_bgr[:, 0:30], axis=(0, 1))
right_bg = np.median(clean_bgr[:, w-30:w], axis=(0, 1))

# Overall dark blue-slate background color
base_bg = np.array([18, 14, 11], dtype=np.float32) # BGR
top_tint = np.array([28, 22, 16], dtype=np.float32)

# Create smooth vertical gradient background
for y in range(CANVAS_H):
    alpha = y / CANVAS_H
    color = (1.0 - alpha) * top_tint + alpha * base_bg
    canvas[y, :] = color.astype(np.uint8)

# Scale clean 3D graphic to fit harmoniously in center
# Original 1024x571 -> Scale up by 1.35x to ~1382x770
target_w = int(w * 1.35)
target_h = int(h * 1.35)
scaled_3d = cv2.resize(clean_bgr, (target_w, target_h), interpolation=cv2.INTER_LANCZOS4)

# Place 3D image centered with slight downward bias for top header
start_x = (CANVAS_W - target_w) // 2
start_y = 150 # Leave 150px at top, 160px at bottom

# Alpha blend edges of scaled_3d onto canvas so there are zero visible seams!
blend_mask = np.ones((target_h, target_w), dtype=np.float32)
edge_margin = 60
for i in range(edge_margin):
    factor = i / float(edge_margin)
    blend_mask[i, :] = np.minimum(blend_mask[i, :], factor)
    blend_mask[target_h - 1 - i, :] = np.minimum(blend_mask[target_h - 1 - i, :], factor)
    blend_mask[:, i] = np.minimum(blend_mask[:, i], factor)
    blend_mask[:, target_w - 1 - i] = np.minimum(blend_mask[:, target_w - 1 - i], factor)

blend_mask_3c = np.repeat(blend_mask[:, :, np.newaxis], 3, axis=2)

roi_canvas = canvas[start_y:start_y+target_h, start_x:start_x+target_w].astype(np.float32)
blended_roi = scaled_3d.astype(np.float32) * blend_mask_3c + roi_canvas * (1.0 - blend_mask_3c)
canvas[start_y:start_y+target_h, start_x:start_x+target_w] = np.clip(blended_roi, 0, 255).astype(np.uint8)

print("Canvas expansion and seamless blending complete.")

# 3. Draw Professional Patent Annotations (PIL)
pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img, "RGBA")

# Font configuration
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

font_title = get_font(34, bold=True)
font_label = get_font(21, bold=True)
font_badge = get_font(22, bold=True)
font_sub = get_font(16, bold=False)

# Color palette
CYAN = (0, 229, 255)
CYAN_BG = (0, 40, 60, 220)
GOLD = (255, 215, 0)
GOLD_BG = (60, 50, 10, 220)
WHITE = (255, 255, 255)
DARK_CARD = (10, 22, 35, 235)
BORDER_CYAN = (0, 200, 230, 255)
BORDER_GOLD = (255, 200, 50, 255)

# A. Header / Title Box (Top-Left)
draw.rounded_rectangle([50, 45, 340, 110], radius=10, fill=DARK_CARD, outline=BORDER_CYAN, width=2)
draw.text((75, 58), "【대표도】 (도 2)", font=font_title, fill=WHITE)

# B. Top Master Title Box: [100: 유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지]
box_100_x1, box_100_y1 = 440, 45
box_100_x2, box_100_y2 = 1480, 110
draw.rounded_rectangle([box_100_x1, box_100_y1, box_100_x2, box_100_y2], radius=10, fill=DARK_CARD, outline=BORDER_GOLD, width=2)

# Badge 100
draw.rounded_rectangle([box_100_x1 + 15, box_100_y1 + 14, box_100_x1 + 90, box_100_y1 + 51], radius=8, fill=GOLD, outline=None)
draw.text((box_100_x1 + 25, box_100_y1 + 18), "100", font=font_badge, fill=(10, 10, 10))
draw.text((box_100_x1 + 105, box_100_y1 + 20), "유리 기판 내장형 다파장 10진 광 인터커넥트 반도체 패키지", font=font_label, fill=WHITE)

# Helper function to draw leader line with pin anchor
def draw_leader(x_text, y_text, x_target, y_target, color=CYAN, is_left=True):
    # Leader line with horizontal segment and elbow
    if is_left:
        elbow_x = x_text + 20
        draw.line([(x_text, y_text), (elbow_x, y_text), (x_target, y_target)], fill=color, width=2)
    else:
        elbow_x = x_text - 20
        draw.line([(x_text, y_text), (elbow_x, y_text), (x_target, y_target)], fill=color, width=2)
    
    # Outer circle + glowing center dot at target
    r = 6
    draw.ellipse([x_target-r, y_target-r, x_target+r, y_target+r], outline=color, width=2)
    draw.ellipse([x_target-3, y_target-3, x_target+3, y_target+3], fill=WHITE)

# Function to draw callout card (Never truncated!)
def draw_callout(x, y, w_box, h_box, num_str, title_str, sub_str, target_xy, is_left=True, is_gold=False):
    border_col = BORDER_GOLD if is_gold else BORDER_CYAN
    badge_bg = GOLD if is_gold else CYAN
    badge_fg = (10, 10, 10)
    line_col = GOLD if is_gold else CYAN

    # Background box
    draw.rounded_rectangle([x, y, x + w_box, y + h_box], radius=8, fill=DARK_CARD, outline=border_col, width=2)

    # Number Badge
    badge_w = 65
    badge_h = 32
    draw.rounded_rectangle([x + 10, y + 10, x + 10 + badge_w, y + 10 + badge_h], radius=6, fill=badge_bg)
    # Center text in badge
    draw.text((x + 18, y + 13), num_str, font=font_badge, fill=badge_fg)

    # Title & Subtitle
    draw.text((x + 85, y + 14), title_str, font=font_label, fill=WHITE)
    if sub_str:
        draw.text((x + 85, y + 42), sub_str, font=font_sub, fill=(180, 210, 230))

    # Leader Line connecting to target
    if is_left:
        conn_x = x + w_box
        conn_y = y + h_box // 2
    else:
        conn_x = x
        conn_y = y + h_box // 2
    
    draw_leader(conn_x, conn_y, target_xy[0], target_xy[1], color=line_col, is_left=is_left)


# -------------------------------------------------------------------------
# C. LEFT CALLOUTS (Generously spaced in 50px ~ 480px left margin)
# -------------------------------------------------------------------------

# Target coordinates on scaled 3D image
# GPU Die: center around (start_x + target_w*0.34, start_y + target_h*0.37)
gpu_target = (start_x + int(target_w * 0.33), start_y + int(target_h * 0.35))
# Micro bumps under GPU: (start_x + target_w*0.27, start_y + target_h*0.48)
bump_target = (start_x + int(target_w * 0.26), start_y + int(target_h * 0.49))
# 10-dec Transmitter (Tx/MRR): (start_x + target_w*0.37, start_y + target_h*0.68)
tx_target = (start_x + int(target_w * 0.36), start_y + int(target_h * 0.69))

# 110: 인공지능 연산 칩렛 (AI GPU / NPU 다이)
draw_callout(
    x=50, y=200, w_box=420, h_box=72,
    num_str="110",
    title_str="인공지능 연산 칩렛",
    sub_str="(AI GPU / NPU 고성능 연산 다이)",
    target_xy=gpu_target,
    is_left=True
)

# 115: 마이크로 범프 어레이 (Micro-Bump Array)
draw_callout(
    x=50, y=410, w_box=420, h_box=72,
    num_str="115",
    title_str="마이크로 범프 어레이",
    sub_str="(고밀도 솔더 범프 신호/전원 재배선)",
    target_xy=bump_target,
    is_left=True
)

# 300: 10진 파장 송신 모듈 (Tx / MRR 어레이)
draw_callout(
    x=50, y=620, w_box=420, h_box=72,
    num_str="300",
    title_str="10진 파장 송신 모듈 (Tx)",
    sub_str="(마이크로 링 공진기 어레이 / 광원 결합)",
    target_xy=tx_target,
    is_left=True,
    is_gold=True
)


# -------------------------------------------------------------------------
# D. RIGHT CALLOUTS (Generously spaced in 1430px ~ 1870px right margin)
# -------------------------------------------------------------------------

# HBM4 Cube: around (start_x + target_w*0.72, start_y + target_h*0.30)
hbm_target = (start_x + int(target_w * 0.73), start_y + int(target_h * 0.28))
# 10-dec Receiver (Rx/AWG): around (start_x + target_w*0.65, start_y + target_h*0.42)
rx_target = (start_x + int(target_w * 0.64), start_y + int(target_h * 0.43))
# Glass Core Substrate: around (start_x + target_w*0.58, start_y + target_h*0.58)
glass_target = (start_x + int(target_w * 0.58), start_y + int(target_h * 0.58))
# 3D Optical Waveguide (Rainbow beam): around (start_x + target_w*0.48, start_y + target_h*0.62)
beam_target = (start_x + int(target_w * 0.49), start_y + int(target_h * 0.62))

# 120: 차세대 메모리 칩렛 (16단 HBM4 큐브)
draw_callout(
    x=1440, y=190, w_box=430, h_box=72,
    num_str="120",
    title_str="차세대 메모리 칩렛",
    sub_str="(16단 적층 HBM4 고대역폭 메모리)",
    target_xy=hbm_target,
    is_left=False
)

# 400: 10진 파장 수신 모듈 (Rx / AWG 및 PD)
draw_callout(
    x=1440, y=390, w_box=430, h_box=72,
    num_str="400",
    title_str="10진 파장 수신 모듈 (Rx)",
    sub_str="(어레이 도파로 회절격자 AWG & 포토다이오드)",
    target_xy=rx_target,
    is_left=False,
    is_gold=True
)

# 200: 초평탄 유리 코어 기판 (Glass Core Substrate)
draw_callout(
    x=1440, y=590, w_box=430, h_box=72,
    num_str="200",
    title_str="초평탄 유리 코어 기판",
    sub_str="(Glass Core: 무휨 초정밀 CPO 기판)",
    target_xy=glass_target,
    is_left=False
)

# 210: 유리 내장형 3D 광 도파로 (무지개 광 링크 λ0~λ9)
draw_callout(
    x=1440, y=790, w_box=430, h_box=72,
    num_str="210",
    title_str="3차원 내장형 광 도파로",
    sub_str="(무지개 10진 다파장 광 링크: λ0~λ9)",
    target_xy=beam_target,
    is_left=False
)

# Bottom Status Footer Bar
draw.rounded_rectangle([440, 990, 1480, 1050], radius=8, fill=(8, 16, 25, 240), outline=(0, 120, 180, 180), width=1)
footer_text = "주식회사 세이프티온 (SAFETYON) ┃ 유리 기판 10진 파장 광 인터커넥트 특허 대표도 (대한민국 특허청 KIPO 규격)"
draw.text((470, 1008), footer_text, font=font_sub, fill=(150, 190, 220))

# Save the final masterpiece images
out_png_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허_도2_대표도_최종완성.png'
out_jpg_path = r'C:\Users\LENOVO\Desktop\세이프티온_특허대표도_무지개10진_유리기판_HBM.jpg'

pil_img.save(out_png_path, "PNG", quality=100)
pil_img.convert("RGB").save(out_jpg_path, "JPEG", quality=98)

print(f"Successfully created 1920x1080 Patent Figure 2 at:\n  - {out_png_path}\n  - {out_jpg_path}")
