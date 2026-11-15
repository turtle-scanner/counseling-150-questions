# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find all popup menu containers
popups = re.findall(r'<div[^>]*id="popup-[^"]*"[^>]*>.*?</div>\s*</div>', text, re.DOTALL)
print(f"Total popup menus: {len(popups)}")

onclick_calls = re.findall(r'onclick="([a-zA-Z0-9_]+)\([^"]*\)"', text)
unique_calls = sorted(list(set(onclick_calls)))
print(f"Total unique onclick functions found in HTML: {len(unique_calls)}")

missing = []
found = []
for fn in unique_calls:
    if f'function {fn}' in text or f'{fn} =' in text:
        found.append(fn)
    else:
        missing.append(fn)

print(f"\nFOUND ({len(found)}): {found}")
print(f"\nMISSING FUNCTIONS ({len(missing)}):")
for m in missing:
    print(f"  - {m}")
