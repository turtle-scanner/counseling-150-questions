import sys
import os
import json

sys.path.insert(0, 'scratch')
from generate_continuous_200 import all_200

# Fix Item 5 to explicitly include 표현적 결과
for it in all_200:
    if it['num'] == 5:
        it['kw'] = "표현적 결과, 교육적 감식안, 교육비평"
        it['q'] = "행동목표의 한계를 비판하며, 사전에 목표를 정하지 않고 교육 활동 중이나 종료 후에 학습자가 얻게 되는 다의적인 성과, 그리고 학생 성취의 미묘한 질적 차이를 감별하고 비평하는 교사의 전문적 심미안을 뜻하는 공식 개념 3가지를 쓸 것."
        it['ans'] = "사전 목표 없이 활동 중이나 후에 얻어지는 '표현적 결과', 성취의 미묘한 질적 차이를 감지하는 교사의 안목인 '교육적 감식안', 그리고 이를 언어화하여 공유하는 '교육비평'이다."
    if it['num'] == 1:
        it['kw'] = "백워드 설계 모형 (영속적 이해)"

pedagogy_kws = ['워커', '자연주의', '라이겔루스', '정교화', '성장참조', '메지로우', '변혁적', '렌줄리', '심화학습', '비고츠키', '역동적', '세르지오바니', '도덕적', '타바', '귀납적', '플립드', '메이거', '루브릭', '겟젤스']
counseling_kws = ['강박', '자폐', '신체증상', '질병불안', '공황', '클라크', '광장공포', '경계선', '의존성', '해리성', '외상후', 'PTSD', 'ADHD', '애착', '탈억제', '적대적', '품행', 'SUI', 'BXD', 'THD', 'RCd', 'RC1', 'RC3', 'MPS', '보웬', '탈삼각화', '미누친', '경계선', '사티어', '일치형', '헤일리', '역설적', '프랑클', '탈숙고', 'REBT', '논박', '아론 벡', '재앙화', '개인화', '선택적', '게슈탈트', '반전', '내사', '융합', '설리반', '머레이', '조하리', '수퍼바이저', '융', '페르소나', '다문화', '미세공격', '사비카스', '갓프레드슨', '수퍼', '홀랜드', '해리스', '자살위기', '안전계획서', '랜드레스', '학폭법']

# Force items 1 and 5
must_have_ped = [it for it in all_200 if it['num'] in [1, 5]]
other_ped = [it for it in all_200 if it['badge'] in ['교육과정', '교육방법', '교육평가', '교육행정'] and it['num'] not in [1, 5]]
coun_items = [it for it in all_200 if it['badge'] not in ['교육과정', '교육방법', '교육평가', '교육행정']]

def score(item, kws):
    text = item['kw'] + ' ' + item['q'] + ' ' + item['ans']
    return sum(1 for k in kws if k in text)

other_ped.sort(key=lambda x: score(x, pedagogy_kws), reverse=True)
coun_items.sort(key=lambda x: score(x, counseling_kws), reverse=True)

final_ped = must_have_ped + other_ped[:18]
final_coun = coun_items[:35]
final_55 = final_ped + final_coun

artifact_dir = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034'
out_path = os.path.join(artifact_dir, '2027_적중1순위_초압축_55제_암기장.md')

md = []
md.append('# 🚨 2027 KICE 출제확률 99% 초압축 55제 (출제금지 구역 제외)\n')
md.append('> [!IMPORTANT]')
md.append('> 선생님의 특별 추가 요청에 따라, **백워드 설계(영속적 이해)** 및 **아이즈너(표현적 결과, 감식안, 교육비평)**를 1순위로 승격하여 55개 영구 동결 범위에 완벽히 반영했습니다.\n')

md.append('## 🎯 1교시: 교육학 논술 핵심 20선')
md.append('<table>')
md.append('<thead><tr><th width="5%">No</th><th width="10%">영역</th><th width="20%">핵심 표제어</th><th width="35%">실전 단서 (문제)</th><th width="30%">공식 정답</th></tr></thead><tbody>')
for i, it in enumerate(final_ped):
    md.append(f'<tr><td>{i+1}</td><td>{it["badge"]}</td><td><b>{it["kw"]}</b></td><td>{it["q"]}</td><td>{it["ans"]}</td></tr>')
md.append('</tbody></table>\n')

md.append('## 🎯 2~3교시: 전공상담 복합형 킬러 35선')
md.append('<table>')
md.append('<thead><tr><th width="5%">No</th><th width="10%">영역</th><th width="20%">핵심 표제어</th><th width="35%">실전 단서 (문제)</th><th width="30%">공식 정답</th></tr></thead><tbody>')
for i, it in enumerate(final_coun):
    md.append(f'<tr><td>{i+1}</td><td>{it["badge"]}</td><td><b>{it["kw"]}</b></td><td>{it["q"]}</td><td>{it["ans"]}</td></tr>')
md.append('</tbody></table>\n')

full_md = '\n'.join(md)
if '*' in full_md:
    full_md = full_md.replace('*', '★')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_md)
print('Updated 55 items artifact successfully.')
