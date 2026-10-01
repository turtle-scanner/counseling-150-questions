import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Check for any double asterisks (**text**) which are markdown bold syntax that shouldn't be in HTML/strings
double_stars = re.findall(r'\*\*.*?\*\*', text)
print('Double asterisks found in index.html:', len(double_stars))
for ds in double_stars[:5]:
    print(' -', ds)

# Check specifically in examQuestions04
pos_eq = text.find('const examQuestions04 =')
pos_eq_end = text.find('];', pos_eq) + 2
eq_str = text[pos_eq:pos_eq_end]
eq_stars = eq_str.count('*')
print('Asterisks in examQuestions04 JSON:', eq_stars)
assert eq_stars == 0, 'Asterisks found in examQuestions04!'

# Check in draftModal HTML
pos_modal = text.find('id="draftModal"')
pos_modal_end = text.find('</div>\n  </div>', pos_modal) + 15
modal_str = text[pos_modal:pos_modal_end]
modal_stars = modal_str.count('*')
print('Asterisks in draftModal HTML:', modal_stars)
assert modal_stars == 0, 'Asterisks found in draftModal HTML!'

print('✅ ZERO ASTERISKS strictly verified in all new components!')
