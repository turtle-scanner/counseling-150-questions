import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

p3_q = text_q[text_q.find('## 【 3교시'):]
p3_a = text_a[text_a.find('## 【 3교시'):]

splits_q = list(re.finditer(r'\*\*(\d+)\.\*\*\s+(.*?)(?=\n\n|\n\[)', p3_q, re.DOTALL))
b_questions = []
for i in range(len(splits_q)):
    start_idx = splits_q[i].start()
    end_idx = splits_q[i+1].start() if i + 1 < len(splits_q) else len(p3_q)
    block = p3_q[start_idx:end_idx].strip()
    qnum = int(splits_q[i].group(1))
    lead = splits_q[i].group(2).strip()
    
    w_pos = block.find('[작성 방법]')
    if w_pos != -1:
        passage = block[:w_pos].strip()
        directions = block[w_pos:].strip()
    else:
        passage = block
        directions = ''
        
    b_questions.append({
        'qnum': qnum,
        'lead': lead,
        'passage': passage,
        'directions': directions
    })

splits_ans = list(re.finditer(r'-\s+\*\*(\d+)번\s*\(([^)]+)\)\*\*\s*:\s*(.*?)(?=\n-\s+\*\*\d+번|\n---|\Z)', p3_a, re.DOTALL))
b_answers = {int(s.group(1)): s.group(3).strip() for s in splits_ans}

for q in b_questions:
    qn = q['qnum']
    ans = b_answers.get(qn, 'NO ANSWER')
    print(f"=== B형 {qn}번 ===")
    print(f"Lead: {q['lead'][:60]}")
    print(f"Passage len: {len(q['passage'])}")
    print(f"Answer snippet: {ans[:100]}...")
