# -*- coding: utf-8 -*-
with open('build_master.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find tabs / navigation buttons
tabs = re.findall(r'<button[^>]*class="[^"]*nav-tab[^"]*"[^>]*>([\s\S]*?)<\/button>', text)
print("Tabs found:", len(tabs))
for t in tabs:
    print("Tab:", re.sub(r'<[^>]+>', '', t).strip())

# Find sections
sections = re.findall(r'<div[^>]*id="tab-[^"]*"[^>]*>', text)
print("\nSections found:", sections)
