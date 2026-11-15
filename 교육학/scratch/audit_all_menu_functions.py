import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 팝업 메뉴 안의 onclick 속성들 전부 추출
onclicks = re.findall(r'onclick="([a-zA-Z0-9_]+)\([^\)]*?\)"', text)
unique_funcs = sorted(list(set(onclicks)))

print(f"Total unique onclick functions: {len(unique_funcs)}")

missing_funcs = []
for fn in unique_funcs:
    if f"function {fn}" not in text and f"{fn} =" not in text and f"{fn}=" not in text:
        missing_funcs.append(fn)

print(f"Missing functions count: {len(missing_funcs)}")
print("Missing functions:", missing_funcs)
