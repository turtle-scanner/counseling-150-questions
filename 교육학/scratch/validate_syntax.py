import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} script tags.")

for idx, sc in enumerate(scripts):
    if not sc.strip():
        continue
    # write to temp file and check with node
    temp_js = f"scratch/temp_test_script_{idx}.js"
    with open(temp_js, 'w', encoding='utf-8') as f:
        f.write(sc)
    res = subprocess.run(["node", "-c", temp_js], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script {idx}: SYNTAX OK!")
    else:
        print(f"Script {idx}: SYNTAX ERROR:\n{res.stderr}")
