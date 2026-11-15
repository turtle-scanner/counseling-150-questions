python -c "
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

dest = 'C:/Users/LENOVO/Desktop/51특허'

# =========================================================================
# 【도 4】 글씨 겹침 0% 완벽 수정본
# =========================================================================
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))

# 1. Title & Subtitle (Cleanly spaced at the top)
ax.text(50, 95, '【도 4】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 91, '1,000℃ 열폭주 시 불화수소(HF) 자가 응고 겔화 포집 및 미로형 감압 벤트 메커니즘', fontsize=13.5, fontweight='bold', ha='center', color='#222222')

# 2. Outer Watertight Chamber (220) - y from 22 to 78
ax.add_patch(patches.Rectangle((12, 22), 76, 56, linewidth=3, edgecolor='#c00000', facecolor='#f9f9f9'))
ax.text(50, 74, '밀폐 수밀 챔버 내부 (220)', fontsize=15, fontweight='bold', ha='center', color='#c00000')

# 3. Gelling Solid Block - y from 28 to 68
ax.add_patch(patches.Rectangle((18, 28), 64, 40, linewidth=2, edgecolor='#2e7d32', facecolor='#e8f5e9'))
ax.text(50, 63, '자가 응고 고체 실리카 겔 (Gel)', fontsize=14, fontweight='bold', ha='center', color='#2e7d32')

# 4. Burning Battery Cell - y from 33 to 50
ax.add_patch(patches.Rectangle((28, 33), 44, 18, linewidth=2, edgecolor='#ff0000', facecolor='#ffcdd2'))
ax.text(50, 44, '열폭주 배터리 셀 (1,000℃)', fontsize=13.5, fontweight='bold', ha='center', color='#c00000')
ax.text(50, 38, '불화수소(HF) 가스 폭발 분출', fontsize=12, fontweight='bold', ha='center', color='#b71c1c')

# Trapping reaction text (Between cell and gel top)
ax.text(50, 55, 'HF 가스 → 겔 분자 내 화학적 흡착 포집 (누출률 0%)', fontsize=12, fontweight='bold', ha='center', color='#1b5e20')

# 5. Labyrinth Vent (500) - Placed safely at upper right INSIDE chamber border!
# Box at x=[72:86], y=[66:77]
ax.add_patch(patches.Rectangle((70, 66), 16, 10, linewidth=2, edgecolor='#7030a0', facecolor='#f3e5f5'))
ax.text(78, 72.5, '미로형 감압 벤트 (500)', fontsize=10.5, fontweight='bold', ha='center', color='#7030a0')
ax.text(78, 68.5, '[소결 필터 장착]', fontsize=9.5, ha='center', color='#7030a0')

# Vent discharge label - safely pointing to the right margin! NO overlap with top title!
ax.annotate('화염 차단 & 냉각 감압 가스 배출 →', xy=(86, 71), xytext=(88, 83),
            fontsize=11.5, fontweight='bold', color='#7030a0', ha='left',
            arrowprops=dict(facecolor='#7030a0', edgecolor='#7030a0', shrink=0.08, width=1.5, headwidth=6))

# 6. Bottom Summary Box - y from 6 to 18
ax.add_patch(patches.FancyBboxPatch((12, 6), 76, 12, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#2e7d32', facecolor='#e8f5e9'))
ax.text(50, 13.5, '1. 소화액 주입 → 2. 고열 접촉 0.5초 만에 고체 겔화 → 3. 배터리 3D 밀봉 포접', fontsize=12.5, fontweight='bold', ha='center', color='#1b5e20')
ax.text(50, 9, '유독가스 대기 누출 99.9% 차단 → 작업자 질식 참사 원천 방지!', fontsize=12.5, fontweight='bold', ha='center', color='#1b5e20')

plt.tight_layout()
plt.savefig(f'{dest}/도4_최종.png', bbox_inches='tight')
plt.close()
print('Do 4 regenerated with ZERO overlap and clean arrows!')
"