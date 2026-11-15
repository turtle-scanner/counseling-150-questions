import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허6탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 도 1: 종래 수동 방열 vs 본 발명 능동 마이크로 TEC + 증기챔버 비교도 (초대형 글씨)
# ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 12), dpi=300)

# [좌측] 종래 수동 방열
ax1.set_title("[종래 기술] 외장 히트싱크 수동 방열\n(다이 계면 열저항 누적 -> 105~125℃ 핫스팟 폭발)", 
              fontsize=24, fontweight='bold', pad=25, color='#B71C1C')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 11)
ax1.axis('off')

# 외장 히트싱크
ax1.add_patch(patches.Rectangle((1.0, 9.2), 8.0, 1.4, facecolor='#90A4AE', edgecolor='#37474F', linewidth=3))
ax1.text(5.0, 9.9, "외장 히트싱크 / 방열판 (1)", fontsize=22, fontweight='bold', ha='center', va='center')

# 상단 DRAM 다이
ax1.add_patch(patches.Rectangle((1.5, 7.2), 7.0, 1.6, facecolor='#CFD8DC', edgecolor='#455A64', linewidth=2.5))
ax1.text(5.0, 8.0, "상부 DRAM 다이층 (17~32층) [85℃]", fontsize=20, fontweight='bold', ha='center', va='center')

# 중앙 다이 핫스팟
ax1.add_patch(patches.Rectangle((1.5, 4.0), 7.0, 2.8, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=4))
ax1.text(5.0, 5.7, "★ 중앙 적층 다이 계면 (8~16층) ★\n[ 극심한 열 고립 : 105℃~125℃ ]", fontsize=22, fontweight='bold', ha='center', va='center', color='#B71C1C')
ax1.text(5.0, 4.6, "※ DRAM 리프레시 붕괴 & 데이터 증발!", fontsize=18, fontweight='bold', ha='center', va='center', color='#D50000')

# 하부 DRAM 및 베이스 다이
ax1.add_patch(patches.Rectangle((1.5, 2.0), 7.0, 1.6, facecolor='#CFD8DC', edgecolor='#455A64', linewidth=2.5))
ax1.text(5.0, 2.8, "하부 DRAM 다이층 (1~8층) [90℃]", fontsize=20, fontweight='bold', ha='center', va='center')

ax1.add_patch(patches.Rectangle((1.0, 0.4), 8.0, 1.3, facecolor='#B0BEC5', edgecolor='#263238', linewidth=3))
ax1.text(5.0, 1.05, "베이스 로직 다이 및 인터포저 (2)", fontsize=21, fontweight='bold', ha='center', va='center')

# 하단 경고
ax1.text(5.0, -0.2, "▶ 한계: 외부 냉각기로 내부 핫스팟 배출 물리적 불가능!", fontsize=19, fontweight='bold', ha='center', color='#B71C1C')


# [우측] 본 발명 능동 마이크로 TEC + 증기챔버
ax2.set_title("[본 발명] 온칩 마이크로 TEC + 증기챔버 복합 냉각\n(펠티어 전자 펌핑 + 인터포저 수평 확산 -> 80℃ 급랭)", 
              fontsize=24, fontweight='bold', pad=25, color='#0D47A1')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 11)
ax2.axis('off')

# 외장 히트스프레더
ax2.add_patch(patches.Rectangle((1.0, 9.2), 8.0, 1.4, facecolor='#BBDEFB', edgecolor='#1565C0', linewidth=3))
ax2.text(5.0, 9.9, "고효율 히트스프레더 (20)", fontsize=22, fontweight='bold', ha='center', va='center', color='#0D47A1')

# 상단 DRAM 다이
ax2.add_patch(patches.Rectangle((1.5, 7.2), 7.0, 1.6, facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2.5))
ax2.text(5.0, 8.0, "상부 DRAM 다이층 (17~32층) [75℃ 유지]", fontsize=20, fontweight='bold', ha='center', va='center')

