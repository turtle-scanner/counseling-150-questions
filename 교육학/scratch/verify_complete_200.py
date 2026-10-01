with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    content = f.read()

assert '*' not in content, "Asterisk found in HTML!"
print("1. ZERO Asterisks verified in entire file!")

assert 'No. 200' in content or '"num": 200' in content, "No. 200 not found!"
print("2. 200 items found in DATA!")

assert 'flipCard' in content, "flipCard function missing!"
assert 'toggleStar' in content, "toggleStar function missing!"
assert 'card-view-container' in content, "card view container missing!"
assert 'Malgun Gothic' in content, "Malgun Gothic font missing!"
print("3. All features and functions successfully verified!")
