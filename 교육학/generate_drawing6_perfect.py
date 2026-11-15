import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허6탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# 캔버스를 좌우 2개로 분할: 좌측 3D 렌더링 + 우측 초대형 텍스트 설명 카드
fig = plt.figure(figsize=(24, 14), dpi=300)

# [좌측] 3D Exploded View 뷰포트
ax3d = fig.add_axes([0.02, 0.08, 0.52, 0.82], projection='3d')

# [우측] 2D 텍스트 설명 패널 (글씨 가려짐 원천 방지)
ax_text = fig.add_axes([0.55, 0.05, 0.43, 0.88])
ax_text.axis('off')

# 전체 상단 타이틀
fig.suptitle("도 6: 32단 초고적층 HBM 및 다이 계면 마이크로 TEC 능동 펠티어 냉각 3D 입체 절개 분해도", 
             fontsize=26, fontweight='bold', y=0.96, color='#1A237E')

# 3D 큐브/슬래브 그리기 함수
def draw_slab(ax, x0, y0, z0, dx, dy, dz, facecolor, edgecolor, alpha=0.9):
    vertices = [
        [[x0, y0, z0], [x0+dx, y0, z0], [x0+dx, y0+dy, z0], [x0, y0+dy, z0]], # bottom
        [[x0, y0, z0+dz], [x0+dx, y0, z0+dz], [x0+dx, y0+dy, z0+dz], [x0, y0+dy, z0+dz]], # top
        [[x0, y0, z0], [x0+dx, y0, z0], [x0+dx, y0, z0+dz], [x0, y0, z0+dz]], # front
        [[x0, y0+dy, z0], [x0+dx, y0+dy, z0], [x0+dx, y0+dy, z0+dz], [x0, y0+dy, z0+dz]], # back
        [[x0, y0, z0], [x0, y0+dy, z0], [x0, y0+dy, z0+dz], [x0, y0, z0+dz]], # left
        [[x0+dx, y0, z0], [x0+dx, y0+dy, z0], [x0+dx, y0+dy, z0+dz], [x0+dx, y0, z0+dz]]  # right
    ]
    poly = Poly3DCollection(vertices, facecolors=facecolor, edgecolors=edgecolor, linewidths=2.0, alpha=alpha)
    ax.add_collection3d(poly)

# 층간 간격을 시원하게 띄운 3D 분해도 (Exploded View)
# 1. 인터포저 및 마이크로 증기챔버 (z = 0 ~ 1.2)
draw_slab(ax3d, 0, 0, 0, 10, 10, 1.2, '#FFF59D', '#FBC02D', alpha=0.95)

# 2. 베이스 로직 다이 (z = 2.4 ~ 3.4)
draw_slab(ax3d, 0.5, 0.5, 2.4, 9, 9, 1.0, '#B0BEC5', '#37474F', alpha=0.9)

# 3. 하부 DRAM 적층군 (1~8층) (z = 4.6 ~ 6.2)
draw_slab(ax3d, 1.0, 1.0, 4.6, 8, 8, 1.6, '#C8E6C9', '#2E7D32', alpha=0.85)

# 4. [핵심] 중앙 마이크로 TEC 필러 어레이 & 포논 다이오드 (z = 7.4 ~ 9.8)
# 하부 전극판
draw_slab(ax3d, 1.0, 1.0, 7.4, 8, 8, 0.3, '#FFE082', '#E65100', alpha=0.7)

# P형(오렌지) 및 N형(블루) 마이크로 열전 기둥들
p_h = 1.6
for px in [2.6, 4.2, 5.8, 7.4]:
    for py in [2.6, 4.2, 5.8, 7.4]:
        # P형 (Bi2Te3)
        draw_slab(ax3d, px-0.45, py-0.45, 7.7, 0.45, 0.45, p_h, '#FF5722', '#BF360C', alpha=1.0)
        # N형 (Bi2Se3)
        draw_slab(ax3d, px+0.1, py+0.1, 7.7, 0.45, 0.45, p_h, '#3F51B5', '#1A237E', alpha=1.0)

# 상부 포논 다이오드 및 흡열 전극판 (z = 9.3 ~ 9.8)
draw_slab(ax3d, 1.0, 1.0, 9.3, 8, 8, 0.5, '#E1BEE7', '#6A1B9A', alpha=0.9)

