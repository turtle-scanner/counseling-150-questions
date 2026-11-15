import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    html = f.read()

kws = re.findall(r'<div class="kw-name">(.*?)</div>', html)

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\eng_kws_list.txt', 'w', encoding='utf-8') as out:
    for i, kw in enumerate(kws):
        if re.search(r'[A-Za-z]', kw):
            out.write(f"[{i+1}] {kw}\n")

print("Done listing English kws.")
