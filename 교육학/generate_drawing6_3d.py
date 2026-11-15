import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허6탄_도면들"
os.makedirs(output_dir, exist_ok=True)

fig = plt.figure(figsize=(18, 14), dpi=300)
ax = fig.add_subplot(111, projection='3d')

ax.set_title("도 6: 32단 초고적층 HBM 및 다이 계면 마이크로 TEC 능동 펠티어 냉각 3D 입체 절개 사시도", 
             fontsize=21, fontweight='bold', pad=30, color='#1A237E')

# 3D 큐브/슬래브 그리기 함수
def draw_slab(ax, x0, y0, z0, dx, dy, dz, facecolor, edgecolor, alpha=0.85):
    vertices = [
        [[x0, y0, z0], [x0+dx, y0, z0], [x0+dx, y0+dy, z0], [x0, y0+dy, z0]], # bottom
        [[x0, y0, z0+dz], [x0+dx, y0, z0+dz], [x0+dx, y0+dy, z0+dz], [x0, y0+dy, z0+dz]], # top
        [[x0, y0, z0], [x0+dx, y0, z0], [x0+dx, y0, z0+dz], [x0, y0, z0+dz]], # front
        [[x0, y0+dy, z0], [x0+dx, y0+dy, z0], [x0+dx, y0+dy, z0+dz], [x0, y0+dy, z0+dz]], # back
        [[x0, y0, z0], [x0, y0+dy, z0], [x0, y0+dy, z0+dz], [x0, y0, z0+dz]], # left
        [[x0+dx, y0, z0], [x0+dx, y0+dy, z0], [x0+dx, y0+dy, z0+dz], [x0+dx, y0, z0+dz]]  # right
    ]
    poly = Poly3DCollection(vertices, facecolors=facecolor, edgecolors=edgecolor, linewidths=1.5, alpha=alpha)
    ax.add_collection3d(poly)

# 1. 최하단 실리콘 인터포저 및 마이크로 증기챔버 (z=0 ~ 1.5)
draw_slab(ax, 0, 0, 0, 10, 10, 1.2, '#FFF9C4', '#FBC02D', alpha=0.9)

# 2. 베이스 로직 다이 (z=1.5 ~ 2.7)
draw_slab(ax, 0.5, 0.5, 1.5, 9, 9, 1.2, '#B0BEC5', '#37474F', alpha=0.85)

# 3. 하부 DRAM 적층군 (제1~8층) (z=3.0 ~ 5.0)
draw_slab(ax, 1.0, 1.0, 3.0, 8, 8, 1.8, '#E8F5E9', '#2E7D32', alpha=0.8)

# 4. 중앙 핫스팟 다이 계면 & 마이크로 TEC 필러 어레이 (z=5.2 ~ 7.0) (핵심 절개 구역)
# 베이스 계면 플레이트
draw_slab(ax, 1.0, 1.0, 5.0, 8, 8, 0.4, '#ECEFF1', '#455A64', alpha=0.6)

# 3D 마이크로 열전 필러 기둥들 (P형 및 N형 배열)
pillar_h = 1.6
for px in [2.5, 4.0, 5.5, 7.0]:
    for py in [2.5, 4.0, 5.5, 7.0]:
        # P형 (오렌지빛 Bi2Te3)
        draw_slab(ax, px-0.4, py-0.4, 5.4, 0.4, 0.4, pillar_h, '#FF7043', '#D84315', alpha=0.95)
        # N형 (청색빛 Bi2Se3)
        draw_slab(ax, px+0.1, py+0.1, 5.4, 0.4, 0.4, pillar_h, '#5C6BC0', '#283593', alpha=0.95)

# 상부 포논 다이오드 및 흡열단 (z=7.0 ~ 7.4)
draw_slab(ax, 1.0, 1.0, 7.0, 8, 8, 0.4, '#E1BEE7', '#8E24AA', alpha=0.85)

# 5. 상부 DRAM 적층군 (제17~32층) (z=7.6 ~ 9.6)
draw_slab(ax, 1.0, 1.0, 7.6, 8, 8, 1.8, '#E3F2FD', '#1565C0', alpha=0.75)

# 6. 최상단 고효율 히트스프레더 (z=9.8 ~ 10.6)
draw_slab(ax, 0.5, 0.5, 9.8, 9, 9, 0.8, '#90CAF9', '#0D47A1', alpha=0.85)

# 텍스트 라벨 (3D 공간 내 배치 및 대형 볼드 글씨)
ax.text(10.5, 5, 0.6, "① 실리콘 인터포저 내장\n   마이크로 증기챔버 (30)", fontsize=16, fontweight='bold', color='#E65100')
ax.text(10.2, 5, 2.1, "② 베이스 로직 다이 (10)\n   (지능형 PWM 열관리 엔진)", fontsize=16, fontweight='bold', color='#263238')
ax.text(9.5, 5, 3.9, "③ 하부 DRAM 다이층 (1~8층)\n   (다단 캐스케이드 방열)", fontsize=15, fontweight='bold', color='#1B5E20')

ax.text(9.5, 5, 6.2, "★ ④ 온칩 분산형 마이크로 TEC 필러 어레이 (110) ★\n   - P형(Bi2Te3) & N형(Bi2Se3) 펠티어 나노 기둥\n   - 나노 완충링(113) & 360도 동축 차폐링(114)\n   - 포논 다이오드(112) 역열류 100% 차단\n   [ 중앙 핫스팟 105℃ -> 80℃ 즉각 급랭! ]", 
        fontsize=16, fontweight='bold', color='#B71C1C', bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#FFCDD2"))

ax.text(9.5, 5, 8.5, "⑤ 상부 DRAM 다이층 (17~32층)\n   (32단 초고적층 구조)", fontsize=15, fontweight='bold', color='#0D47A1')
ax.text(10.0, 5, 10.2, "⑥ 최상단 히트스프레더 (20)", fontsize=16, fontweight='bold', color='#0D47A1')

# 3D 뷰 시점 설정 (입체 사시도 각도)
ax.view_init(elev=24, azim=-55)

ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.set_zlim(0, 12)

# 축 눈금 제거하여 깔끔한 CAD 느낌
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.axis('off')

plt.tight_layout()
target_file = os.path.join(output_dir, "도6_3D입체_패키지절개도.png")
plt.savefig(target_file, dpi=300)
plt.close()
print("도6 3D 입체 절개 사시도 생성 완료:", target_file)
