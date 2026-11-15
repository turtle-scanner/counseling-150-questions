import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허6탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 도 4: 화살표 글씨 겹침 100% 박멸 & 초깔끔 정밀 배치
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(19, 13), dpi=300)
ax.set_title("도 4: 32단 초고적층 HBM의 다단 캐스케이드 펌핑 및 증기챔버 수평 열배출 구조", 
             fontsize=23, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 19)
ax.set_ylim(0, 13)
ax.axis('off')

# 6개 박스의 정확한 y좌표 및 높이 (간격을 시원하게 1.0 이상 확보)
layers = [
    ("최상단 고효율 방열판 (Heat Spreader) (20) [외부 방열판으로 열 최종 방출]", '#90CAF9', '#0D47A1', '#0D47A1', 10.8),
    ("DRAM 다이 제25층~제32층 [TEC 제4단 열 펌핑 캐스케이드]", '#E3F2FD', '#1976D2', '#1565C0', 8.8),
    ("DRAM 다이 제17층~제24층 [TEC 제3단 열 펌핑 캐스케이드]", '#E1F5FE', '#0288D1', '#01579B', 6.8),
    ("★ DRAM 다이 제9층~제16층 [중앙 핫스팟 집중 흡열단 : 105℃ -> 80℃ 급랭] ★", '#FFCDD2', '#C62828', '#B71C1C', 4.8),
    ("DRAM 다이 제1층~제8층 [TEC 제1단 열 배출 캐스케이드]", '#E8F5E9', '#2E7D32', '#1B5E20', 2.8),
    ("실리콘 인터포저 내장 마이크로 증기챔버 (30) [초고속 수평 열분산 -> 하부 열포화 0%]", '#FFF9C4', '#FBC02D', '#E65100', 0.8)
]

box_x = 1.2
box_w = 14.2
box_h = 1.2

for title, fc, ec, tc, y in layers:
    # 박스 그리기
    ax.add_patch(patches.Rectangle((box_x, y), box_w, box_h, facecolor=fc, edgecolor=ec, linewidth=3))
    # 텍스트는 박스 정중앙에 배치 (절대 화살표와 겹치지 않음)
    ax.text(box_x + box_w/2, y + box_h/2, title, fontsize=18, fontweight='bold', ha='center', va='center', color=tc)

# 박스와 박스 사이의 '순수한 빈 공간'에만 깔끔한 화살표 연결!
# 각 화살표 시작: 윗박스 바닥 (y), 끝: 아랫박스 뚜껑 (y_next + box_h)
arrow_y_pairs = [
    (10.8, 8.8 + box_h),  # Spreader -> Layer 25-32
    (8.8, 6.8 + box_h),   # Layer 25-32 -> Layer 17-24
    (6.8, 4.8 + box_h),   # Layer 17-24 -> Layer 9-16 (Hotspot)
    (4.8, 2.8 + box_h),   # Hotspot -> Layer 1-8
    (2.8, 0.8 + box_h)    # Layer 1-8 -> Vapor Chamber
]

# 중앙 정렬 화살표 (두께 4, 깔끔한 헤드)
for y_top, y_bot in arrow_y_pairs:
    mid_x = box_x + box_w/2
    # 여백 0.15씩 두어 박스 테두리에 딱 붙지 않고 깔끔하게 떨어짐
    ax.annotate("", 
                xy=(mid_x, y_bot + 0.12), 
                xytext=(mid_x, y_top - 0.12),
                arrowprops=dict(facecolor='#D32F2F', edgecolor='#B71C1C', width=4, headwidth=13, headlength=11))

# 우측 캐스케이드 열 압송 안내 카드 (위치 여유 있게 안쪽으로 배치)
badge_x = 16.0
badge_y = 4.2
ax.add_patch(patches.FancyBboxPatch((badge_x, badge_y), 2.6, 3.8, 
                                     boxstyle="round,pad=0.25", facecolor='#FFEBEE', edgecolor='#D32F2F', linewidth=3))
ax.text(badge_x + 1.3, badge_y + 1.9, 
        "단계별\n캐스케이드\n열 강제 압송\n\n(Peltier\nActive\nPumping)", 
        fontsize=17, fontweight='bold', ha='center', va='center', color='#B71C1C', linespacing=1.25)

# 하방 압송 전체 흐름 대형 점선 화살표 (우측 뱃지에서 아랫방향)
ax.annotate("", xy=(badge_x + 1.3, 1.8), xytext=(badge_x + 1.3, 4.0),
            arrowprops=dict(facecolor='#D32F2F', edgecolor='#B71C1C', width=3, headwidth=10, linestyle='--'))
ax.text(badge_x + 1.3, 1.2, "하방 고속 배출", fontsize=14, fontweight='bold', ha='center', color='#B71C1C')

plt.tight_layout()
target_file = os.path.join(output_dir, "도4_다단캐스케이드_열펌핑도.png")
plt.savefig(target_file, dpi=300)
plt.close()
print("도4 화살표 글씨 겹침 완전 해결 완료:", target_file)