# 중앙 다이 계면 (능동 마이크로 TEC 냉각)
ax2.add_patch(patches.Rectangle((1.5, 4.0), 7.0, 2.8, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=4))
ax2.text(5.0, 5.7, "★ 중앙 계면 마이크로 TEC 냉각 ★\n[ 펠티어 전자 펌핑 : 105℃ -> 80℃ 급랭! ]", fontsize=22, fontweight='bold', ha='center', va='center', color='#1B5E20')
ax2.text(5.0, 4.6, "온칩 P-N 열전 필러 + 포논 다이오드 (110, 112)", fontsize=18, fontweight='bold', ha='center', va='center', color='#2E7D32')

# 하부 DRAM
ax2.add_patch(patches.Rectangle((1.5, 2.0), 7.0, 1.6, facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2.5))
ax2.text(5.0, 2.8, "하부 DRAM 다이층 (1~8층) [78℃ 유지]", fontsize=20, fontweight='bold', ha='center', va='center')

# 마이크로 증기챔버 인터포저
ax2.add_patch(patches.Rectangle((1.0, 0.4), 8.0, 1.3, facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=3))
ax2.text(5.0, 1.05, "실리콘 인터포저 내장 마이크로 증기챔버 (30)\n[ 수평 초고속 열확산 -> 하부 열포화 완전 방지 ]", fontsize=18, fontweight='bold', ha='center', va='center', color='#F57F17')

# 하단 결과
ax2.text(5.0, -0.2, "▶ 결과: 리프레시 붕괴 0% & 32단 초고적층 양산 실현!", fontsize=19, fontweight='bold', ha='center', color='#0D47A1')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도1_냉각개념_비교도.png"), dpi=300)
plt.close()
print("도1 초대형 글씨 완료")

