target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace font-weight: 600 in ULTRA-STRICT block with font-weight: 400
html = html.replace('.card-q, #c-q {\n      font-weight: 600 !important;', '.card-q, #c-q {\n      font-weight: 400 !important;')
html = html.replace('.card-q, #c-q {\r\n      font-weight: 600 !important;', '.card-q, #c-q {\r\n      font-weight: 400 !important;')

html = html.replace('.answer-text, #c-ans {\n      font-weight: 600 !important;', '.answer-text, #c-ans {\n      font-weight: 400 !important;')
html = html.replace('.answer-text, #c-ans {\r\n      font-weight: 600 !important;', '.answer-text, #c-ans {\r\n      font-weight: 400 !important;')

# In case there are other font-weight: 600 on card-q or answer-text
html = html.replace('font-weight: 600 !important;', 'font-weight: 400 !important;')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully set font-weight to 400!")
