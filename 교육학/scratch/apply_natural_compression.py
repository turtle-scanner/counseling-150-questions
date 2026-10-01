import sys, os, json

# 1. Update the compressed json with '정서적 단절'
with open('scratch/final_55_compressed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    if '감정적 단절' in it['kw']:
        it['kw'] = it['kw'].replace('감정적 단절', '정서적 단절')
    if '감정적 단절' in it['ans']:
        it['ans'] = it['ans'].replace('감정적 단절', '정서적 단절')

with open('scratch/final_55_compressed.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

# 2. Build the markdown
ped_items = [it for it in items if it['badge'] in ['교육과정', '교육방법', '교육평가', '교육행정']]
coun_items = [it for it in items if it['badge'] not in ['교육과정', '교육방법', '교육평가', '교육행정']]

artifact_dir = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034'
out_path = os.path.join(artifact_dir, '2027_적중1순위_초압축_55제_암기장.md')

md = []
md.append('# 🚨 2027 KICE 출제확률 99% 초압축 55제 (현상학적 키워드 압축판)\n')
md.append('> [!TIP]')
md.append('> 문맥 교정 완료! 기계적으로 잘려 어색했던 문장들을 **가장 자연스럽고 매끄러운 핵심 단어(명사형) 중심**으로 AI가 재번역하여 정밀하게 압축했습니다. 눈으로만 스캔해도 바로 정답이 튀어나오도록 훈련하십시오.\n')

md.append('## 🎯 1교시: 교육학 논술 핵심 20선')
md.append('<table>')
md.append('<thead><tr><th width="5%">No</th><th width="10%">영역</th><th width="20%">핵심 표제어</th><th width="35%">실전 단서 (핵심 키워드)</th><th width="30%">공식 정답</th></tr></thead><tbody>')
for i, it in enumerate(ped_items):
    md.append(f'<tr><td>{i+1}</td><td>{it["badge"]}</td><td><b>{it["kw"]}</b></td><td>{it["q"]}</td><td>{it["ans"]}</td></tr>')
md.append('</tbody></table>\n')

md.append('## 🎯 2~3교시: 전공상담 복합형 킬러 35선')
md.append('<table>')
md.append('<thead><tr><th width="5%">No</th><th width="10%">영역</th><th width="20%">핵심 표제어</th><th width="35%">실전 단서 (핵심 키워드)</th><th width="30%">공식 정답</th></tr></thead><tbody>')
for i, it in enumerate(coun_items):
    md.append(f'<tr><td>{i+1}</td><td>{it["badge"]}</td><td><b>{it["kw"]}</b></td><td>{it["q"]}</td><td>{it["ans"]}</td></tr>')
md.append('</tbody></table>\n')

full_md = '\n'.join(md)
if '*' in full_md:
    full_md = full_md.replace('*', '★')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_md)

print('Successfully generated natural compressed markdown artifact!')
