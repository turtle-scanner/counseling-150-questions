import re

with open('kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()

rows = re.findall(r'<tr>\s*<td class="td-num">(\d+)</td>\s*<td class="td-q">(.*?)</td>\s*<td class="td-kw">\s*<span class="kw-badge">(.*?)</span>\s*<div class="kw-name">(.*?)</div>\s*</td>\s*<td class="td-ans">\s*<div class="ans-box">(.*?)</div>\s*</td>', text, re.DOTALL)

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\dump_150_all.txt', 'w', encoding='utf-8') as out:
    for num, q, badge, kw, ans in rows:
        out.write(f"[{num}] ({badge}) {kw}\n")
        out.write(f"  Q: {q.strip()}\n")
        out.write(f"  A: {ans.strip()}\n\n")

print(f"Dumped {len(rows)} rows successfully.")
