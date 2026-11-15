import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

output_dir = r"C:\Users\LENOVO\Desktop\세이프티온_특허5탄_도면들"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 도 1: 종래 물리적 프로브 핀 방식 vs 본 발명 비접촉 근접장 공진 결합 검사 비교도
# ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10), dpi=300)

# [좌측] 종래 물리적 접촉 프로브 방식
ax1.set_title("[종래 기술] 물리적 프로브 핀 접촉 방식\n(패드 스크래치 및 소성 변형 발생 -> 본딩 불량)", fontsize=18, fontweight='bold', pad=15, color='#B71C1C')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# 실리콘 기판 및 절연막
ax1.add_patch(patches.Rectangle((1, 1), 8, 3, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=2))
ax1.text(5, 2.2, "실리콘 다이 기판 (10)", fontsize=16, fontweight='bold', ha='center')

# 구리 패드 (손상됨)
ax1.add_patch(patches.Rectangle((3.5, 4), 3, 1.5, facecolor='#FFCC80', edgecolor='#E65100', linewidth=2))
ax1.text(5, 4.7, "초미세 구리 패드 (20)", fontsize=15, fontweight='bold', ha='center')

# 프로브 핀 (접촉 및 압력)
ax1.add_patch(patches.Polygon([[5, 5.2], [4.4, 8.5], [5.6, 8.5]], facecolor='#78909C', edgecolor='#263238', linewidth=2))
ax1.text(5, 8.8, "기계적 프로브 핀 (1)", fontsize=16, fontweight='bold', ha='center', color='#B71C1C')

# 기계적 압력 및 스크래치 표시
ax1.annotate("기계적 하중 (P)", xy=(5, 5.5), xytext=(5, 7.2),
             arrowprops=dict(facecolor='#D32F2F', edgecolor='#B71C1C', width=3, headwidth=10),
             fontsize=14, fontweight='bold', color='#D32F2F', ha='center')

