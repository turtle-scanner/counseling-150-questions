with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_d54_phase1_wordbook.html', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

bad_phrases = [
    '가족 하위체계 간의 경계선을 명료화하고 자아분화 수준을 높여',
    '핵심 병리적 신념과 부적응적 행동을 소거하여',
    '표적 문제행동의 발생 빈도를 효과적으로 소거하고',
    '내담자의 통찰을 촉진하고 정서적 안정을 확립하여 긍정적 자아개념과',
    '궁극적으로 진로 적응도(4C)를 극대화하고 변화하는 미래 직업 세계에'
]

print('=== CHECKING kice_d54_phase1_wordbook.html ===')
for bp in bad_phrases:
    cnt = text1.count(bp)
    print(f'Count of "{bp[:25]}...": {cnt}')

print('=== CHECKING kice_55_core_compressed.html ===')
for bp in bad_phrases:
    cnt = text2.count(bp)
    print(f'Count of "{bp[:25]}...": {cnt}')
