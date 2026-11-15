python -c "
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

dest = 'C:/Users/LENOVO/Desktop/51특허'

# =========================================================================
# 【도 2】 글씨 겹침 0% 완벽 수정본
# =========================================================================
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))

# Title
ax.text(50, 95, '【도 2】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 91, '평상시 개방 상태(a)와 화재 시 특정 단(Tier) 선별 수밀 침수 상태(b) 단면 비교도', fontsize=14, fontweight='bold', ha='center', color='#222222')
ax.plot([50, 50], [6, 87], color='#cccccc', linewidth=1.5, linestyle='--')

# (a) 평상시 상태
ax.text(26, 85, '(a) 평상시 정상 물류 상태', fontsize=17, fontweight='bold', ha='center', color='#1f4e79')

# 3단, 2단, 1단 박스 위치 (높이 11, 간격 넉넉히)
# 3단: y=68~79, 텍스트 y=64.5
# 2단: y=49~60, 텍스트 y=45.5
# 1단: y=30~41, 텍스트 y=26.5
# 하단박스: y=9~21

tiers_a = [
    (68, '3단 : 정상 배터리 트레이', 64.5),
    (49, '2단 : 정상 배터리 트레이', 45.5),
    (30, '1단 : 정상 배터리 트레이', 26.5),
]

for y_box, name, y_sub in tiers_a:
    ax.add_patch(patches.Rectangle((12, y_box), 28, 11, linewidth=2, edgecolor='#1f4e79', facecolor='#e9f1f7'))
    ax.text(26, y_box + 5.5, name, fontsize=13, fontweight='bold', ha='center', va='center', color='#1f4e79')
    ax.text(26, y_sub, '사방 100% 개방 (지게차 상하차 간섭 0%)', fontsize=11, fontweight='bold', ha='center', color='#385723')

# 하단 요약 박스 (a) - y=9 ~ 21 (겹침 완전 없음!)
ax.add_patch(patches.FancyBboxPatch((8, 9), 36, 12, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#1f4e79', facecolor='#e9f1f7'))
ax.text(26, 16.5, '• 전 단 개방 적재', fontsize=13, fontweight='bold', ha='center', color='#1f4e79')
ax.text(26, 12.5, '• 표준 지게차 자유 이송', fontsize=13, fontweight='bold', ha='center', color='#1f4e79')

# (b) 화재 발생 시 선별 침수 상태
ax.text(74, 85, '(b) 2단 화재 발생 시 선별 침수 상태', fontsize=17, fontweight='bold', ha='center', color='#c00000')

# 3단 (정상)
ax.add_patch(patches.Rectangle((60, 68), 28, 11, linewidth=2, edgecolor='#2e7d32', facecolor='#e8f5e9'))
ax.text(74, 75, '3단 : 물 한 방울 안 묻음!', fontsize=12.5, fontweight='bold', ha='center', color='#1b5e20')
ax.text(74, 71, '[100% 정상 제품 보존]', fontsize=11.5, fontweight='bold', ha='center', color='#2e7d32')

# 2단 (화재 발생 ➔ 침수 소화)
ax.add_patch(patches.Rectangle((60, 49), 28, 11, linewidth=2.5, edgecolor='#c00000', facecolor='#bdd7ee'))
ax.text(74, 56.5, '2단 [열폭주 발생 단]', fontsize=12.5, fontweight='bold', ha='center', color='#c00000')
ax.text(74, 52.5, '0.05초 수밀 벨로우즈 전개', fontsize=11.5, fontweight='bold', ha='center', color='#b71c1c')
ax.text(74, 45.5, '→ 해당 단만 핀포인트 급랭 침수(소화)', fontsize=11.5, fontweight='bold', ha='center', color='#c00000')

# 2단 좌우 벨로우즈 수밀벽 두껍게 표시
ax.plot([59, 59], [49, 60], color='#c00000', linewidth=6)
ax.plot([89, 89], [49, 60], color='#c00000', linewidth=6)

# 1단 (정상)
ax.add_patch(patches.Rectangle((60, 30), 28, 11, linewidth=2, edgecolor='#2e7d32', facecolor='#e8f5e9'))
ax.text(74, 37, '1단 : 물 한 방울 안 묻음!', fontsize=12.5, fontweight='bold', ha='center', color='#1b5e20')
ax.text(74, 33, '[100% 정상 제품 보존]', fontsize=11.5, fontweight='bold', ha='center', color='#2e7d32')

# 하단 요약 박스 (b) - y=9 ~ 21 (겹침 완전 없음!)
ax.add_patch(patches.FancyBboxPatch((54, 9), 40, 12, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#c00000', facecolor='#fce4d6'))
ax.text(74, 16.5, '• 발화 층만 핀포인트 수조화 소화', fontsize=13, fontweight='bold', ha='center', color='#c00000')
ax.text(74, 12.5, '• 수천만 원 정상 배터리 전손 방지!', fontsize=13, fontweight='bold', ha='center', color='#c00000')

plt.tight_layout()
plt.savefig(f'{dest}/도2_최종.png', bbox_inches='tight')
plt.close()
print('Do 2 regenerated with ZERO overlap!')
"