# 스크래치 결함 표시
ax1.plot([4.6, 4.9, 5.1, 5.4], [5.2, 5.0, 5.15, 5.0], color='#D50000', linewidth=3)
ax1.text(5, 3.4, "※ 미세 스크래치 및 소성 변형 (21)\n-> 하이브리드 본딩 보이드(Void) 발생!", fontsize=13, fontweight='bold', ha='center', color='#B71C1C', bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#FFCDD2"))


# [우측] 본 발명 비접촉 근접장 공진 결합 검사
ax2.set_title("[본 발명] 온칩 근접장 공진 결합 비접촉 검사\n(물리적 접촉 0% -> 패드 원자단위 평탄도 100% 보존)", fontsize=18, fontweight='bold', pad=15, color='#0D47A1')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

# 실리콘 기판 및 절연막
ax2.add_patch(patches.Rectangle((1, 1), 8, 3, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=2))
ax2.text(5, 1.8, "실리콘 다이 기판 (100)", fontsize=16, fontweight='bold', ha='center')

# 온칩 마이크로 공진 루프 (패드 하부)
ax2.add_patch(patches.Rectangle((2.5, 2.7), 5, 1.0, facecolor='#E1F5FE', edgecolor='#0288D1', linewidth=2, linestyle='--'))
ax2.text(5, 3.2, "온칩 마이크로 공진 루프 (120)", fontsize=14, fontweight='bold', ha='center', color='#0277BD')

# 구리 패드 (완전 무결)
ax2.add_patch(patches.Rectangle((3.5, 4.3), 3, 1.5, facecolor='#FFE082', edgecolor='#FF8F00', linewidth=2))
ax2.text(5, 5.0, "초미세 구리 패드 (110)\n(RMS < 0.5nm 완전 보존)", fontsize=14, fontweight='bold', ha='center')

# 상공 비접촉 검사 헤드 (갭 유지)
ax2.add_patch(patches.Rectangle((2.5, 7.5), 5, 1.5, facecolor='#E8EAF6', edgecolor='#1A237E', linewidth=2))
ax2.text(5, 8.2, "비접촉 고주파 검사 헤드 (200)", fontsize=16, fontweight='bold', ha='center', color='#1A237E')

# 공기 간극 (에어 갭)
ax2.text(8.2, 6.6, "에어 갭 (G)\n(50nm~2um)", fontsize=13, fontweight='bold', ha='center', color='#00695C')
ax2.annotate("", xy=(7.2, 5.8), xytext=(7.2, 7.5), arrowprops=dict(arrowstyle="<->", color="#00695C", lw=2))

# 근접장 전자기 공진 커플링 파동 표시
for y_pos in [6.2, 6.7, 7.1]:
    ax2.plot([3.8, 5.0, 6.2], [y_pos-0.1, y_pos+0.1, y_pos-0.1], color='#0288D1', linewidth=2.5)
ax2.text(5, 6.6, "근접장 전자기 공진파 (150)\n(10GHz ~ 60GHz FDM)", fontsize=12, fontweight='bold', ha='center', color='#01579B', bbox=dict(boxstyle="round,pad=0.2", facecolor="#E1F5FE", edgecolor="#81D4FA"))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도1_검사개념_비교도.png"), dpi=300)
plt.close()
print("도1 생성 완료")

# ----------------------------------------------------
# 도 2: 온칩 마이크로 공진 루프 및 차동 커플링 단면 상세도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 10), dpi=300)
ax.set_title("도 2: 온칩 근접장 마이크로 공진 루프 및 차동 커플링 단면 구조", fontsize=20, fontweight='bold', pad=20, color='#1A237E')
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# 1. 비접촉 프로브 검사 헤드 (상단)
ax.add_patch(patches.Rectangle((2, 8.5), 10, 2, facecolor='#E8EAF6', edgecolor='#283593', linewidth=2.5))
ax.text(7, 9.8, "비접촉 웨이퍼 프로브 검사 헤드 (200)", fontsize=17, fontweight='bold', ha='center', color='#1A237E')
ax.add_patch(patches.Rectangle((3, 8.8), 3.5, 0.8, facecolor='#C5CAE9', edgecolor='#3F51B5', linewidth=1.5))
ax.text(4.75, 9.2, "송신 공진 코일 (210)", fontsize=13, fontweight='bold', ha='center')
ax.add_patch(patches.Rectangle((7.5, 8.8), 3.5, 0.8, facecolor='#C5CAE9', edgecolor='#3F51B5', linewidth=1.5))
ax.text(9.25, 9.2, "수신 센싱 코일 (220)", fontsize=13, fontweight='bold', ha='center')

# 에어 갭 (비접촉)
ax.text(12.5, 7.8, "비접촉 간극 (G)\n(50nm~2um)", fontsize=13, fontweight='bold', ha='center', color='#00695C')
ax.annotate("", xy=(12.5, 7.1), xytext=(12.5, 8.5), arrowprops=dict(arrowstyle="<->", color="#00695C", lw=2))

# 2. 반도체 다이 표면 구리 패드 및 유전체 (중단)
ax.add_patch(patches.Rectangle((1, 5.2), 12, 1.8, facecolor='#ECEFF1', edgecolor='#455A64', linewidth=2))
ax.text(1.8, 6.1, "층간 절연막 (SiO2/SiCN)\n(102)", fontsize=12, fontweight='bold', ha='left')

# 구리 패드 2개 (차동 구조)
ax.add_patch(patches.Rectangle((3.5, 5.4), 2.5, 1.4, facecolor='#FFE082', edgecolor='#E65100', linewidth=2))
ax.text(4.75, 6.1, "제1 구리 패드 (110a)\n(Positive)", fontsize=13, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((8.0, 5.4), 2.5, 1.4, facecolor='#FFE082', edgecolor='#E65100', linewidth=2))
ax.text(9.25, 6.1, "제2 구리 패드 (110b)\n(Negative)", fontsize=13, fontweight='bold', ha='center')

# 3. 온칩 마이크로 공진 루프 및 퓨즈 (하부)
ax.add_patch(patches.Rectangle((1, 1.5), 12, 3.7, facecolor='#CFD8DC', edgecolor='#37474F', linewidth=2))
ax.text(1.8, 2.5, "실리콘 기판 (100)\n& 배선층 (M1-M4)", fontsize=13, fontweight='bold', ha='left')

# 공진 루프 회로 블록
ax.add_patch(patches.Rectangle((3.2, 3.2), 3.1, 1.5, facecolor='#E1F5FE', edgecolor='#0288D1', linewidth=2))
ax.text(4.75, 4.1, "제1 LC 공진 탱크 (120a)\n(마이크로 인덕터/커패시터)", fontsize=12, fontweight='bold', ha='center', color='#01579B')

ax.add_patch(patches.Rectangle((7.7, 3.2), 3.1, 1.5, facecolor='#E1F5FE', edgecolor='#0288D1', linewidth=2))
ax.text(9.25, 4.1, "제2 LC 공진 탱크 (120b)\n(마이크로 인덕터/커패시터)", fontsize=12, fontweight='bold', ha='center', color='#01579B')

# 열감응형 절연 퓨즈
ax.add_patch(patches.Rectangle((4.0, 2.0), 6.0, 0.9, facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=2))
ax.text(7.0, 2.45, "열감응형 영구 절연 퓨즈 (140) [본딩 열처리시 자동 OFF]", fontsize=13, fontweight='bold', ha='center', color='#F57F17')

# 내부 TSV 및 DRAM 로직 연결 라인
ax.plot([4.75, 4.75], [3.2, 2.9], color='#37474F', linewidth=2)
ax.plot([9.25, 9.25], [3.2, 2.9], color='#37474F', linewidth=2)
ax.text(7.0, 1.7, "내부 DRAM 셀 어레이 및 TSV 관통 전극 연동 버스 (130)", fontsize=13, fontweight='bold', ha='center', color='#263238')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도2_공진루프_단면구조.png"), dpi=300)
plt.close()
print("도2 생성 완료")

# ----------------------------------------------------
# 도 3: 2048비트 다중 주파수 분할 다중화(FDM) 매트릭스 블록도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
ax.set_title("도 3: 2048비트 비접촉 고속 전수 검사를 위한 다중 주파수 분할 다중화(FDM) 매트릭스", fontsize=19, fontweight='bold', pad=20, color='#1A237E')
ax.set_xlim(0, 15)
ax.set_ylim(0, 11)
ax.axis('off')

# 외부 검사 시스템 (좌측)
ax.add_patch(patches.Rectangle((0.8, 2.5), 3.8, 6.5, facecolor='#E8EAF6', edgecolor='#1A237E', linewidth=2.5))
ax.text(2.7, 8.4, "초광대역 비접촉\n테스터 장비 (300)", fontsize=16, fontweight='bold', ha='center', color='#1A237E')

ax.add_patch(patches.Rectangle((1.2, 6.2), 3.0, 1.3, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=1.5))
ax.text(2.7, 6.85, "다중 주파수 RF 송신기\n(f1 ~ f16 생성)", fontsize=13, fontweight='bold', ha='center')

ax.add_patch(patches.Rectangle((1.2, 4.2), 3.0, 1.3, facecolor='#C5CAE9', edgecolor='#303F9F', linewidth=1.5))
ax.text(2.7, 4.85, "후방산란 위상 복조기\n(IQ 감지 / KGD 판정)", fontsize=13, fontweight='bold', ha='center')

# 무선 전파 전송 구간 (중간)
ax.annotate("", xy=(5.8, 7.0), xytext=(4.2, 7.0), arrowprops=dict(facecolor='#0288D1', edgecolor='#01579B', width=3, headwidth=10))
ax.text(5.0, 7.4, "다중 RF 여기파\n(20~60GHz)", fontsize=12, fontweight='bold', ha='center', color='#0277BD')

ax.annotate("", xy=(4.2, 4.8), xytext=(5.8, 4.8), arrowprops=dict(facecolor='#D81B60', edgecolor='#880E4F', width=3, headwidth=10))
ax.text(5.0, 4.1, "후방산란 응답파\n(위상/진폭 피드백)", fontsize=12, fontweight='bold', ha='center', color='#AD1457')

# HBM 반도체 다이 내부 블록 (우측)
ax.add_patch(patches.Rectangle((5.8, 1.5), 8.5, 8.5, facecolor='#F5F5F5', edgecolor='#212121', linewidth=2.5))
ax.text(10.05, 9.5, "HBM4 반도체 다이 온칩 검사 아키텍처 (100)", fontsize=16, fontweight='bold', ha='center', color='#212121')

# 4개 쿼드런트(뱅크) 매트릭스
colors_q = ['#E1F5FE', '#FFF8E1', '#E8F5E9', '#F3E5F5']
labels_q = [
    "구역 A (채널 1~512)\n공진 주파수 f1 (28GHz)\n512개 패드 병렬 감지",
    "구역 B (채널 513~1024)\n공진 주파수 f2 (32GHz)\n512개 패드 병렬 감지",
    "구역 C (채널 1025~1536)\n공진 주파수 f3 (38GHz)\n512개 패드 병렬 감지",
    "구역 D (채널 1537~2048)\n공진 주파수 f4 (45GHz)\n512개 패드 병렬 감지"
]
coords = [(6.3, 5.6), (10.2, 5.6), (6.3, 2.0), (10.2, 2.0)]

for i in range(4):
    cx, cy = coords[i]
    ax.add_patch(patches.Rectangle((cx, cy), 3.6, 3.0, facecolor=colors_q[i], edgecolor='#424242', linewidth=1.5))
    ax.text(cx + 1.8, cy + 1.5, labels_q[i], fontsize=12, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도3_2048비트_FDM매트릭스.png"), dpi=300)
plt.close()
print("도3 생성 완료")

# ----------------------------------------------------
# 도 4: 열감응형 절연 퓨즈(Thermal Isolation Fuse) 동작 상태도
# ----------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), dpi=300)

# [상태 A] 검사 시 (상온 25℃) : 통전 상태
ax1.set_title("[검사 단계 : 상온 25℃]\n열감응 퓨즈 통전 (ON) -> 비접촉 RF 검사 정상 가동", fontsize=17, fontweight='bold', pad=15, color='#0D47A1')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

ax1.add_patch(patches.Rectangle((1.5, 6.0), 7.0, 2.5, facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=2))
ax1.text(5.0, 7.25, "마이크로 공진 루프 회로 (120)", fontsize=16, fontweight='bold', ha='center', color='#0D47A1')

# 퓨즈 (연결됨)
ax1.add_patch(patches.Rectangle((3.5, 4.0), 3.0, 1.2, facecolor='#C8E6C9', edgecolor='#2E7D32', linewidth=2))
ax1.text(5.0, 4.6, "열감응 저융점 나노 합금 (141)\n[연결 상태 : ON]", fontsize=14, fontweight='bold', ha='center', color='#1B5E20')

ax1.plot([5.0, 5.0], [6.0, 5.2], color='#1B5E20', linewidth=4)
ax1.plot([5.0, 5.0], [4.0, 3.0], color='#1B5E20', linewidth=4)

ax1.add_patch(patches.Rectangle((1.5, 1.0), 7.0, 2.0, facecolor='#ECEFF1', edgecolor='#37474F', linewidth=2))
ax1.text(5.0, 2.0, "내부 DRAM 데이터 라인 (130)", fontsize=16, fontweight='bold', ha='center')

ax1.text(5.0, 0.3, "결과: 검사용 신호 흐름 정상 활성화 (수율 100% 측정)", fontsize=14, fontweight='bold', ha='center', color='#0D47A1')


# [상태 B] 하이브리드 본딩 시 (180~200℃ 열압착) : 영구 절연
ax2.set_title("[하이브리드 본딩 열압착 단계 : 180~200℃]\n열감응 퓨즈 용융 절연 (OFF) -> 영구 노이즈 원천 차단", fontsize=17, fontweight='bold', pad=15, color='#B71C1C')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

ax2.add_patch(patches.Rectangle((1.5, 6.0), 7.0, 2.5, facecolor='#ECEFF1', edgecolor='#78909C', linewidth=2))
ax2.text(5.0, 7.25, "마이크로 공진 루프 (120)\n[완전 격리 / 비활성화]", fontsize=16, fontweight='bold', ha='center', color='#546E7A')

# 퓨즈 (끊어짐 / 기화 또는 볼링 분리)
ax2.add_patch(patches.Rectangle((3.5, 4.0), 1.2, 1.2, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=2))
ax2.add_patch(patches.Rectangle((5.3, 4.0), 1.2, 1.2, facecolor='#FFCDD2', edgecolor='#C62828', linewidth=2))
ax2.text(5.0, 4.6, "단선\n(OPEN)", fontsize=13, fontweight='bold', ha='center', color='#B71C1C')

ax2.plot([4.1, 4.1], [6.0, 5.2], color='#C62828', linewidth=3)
ax2.plot([5.9, 5.9], [4.0, 3.0], color='#C62828', linewidth=3)

# 열 표시
ax2.text(8.5, 4.6, "열 인가\n(180~200℃)", fontsize=14, fontweight='bold', ha='center', color='#D84315', bbox=dict(boxstyle="round,pad=0.3", facecolor="#FBE9E7", edgecolor="#FFAB91"))

ax2.add_patch(patches.Rectangle((1.5, 1.0), 7.0, 2.0, facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=2))
ax2.text(5.0, 2.0, "내부 DRAM 데이터 라인 (130)\n[초고속 HBM4 정상 동작 / 기생 노이즈 0%]", fontsize=15, fontweight='bold', ha='center', color='#1B5E20')

ax2.text(5.0, 0.3, "결과: 양산 동작 시 RF 간섭 및 고주파 기생 손실 영구 제거!", fontsize=14, fontweight='bold', ha='center', color='#B71C1C')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "도4_열감응퓨즈_절연동작도.png"), dpi=300)
plt.close()
print("도4 생성 완료")

