import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I will use .replace() instead of re.sub() this time to avoid escape processing!
old_format = html.split('function formatText(text) {')[1].split('return t;\n    }')[0]

new_format = """
      if (!text) return '';
      let t = text.replace(/\\*\\*(.*?)\\*\\*/g, '<span style="color:#d97706; font-weight:bold;">$1</span>');
      t = t.split('$\\\\Rightarrow$').join('-->');
      t = t.split('\\\\Rightarrow').join('-->');
      t = t.split('$\\\\rightarrow$').join('-->');
      t = t.split('\\\\rightarrow').join('-->');
      t = t.split('$\\\\Leftrightarrow$').join('<-->');
      t = t.split('\\\\Leftrightarrow').join('<-->');
      """

html = html.replace(old_format, new_format)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Replaced safely without re.sub()")
