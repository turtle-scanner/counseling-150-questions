import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

names = ['황충', '서황', '태사자', '공손찬']
for name in names:
    pos = text.find(name)
    print(f"Officer '{name}' in text:", pos != -1)
    if pos != -1:
        start = max(0, text.rfind('{', 0, pos))
        end = text.find('}', pos) + 1
        sys.stdout.buffer.write(text[start:end].encode('utf-8') + b'\n---\n')
