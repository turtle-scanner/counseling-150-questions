import os
from PIL import Image

src_gen = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034\passport_photo_official_1791709443320.jpg'
img = Image.open(src_gen)
print("Original Generated Size:", img.size)

# 1. 나이스 표준 규격: 350 x 450 (3.5cm x 4.5cm 비율)
# 여권사진 규정: 얼굴(정수리부터 턱) 길이가 세로의 약 70-80%를 차지해야 함.
# 현재 이미지 비율을 350:450 (7:9)로 중앙 크롭 후 리사이즈
w, h = img.size
target_ratio = 350.0 / 450.0 # ~0.7778

current_ratio = w / h
if current_ratio > target_ratio:
    # 너비가 넓음 -> 좌우 크롭
    new_w = int(h * target_ratio)
    left = (w - new_w) // 2
    img_cropped = img.crop((left, 0, left + new_w, h))
else:
    # 세로가 긺 -> 상하 크롭 (얼굴 위치 고려하여 살짝 위쪽 기준)
    new_h = int(w / target_ratio)
    top = 0
    img_cropped = img.crop((0, top, w, top + new_h))

# 표준 나이스 제출용: 350 x 450
img_neis = img_cropped.resize((350, 450), Image.Resampling.LANCZOS)

# 고해상도 인쇄용: 413 x 531 (300 DPI 3.5cm x 4.5cm)
img_highres = img_cropped.resize((826, 1062), Image.Resampling.LANCZOS)

# 저장할 대상 경로들
desktop_path = os.path.expanduser(r'~\Desktop')
save_paths = [
    # 바탕화면
    os.path.join(desktop_path, '2027_임용고시_원서접수_여권사진_변귀섭(나이스용_350x450).jpg'),
    os.path.join(desktop_path, '2027_임용고시_원서접수_여권사진_변귀섭(고해상도).jpg'),
    # 작업 디렉토리
    r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\2027_임용고시_원서접수_여권사진_변귀섭.jpg',
    r'g:\내 드라이브\ANTI GRAVITY\전문상담임용고시\2027_임용고시_원서접수_여권사진_변귀섭.jpg'
]

# 바탕화면 나이스용 (용량 100KB 이하 최적화: quality=92)
img_neis.save(save_paths[0], 'JPEG', quality=92)
print(f"Saved: {save_paths[0]} ({os.path.getsize(save_paths[0]) // 1024} KB)")

# 바탕화면 고해상도용
img_highres.save(save_paths[1], 'JPEG', quality=95)
print(f"Saved: {save_paths[1]} ({os.path.getsize(save_paths[1]) // 1024} KB)")

# 작업 폴더 저장
img_neis.save(save_paths[2], 'JPEG', quality=92)
print(f"Saved: {save_paths[2]}")
img_neis.save(save_paths[3], 'JPEG', quality=92)
print(f"Saved: {save_paths[3]}")

print("All passport photos processed and saved successfully!")
