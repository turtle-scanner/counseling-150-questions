import numpy as np
from PIL import Image

src_orig = r'C:/Users/LENOVO/.gemini/antigravity/brain/022db66e-d9b4-4946-a17a-1330d1eea034/.user_uploaded/media_1791709337620_23f9b2a6.png'
img_orig = Image.open(src_orig).convert('RGBA')

# 테두리 2px 크롭
w, h = img_orig.size
img_cropped = img_orig.crop((2, 2, w - 2, h - 2))

# 배경 제거: 배경은 회색-남색 계열 (R, G, B가 대체로 60~150 사이이고, 채도가 낮거나 파란빛)
arr = np.array(img_cropped)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# 배경 마스크 검출: 상단 모서리 배경 색상과 유사한 영역
# 인물 피부는 R>150, B<140이거나, 옷은 R<60 등 어두움
bg_mask = (r > 60) & (r < 150) & (g > 70) & (g < 155) & (b > 85) & (b < 180) & (r < g + 10) & (b >= g - 10)

# 머리카락/옷/피부 제외 보호
# 피부: R이 G보다 높고 B보다 뚜렷하게 높음 (R > G + 15)
skin_mask = (r > 130) & (r > g) & (g > b)
# 옷: R, G, B가 모두 매우 어두움 (< 50)
suit_mask = (r < 60) & (g < 65) & (b < 80)
# 넥타이: 파란색이지만 어두움
tie_mask = (b > r + 15) & (r < 80)

final_bg_mask = bg_mask & (~skin_mask) & (~suit_mask) & (~tie_mask)

# 배경을 흰색으로 교체
arr_white_bg = arr.copy()
arr_white_bg[final_bg_mask, :3] = [255, 255, 255]

img_white = Image.fromarray(arr_white_bg[:, :, :3])
# 350x450으로 리샘플링
img_white_neis = img_white.resize((350, 450), Image.Resampling.LANCZOS)

import os
desktop_path = os.path.expanduser(r'~\Desktop')
orig_save_path = os.path.join(desktop_path, '2027_임용고시_원서접수_여권사진_변귀섭(원본얼굴보존_흰배경).jpg')
img_white_neis.save(orig_save_path, 'JPEG', quality=95)
print(f"Saved original face preserved white-bg photo: {orig_save_path}")
