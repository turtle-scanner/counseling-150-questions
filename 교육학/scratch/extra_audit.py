import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('let items = [') + len('let items = ')
end = text.find('];', start) + 1
items = json.loads(text[start:end])
all_text = ' '.join([it['kw'] + ' ' + it['q'] + ' ' + it['ans'] for it in items])

extra_checks = {
    '렌줄리 (심화학습/3고리)': '렌줄리',
    '비고츠키 (ZPD/역동적평가)': '비고츠키',
    '타바 (귀납적 교육과정)': '타바',
    '플립드 러닝': '플립드',
    '아들러 4대 생활양식': '생활양식',
    '로저스 인간중심 3대 필요충분조건': '일치성',
    '얄롬 집단상담 치료적 요인': '얄롬',
    '수퍼바이저 3대 역할 (버나드)': '버나드'
}

with open('scratch/extra_checks.txt', 'w', encoding='utf-8') as out:
    for k, v in extra_checks.items():
        out.write(f"[{'O' if v in all_text else 'X'}] {k}\n")

print("Extra checks done.")
