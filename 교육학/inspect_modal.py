# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = 0
found = []
while True:
    p = text.find('liu-bei-intro-modal', pos)
    if p == -1:
        break
    found.append(p)
    pos = p + 1

print(f"Total occurrences of liu-bei-intro-modal: {len(found)}")
for p in found:
    print(f"\n--- At index {p} ---")
    snippet = text[max(0, p - 80): min(len(text), p + 800)]
    print(snippet.encode('ascii', errors='backslashreplace').decode('ascii'))
