import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def clean_no_stars(s):
    if not s:
        return ''
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    s = s.replace('*', '')
    return s.strip()

def extract_model_answer(ans_str):
    if not ans_str:
        return ''
    pos_trophy = ans_str.find('🏆 [KICE 4점 만점 서술문]')
    if pos_trophy != -1:
        part = ans_str[pos_trophy + len('🏆 [KICE 4점 만점 서술문]'):].strip()
        pos_next = part.find('🔍')
        if pos_next != -1:
            part = part[:pos_next].strip()
        return part
    lines = ans_str.strip().split('\n')
    return lines[0].strip()

# Print sample of page 1 and page 7 to see how clean the text is
for p in [pages[0], pages[6]]:
    print(f"=== {p['pageTitle']} ===")
    for it in p['items'][:3]:
        print(f"[{it['id']}] {clean_no_stars(it['keywords'])}")
        print(f" Q: {clean_no_stars(it['question'])[:50]}")
        print(f" A: {clean_no_stars(extract_model_answer(it['answer']))[:70]}")
