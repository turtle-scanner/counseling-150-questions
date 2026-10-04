import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

trap_html = '<div class="trap-box" id="c-trap" style="display:none;"></div>'

if 'id="c-trap"' not in html:
    # Use regex that handles any whitespace / CRLF
    html = re.sub(
        r'(<div class="answer-text" id="c-ans">[\s\S]*?</div>)',
        r'\1\n            ' + trap_html,
        html
    )

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected c-trap with regex successfully!")
