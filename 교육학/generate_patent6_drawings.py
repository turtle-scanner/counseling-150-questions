import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허6탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 도 1: 종래 수동 방열 vs 본 발명 능동 마이크로 TEC 펠티어 냉각 비교도
# ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 11), dpi=300)

# [좌측] 종래 수동 방열
ax1.set_title("[종래 기술] 외장 히트싱크 기반 수동 방열\n(다이 계면 열저항 누적 -> 105~125℃ 핫스팟 폭발)", 
              fontsize=20, fontweight='bold', pad=20, color='#B71C1C')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 11)
ax1.axis('off')

# 외장 히트싱크
ax1.add_patch(patches.Rectangle((1.5, 9.2), 7.0, 1.2, facecolor='#90A4AE', edgecolor='#37474F', linewidth=2.5))
ax1.text(5.0, 9.8, "외장 히트싱크 / 쿨러 (1)", fontsize=18, fontweight='bold', ha='center', va='center')

# 상단 DRAM 다이들
ax1.add_patch(patches.Rectangle((2.0, 7.2), 6.0, 1.5, facecolor='#CFD8DC', edgecolor='#455A64', linewidth=2))
ax1.text(5.0, 7.95, "상부 DRAM 다이층 (16~32층) [85℃]", fontsize=16, fontweight='bold', ha='center', va='center')

# 중앙 다이 핫스팟 (적색 폭발)
ax1.add_patch(patches.Rectangle((2.0, 4.2), 6.0, 2.5, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=3.5))
ax1.text(5.0, 5.7, "★ 중앙 적층 다이 계면 (8~16층) ★\n[ 극심한 열 고립 핫스팟 : 105℃~125℃ ]", fontsize=18, fontweight='bold', ha='center', va='center', color='#B71C1C')
ax1.text(5.0, 4.8, "※ DRAM 리프레시 붕괴 & 데이터 증발 발생!", fontsize=15, fontweight='bold', ha='center', va='center', color='#D50000')

# 하부 DRAM 및 베이스 다이
ax1.add_patch(patches.Rectangle((2.0, 2.2), 6.0, 1.5, facecolor='#CFD8DC', edgecolor='#455A64', linewidth=2))
ax1.text(5.0, 2.95, "하부 DRAM 다이층 (1~8층) [90℃]", fontsize=16, fontweight='bold', ha='center', va='center')

ax1.add_patch(patches.Rectangle((1.5, 0.5), 7.0, 1.2, facecolor='#B0BEC5', edgecolor='#263238', linewidth=2))
ax1.text(5.0, 1.1, "베이스 로직 다이 및 인터포저 (2)", fontsize=17, fontweight='bold', ha='center', va='center')

# 열 막힘 화살표
ax1.text(8.8, 5.5, "열 탈출 불가\n(열저항 Rth 누적)", fontsize=15, fontweight='bold', ha='center', color='#B71C1C')


# [우측] 본 발명 능동 마이크로 TEC 펠티어 냉각
ax2.set_title("[본 발명] 온칩 분산형 마이크로 TEC 능동 펠티어 냉각\n(더미 비아 내장 전자 펌핑 -> 핫스팟 25℃ 즉각 급속 냉각)", 
              fontsize=20, fontweight='bold', pad=20, color='#0D47A1')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 11)
ax2.axis('off')

# 외장 히트스프레더
ax2.add_patch(patches.Rectangle((1.5, 9.2), 7.0, 1.2, facecolor='#BBDEFB', edgecolor='#1565C0', linewidth=2.5))
ax2.text(5.0, 9.8, "고효율 히트스프레더 (20)", fontsize=18, fontweight='bold', ha='center', va='center', color='#0D47A1')

# 상단 DRAM 다이
ax2.add_patch(patches.Rectangle((2.0, 7.2), 6.0, 1.5, facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2))
ax2.text(5.0, 7.95, "상부 DRAM 다이층 (16~32층) [75℃ 유지]", fontsize=16, fontweight='bold', ha='center', va='center')

# 중앙 다이 계면 (능동 냉각)
ax2.add_patch(patches.Rectangle((2.0, 4.2), 6.0, 2.5, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=3.5))
ax2.text(5.0, 5.7, "★ 중앙 다이 계면 마이크로 TEC 냉각 ★\n[ 펠티어 전자 펌핑 : 105℃ -> 80℃ 급랭! ]", fontsize=18, fontweight='bold', ha='center', va='center', color='#1B5E20')
ax2.text(5.0, 4.8, "온칩 P-N 열전 필러 (110) [Bi2Te3/Bi2Se3]", fontsize=16, fontweight='bold', ha='center', va='center', color='#2E7D32')

