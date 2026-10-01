import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

p2_q = text_q[text_q.find('## 【 2교시'):text_q.find('## 【 3교시')]
p3_q = text_q[text_q.find('## 【 3교시'):]

def split_major_questions(period_text, period_name):
    # Regex matching **1.** or **2.** etc.
    splits = list(re.finditer(r'\*\*(\d+)\.\*\*\s+(.*?)(?=\n\n|\n\[)', period_text, re.DOTALL))
    questions = []
    for i in range(len(splits)):
        start_idx = splits[i].start()
        end_idx = splits[i+1].start() if i + 1 < len(splits) else len(period_text)
        block = period_text[start_idx:end_idx].strip()
        
        qnum = int(splits[i].group(1))
        lead_line = splits[i].group(2).strip()
        
        # parse passage and 작성 방법
        # Look for [작성 방법]
        w_pos = block.find('[작성 방법]')
        if w_pos != -1:
            main_body = block[:w_pos].strip()
            directions = block[w_pos:].strip()
        else:
            main_body = block
            directions = ''
            
        questions.append({
            'period': period_name,
            'qnum': qnum,
            'lead_line': lead_line,
            'main_body': main_body,
            'directions': directions
        })
    return questions

q_a = split_major_questions(p2_q, '2교시 전공상담 A형')
q_b = split_major_questions(p3_q, '3교시 전공상담 B형')

print(f'Parsed {len(q_a)} questions for A형:')
for q in q_a:
    print(f" A {q['qnum']}: length {len(q['main_body'])}, directions len {len(q['directions'])}")

print(f'Parsed {len(q_b)} questions for B형:')
for q in q_b:
    print(f" B {q['qnum']}: length {len(q['main_body'])}, directions len {len(q['directions'])}")
