import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허5탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 도 4: 열감응형 절연 퓨즈(Thermal Isolation Fuse) 동작 상태도 (초대형 글씨 업그레이드)
# ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 11), dpi=300)

# [상태 A] 검사 단계 : 상온 25℃
ax1.set_title("[검사 단계 : 상온 25℃]\n열감응 퓨즈 통전 (ON) -> 비접촉 RF 검사 가동", 
              fontsize=22, fontweight='bold', pad=25, color='#0D47A1')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# 상단 박스: 마이크로 공진 루프 회로 (120)
ax1.add_patch(patches.Rectangle((1.0, 6.2), 8.0, 2.3, facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=3))
ax1.text(5.0, 7.35, "마이크로 공진 루프 회로 (120)", fontsize=22, fontweight='bold', ha='center', va='center', color='#0D47A1')

# 연결선 1
ax1.plot([5.0, 5.0], [6.2, 5.2], color='#1B5E20', linewidth=5)

# 중간 박스: 열감응 저융점 나노 합금 (141) [ON]
ax1.add_patch(patches.Rectangle((1.5, 3.8), 7.0, 1.4, facecolor='#C8E6C9', edgecolor='#2E7D32', linewidth=3))
ax1.text(5.0, 4.5, "열감응 저융점 나노 합금 (141)\n[ 연결 상태 : 통전(ON) ]", fontsize=20, fontweight='bold', ha='center', va='center', color='#1B5E20')

# 연결선 2
ax1.plot([5.0, 5.0], [3.8, 2.8], color='#1B5E20', linewidth=5)

# 하단 박스: 내부 DRAM 데이터 라인 (130)
ax1.add_patch(patches.Rectangle((1.0, 0.8), 8.0, 2.0, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=3))
ax1.text(5.0, 1.8, "내부 DRAM 데이터 라인 (130)", fontsize=22, fontweight='bold', ha='center', va='center', color='#263238')

# 하단 결과
ax1.text(5.0, 0.2, "▶ 결과: 검사용 신호 흐름 100% 정상 활성화", fontsize=18, fontweight='bold', ha='center', color='#0D47A1')


# [상태 B] 하이브리드 본딩 열압착 단계 : 180~200℃
ax2.set_title("[하이브리드 본딩 열압착 : 180~200℃]\n열감응 퓨즈 용융 절연 (OFF) -> 노이즈 100% 차단", 
              fontsize=22, fontweight='bold', pad=25, color='#B71C1C')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

# 상단 박스: 마이크로 공진 루프 (120) [완전 격리]
ax2.add_patch(patches.Rectangle((1.0, 6.2), 8.0, 2.3, facecolor='#ECEFF1', edgecolor='#78909C', linewidth=3))
ax2.text(5.0, 7.35, "마이크로 공진 루프 (120)\n[ 완전 격리 / 비활성화 ]", fontsize=21, fontweight='bold', ha='center', va='center', color='#546E7A')

# 연결선 (끊어짐 표시)
ax2.plot([3.8, 3.8], [6.2, 5.2], color='#C62828', linewidth=4)
ax2.plot([6.2, 6.2], [3.8, 2.8], color='#C62828', linewidth=4)

# 중간 분리된 퓨즈 박스 2개
ax2.add_patch(patches.Rectangle((2.3, 3.8), 2.2, 1.4, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=3))
ax2.add_patch(patches.Rectangle((5.5, 3.8), 2.2, 1.4, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=3))
ax2.text(5.0, 4.5, "단선\n(OPEN)", fontsize=21, fontweight='bold', ha='center', va='center', color='#B71C1C')

# 우측 열 인가 배지
ax2.add_patch(patches.FancyBboxPatch((7.9, 3.8), 1.9, 1.4, boxstyle="round,pad=0.1", facecolor='#FBE9E7', edgecolor='#FF5722', linewidth=2.5))
ax2.text(8.85, 4.5, "열 인가\n(180~200℃)", fontsize=16, fontweight='bold', ha='center', va='center', color='#D84315')

# 하단 박스: 내부 DRAM 데이터 라인 (130)
ax2.add_patch(patches.Rectangle((1.0, 0.8), 8.0, 2.0, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=3))
ax2.text(5.0, 1.8, "내부 DRAM 데이터 라인 (130)\n[ HBM4 정상 동작 / 기생 노이즈 0% ]", fontsize=20, fontweight='bold', ha='center', va='center', color='#1B5E20')

# 하단 결과
ax2.text(5.0, 0.2, "▶ 결과: 양산 동작 시 RF 간섭 및 기생 손실 영구 제거!", fontsize=18, fontweight='bold', ha='center', color='#B71C1C')

plt.tight_layout()
target_file = os.path.join(output_dir, "도4_열감응퓨즈_절연동작도.png")
plt.savefig(target_file, dpi=300)
plt.close()
print("도4 초대형 볼드 글씨 업그레이드 완료:", target_file)