# 5. 상부 DRAM 적층군 (17~32층) (z = 11.0 ~ 12.6)
draw_slab(ax3d, 1.0, 1.0, 11.0, 8, 8, 1.6, '#BBDEFB', '#1565C0', alpha=0.85)

# 6. 최상단 고효율 히트스프레더 (z = 13.8 ~ 14.8)
draw_slab(ax3d, 0.5, 0.5, 13.8, 9, 9, 1.0, '#90CAF9', '#0D47A1', alpha=0.95)

# 3D 뷰 시점
ax3d.view_init(elev=22, azim=-50)
ax3d.set_xlim(-1, 11)
ax3d.set_ylim(-1, 11)
ax3d.set_zlim(-1, 16)
ax3d.axis('off')

# ----------------------------------------------------
# [우측 패널] 글씨가 100% 또렷하게 보이는 초대형 설명 카드 배치
# ----------------------------------------------------
cards = [
    ("⑥ 최상단 고효율 히트스프레더 (20)", 
     "• 외부 수랭/공랭 방열판과 밀착되어 최종 열을 공기 중으로 방출",
     '#E3F2FD', '#1565C0', '#0D47A1', 0.85),

    ("⑤ 상부 DRAM 다이층 (17~32층)", 
     "• 32단 초고용량 적층 DRAM 메모리 셀 어레이\n• 2048비트 TSV 관통 전극 고속 데이터 버스 연결",
     '#E8F5E9', '#2E7D32', '#1B5E20', 0.69),

    ("★ ④ 온칩 분산형 마이크로 TEC 능동 냉각 어레이 (110) ★", 
     "• P형(Bi2Te3) & N형(Bi2Se3) 펠티어 나노 기둥 매트릭스 배열\n• 그래핀/h-BN 포논 다이오드 (112) : 역방향 열 누설 100% 차단!\n• 나노 탄성 완충 링 (113) : 열팽창 크랙/박리 0% 달성\n• 360도 동축 차폐 가드링 (114) : 2048비트 EMI 노이즈 60dB 차단\n▶ 중앙 핫스팟 105℃~125℃ -> 80℃ 이하로 25℃ 즉각 급랭!",
     '#FFEBEE', '#C62828', '#B71C1C', 0.44),

    ("③ 하부 DRAM 다이층 (1~8층)", 
     "• 상부에서 펌핑된 열을 막힘없이 하방으로 전달하는 다단 캐스케이드 경로",
     '#E8F5E9', '#2E7D32', '#1B5E20', 0.31),

    ("② 베이스 로직 다이 (10)", 
     "• 온칩 센서 실시간 모니터링 및 핫스팟 구역별 독립 PWM 펄스 제어\n• 정상 온도 도달 시 제벡(Seebeck) 자가발전 하베스팅 자동 전환",
     '#ECEFF1', '#455A64', '#263238', 0.18),

    ("① 실리콘 인터포저 내장 마이크로 증기챔버 (30)", 
     "• 하방으로 펌핑된 고열을 상변화 순환을 통해 패키지 외곽으로 수평 초고속 배출\n• 하부 베이스 다이의 열포화(Thermal Saturation) 현상 원천 해결!",
     '#FFFDE7', '#FBC02D', '#F57F17', 0.05)
]

for title, desc, fc, ec, tc, y_pos in cards:
    box_h = 0.12 if "④" not in title else 0.22
    # 배경 박스
    ax_text.add_patch(patches.FancyBboxPatch((0.02, y_pos), 0.96, box_h, 
                                             boxstyle="round,pad=0.03", facecolor=fc, edgecolor=ec, linewidth=3))
    # 제목
    ax_text.text(0.05, y_pos + box_h - 0.035, title, fontsize=18, fontweight='bold', color=tc, va='top')
    # 본문 설명
    ax_text.text(0.05, y_pos + box_h - 0.075, desc, fontsize=14, fontweight='bold', color='#212121', va='top', linespacing=1.3)

target_file = os.path.join(output_dir, "도6_3D입체_패키지절개도.png")
plt.savefig(target_file, dpi=300)
plt.close()
print("도6 좌우 분할 초대형 텍스트 카드 3D 도면 생성 완료:", target_file)
