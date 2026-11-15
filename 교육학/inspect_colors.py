import numpy as np
from PIL import Image

src_path = r'C:/Users/LENOVO/.gemini/antigravity/brain/022db66e-d9b4-4946-a17a-1330d1eea034/.user_uploaded/media_1791709337620_23f9b2a6.png'
img = Image.open(src_path).convert('RGB')
arr = np.array(img)

# 모서리 색상 확인
print("Top-left color:", arr[5, 5])
print("Top-right color:", arr[5, -5])
print("Top-middle color:", arr[5, arr.shape[1]//2])

# 외곽 1-2픽셀 테두리 확인
print("Border check left 3 cols:", arr[10, :3])
print("Border check top 3 rows:", arr[:3, 10])
