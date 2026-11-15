# -*- coding: utf-8 -*-
import pypdf
import os

base = r"g:\내 드라이브\ANTI GRAVITY\전문상담임용고시"
ped_dirs = [d for d in os.listdir(base) if "교육학" in d and "자료" in d]

with open('past_ped_out.txt', 'w', encoding='utf-8') as out:
    if ped_dirs:
        target_dir = os.path.join(base, ped_dirs[0])
        files = sorted(os.listdir(target_dir))
        for f in files:
            if f.endswith('.pdf') and any(y in f for y in ['2026', '2025', '2024', '2023', '2022', '2021']):
                fpath = os.path.join(target_dir, f)
                out.write(f"=== {f} ===\n")
                reader = pypdf.PdfReader(fpath)
                for i, page in enumerate(reader.pages):
                    txt = page.extract_text() or ""
                    out.write(f"--- Page {i+1} ---\n")
                    out.write(txt + "\n")
                out.write("\n" + "="*50 + "\n\n")

print("Finished writing past_ped_out.txt")
