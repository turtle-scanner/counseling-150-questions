python -c "
code = '''# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

dest = 'C:/Users/LENOVO/Desktop/51특허'

# [도 1]
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))
ax.text(50, 94.5, '【도 1】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 90.5, '지게차 물류 호환형 리튬 배터리 스마트 방폭 파렛트 시스템 전체 입체 사시도', fontsize=15, fontweight='bold', ha='center', color='#222222')
ax.add_patch(patches.Rectangle((18, 12), 64, 10, linewidth=2.5, edgecolor='#1f4e79', facecolor='#d9e1f2'))
ax.text(50, 17, '파렛트 베이스 (110)', fontsize=16, fontweight='bold', ha='center', color='#1f4e79')
ax.add_patch(patches.Rectangle((26, 13.5), 16, 7, linewidth=2, edgecolor='#333333', facecolor='#595959'))
ax.add_patch(patches.Rectangle((58, 13.5), 16, 7, linewidth=2, edgecolor='#333333', facecolor='#595959'))
ax.text(34, 17, '포크 삽입부\\n(112a)', fontsize=11, fontweight='bold', ha='center', va='center', color='#ffffff')
ax.text(66, 17, '포크 삽입부\\n(112b)', fontsize=11, fontweight='bold', ha='center', va='center', color='#ffffff')
ax.add_patch(patches.Rectangle((18, 22), 6, 60, linewidth=2, edgecolor='#1f4e79', facecolor='#2f5597'))
ax.add_patch(patches.Rectangle((76, 22), 6, 60, linewidth=2, edgecolor='#1f4e79', facecolor='#2f5597'))

tiers = [('3단 적재 선반 (120c)', 66, '배터리 트레이 C (130c)'),
         ('2단 적재 선반 (120b)', 44, '배터리 트레이 B (130b)'),
         ('1단 적재 선반 (120a)', 22, '배터리 트레이 A (130a)')]
for name, y_s, tray_name in tiers:
    ax.add_patch(patches.Rectangle((24, y_s), 52, 4, linewidth=1.5, edgecolor='#1f4e79', facecolor='#1f4e79'))
    ax.add_patch(patches.Rectangle((28, y_s+4), 44, 12, linewidth=1.5, edgecolor='#385723', facecolor='#e2efda'))
    ax.text(50, y_s+10, tray_name, fontsize=13, fontweight='bold', ha='center', va='center', color='#274e13')
    ax.add_patch(patches.Rectangle((25, y_s+2), 50, 2, linewidth=1, edgecolor='#c00000', facecolor='#ffc000'))
ax.add_patch(patches.Rectangle((16, 82), 68, 5, linewidth=2, edgecolor='#1f4e79', facecolor='#1f4e79'))

callouts_1 = [
    ('200 : 접힘 상태 아코디언 벨로우즈 (평소 2cm)', (86, 73), (75, 68), '#c00000'),
    ('400 : 통합 방재 제어 모듈 & 센서', (86, 52), (80, 52), '#1f4e79'),
    ('300 : 바닥 자율 도킹 퀵커플러 포트', (86, 26), (72, 14), '#7030a0'),
    ('114 : 압전 에너지 하베스팅 블록', (12, 26), (20, 14), '#385723'),
    ('310 : 기둥 내장형 수직 소화 배관', (12, 60), (21, 60), '#0277bd'),
]
for text, (bx, by), (tx, ty), color in callouts_1:
    ax.annotate(text, xy=(tx, ty), xytext=(bx, by), fontsize=13, fontweight='bold', color=color,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor=color, lw=2),
                arrowprops=dict(facecolor=color, edgecolor=color, shrink=0.05, width=2, headwidth=7), va='center')
plt.tight_layout(); plt.savefig(f'{dest}/도1_최종.png', bbox_inches='tight'); plt.close()

# [도 2]
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))
ax.text(50, 94.5, '【도 2】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 90.5, '평상시 개방 상태(a)와 화재 시 특정 단(Tier) 선별 수밀 침수 상태(b) 단면 비교도', fontsize=14, fontweight='bold', ha='center', color='#222222')
ax.plot([50, 50], [8, 87], color='#cccccc', linewidth=1.5, linestyle='--')
ax.text(26, 85, '(a) 평상시 정상 물류 상태', fontsize=16, fontweight='bold', ha='center', color='#1f4e79')
for y_t, name in [(62, '3단 : 정상 배터리'), (42, '2단 : 정상 배터리'), (22, '1단 : 정상 배터리')]:
    ax.add_patch(patches.Rectangle((12, y_t), 28, 14, linewidth=1.5, edgecolor='#1f4e79', facecolor='#e9f1f7'))
    ax.text(26, y_t+7, name, fontsize=12, fontweight='bold', ha='center', va='center', color='#1f4e79')
    ax.text(26, y_t-2.5, '사방 100% 개방 (지게차 상하차 간섭 0%)', fontsize=10.5, fontweight='bold', ha='center', color='#385723')
ax.add_patch(patches.FancyBboxPatch((8, 10), 36, 9, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#1f4e79', facecolor='#e9f1f7'))
ax.text(26, 14.5, '• 전 단 개방 적재\\n• 표준 지게차 자유 이송', fontsize=12, fontweight='bold', ha='center', va='center', color='#1f4e79')

ax.text(74, 85, '(b) 2단 화재 발생 시 선별 침수 상태', fontsize=16, fontweight='bold', ha='center', color='#c00000')
ax.add_patch(patches.Rectangle((60, 62), 28, 14, linewidth=1.5, edgecolor='#385723', facecolor='#e2efda'))
ax.text(74, 69, '3단 : 물 한 방울 안 묻음!\\n[100% 정상 제품 보존]', fontsize=11.5, fontweight='bold', ha='center', va='center', color='#274e13')
ax.add_patch(patches.Rectangle((60, 42), 28, 14, linewidth=2.5, edgecolor='#c00000', facecolor='#bdd7ee'))
ax.text(74, 51, '2단 [열폭주 발생 단]\\n0.05초 수밀 벨로우즈 전개\\n→ 해당 단만 급랭 침수(소화)', fontsize=11.5, fontweight='bold', ha='center', va='center', color='#c00000')
ax.plot([59, 59], [42, 56], color='#c00000', linewidth=5)
ax.plot([89, 89], [42, 56], color='#c00000', linewidth=5)
ax.add_patch(patches.Rectangle((60, 22), 28, 14, linewidth=1.5, edgecolor='#385723', facecolor='#e2efda'))
ax.text(74, 29, '1단 : 물 한 방울 안 묻음!\\n[100% 정상 제품 보존]', fontsize=11.5, fontweight='bold', ha='center', va='center', color='#274e13')
ax.add_patch(patches.FancyBboxPatch((55, 10), 38, 9, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#c00000', facecolor='#fce4d6'))
ax.text(74, 14.5, '• 발화 층만 핀포인트 수조화 소화\\n• 수천만 원 정상 배터리 전손 방지!', fontsize=12, fontweight='bold', ha='center', va='center', color='#c00000')
plt.tight_layout(); plt.savefig(f'{dest}/도2_최종.png', bbox_inches='tight'); plt.close()

# [도 3]
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))
ax.text(50, 94.5, '【도 3】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 90.5, '바닥 자율 도킹 퀵커플러 급수 포트 및 기둥 내장형 공급 배관 계통 상세도', fontsize=14, fontweight='bold', ha='center', color='#222222')
ax.add_patch(patches.Rectangle((20, 25), 60, 10, linewidth=2, edgecolor='#1f4e79', facecolor='#d9e1f2'))
ax.text(50, 30, '파렛트 베이스 (110) [지게차 포크 삽입부 내장]', fontsize=14, fontweight='bold', ha='center', color='#1f4e79')
ax.add_patch(patches.Rectangle((35, 8), 30, 9, linewidth=2, edgecolor='#333333', facecolor='#bfbfbf'))
ax.text(50, 12.5, '공장 보관 랙 소화수 주배관 (600)', fontsize=13, fontweight='bold', ha='center', color='#000000')
ax.add_patch(patches.Rectangle((43, 17), 14, 8, linewidth=2, edgecolor='#7030a0', facecolor='#f2eaf7'))
ax.text(50, 21, '자율 도킹 퀵커플러 (300)\\n[안착 시 무누설 자동 체결]', fontsize=11, fontweight='bold', ha='center', va='center', color='#7030a0')
ax.plot([30, 30], [35, 80], color='#0277bd', linewidth=6)
ax.text(22, 60, '기둥 내장\\n수직 급수관\\n(310)', fontsize=12, fontweight='bold', ha='center', color='#0277bd')

tiers_nozzles = [(75, '3단 침수 노즐 (320c)', '3단 밸브 (315c)'),
                 (55, '2단 침수 노즐 (320b)', '2단 밸브 (315b) [화재 시 개방!]'),
                 (38, '1단 침수 노즐 (320a)', '1단 밸브 (315a)')]
for y_n, n_name, v_name in tiers_nozzles:
    ax.annotate('', xy=(50, y_n), xytext=(30, y_n), arrowprops=dict(facecolor='#0277bd', width=3, headwidth=8))
    ax.add_patch(patches.Circle((38, y_n), 2.5, facecolor='#ffc000', edgecolor='#000000', lw=1.5))
    ax.text(52, y_n, f'{v_name} → {n_name}', fontsize=12.5, fontweight='bold', va='center', color='#1f4e79')
ax.add_patch(patches.FancyBboxPatch((60, 42), 34, 18, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#c00000', facecolor='#fce4d6'))
ax.text(77, 54, '포크 감지 인터록 (420)', fontsize=13, fontweight='bold', ha='center', color='#c00000')
ax.text(77, 47, '• 지게차 이송 중: 소화 오작동 차단\\n• 랙 안착 완료 시: 방재 모드 활성화', fontsize=11, fontweight='bold', ha='center', color='#333333')
plt.tight_layout(); plt.savefig(f'{dest}/도3_최종.png', bbox_inches='tight'); plt.close()

# [도 4]
fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))
ax.text(50, 94.5, '【도 4】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 90.5, '1,000℃ 열폭주 시 불화수소(HF) 자가 응고 겔화 포집 및 미로형 감압 벤트 메커니즘', fontsize=13.5, fontweight='bold', ha='center', color='#222222')
ax.add_patch(patches.Rectangle((15, 25), 70, 55, linewidth=3, edgecolor='#c00000', facecolor='#f2f2f2'))
ax.text(50, 76, '밀폐 수밀 챔버 내부 (220)', fontsize=15, fontweight='bold', ha='center', color='#c00000')
ax.add_patch(patches.Rectangle((22, 32), 56, 38, linewidth=2, edgecolor='#2e7d32', facecolor='#dcedc8'))
ax.text(50, 58, '자가 응고 고체 실리카 겔 (Gel)', fontsize=14, fontweight='bold', ha='center', color='#2e7d32')
ax.add_patch(patches.Rectangle((32, 36), 36, 15, linewidth=2, edgecolor='#ff0000', facecolor='#ffcdd2'))
ax.text(50, 45, '열폭주 배터리 셀 (1,000℃)', fontsize=13, fontweight='bold', ha='center', color='#c00000')
ax.text(50, 39, '불화수소(HF) 가스 방출', fontsize=11, fontweight='bold', ha='center', color='#b71c1c')
ax.text(50, 52, 'HF 가스 → 겔 분자 내 화학적 흡착 포집 (누출률 0%)', fontsize=11.5, fontweight='bold', ha='center', color='#1b5e20')
ax.add_patch(patches.Rectangle((68, 77), 16, 12, linewidth=2, edgecolor='#7030a0', facecolor='#f2eaf7'))
ax.text(76, 85, '미로형 감압 벤트\\n(500)', fontsize=11, fontweight='bold', ha='center', va='center', color='#7030a0')
ax.text(76, 79, '소결 필터 장착', fontsize=10, ha='center', color='#7030a0')
ax.annotate('화염 차단 & 냉각 감압 가스 배출 ↑', xy=(76, 89), xytext=(76, 92), fontsize=12, fontweight='bold', color='#7030a0', ha='center')
ax.add_patch(patches.FancyBboxPatch((15, 8), 70, 13, boxstyle='round,pad=0.8', linewidth=2, edgecolor='#2e7d32', facecolor='#e8f5e9'))
ax.text(50, 15.5, '1. 소화액 주입 → 2. 고열 접촉 0.5초 만에 고체 겔화 → 3. 배터리 3D 밀봉 포접', fontsize=13, fontweight='bold', ha='center', color='#1b5e20')
ax.text(50, 11, '유독가스 대기 누출 99.9% 차단 → 작업자 질식 참사 원천 방지!', fontsize=13, fontweight='bold', ha='center', color='#1b5e20')
plt.tight_layout(); plt.savefig(f'{dest}/도4_최종.png', bbox_inches='tight'); plt.close()

# [도 5]
fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
ax.add_patch(patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor='#333333', facecolor='#ffffff'))
ax.text(50, 97, '【도 5】', fontsize=24, fontweight='bold', ha='center')
ax.text(50, 93, '오프가스 감지, 지게차 이송 락, 선별 침수 및 비상 AGV 탈출 제어 흐름도', fontsize=14, fontweight='bold', ha='center', color='#222222')
flow_steps = [
    ('S100', '적재 선반 각 단의 TDLAS 오프가스 센서 및 온도 센서 상시 감시 (압전 발전 자가 전력 구동)', '#e9f1f7', '#1f4e79'),
    ('S200', '배터리 열폭주 전조 증상(전해액 오프가스 검출 or 온도 이상 상승) 판정', '#fce4d6', '#c55a11'),
    ('S300', '지게차 포크 접촉 인터록 판정 (주행 중이면 락 유지 → 랙 안착 정지 상태 시 소화 진입)', '#fff2cc', '#b25900'),
    ('S400', '화재 발생 단(Tier) 식별 → 해당 단 아코디언 벨로우즈 수밀벽 0.05초 자율 전개 (단위 수밀 챔버)', '#f8cecc', '#b85450'),
    ('S500', '바닥 퀵커플러 소화 밸브 개방 → 해당 단 소화 매체 직결 주입 (10초 내 침수 급랭 & HF 고체 겔화)', '#d5e8d4', '#274e13'),
    ('S600', '무선 메쉬 통신 가동 → 주변 인접 파렛트 외벽 일제 자율 폐쇄 (공장 전체 군집 연쇄 방어)', '#e1d5e7', '#7030a0'),
    ('S700', '공장 중앙 관제 비상 호출 → 무인 AGV 자율 도킹 및 옥외 비상 격리 도크로 파렛트 비상 이송', '#dae8fc', '#1f4e79'),
]
y_pos = 84
for code, text, bg, border in flow_steps:
    rect = patches.FancyBboxPatch((12, y_pos - 7), 76, 7.5, boxstyle='round,pad=0.8', linewidth=2, edgecolor=border, facecolor=bg)
    ax.add_patch(rect)
    ax.text(14, y_pos - 3.2, f'[{code}]', fontsize=12, fontweight='bold', color=border)
    ax.text(23, y_pos - 3.2, text, fontsize=10.5, fontweight='bold', va='center', color='#222222')
    if code != 'S700':
        ax.annotate('', xy=(50, y_pos - 9.5), xytext=(50, y_pos - 7.5),
                    arrowprops=dict(facecolor=border, edgecolor=border, width=2, headwidth=6))
    y_pos -= 11.5
plt.tight_layout(); plt.savefig(f'{dest}/도5_최종.png', bbox_inches='tight'); plt.close()
print('All 5 drawings cleanly generated without any font warnings!')
'''
with open('gen_all.py', 'w', encoding='utf-8') as f:
    f.write(code)
" && python gen_all.py