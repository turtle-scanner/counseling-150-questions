from bs4 import BeautifulSoup

file_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check asterisks
assert '*' not in content, "Asterisk found in HTML!"
print("1. ZERO Asterisks verified!")

# Parse HTML
soup = BeautifulSoup(content, 'html.parser')
rows = soup.find('tbody').find_all('tr')
print(f"2. Total table rows in tbody: {len(rows)}")
assert len(rows) == 150, f"Expected 150 rows, found {len(rows)}"

# Check No 1, 75, 150
first_row = [td.get_text(strip=True) for td in rows[0].find_all('td')]
row_75 = [td.get_text(strip=True) for td in rows[74].find_all('td')]
row_129 = [td.get_text(strip=True) for td in rows[128].find_all('td')]
last_row = [td.get_text(strip=True) for td in rows[149].find_all('td')]

with open('scratch/verification_summary.txt', 'w', encoding='utf-8') as f:
    f.write(f"Row 1: {first_row}\n\n")
    f.write(f"Row 75 (탈숙고): {row_75}\n\n")
    f.write(f"Row 129 (CASE 모델): {row_129}\n\n")
    f.write(f"Row 150: {last_row}\n\n")

print("3. Verification successful and saved to scratch/verification_summary.txt!")
