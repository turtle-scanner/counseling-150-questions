# -*- coding: utf-8 -*-
import subprocess, re, sys

with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Fix openMoveModal and openTransportModal first
old_bad = '''    function openMoveModal() {
      closeAllPopups();
      alert("\U0001f40e [\uad70\uc0ac \uc774\ub3d9]

\uc544\uad70 \uc601\uc9c0 \uac04\uc5d0 \uc7a5\uc218\uc640 \ubcd1\ub825\uc744 \uc774\ub3d9\uc2dc\ud0b5\ub2c8\ub2e4. \uc9c0\ub3c4\uc5d0\uc11c \uc774\ub3d9\ud560 \ubcf8\uac70\uc9c0 \uc601\uc9c0\ub97c \uc120\ud0dd\ud558\uc2ed\uc2dc\uc624.");
    }

    function openTransportModal() {
      closeAllPopups();
      alert("\U0001f33e [\uad70\ub7c9/\uad70\uc790\uae08 \uc218\uc1a1]

\uc548\uc804\ud55c \ud6c4\ubc29 \uc601\uc9c0\uc5d0\uc11c \ucd5c\uc804\ubc29 \uc601\uc9c0\ub85c \uae08\uacfc \uad70\ub7c9\uc744 \uc548\uc804\ud558\uac8c \uc218\uc1a1\ud569\ub2c8\ub2e4.");
    }'''

print("Checking old_bad in html...")
if old_bad in html:
    print("Found exact old_bad string! Replacing...")
    new_good = '''    function openMoveModal() {
      closeAllPopups();
      alert("🐎 [군사 이동]\\n\\n아군 영지 간에 장수와 병력을 이동시킵니다. 지도에서 이동할 본거지 영지를 선택하십시오.");
    }

    function openTransportModal() {
      closeAllPopups();
      alert("🌾 [군량/군자금 수송]\\n\\n안전한 후방 영지에서 최전방 영지로 금과 군량을 안전하게 수송합니다.");
    }'''
    html = html.replace(old_bad, new_good)
else:
    print("Exact old_bad not found by string, doing regex replacement...")
    # Regex fallback
    pattern = r'function\s+openMoveModal\(\)\s*\{[^}]*alert\([^)]*\)[^}]*\}\s*function\s+openTransportModal\(\)\s*\{[^}]*alert\([^)]*\)[^}]*\}'
    # let's find openMoveModal
    pos = html.find('function openMoveModal()')
    if pos != -1:
        print("openMoveModal found at", pos)
        print(html[pos:pos+400].encode('ascii', errors='backslashreplace').decode('ascii'))
        # replace manually
        pos_transport = html.find('function openTransportModal()', pos)
        pos_end = html.find('function myCapitalName()', pos_transport)
        if pos_end != -1:
            snippet = html[pos:pos_end]
            print("Old snippet:\n", snippet.encode('ascii', errors='backslashreplace').decode('ascii'))
            new_snippet = '''function openMoveModal() {
      closeAllPopups();
      alert("🐎 [군사 이동]\\n\\n아군 영지 간에 장수와 병력을 이동시킵니다. 지도에서 이동할 본거지 영지를 선택하십시오.");
    }

    function openTransportModal() {
      closeAllPopups();
      alert("🌾 [군량/군자금 수송]\\n\\n안전한 후방 영지에서 최전방 영지로 금과 군량을 안전하게 수송합니다.");
    }

    '''
            html = html[:pos] + new_snippet + html[pos_end:]
            print("Replaced snippet successfully!")

# Now save to temp and check JS syntax
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
print(f"Total script tags: {len(scripts)}")
has_error = False
for idx, sc in enumerate(scripts):
    tmp_file = f'temp_fixed_script_{idx}.js'
    with open(tmp_file, 'w', encoding='utf-8') as tf:
        tf.write(sc)
    res = subprocess.run(['node', '--check', tmp_file], capture_output=True)
    if res.returncode != 0:
        has_error = True
        err = res.stderr.decode('utf-8', errors='replace')
        print(f"Script {idx} STILL HAS ERROR:")
        for l in err.splitlines()[:15]:
            print("  " + l.encode('ascii', errors='backslashreplace').decode('ascii'))
    else:
        print(f"Script {idx} is 100% VALID JS! Length: {len(sc)}")

if not has_error:
    print("ALL SCRIPTS ARE 100% VALID JS! Writing back to sam3_update.html...")
    with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated C:\\Users\\LENOVO\\Desktop\\sam3_update.html")