# ----------------------------------------------------
# 도 2: DRAM 다이 계면 마이크로 열전 필러(P-N) 단면 상세도 (초대형 글씨)
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
ax.set_title("도 2: DRAM 다이 계면 더미 비아 내장 P-N 마이크로 열전소자(TEC) 및 차폐 구조 단면도", 
             fontsize=23, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# 상부 DRAM 다이 (핫스팟 발생원)
ax.add_patch(patches.Rectangle((1.0, 8.2), 14.0, 2.2, facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=3.5))
ax.text(8.0, 9.3, "상부 DRAM 다이 (100A) [국소 핫스팟 열원 : 105℃]", fontsize=22, fontweight='bold', ha='center', color='#0D47A1')

# 상부 흡열 전극
ax.add_patch(patches.Rectangle((3.0, 8.4), 10.0, 0.8, facecolor='#81D4FA', edgecolor='#0288D1', linewidth=2.5))
ax.text(8.0, 8.8, "상부 흡열 전극 (Cold Junction) (111) [열 흡수: Qc]", fontsize=19, fontweight='bold', ha='center', color='#01579B')

# 포논 다이오드 나노 박막층 (역열류 차단)
ax.add_patch(patches.Rectangle((3.0, 7.8), 10.0, 0.5, facecolor='#E1BEE7', edgecolor='#8E24AA', linewidth=2))
ax.text(8.0, 8.05, "★ 그래핀 / h-BN 포논 다이오드층 (112) [역방향 열 누설 100% 차단!] ★", fontsize=16, fontweight='bold', ha='center', color='#4A148C')

# 다이 계면 절연층
ax.add_patch(patches.Rectangle((1.0, 3.6), 14.0, 4.2, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=2.5))
ax.text(1.8, 5.7, "다이 계면 접합층\n(SiO2/언더필)\n(102)", fontsize=17, fontweight='bold', ha='left')

# P형 열전 필러 (Bi2Te3)
ax.add_patch(patches.Rectangle((4.2, 4.0), 3.2, 3.8, facecolor='#FFAB91', edgecolor='#D84315', linewidth=3))
ax.text(5.8, 6.2, "P형 열전 필러 (110P)\n(Bi2Te3 나노구조체)", fontsize=18, fontweight='bold', ha='center', color='#BF360C')
ax.text(5.8, 4.8, "정공 이동 ↓ (열 하방 수송)", fontsize=16, fontweight='bold', ha='center', color='#D84315')

# N형 열전 필러 (Bi2Se3)
ax.add_patch(patches.Rectangle((8.6, 4.0), 3.2, 3.8, facecolor='#C5CAE9', edgecolor='#283593', linewidth=3))
ax.text(10.2, 6.2, "N형 열전 필러 (110N)\n(Bi2Se3 나노구조체)", fontsize=18, fontweight='bold', ha='center', color='#1A237E')
ax.text(10.2, 4.8, "전자 이동 ↑ (열 하방 수송)", fontsize=16, fontweight='bold', ha='center', color='#283593')

# 완충링 & 동축 차폐 표시 배지
ax.add_patch(patches.FancyBboxPatch((12.2, 5.8), 3.5, 1.8, boxstyle="round,pad=0.2", facecolor='#FFF3E0', edgecolor='#E65100', linewidth=2.5))
ax.text(13.95, 6.7, "나노 탄성 완충 링 (113)\n[CTE 크랙 100% 방지]", fontsize=15, fontweight='bold', ha='center', color='#E65100')

ax.add_patch(patches.FancyBboxPatch((12.2, 3.8), 3.5, 1.8, boxstyle="round,pad=0.2", facecolor='#E8EAF6', edgecolor='#1A237E', linewidth=2.5))
ax.text(13.95, 4.7, "동축 차폐 가드링 (114)\n[EMI 노이즈 60dB 차단]", fontsize=15, fontweight='bold', ha='center', color='#1A237E')

# 하부 DRAM 다이 (발열단)
ax.add_patch(patches.Rectangle((1.0, 0.8), 14.0, 2.6, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=3.5))
ax.text(8.0, 1.6, "하부 DRAM 다이 또는 베이스 로직 다이 (100B)", fontsize=21, fontweight='bold', ha='center', color='#1B5E20')

# 하부 발열 전극
ax.add_patch(patches.Rectangle((3.5, 3.2), 4.2, 0.7, facecolor='#FFCC80', edgecolor='#E65100', linewidth=2))
ax.text(5.6, 3.55, "발열 전극 (+)", fontsize=16, fontweight='bold', ha='center', color='#BF360C')

ax.add_patch(patches.Rectangle((8.3, 3.2), 4.2, 0.7, facecolor='#FFCC80', edgecolor='#E65100', linewidth=2))
ax.text(10.4, 3.55, "발열 전극 (-)", fontsize=16, fontweight='bold', ha='center', color='#BF360C')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도2_마이크로열전필러_단면도.png"), dpi=300)
plt.close()
print("도2 초대형 글씨 완료")

# ----------------------------------------------------
# 도 3: 온칩 온도 센서 어레이 및 구역별 독립 PWM 드라이버 (초대형 글씨)
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
ax.set_title("도 3: 온칩 온도 센서 매트릭스 및 핫스팟 구역별(Zone-by-Zone) 독립 PWM 제어 회로", 
             fontsize=22, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# 중앙 제어기 (베이스 로직 다이)
ax.add_patch(patches.Rectangle((0.8, 1.2), 4.8, 8.5, facecolor='#E8EAF6', edgecolor='#1A237E', linewidth=3.5))
ax.text(3.2, 9.0, "베이스 로직 다이 (10)\n지능형 열 관리 엔진", fontsize=20, fontweight='bold', ha='center', color='#1A237E')

ax.add_patch(patches.Rectangle((1.2, 6.3), 4.0, 1.9, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=2.5))
ax.text(3.2, 7.25, "온도 센서 모니터링부\n(실시간 핫스팟 검출)", fontsize=17, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((1.2, 3.8), 4.0, 1.9, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=2.5))
ax.text(3.2, 4.75, "구역별 적응형 PWM 드라이버\n(주기 및 듀티비 가변)", fontsize=17, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((1.2, 1.6), 4.0, 1.6, facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=2.5))
ax.text(3.2, 2.4, "제벡 하베스팅 모드 스위치\n(자가발전 전력 회수)", fontsize=16, fontweight='bold', ha='center', color='#F57F17')

# DRAM 다이 상의 4개 구역 매트릭스
ax.add_patch(patches.Rectangle((6.5, 0.8), 9.0, 9.2, facecolor='#F5F5F5', edgecolor='#37474F', linewidth=3))
ax.text(11.0, 9.5, "DRAM 다이 계면 핫스팟 분할 제어 매트릭스 (100)", fontsize=20, fontweight='bold', ha='center')

zones = [
    ("구역 1 (Zone 1) [정상 : 78℃]\nTEC 대기 / 제벡 자가발전", '#E8F5E9', '#2E7D32', (7.0, 5.3)),
    ("구역 2 (Zone 2) [핫스팟 : 108℃!]\n★ TEC 급속 펠티어 냉각 가동 ★\n(PWM Duty 80% 집중 투입)", '#FFCDD2', '#C62828', (11.2, 5.3)),
    ("구역 3 (Zone 3) [주의 : 88℃]\nTEC 완만 냉각 (PWM Duty 30%)", '#FFF8E1', '#F57F17', (7.0, 1.3)),
    ("구역 4 (Zone 4) [정상 : 76℃]\nTEC 대기 / 제벡 자가발전", '#E8F5E9', '#2E7D32', (11.2, 1.3))
]

for title, fc, ec, (zx, zy) in zones:
    ax.add_patch(patches.Rectangle((zx, zy), 3.9, 3.6, facecolor=fc, edgecolor=ec, linewidth=3))
    ax.text(zx + 1.95, zy + 1.8, title, fontsize=16, fontweight='bold', ha='center', va='center', color=ec)

# 신호선 연결 화살표
ax.annotate("", xy=(6.5, 7.25), xytext=(5.2, 7.25), arrowprops=dict(facecolor='#1565C0', edgecolor='#0D47A1', width=3.5, headwidth=11))
ax.text(5.85, 7.7, "온도 센싱", fontsize=15, fontweight='bold', ha='center', color='#0D47A1')

ax.annotate("", xy=(6.5, 4.75), xytext=(5.2, 4.75), arrowprops=dict(facecolor='#C2185B', edgecolor='#880E4F', width=3.5, headwidth=11))
ax.text(5.85, 5.2, "PWM 펄스", fontsize=15, fontweight='bold', ha='center', color='#C2185B')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도3_구역별_PWM드라이버.png"), dpi=300)
plt.close()
print("도3 초대형 글씨 완료")

# ----------------------------------------------------
# 도 4: 32단 다단 캐스케이드 및 인터포저 증기챔버 상태도 (초대형 글씨)
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
ax.set_title("도 4: 32단 초고적층 HBM의 다단 캐스케이드 펌핑 및 증기챔버 수평 열배출 구조", 
             fontsize=22, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

layers = [
    ("최상단 고효율 방열판 (Heat Spreader) (20) [외부 방열판으로 열 최종 방출]", '#90CAF9', '#0D47A1', 10.2),
    ("DRAM 다이 제25층~제32층 [TEC 제4단 열 펌핑 캐스케이드]", '#E3F2FD', '#1976D2', 8.2),
    ("DRAM 다이 제17층~제24층 [TEC 제3단 열 펌핑 캐스케이드]", '#E1F5FE', '#0288D1', 6.2),
    ("★ DRAM 다이 제9층~제16층 [중앙 핫스팟 집중 흡열단 : 105℃ -> 80℃ 급랭] ★", '#FFCDD2', '#C62828', 4.2),
    ("DRAM 다이 제1층~제8층 [TEC 제1단 열 배출 캐스케이드]", '#E8F5E9', '#2E7D32', 2.2),
    ("실리콘 인터포저 내장 마이크로 증기챔버 (30) [초고속 수평 열분산 -> 하부 열포화 0%]", '#FFF9C4', '#F57F17', 0.2)
]

for title, fc, ec, ly in layers:
    ax.add_patch(patches.Rectangle((1.5, ly), 13.0, 1.5, facecolor=fc, edgecolor=ec, linewidth=3))
    ax.text(8.0, ly + 0.75, title, fontsize=18, fontweight='bold', ha='center', va='center', color=ec if ec!='#90CAF9' else '#0D47A1')

# 캐스케이드 열 펌핑 하방 화살표들
for ly in [8.2, 6.2, 4.2, 2.2]:
    ax.annotate("", xy=(8.0, ly), xytext=(8.0, ly + 0.6), arrowprops=dict(facecolor='#D32F2F', edgecolor='#B71C1C', width=5, headwidth=13))

ax.text(15.0, 5.2, "단계별\n캐스케이드\n열 강제 압송\n(Peltier)", fontsize=18, fontweight='bold', ha='center', color='#B71C1C',
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#FFCDD2"))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도4_다단캐스케이드_열펌핑도.png"), dpi=300)
plt.close()
print("도4 초대형 글씨 완료")

# ----------------------------------------------------
# 도 5: 온칩 핫스팟 실시간 모니터링 순서도 (초대형 글씨)
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 13), dpi=300)
ax.set_title("도 5: 온칩 핫스팟 실시간 모니터링, 능동 펠티어 급속 냉각 및 제벡 제어 순서도", 
             fontsize=22, fontweight='bold', pad=25, color='#1A237E')
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

steps = [
    ("S201. 32단 HBM 가동 중 각 DRAM 계면 온칩 온도 센서 매트릭스 실시간 스캔", '#E3F2FD', '#1565C0'),
    ("S202. 특정 구역(Zone)의 온도가 기설정된 핫스팟 임계치(95℃)를 초과하는지 판정", '#FFF8E1', '#F57F17'),
    ("S203. 임계치 초과 시: 해당 구역 마이크로 TEC에 PWM 급속 펠티어 냉각 전류 투입", '#FFEBEE', '#C62828'),
    ("S204. 포논 다이오드로 역열류 차단 + 인터포저 증기챔버로 열 초고속 수평 분산 배출", '#FCE4EC', '#C2185B'),
    ("S205. 핫스팟 국소 온도가 목표 안전 온도(80℃) 이하로 급랭 안정화되었는지 검증", '#E1F5FE', '#0288D1'),
    ("S206. 정상 온도 도달 시: 펠티어 전류 차단 및 제벡(Seebeck) 자가발전 모드 자동 전환", '#E8F5E9', '#2E7D32'),
    ("S207. 다이 간 잔류 온도차로부터 전력을 회수(Harvesting)하여 온칩 센서로 재공급", '#E0F2F1', '#00695C')
]

y_start = 11.0
box_height = 1.05
gap = 0.5

for i, (text, fcolor, ecolor) in enumerate(steps):
    y = y_start - i * (box_height + gap)
    ax.add_patch(patches.FancyBboxPatch((0.8, y - box_height), 8.4, box_height, boxstyle="round,pad=0.15", facecolor=fcolor, edgecolor=ecolor, linewidth=2.5))
    ax.text(5.0, y - box_height/2, text, fontsize=15, fontweight='bold', ha='center', va='center', color=ecolor)
    
    if i < len(steps) - 1:
        ax.annotate("", xy=(5.0, y - box_height - gap + 0.1), xytext=(5.0, y - box_height - 0.05),
                    arrowprops=dict(facecolor='#37474F', edgecolor='#263238', width=3, headwidth=9))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도5_능동냉각제어_순서도.png"), dpi=300)
plt.close()
print("도5 초대형 글씨 완료")

print("특허 6탄 도면 1~5 전체 초대형 볼드 글씨 업그레이드 완료!")
