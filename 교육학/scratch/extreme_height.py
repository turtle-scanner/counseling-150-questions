import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Textarea (답안작성란)
html = re.sub(r'textarea \{.*?\}', 'textarea { width: 100%; height: 50px; background: #0f1117; border: 1.5px solid #334155; border-radius: 6px; padding: 8px; color: #f8fafc; font-family: inherit; font-size: 0.95rem; resize: none; box-sizing: border-box; line-height: 1.4; }', html)

# 2. Hide Button (숨기기 버튼)
html = re.sub(r'\.btn-flip \{.*?\}', '.btn-flip { width: 100%; background: #d97706; color: #fff; border: none; padding: 6px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; cursor: pointer; transition: background 0.2s; box-shadow: 0 2px 5px rgba(217, 119, 6, 0.3); }', html)

# 3. Reward Buttons
html = re.sub(r'\.reward-btn \{.*?\}', '.reward-btn { flex: 1; color: #fff; border: none; padding: 8px; border-radius: 6px; font-size: 0.9rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3); }', html)

# 4. Overall Card Padding
html = re.sub(r'\.anki-card \{.*?\}', '.anki-card { width: 100%; background: #161a24; border: 1px solid #2d3748; border-radius: 8px; padding: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); box-sizing: border-box; }', html)

# 5. Margins and other spacings
html = re.sub(r'\.card-q \{.*?\}', '.card-q { font-size: 1.1rem; font-weight: 700; line-height: 1.4; color: #f1f5f9; margin-bottom: 8px; }', html)
html = re.sub(r'\.input-area \{.*?\}', '.input-area { width: 100%; margin-bottom: 8px; }', html)
html = re.sub(r'\.card-back \{.*?\}', '.card-back { margin-top: 8px; padding-top: 8px; border-top: 2px dashed #334155; display: none; animation: fadeIn 0.3s ease; }', html)
html = re.sub(r'\.answer-kw \{.*?\}', '.answer-kw { font-size: 1.1rem; font-weight: 800; color: #fde047; margin-bottom: 6px; text-align: center; }', html)
html = re.sub(r'\.answer-text \{.*?\}', '.answer-text { font-size: 0.95rem; color: #fef08a; line-height: 1.4; font-weight: 600; background: #1f2937; padding: 8px; border-radius: 6px; border-left: 4px solid #facc15; margin-bottom: 8px; }', html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Extreme height reduction applied.")
