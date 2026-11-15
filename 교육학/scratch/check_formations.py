import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_form = text.find('const FORMATIONS = {')
print('FORMATIONS found at:', pos_form)
if pos_form != -1:
    sys.stdout.buffer.write(text[pos_form:pos_form+1200].encode('utf-8'))
