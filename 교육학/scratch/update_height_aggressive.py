import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Aggressively reduce heights and paddings via regex
# 1. Header
html = re.sub(r'\.app-header \{.*?\}', '.app-header { background: #161a23; padding: 5px 10px; border-bottom: 2px solid #d97706; text-align: center; }', html)
html = re.sub(r'\.app-title \{.*?\}', '.app-title { font-size: 1.1rem; font-weight: 800; color: #fbbf24; margin-bottom: 2px; }', html)
html = re.sub(r'\.app-sub \{.*?\}', '.app-sub { font-size: 0.8rem; color: #94a3b8; margin-bottom: 0; }', html)

# 2. Controls
html = re.sub(r'\.controls \{.*?\}', '.controls { display: flex; justify-content: center; gap: 8px; margin: 10px 0; padding: 0 10px; flex-wrap: wrap; }', html)
html = re.sub(r'\.btn-control \{.*?\}', '.btn-control { background: #1e293b; border: 1.5px solid #3b82f6; color: #93c5fd; padding: 8px 15px; border-radius: 6px; font-weight: 700; cursor: pointer; transition: 0.2s; flex: 1; min-width: 100px; font-size: 0.9rem; }', html)

# 3. Anki Card container
html = re.sub(r'\.anki-card \{.*?\}', '.anki-card { width: 100%; background: #161a24; border: 1px solid #2d3748; border-radius: 8px; padding: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); box-sizing: border-box; }', html)
html = re.sub(r'\.card-badge \{.*?\}', '.card-badge { display: inline-block; background: #0c4a6e; color: #38bdf8; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: 800; margin-bottom: 10px; border: 1px solid #0369a1; }', html)
html = re.sub(r'\.card-q \{.*?\}', '.card-q { font-size: 1.15rem; font-weight: 700; line-height: 1.4; color: #f1f5f9; margin-bottom: 12px; }', html)

# 4. Textarea
html = re.sub(r'textarea \{.*?\}', 'textarea { width: 100%; height: 70px; background: #0f1117; border: 1.5px solid #334155; border-radius: 6px; padding: 10px; color: #f8fafc; font-family: inherit; font-size: 1rem; resize: none; box-sizing: border-box; line-height: 1.4; }', html)
html = re.sub(r'\.input-area \{.*?\}', '.input-area { width: 100%; margin-bottom: 12px; }', html)

# 5. Buttons
html = re.sub(r'\.btn-flip \{.*?\}', '.btn-flip { width: 100%; background: #d97706; color: #fff; border: none; padding: 10px; border-radius: 6px; font-size: 1rem; font-weight: 800; cursor: pointer; transition: background 0.2s; box-shadow: 0 2px 5px rgba(217, 119, 6, 0.3); }', html)
html = re.sub(r'\.reward-btn \{.*?\}', '.reward-btn { flex: 1; color: #fff; border: none; padding: 10px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3); }', html)
html = re.sub(r'\.btn-nav \{.*?\}', '.btn-nav { flex: 1; background: #1e293b; color: #cbd5e1; border: 1px solid #334155; padding: 10px; border-radius: 6px; font-size: 0.95rem; font-weight: 700; cursor: pointer; }', html)

# 6. Card Back
html = re.sub(r'\.card-back \{.*?\}', '.card-back { margin-top: 12px; padding-top: 12px; border-top: 2px dashed #334155; display: none; animation: fadeIn 0.3s ease; }', html)
html = re.sub(r'\.answer-kw \{.*?\}', '.answer-kw { font-size: 1.15rem; font-weight: 800; color: #fde047; margin-bottom: 8px; text-align: center; }', html)
html = re.sub(r'\.answer-text \{.*?\}', '.answer-text { font-size: 1rem; color: #fef08a; line-height: 1.4; font-weight: 600; background: #1f2937; padding: 10px; border-radius: 6px; border-left: 4px solid #facc15; margin-bottom: 12px; }', html)

# Remove all the tablet override CSS that made things artificially huge
html = re.sub(r'/\* TABLET SPECIFIC TWEAKS \*/.*?\}', '', html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Aggressive height reduction applied.")
