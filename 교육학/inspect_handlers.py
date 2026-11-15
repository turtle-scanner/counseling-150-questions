# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's inspect closeModal and safe click handlers
print("Checking closeModal definition:")
import re
match = re.search(r'function closeModal\(id\)\s*\{[^}]*\}', text)
if match:
    print(match.group(0))

# Also check if there's any backdrop or element with pointer-events issue
# And let's inspect the game start button onclick handler
btn_matches = re.findall(r'<button[^>]*closeModal\(\'liu-bei-intro-modal\'\)[^>]*>.*?</button>', text, re.DOTALL)
for b in btn_matches:
    print("\nButton found:\n", b[:200].encode('ascii', errors='backslashreplace').decode('ascii'))
