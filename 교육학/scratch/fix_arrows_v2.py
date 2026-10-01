import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the formatText function to be 100% bulletproof using string splitting
# This avoids any JS/Python regex escape sequence confusion with \r, \n, etc.
new_formatter_js = """
    function formatText(text) {
      if (!text) return '';
      let t = text.replace(/\\*\\*(.*?)\\*\\*/g, '<span style="color:#d97706; font-weight:bold;">$1</span>');
      // Replace LaTeX arrows safely
      t = t.split('$\\\\Rightarrow$').join('➔');
      t = t.split('\\\\Rightarrow').join('➔');
      t = t.split('$\\\\rightarrow$').join('→');
      t = t.split('\\\\rightarrow').join('→');
      t = t.split('$\\\\Leftrightarrow$').join('↔');
      t = t.split('\\\\Leftrightarrow').join('↔');
      return t;
    }
"""

# Extract the old formatText block and replace
html = re.sub(r'function formatText\(text\) \{[\s\S]*?return t;\s*\}', new_formatter_js.strip(), html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Arrows fixed completely.")
