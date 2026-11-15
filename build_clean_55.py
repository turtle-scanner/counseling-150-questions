# -*- coding: utf-8 -*-
import os
import re
import json

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
py_path = os.path.join(base_dir, "complete_counseling_55_builder.py")

with open(py_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Extract counseling_55_topics
match = re.search(r'counseling_55_topics\s*=\s*(\[[\s\S]*?\])\n\n# Validation', code)
if not match:
    # Try finding up to html = 
    match = re.search(r'counseling_55_topics\s*=\s*(\[[\s\S]*?\])\n\n#', code)

topics = eval(match.group(1))
print(f"Loaded {len(topics)} topics successfully.")

# Exact replacements: (topic_num, line_idx 0..3) -> clean_text
fixes = {
    (1, 0): "자폐스펙트럼장애는 사회적 상호작용 결함과 상동증적 반복 행동을 동반한다.",
    (2, 0): "지속적인 주의 집중 곤란과 가만있지 못하는 과잉행동 및 충동성을 보인다.",
    (3, 0): "적대적 반항장애는 권위자에게 자주 화를 내고 논쟁하며 심하게 반항한다.",
    (4, 0): "상황에 부합하지 않게 극심한 분노를 폭발하며 매주 3회 이상 지속된다.",
    (4, 1): "분노 폭발 사이의 기간에도 거의 매일 지속적인 과민한 기분 상태를 보인다.",
    (4, 3): "만 6세 이상부터 진단 가능하며 10세 이전에 증상이 시작되어야 한다.",
    (6, 3): "고통스러운 실제 신체 증상의 존재 유무를 기준으로 두 장애를 감별한다.",
    (7, 1): "강박성 성격장애는 엄격한 완벽주의와 정리정돈 및 대인 통제에 집착한다.",
    (7, 2): "강박장애는 스스로 고통스러운 자아이질적이며 성격장애는 자아동질적이다.",
    (8, 2): "과도한 놀람 반응과 분노 폭발 등 신경계의 지속적 과각성 상태를 보인다.",
    (10, 1): "의존성 성격장애는 지속적인 돌봄을 받기 위해 타인에게 굴종 복종한다.",
    (11, 1): "망상이나 환각 및 와해된 언어 중 하나는 진단에 반드시 포함되어야 한다.",
    (12, 2): "임상적으로 현저하게 낮은 저체중이 존재하면 식욕부진증으로 우선 진단한다.",
    (12, 3): "부모가 자녀의 건강한 식사를 감독하고 왜곡된 인지적 신체상을 수정 지원한다.",
    (21, 3): "자율성과 협동성이 모두 낮을 때 성격장애의 발병 위험성이 매우 높다.",
    (22, 0): "내담자가 자신과 가장 강하게 동일시하는 인물을 핵심 주인공으로 정한다.",
    (22, 1): "주인공의 내적 감정과 동기를 분석하여 내담자의 무의식적 욕구를 캔다.",
    (23, 3): "통찰을 실제 일상생활에서 반복 연습하고 행동을 수정하는 훈습을 거친다.",
    (37, 0): "일치형은 자신과 타인 및 상황을 모두 온전히 존중하며 솔직히 소통한다.",
    (38, 0): "표면의 외현적 문제 행동 이면에 숨겨진 무의식적 감정과 기대를 캔다.",
    (38, 1): "화가 난 자신에게 죄책감을 느끼는 등 억압된 감정에 대한 감정을 본다.",
    (38, 2): "부모에게 끝내 충족되지 못한 과거의 오랜 기대를 스스로 내려놓고 벗어난다."
}

def remove_tilde(s):
    if isinstance(s, str):
        return s.replace("~", "-")
    elif isinstance(s, list):
        return [remove_tilde(x) for x in s]
    elif isinstance(s, dict):
        return {k: remove_tilde(v) for k, v in s.items()}
    return s

# Apply fixes and clean
for t in topics:
    num = t['num']
    for idx in range(len(t['model_answer'])):
        if (num, idx) in fixes:
            clean_text = fixes[(num, idx)]
            t['model_answer'][idx] = f"{clean_text} ({len(clean_text)}자)"
        else:
            line = t['model_answer'][idx]
            clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
            clean = clean.replace("~", "-")
            t['model_answer'][idx] = f"{clean} ({len(clean)}자)"
    
    # Remove tildes from all other fields
    t['title'] = remove_tilde(t.get('title', ''))
    t['concept'] = remove_tilde(t.get('concept', ''))
    t['sub_questions'] = remove_tilde(t.get('sub_questions', []))
    t['keywords'] = remove_tilde(t.get('keywords', []))
    t['rubric'] = remove_tilde(t.get('rubric', []))

# Validate all 55 topics
print("--- VALIDATION OF ALL 55 TOPICS ---")
err_count = 0
for t in topics:
    for idx, line in enumerate(t['model_answer']):
        clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
        l = len(clean)
        if l < 38 or l > 45:
            print(f"[FAIL] Topic {t['num']} Line {idx+1}: len={l} -> {clean}")
            err_count += 1

if err_count == 0:
    print(f"[SUCCESS] All {len(topics)*4} lines are strictly between 38 and 45 characters!")
else:
    print(f"[ERROR] {err_count} errors remain!")
    exit(1)

# Format topics to python code string
def format_topic_dict(t):
    lines = []
    lines.append("    {")
    lines.append(f'        "domain": {json.dumps(t["domain"], ensure_ascii=False)},')
    lines.append(f'        "num": {t["num"]},')
    lines.append(f'        "title": {json.dumps(t["title"], ensure_ascii=False)},')
    lines.append(f'        "concept": {json.dumps(t["concept"], ensure_ascii=False)},')
    
    # sub_questions
    lines.append('        "sub_questions": [')
    for q in t["sub_questions"]:
        lines.append(f'            {json.dumps(q, ensure_ascii=False)},')
    if t["sub_questions"]:
        lines[-1] = lines[-1].rstrip(',')
    lines.append('        ],')
    
    # keywords
    kw_str = ", ".join(json.dumps(k, ensure_ascii=False) for k in t["keywords"])
    lines.append(f'        "keywords": [{kw_str}],')
    
    # model_answer
    lines.append('        "model_answer": [')
    for a in t["model_answer"]:
        lines.append(f'            {json.dumps(a, ensure_ascii=False)},')
    if t["model_answer"]:
        lines[-1] = lines[-1].rstrip(',')
    lines.append('        ],')
    
    # rubric
    lines.append('        "rubric": [')
    for r in t["rubric"]:
        lines.append(f'            {json.dumps(r, ensure_ascii=False)},')
    if t["rubric"]:
        lines[-1] = lines[-1].rstrip(',')
    lines.append('        ]')
    lines.append("    }")
    return "\n".join(lines)

formatted_topics = "[\n" + ",\n".join(format_topic_dict(t) for t in topics) + "\n]"

# Build the complete python script content
# Find the rest of complete_counseling_55_builder.py after the topics array
val_idx = code.find("# Validation")
if val_idx == -1:
    val_idx = code.find("# Validation", code.find("counseling_55_topics ="))
header_code = code[:code.find("counseling_55_topics = ")] + "counseling_55_topics = "
rest_code = code[val_idx:]

new_py_content = header_code + formatted_topics + "\n\n" + rest_code
# Replace any remaining tildes in HTML template
new_py_content = new_py_content.replace("3~4개", "3-4개")
new_py_content = new_py_content.replace("38~45자", "38-45자")
new_py_content = new_py_content.replace("1~9호", "1호-9호")

with open(py_path, 'w', encoding='utf-8') as f:
    f.write(new_py_content)
print(f"[UPDATED] {py_path}")

# Now generate the HTML files
# We can execute the updated script or generate HTML directly
with open('counseling_data.json', 'w', encoding='utf-8') as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)
print("[SAVED] counseling_data.json")