# ----------------------------------------------------
# 도 5: 웨이퍼 레벨 비접촉 초고속 전수 검사 전체 순서도
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 12), dpi=300)
ax.set_title("도 5: 웨이퍼 레벨 온칩 비접촉 초고속 전수 검사 및 KGD 선별 순서도", fontsize=19, fontweight='bold', pad=20, color='#1A237E')
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

steps = [
    ("S101. 하이브리드 본딩용 초미세 구리 패드 및 온칩 공진 루프 구비 HBM4 웨이퍼 로딩", '#E3F2FD', '#1565C0'),
    ("S102. 비접촉 테스터 헤드를 웨이퍼 상공 50nm~2um 간극(G)으로 비접촉 정렬", '#E8EAF6', '#283593'),
    ("S103. 2048비트 다중 주파수(f1~f4) RF 여기 신호 무선 인가 및 근접장 공진 유도", '#E1F5FE', '#0288D1'),
    ("S104. 내부 DRAM 메모리 셀 및 TSV 응답에 따른 후방산란(Backscatter) 위상 신호 수신", '#FFF8E1', '#F57F17'),
    ("S105. 수신 위상/임피던스 데이터 기반 구리 패드 결함 및 칩 KGD(Known Good Die) 0.5초 판정", '#FCE4EC', '#C2185B'),
    ("S106. 양품 다이 선별 및 하이브리드 본딩 공정 투입 (180~200℃ 열압착)", '#E8F5E9', '#2E7D32'),
    ("S107. 열처리에 의해 온칩 공진 루프 열감응 퓨즈 자동 단선 -> 영구 절연 및 HBM4 완성", '#FFEBEE', '#C62828')
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
plt.savefig(os.path.join(output_dir, "도5_전수검사_순서도.png"), dpi=300)
plt.close()
print("도5 생성 완료")

print("모든 300 DPI 도면 1~5 제작 완료!")
