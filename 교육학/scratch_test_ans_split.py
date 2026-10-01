import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

p2_a = text_a[text_a.find('## 【 2교시'):text_a.find('## 【 3교시')]
p3_a = text_a[text_a.find('## 【 3교시'):]

def split_major_answers(period_text):
    # Regex matching - **1번 (2점)** : or similar
    splits = list(re.finditer(r'-\s+\*\*(\d+)번\s*\(([^)]+)\)\*\*\s*:\s*(.*?)(?=\n-\s+\*\*\d+번|\n---|\Z)', period_text, re.DOTALL))
    answers = {}
    for s in splits:
        qnum = int(s.group(1))
        score_str = s.group(2)
        content = s.group(3).strip()
        answers[qnum] = {
            'score': score_str,
            'content': content
        }
    return answers

ans_a = split_major_answers(p2_a)
ans_b = split_major_answers(p3_a)

print(f'Parsed {len(ans_a)} answers for A형: {list(ans_a.keys())}')
print(f'Parsed {len(ans_b)} answers for B형: {list(ans_b.keys())}')