# 하부 DRAM 및 베이스 다이
ax2.add_patch(patches.Rectangle((2.0, 2.2), 6.0, 1.5, facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2))
ax2.text(5.0, 2.95, "하부 DRAM 다이층 (1~8층) [78℃ 유지]", fontsize=16, fontweight='bold', ha='center', va='center')

ax2.add_patch(patches.Rectangle((1.5, 0.5), 7.0, 1.2, facecolor='#90CAF9', edgecolor='#0D47A1', linewidth=2.5))
ax2.text(5.0, 1.1, "베이스 로직 다이 (10) [PWM 드라이버 내장]", fontsize=17, fontweight='bold', ha='center', va='center', color='#0D47A1')

# 강제 열 펌핑 화살표
ax2.annotate("", xy=(8.5, 1.8), xytext=(8.5, 6.0), arrowprops=dict(facecolor='#0288D1', edgecolor='#01579B', width=4, headwidth=12))
ax2.text(8.8, 3.8, "능동 펠티어\n열 펌핑 (Q)\n(하방 배출)", fontsize=15, fontweight='bold', ha='center', color='#0277BD')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도1_냉각개념_비교도.png"), dpi=300)
plt.close()
print("도1 완료")

# ----------------------------------------------------
# 도 2: DRAM 다이 계면 마이크로 열전 필러(P-N) 단면 상세도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
ax.set_title("도 2: DRAM 다이 계면 더미 비아 내장 P-N 마이크로 열전소자(TEC) 단면 구조", fontsize=21, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# 상부 DRAM 다이 (흡열단: Cold Junction)
ax.add_patch(patches.Rectangle((1.5, 7.8), 13.0, 2.5, facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=3))
ax.text(8.0, 9.3, "상부 DRAM 다이 (100A) [국소 핫스팟 발생원 : 105℃]", fontsize=20, fontweight='bold', ha='center', color='#0D47A1')

# 상부 흡열 전극 (Cold Copper Pad)
ax.add_patch(patches.Rectangle((3.5, 8.0), 9.0, 0.8, facecolor='#81D4FA', edgecolor='#0288D1', linewidth=2))
ax.text(8.0, 8.4, "상부 흡열 전극 (Cold Junction) (111) [열 흡수: Qc]", fontsize=17, fontweight='bold', ha='center', color='#01579B')

# P형 및 N형 마이크로 열전 필러 (중간 계면)
ax.add_patch(patches.Rectangle((1.5, 3.8), 13.0, 4.0, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=2))
ax.text(2.2, 5.8, "다이 계면 접합층\n(SiO2/언더필)\n(102)", fontsize=15, fontweight='bold', ha='left')

# P형 필러 (Bi2Te3)
ax.add_patch(patches.Rectangle((4.5, 4.2), 2.8, 3.8, facecolor='#FFAB91', edgecolor='#D84315', linewidth=2.5))
ax.text(5.9, 6.4, "P형 열전 필러 (110P)\n(Bi2Te3 나노구조체)", fontsize=16, fontweight='bold', ha='center', color='#BF360C')
ax.text(5.9, 5.0, "정공(Hole) 이동 방향 ↓\n(열을 아래로 수송)", fontsize=14, fontweight='bold', ha='center', color='#D84315')

# N형 필러 (Bi2Se3)
ax.add_patch(patches.Rectangle((8.7, 4.2), 2.8, 3.8, facecolor='#C5CAE9', edgecolor='#283593', linewidth=2.5))
ax.text(10.1, 6.4, "N형 열전 필러 (110N)\n(Bi2Se3 나노구조체)", fontsize=16, fontweight='bold', ha='center', color='#1A237E')
ax.text(10.1, 5.0, "전자(Electron) 이동 ↑\n(전류와 반대로 열 수송)", fontsize=14, fontweight='bold', ha='center', color='#283593')

# 하부 DRAM 다이 (발열단: Hot Junction)
ax.add_patch(patches.Rectangle((1.5, 0.8), 13.0, 3.0, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=3))
ax.text(8.0, 1.4, "하부 DRAM 다이 또는 베이스 로직 다이 (100B)", fontsize=19, fontweight='bold', ha='center', color='#1B5E20')

# 하부 발열 전극
ax.add_patch(patches.Rectangle((3.5, 3.4), 4.0, 0.8, facecolor='#FFCC80', edgecolor='#E65100', linewidth=2))
ax.text(5.5, 3.8, "발열 전극 (+)", fontsize=15, fontweight='bold', ha='center', color='#BF360C')

ax.add_patch(patches.Rectangle((8.5, 3.4), 4.0, 0.8, facecolor='#FFCC80', edgecolor='#E65100', linewidth=2))
ax.text(10.5, 3.8, "발열 전극 (-)", fontsize=15, fontweight='bold', ha='center', color='#BF360C')

# 전류 인가 표시
ax.text(14.0, 5.8, "DC 펄스 전류 (I)\n(PWM 구동)", fontsize=16, fontweight='bold', ha='center', color='#C2185B',
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FCE4EC", edgecolor="#F48FB1"))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도2_마이크로열전필러_단면도.png"), dpi=300)
plt.close()
print("도2 완료")

# ----------------------------------------------------
# 도 3: 온칩 온도 센서 어레이 및 구역별 독립 PWM 드라이버 블록도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
ax.set_title("도 3: 온칩 온도 센서 매트릭스 및 핫스팟 구역별(Zone-by-Zone) 독립 PWM 제어 회로", fontsize=20, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# 중앙 제어기 (베이스 로직 다이)
ax.add_patch(patches.Rectangle((1.0, 1.5), 4.5, 8.0, facecolor='#E8EAF6', edgecolor='#1A237E', linewidth=3))
ax.text(3.25, 8.8, "베이스 로직 다이 (10)\n지능형 열 관리 엔진", fontsize=18, fontweight='bold', ha='center', color='#1A237E')

ax.add_patch(patches.Rectangle((1.4, 6.2), 3.7, 1.8, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=2))
ax.text(3.25, 7.1, "온도 센서 모니터링부\n(실시간 핫스팟 검출)", fontsize=15, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((1.4, 3.8), 3.7, 1.8, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=2))
ax.text(3.25, 4.7, "구역별 적응형 PWM 드라이버\n(주기 및 듀티비 가변)", fontsize=15, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((1.4, 1.8), 3.7, 1.4, facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=2))
ax.text(3.25, 2.5, "제벡 하베스팅 모드 스위치\n(자가발전 전력 회수)", fontsize=14, fontweight='bold', ha='center', color='#F57F17')

# DRAM 다이 상의 4개 구역 매트릭스 (우측)
ax.add_patch(patches.Rectangle((6.5, 1.0), 8.8, 9.0, facecolor='#F5F5F5', edgecolor='#37474F', linewidth=2.5))
ax.text(10.9, 9.5, "DRAM 다이 계면 핫스팟 분할 제어 매트릭스 (100)", fontsize=18, fontweight='bold', ha='center')

zones = [
    ("구역 1 (Zone 1) [정상 : 78℃]\nTEC 대기 모드 (자가발전)", '#E8F5E9', '#2E7D32', (7.0, 5.5)),
    ("구역 2 (Zone 2) [핫스팟 : 108℃!]\n★ TEC 급속 펠티어 냉각 가동 ★\n(PWM Duty 80% 인가)", '#FFCDD2', '#C62828', (11.0, 5.5)),
    ("구역 3 (Zone 3) [주의 : 88℃]\nTEC 완만 냉각 (PWM Duty 30%)", '#FFF8E1', '#F57F17', (7.0, 1.5)),
    ("구역 4 (Zone 4) [정상 : 76℃]\nTEC 대기 모드 (자가발전)", '#E8F5E9', '#2E7D32', (11.0, 1.5))
]

for title, fc, ec, (zx, zy) in zones:
    ax.add_patch(patches.Rectangle((zx, zy), 3.8, 3.5, facecolor=fc, edgecolor=ec, linewidth=2.5))
    ax.text(zx + 1.9, zy + 1.75, title, fontsize=15, fontweight='bold', ha='center', va='center', color=ec)

# 신호선 연결 화살표
ax.annotate("", xy=(6.5, 7.1), xytext=(5.1, 7.1), arrowprops=dict(facecolor='#1565C0', edgecolor='#0D47A1', width=3, headwidth=10))
ax.text(5.8, 7.5, "온도 센싱", fontsize=13, fontweight='bold', ha='center', color='#0D47A1')

ax.annotate("", xy=(6.5, 4.7), xytext=(5.1, 4.7), arrowprops=dict(facecolor='#C2185B', edgecolor='#880E4F', width=3, headwidth=10))
ax.text(5.8, 5.1, "PWM 펄스 전류", fontsize=13, fontweight='bold', ha='center', color='#C2185B')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도3_구역별_PWM드라이버.png"), dpi=300)
plt.close()
print("도3 완료")

# ----------------------------------------------------
# 도 4: 32단 다단 캐스케이드(Cascaded) 열 펌핑 메커니즘 상태도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
ax.set_title("도 4: 32단 초고적층 HBM의 다단 캐스케이드(Cascaded) 능동 열전 펌핑 구조", fontsize=20, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# 층별 블록들
layers = [
    ("최상단 방열판 (Heat Spreader) [외부 방열판으로 열 최종 방출]", '#90CAF9', '#0D47A1', 10.2),
    ("DRAM 다이 제25층~제32층 [TEC 제4단 열 펌핑 캐스케이드]", '#E3F2FD', '#1976D2', 8.2),
    ("DRAM 다이 제17층~제24층 [TEC 제3단 열 펌핑 캐스케이드]", '#E1F5FE', '#0288D1', 6.2),
    ("DRAM 다이 제9층~제16층 [중앙 핫스팟 집중 흡열단]", '#FFCDD2', '#C62828', 4.2),
    ("DRAM 다이 제1층~제8층 [TEC 제1단 열 배출 캐스케이드]", '#E8F5E9', '#2E7D32', 2.2),
    ("베이스 로직 다이 및 인터포저 패키지 기판 [방열 패스 연결]", '#B0BEC5', '#263238', 0.2)
]

for title, fc, ec, ly in layers:
    ax.add_patch(patches.Rectangle((2.0, ly), 12.0, 1.4, facecolor=fc, edgecolor=ec, linewidth=2.5))
    ax.text(8.0, ly + 0.7, title, fontsize=17, fontweight='bold', ha='center', va='center', color=ec if ec!='#90CAF9' else '#0D47A1')

# 캐스케이드 열 펌핑 하방 화살표들
for ly in [8.2, 6.2, 4.2, 2.2]:
    ax.annotate("", xy=(8.0, ly), xytext=(8.0, ly + 0.6), arrowprops=dict(facecolor='#D32F2F', edgecolor='#B71C1C', width=4, headwidth=12))

ax.text(14.8, 5.2, "단계별\n캐스케이드\n열 강제 압송\n(Peltier Pumping)", fontsize=16, fontweight='bold', ha='center', color='#B71C1C',
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#FFCDD2"))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도4_다단캐스케이드_열펌핑도.png"), dpi=300)
plt.close()
print("도4 완료")

# ----------------------------------------------------
# 도 5: 실시간 감지 및 능동 펠티어 냉각 순서도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 12), dpi=300)
ax.set_title("도 5: 온칩 핫스팟 실시간 모니터링, 능동 펠티어 냉각 및 자가발전 제어 순서도", fontsize=19, fontweight='bold', pad=20, color='#1A237E')
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

steps = [
    ("S201. 32단 HBM 가동 중 각 DRAM 다이 계면의 온칩 온도 센서 매트릭스 실시간 스캔", '#E3F2FD', '#1565C0'),
    ("S202. 특정 구역(Zone)의 온도가 기설정된 핫스팟 임계치(예: 95℃)를 초과하는지 판정", '#FFF8E1', '#F57F17'),
    ("S203. 임계치 초과 시: 해당 구역의 마이크로 TEC 필러에 PWM 급속 펠티어 냉각 펄스 전류 투입", '#FFEBEE', '#C62828'),
    ("S204. 다단 캐스케이드 제어를 통해 중앙 다이 계면의 열을 하부 다이 및 기판으로 강제 압송", '#FCE4EC', '#C2185B'),
    ("S205. 핫스팟 국소 온도가 목표 안전 온도(예: 80℃) 이하로 급랭 안정화되었는지 검증", '#E1F5FE', '#0288D1'),
    ("S206. 정상 온도 도달 시: 펠티어 전류 차단 및 제벡(Seebeck) 자가발전 모드로 자동 전환", '#E8F5E9', '#2E7D32'),
    ("S207. 다이 간 잔류 온도차로부터 전력을 회수(Harvesting)하여 온칩 센서로 재공급", '#E0F2F1', '#00695C')
]

y_start = 11.0
box_height = 0.95
gap = 0.55

for i, (text, fcolor, ecolor) in enumerate(steps):
    y = y_start - i * (box_height + gap)
    ax.add_patch(patches.FancyBboxPatch((1.0, y - box_height), 8.0, box_height, boxstyle="round,pad=0.15", facecolor=fcolor, edgecolor=ecolor, linewidth=2))
    ax.text(5.0, y - box_height/2, text, fontsize=13, fontweight='bold', ha='center', va='center', color=ecolor)
    
    if i < len(steps) - 1:
        ax.annotate("", xy=(5.0, y - box_height - gap + 0.1), xytext=(5.0, y - box_height - 0.05),
                    arrowprops=dict(facecolor='#37474F', edgecolor='#263238', width=2.5, headwidth=8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도5_능동냉각제어_순서도.png"), dpi=300)
plt.close()
print("도5 완료")

print("모든 특허6탄 300 DPI 도면 생성 완료!")
