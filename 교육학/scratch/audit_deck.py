import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('let items = [') + len('let items = ')
end = text.find('];', start) + 1
items = json.loads(text[start:end])

all_text = ' '.join([it['kw'] + ' ' + it['q'] + ' ' + it['ans'] for it in items])

checks = {
    '탈숙고 (Dereflection)': '탈숙고',
    '숀 셰이 (CASE 모델)': 'CASE',
    'SUI 척도 (MMPI-2-RF)': 'SUI',
    'BXD 척도 (MMPI-2-RF)': 'BXD',
    'THD 척도 (MMPI-2-RF)': 'THD',
    'RAD vs DSED (반응성 vs 탈억제 애착장애)': '탈억제',
    'OCD vs OCPD (강박장애 vs 강박성 성격장애)': '강박성',
    '신체증상장애 vs 질병불안장애': '질병불안',
    '설리반 3대 자아상 (좋은 나, 나쁜 나, 내가 아닌 나)': '설리반',
    '머레이 욕구-압착 이론': '압착',
    '조하리의 창 4대 영역': '조하리',
    '메지로우 변혁적 학습 이론': '메지로우',
    '라이겔루스 정교화 이론': '라이겔루스',
    '성장참조평가 & 능력참조평가': '성장참조',
    '세르지오바니 도덕적 리더십': '세르지오바니',
    '겟젤스-구바 사회체계 모형': '겟젤스',
    '루브릭 (채점기준표 4요소)': '루브릭',
    '사비카스 생애 직업 스타일 면담 (CSI)': '사비카스',
    '갓프레드슨 직업포부 제한-타협': '갓프레드슨',
    'Sue 다문화 역량 & 미세공격 (Microaggression)': '미세공격',
    '길리랜드 & 제임스 6단계 & 안전계획서': '안전계획서'
}

with open('scratch/audit_results.txt', 'w', encoding='utf-8') as out:
    for k, v in checks.items():
        present = v in all_text
        out.write(f"[{'O' if present else 'X'}] {k}\n")

print("Audit finished successfully.")
