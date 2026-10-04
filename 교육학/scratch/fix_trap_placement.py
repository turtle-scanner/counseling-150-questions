target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

trap_html = '<div class="trap-box" id="c-trap" style="display:none;"></div>'

if 'id="c-trap"' not in html:
    # insert right after <div class="answer-text" id="c-ans">...</div>
    html = html.replace('</div>\n            <div class="reward-container"', '</div>\n            ' + trap_html + '\n            <div class="reward-container"')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected c-trap successfully!")
