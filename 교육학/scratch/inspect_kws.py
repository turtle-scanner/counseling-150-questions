from bs4 import BeautifulSoup
import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

rows = soup.find_all('tr')
items = []
for r in rows:
    td_num = r.find('td', class_='td-num')
    if td_num:
        num = int(td_num.get_text(strip=True))
        td_kw = r.find('td', class_='td-kw')
        badge = td_kw.find('span', class_='kw-badge').get_text(strip=True) if td_kw.find('span', class_='kw-badge') else ''
        kw_name = td_kw.find('div', class_='kw-name').get_text(strip=True) if td_kw.find('div', class_='kw-name') else ''
        td_q = r.find('td', class_='td-q').get_text(strip=True) if r.find('td', class_='td-q') else ''
        td_ans = r.find('td', class_='td-ans')
        ans_box = td_ans.find('div', class_='ans-box') if td_ans else None
        ans = ans_box.get_text(strip=True) if ans_box else (td_ans.get_text(strip=True) if td_ans else '')
        items.append({
            'num': num,
            'badge': badge,
            'kw_name': kw_name,
            'question': td_q,
            'answer': ans
        })

print(f"Total extracted: {len(items)}")

# Save all kw_names to a file to inspect English full names
with open('scratch/all_keywords.txt', 'w', encoding='utf-8') as f:
    for it in items:
        f.write(f"{it['num']:3d} | [{it['badge']}] {it['kw_name']}\n")

print("Saved all_keywords.txt")
