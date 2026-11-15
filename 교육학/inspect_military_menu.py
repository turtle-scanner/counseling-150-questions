# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find popup-military in HTML
pos = text.find('popup-military')
print(f"popup-military found at {pos}")
if pos != -1:
    print(text[pos-100:pos+2500].encode('ascii', errors='backslashreplace').decode('ascii'))
