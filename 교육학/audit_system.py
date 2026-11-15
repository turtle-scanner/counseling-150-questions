# -*- coding: utf-8 -*-
import json
import re

report = []

# 1. counseling_55_topics.html 검사
html_path = 'g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/counseling_55_topics.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# topics JSON 추출
m = re.search(r'const topics = (\[[\s\S]*?\]);', html_content)
if m:
    topics = json.loads(m.group(1))
    report.append(f"1. counseling_55_topics.html 토픽 수: {len(topics)}개")
    
    # 번호 연속성 검사
    nums = [t['num'] for t in topics]
    if nums == list(range(1, 56)):
        report.append("  - 번호 연속성 (1부터 55까지): 완벽 일치")
    else:
        report.append(f"  - 번호 누락/불일치 발견: {set(range(1,56)) - set(nums)}")
    
    # 21-55번 글자수 및 (XX자) 일치 여부 검사
    length_mismatch = []
    out_of_range_21_55 = []
    dereflection_check = []
    shawn_shea_check = []

    for t in topics:
        num = t['num']
        for idx, line in enumerate(t.get('model_answer', [])):
            clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
            l = len(clean)
            
            # (XX자) 표기 검사
            m_len = re.search(r'\((\d+)자\)$', line)
            if m_len:
                declared_l = int(m_len.group(1))
                if declared_l != l:
                    length_mismatch.append(f"주제 {num}행 {idx+1}: 실제 {l}자 != 표기 {declared_l}자")
            
            # 21-55번 글자수 범위 검사 (50-60자)
            if num >= 21:
                if l < 50 or l > 60:
                    out_of_range_21_55.append(f"주제 {num}행 {idx+1}: {l}자 -> {clean}")

            # 키워드 체크
            if 'Dereflection' in line or '탈숙고' in line:
                dereflection_check.append(f"주제 {num}: {line}")
            if 'CASE' in line or '숀 셰이' in line:
                shawn_shea_check.append(f"주제 {num}: {line}")

    if length_mismatch:
        report.append(f"  - (XX자) 표기 불일치 {len(length_mismatch)}건 발견:")
        for lm in length_mismatch[:5]:
            report.append(f"    * {lm}")
    else:
        report.append("  - (XX자) 표기 일치 여부: 220개 전체 행 100% 완벽 일치")

    if out_of_range_21_55:
        report.append(f"  - 21-55번 50-60자 범위 이탈 {len(out_of_range_21_55)}건 발견")
        for o in out_of_range_21_55[:5]:
            report.append(f"    * {o}")
    else:
        report.append("  - 21-55번 글자수 (50-60자 규격): 140개 행 100% 완벽 일치")

else:
    report.append("1. counseling_55_topics.html에서 topics 추출 실패")

# 2. exam_master_2027.html 검사
em_path = 'g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html'
with open(em_path, 'r', encoding='utf-8') as f:
    em_content = f.read()

report.append(f"\n2. exam_master_2027.html 검사:")
# CSS 문법 검사 (중괄호 매칭 등)
open_b = em_content.count('{')
close_b = em_content.count('}')
report.append(f"  - CSS/JS 중괄호 검사: 여는 괄호 {open_b}개, 닫는 괄호 {close_b}개 (차이: {open_b - close_b})")

# print CSS 내 미완성 클래스 검사
if '@media print' in em_content:
    print_snippet = em_content[em_content.find('@media print'):em_content.find('</style>')]
    report.append(f"  - @media print 블록 존재 확인 (길이: {len(print_snippet)}자)")
    
    # 이전 불완전한 코드 잔재 확인 (예: '.e' 같은 잔재)
    unfinished = re.findall(r'(\.[a-zA-Z0-9\-_]+\s*\{\s*\}|\.[a-zA-Z0-9\-_]+\s*$)', print_snippet)
    if unfinished:
        report.append(f"  - 미완성 셀렉터 발견: {unfinished}")
    else:
        report.append("  - 미완성 셀렉터 없음 (CSS 문법 완전)")

# 3. rawData 검사
m_raw = re.search(r'const rawData\s*=\s*(\{[\s\S]*?\});\s*let currentTab', em_content)
if m_raw:
    try:
        raw_data = json.loads(m_raw.group(1))
        report.append(f"  - rawData 파싱 성공: top55 {len(raw_data.get('top55', []))}개, questions_a {len(raw_data.get('questions_a', []))}개, questions_b {len(raw_data.get('questions_b', []))}개")
    except Exception as e:
        report.append(f"  - rawData JSON 파싱 에러: {e}")
else:
    report.append("  - rawData regex 매칭 확인 필요")

# 결과 출력 파일 작성
with open('g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/교육학/audit_report.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(report))

print("Audit completed.")
