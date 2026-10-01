import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Read source files
with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

def clean_no_stars(s):
    if not s:
        return ''
    # Replace **bold** with <strong>bold</strong>
    s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
    s = s.replace('*', '')
    return s.strip()

# Partition 문제지
p1_q = text_q[text_q.find('## 【 1교시'):text_q.find('## 【 2교시')].strip()
p2_q = text_q[text_q.find('## 【 2교시'):text_q.find('## 【 3교시')].strip()
p3_q = text_q[text_q.find('## 【 3교시'):].strip()

# Partition 해설지
p1_a = text_a[text_a.find('## 【 1교시'):text_a.find('## 【 2교시')].strip()
p2_a = text_a[text_a.find('## 【 2교시'):text_a.find('## 【 3교시')].strip()
p3_a = text_a[text_a.find('## 【 3교시'):].strip()

def split_major_questions(period_text, period_name, period_key):
    splits = list(re.finditer(r'\*\*(\d+)\.\*\*\s+(.*?)(?=\n\n|\n\[)', period_text, re.DOTALL))
    questions = []
    for i in range(len(splits)):
        start_idx = splits[i].start()
        end_idx = splits[i+1].start() if i + 1 < len(splits) else len(period_text)
        block = period_text[start_idx:end_idx].strip()
        
        qnum = int(splits[i].group(1))
        lead = splits[i].group(2).strip()
        
        w_pos = block.find('[작성 방법]')
        if w_pos != -1:
            passage = block[:w_pos].strip()
            directions = block[w_pos:].strip()
        else:
            passage = block
            directions = ''
            
        questions.append({
            'period': period_name,
            'periodKey': period_key,
            'qnum': qnum,
            'lead': clean_no_stars(lead),
            'passage': clean_no_stars(passage),
            'directions': clean_no_stars(directions)
        })
    return questions

def split_major_answers(period_text):
    splits = list(re.finditer(r'-\s+\*\*(\d+)번\s*\(([^)]+)\)\*\*\s*:\s*(.*?)(?=\n-\s+\*\*\d+번|\n---|\Z)', period_text, re.DOTALL))
    answers = {}
    for s in splits:
        qnum = int(s.group(1))
        score_str = s.group(2).strip()
        content = s.group(3).strip()
        answers[qnum] = {
            'score': score_str,
            'content': clean_no_stars(content)
        }
    return answers

q_a = split_major_questions(p2_q, '2교시 전공상담 A형', 'major_a')
q_b = split_major_questions(p3_q, '3교시 전공상담 B형', 'major_b')

ans_a = split_major_answers(p2_a)
ans_b = split_major_answers(p3_a)

print(f'Major A questions: {len(q_a)}, answers: {len(ans_a)}')
print(f'Major B questions: {len(q_b)}, answers: {len(ans_b)}')
