import sys, os, json, re

with open('scratch/final_55_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def compress_q(text):
    text = re.sub(r'의\s+공식\s+명칭을\s+쓸\s+것\.', '', text)
    text = re.sub(r'의\s+명칭을\s+쓸\s+것\.', '', text)
    text = re.sub(r'공식\s+개념\s+\d+가지를\s+쓸\s+것\.', '', text)
    text = re.sub(r'를\s+뜻하는', '', text)
    text = re.sub(r'을\s+뜻하는', '', text)
    text = re.sub(r'를\s+의미하는', '', text)
    text = re.sub(r'을\s+의미하는', '', text)
    text = re.sub(r'를\s+특징으로\s+하는', '', text)
    text = re.sub(r'을\s+특징으로\s+하는', '', text)
    text = re.sub(r'명칭\?', '', text)
    text = re.sub(r'개념\?', '', text)
    
    # Compress clauses
    text = re.sub(r'하여(서)?\s+', ' ➔ ', text)
    text = re.sub(r'하며\s+', ' ➔ ', text)
    text = re.sub(r'하고\s+', ' ➔ ', text)
    text = re.sub(r'하는\s+', ' ', text)
    text = re.sub(r'으로,\s+', ' ➔ ', text)
    text = re.sub(r'상태로,\s+', ' ➔ ', text)
    text = re.sub(r'현상으로,\s+', ' ➔ ', text)
    
    # Remove markers
    text = re.sub(r'은\s+', ' ', text)
    text = re.sub(r'는\s+', ' ', text)
    text = re.sub(r'이\s+', ' ', text)
    text = re.sub(r'가\s+', ' ', text)
    text = re.sub(r'을\s+', ' ', text)
    text = re.sub(r'를\s+', ' ', text)
    text = re.sub(r'에\s+', ' ', text)
    text = re.sub(r'에서\s+', ' ', text)
    text = re.sub(r'로\s+', ' ', text)
    text = re.sub(r'으로\s+', ' ', text)
    text = re.sub(r'과\s+', '·', text)
    text = re.sub(r'와\s+', '·', text)
    
    # Cleanup double spaces and arrows
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'( ➔ )+', ' ➔ ', text)
    text = text.strip(' ➔')
    return text.strip()

for it in items:
    it['q'] = compress_q(it['q'])

ped_items = [it for it in items if it['badge'] in ['교육과정', '교육방법', '교육평가', '교육행정']]
coun_items = [it for it in items if it['badge'] not in ['교육과정', '교육방법', '교육평가', '교육행정']]

artifact_dir = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034'
out_path = os.path.join(artifact_dir, '2027_적중1순위_초압축_55제_암기장.md')

md = []
md.append('# 🚨 2027 KICE 출제확률 99% 초압축 55제 (현상학적 키워드 압축판)\n')
md.append('> [!TIP]')
md.append('> 선생님의 요청에 따라, 실전 문제 지문(단서)까지 **조사 및 서술어를 모두 제거하고 핵심 단어(명사형) 중심**으로 한 번 더 초압축했습니다. 눈으로만 스캔해도 바로 정답이 튀어나오도록 훈련하십시오.\n')

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
print('Done generating compressed artifact!')
