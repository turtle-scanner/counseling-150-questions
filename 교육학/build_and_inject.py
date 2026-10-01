import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

def no_stars(s):
    if not s:
        return ''
    s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
    s = s.replace('*', '')
    return s.strip()

# Let's inspect index.html path
target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

print('Read index.html, size:', len(html_content))
