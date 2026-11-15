# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

suspicious_keywords = [
    'save_modal_target', 'multiplay_modal_html', 'multiplay_js_code', 'Step 3:', 
    'print(', 'def ', 'import os', 'import sys', 'subprocess'
]

print("Checking for suspicious python residues in sam3_update.html:")
for kw in suspicious_keywords:
    cnt = text.count(kw)
    print(f"  {kw}: count = {cnt}")

# Check CSS rule for .hidden
print("\nChecking .hidden style definition:")
import re
hidden_rules = re.findall(r'\.hidden\s*\{[^}]*\}', text)
for hr in hidden_rules:
    print(" ", hr)

# Let's ensure .hidden has !important display none and pointer-events none
if '.hidden { display: none !important; pointer-events: none !important; }' not in text:
    print("Notice: Updating .hidden CSS to ensure pointer-events: none !important;")
