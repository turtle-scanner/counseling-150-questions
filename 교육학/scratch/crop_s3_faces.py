# -*- coding: utf-8 -*-
from PIL import Image
import os
import json
import base64
from io import BytesIO

img_path = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0\.user_uploaded\media_1793683139288_5478174f.png"
img = Image.open(img_path)
W, H = img.size
print(f"Image W={W}, H={H}")

# 3 columns, 3 rows
# Let's inspect coordinates
# Col 0: x approx 18 to 195
# Col 1: x approx 218 to 395
# Col 2: x approx 418 to 595
# Row 0: y approx 10 to 225
# Row 1: y approx 305 to 520
# Row 2: y approx 600 to 815

grid_crops = {
    "caocao_s3": (20, 12, 195, 226),      # 1행 1열: 조조
    "liubei_s3": (220, 12, 395, 226),     # 1행 2열: 유비
    "sunquan_s3": (420, 12, 595, 226),    # 1행 3열: 손권
    "yuanshao_s3": (20, 305, 195, 520),   # 2행 1열: 원소
    "liuzhang_s3": (220, 305, 395, 520),  # 2행 2열: 유장
    "mateng_s3": (420, 305, 595, 520),    # 2행 3열: 마등
    "zhanglu_s3": (20, 600, 195, 815),    # 3행 1열: 장노
    "liubiao_s3": (220, 600, 395, 815),   # 3행 2열: 유표
}

out_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0\portraits_s3_extracted"
os.makedirs(out_dir, exist_ok=True)

b64_dict = {}
for name, box in grid_crops.items():
    crop = img.crop(box)
    p = os.path.join(out_dir, f"{name}.png")
    crop.save(p)
    
    buf = BytesIO()
    crop.save(buf, format="PNG")
    b64_str = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
    b64_dict[name] = b64_str
    print(f"Cropped {name}: {crop.size}, b64 len={len(b64_str)}")

# Save to json
json_path = os.path.join(out_dir, "s3_faces.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(b64_dict, f)

print("Saved s3_faces.json successfully!")
