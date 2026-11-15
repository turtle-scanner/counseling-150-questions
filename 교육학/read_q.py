import json, re

with open('exam_2027_kice_ab.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const questions\s*=\s*(\[.*?\]);\s*\n', text, re.DOTALL)
if not m:
    # search without strict semicolon
    idx_start = text.find('const questions = [')
    if idx_start != -1:
        # find matching bracket
        print('Found questions start at', idx_start)
        # find closing bracket
        idx_end = text.find('];', idx_start)
        raw_json = text[idx_start + len('const questions = '):idx_end + 1]
        questions = json.loads(raw_json)
        for q in questions:
            if q.get('id') in ['B8', 'B9', 'B10', 'B11']:
                print('====================', q['id'], '====================')
                print('CONTENT:', q.get('content'))
                print('INSTRUCTIONS:', q.get('instructions'))
                print('ANSWER:', q.get('answer'))
                print('RUBRIC:', q.get('rubric'))
