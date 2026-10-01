from bs4 import BeautifulSoup

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

rows = soup.find_all('tr')
# header rows vs data rows
data_rows = []
for r in rows:
    td_num = r.find('td', class_='td-num')
    if td_num:
        num = td_num.get_text(strip=True)
        td_kw = r.find('td', class_='td-kw')
        badge = td_kw.find('span', class_='kw-badge').get_text(strip=True) if td_kw.find('span', class_='kw-badge') else ''
        kw_name = td_kw.find('div', class_='kw-name').get_text(strip=True) if td_kw.find('div', class_='kw-name') else ''
        td_q = r.find('td', class_='td-q').get_text(strip=True) if r.find('td', class_='td-q') else ''
        td_ans = r.find('td', class_='td-ans').get_text(strip=True) if r.find('td', class_='td-ans') else ''
        data_rows.append({
            'num': num,
            'badge': badge,
            'kw_name': kw_name,
            'question': td_q,
            'answer': td_ans
        })

print(f"Extracted {len(data_rows)} data rows from existing HTML.")
print("First row:", data_rows[0])
print("Last row:", data_rows[-1])
