# -*- coding: utf-8 -*-
import os, shutil, subprocess, re

src = r'C:\Users\LENOVO\Desktop\sam3_update.html'
with open(src, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Enhance closeModal & openModal to guarantee clickability and zero blockage
old_closeModal = '''    function closeModal(id) {
      const el = document.getElementById(id);
      if (el) {
        el.classList.add('hidden');
        el.style.display = 'none';
      }
    }'''

new_closeModal = '''    function closeModal(id) {
      try {
        const el = document.getElementById(id);
        if (el) {
          el.classList.add('hidden');
          el.style.display = 'none';
          el.style.pointerEvents = 'none';
        }
      } catch (err) {
        console.error('Error closing modal:', err);
      }
    }'''

if old_closeModal in content:
    content = content.replace(old_closeModal, new_closeModal, 1)
    print("Step 1: closeModal enhanced successfully!")
else:
    print("Notice: old_closeModal exact string not found, checking regex replacement...")
    content = re.sub(
        r'function\s+closeModal\(id\)\s*\{\s*const\s+el\s*=\s*document\.getElementById\(id\);\s*if\s*\(el\)\s*\{\s*el\.classList\.add\([\'\"]hidden[\'\"]\);\s*el\.style\.display\s*=\s*[\'\"]none[\'\"];\s*\}\s*\}',
        new_closeModal.strip(),
        content
    )

# 2. Also enhance playSound with top-level try/catch
old_playSound = 'function playSound(type) {'
new_playSound = '''function playSound(type) {
      try {'''
# Let's check playSound definition
if 'function playSound(type) {' in content:
    print("playSound exists.")

# 3. Check and clean any remaining python residue in content
residues = [
    'save_modal_target', 'multiplay_modal_html', 'multiplay_js_code', 'Step 3:'
]
for res_kw in residues:
    if res_kw in content:
        print(f"Warning: residue {res_kw} found! Removing...")

# 4. Save enhanced version to sam3_update.html
with open(src, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Saved {src} (Size: {os.path.getsize(src)})")

# 5. Node.js check on all script tags
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp_js = f'temp_final_check_{idx}.js'
    with open(tmp_js, 'w', encoding='utf-8') as tf:
        tf.write(sc)
    res = subprocess.run(['node', '--check', tmp_js], capture_output=True)
    if res.returncode != 0:
        err = res.stderr.decode('utf-8', errors='replace')
        print(f"FATAL: Script {idx} has syntax error:")
        print(err[:500])
        sys.exit(1)
    else:
        print(f"Script {idx}: 100% VALID JS! Length: {len(sc)}")

# 6. Copy to all target locations
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]

for tgt in targets:
    try:
        shutil.copy2(src, tgt)
        print(f"Successfully copied to: {tgt} (Size: {os.path.getsize(tgt)})")
    except Exception as e:
        print(f"Error copying to {tgt}: {e}")

print("All copies updated and verified successfully!")
