from bs4 import BeautifulSoup

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

rows = soup.find_all('tr')
answers = []
for r in rows:
    td_ans = r.find('td', class_='td-ans')
    if td_ans:
        ans_box = td_ans.find('div', class_='ans-box')
        text = ans_box.get_text(strip=True) if ans_box else td_ans.get_text(strip=True)
        answers.append(text)

print(f"Total answers extracted from existing HTML: {len(answers)}")
with open('scratch/extracted_answers.txt', 'w', encoding='utf-8') as f:
    for i, a in enumerate(answers[:5]):
        f.write(f"Item {i+1}: {a}\n")
print("Done writing sample extracted answers.")
