import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to extract the three blocks: input-area, btn-flip, card-back
# and reorder them to: btn-flip -> card-back -> input-area

# 1. Extract input-area
input_area_match = re.search(r'(<div class="input-area">.*?</div>)', html, flags=re.DOTALL)
input_area_html = input_area_match.group(1)

# 2. Extract btn-flip
btn_flip_match = re.search(r'(<button class="btn-flip".*?</button>)', html, flags=re.DOTALL)
btn_flip_html = btn_flip_match.group(1)

# 3. Extract card-back
card_back_match = re.search(r'(<div class="card-back" id="c-back">.*?</div>\s*</div>\s*</div>)', html, flags=re.DOTALL)
# The regex above might be tricky with nested divs. Let's just find exactly what we need.
# card-back contains answer-kw, answer-text, reward-container.
card_back_match = re.search(r'(<div class="card-back" id="c-back">.*?<button class="reward-btn right".*?</button>\s*</div>\s*</div>)', html, flags=re.DOTALL)
card_back_html = card_back_match.group(1)

# Wait, a safer way to reorder these 3 sequential blocks is to just replace the whole chunk.
old_chunk_match = re.search(r'<div class="input-area">.*?</button>\s*</div>\s*</div>', html, flags=re.DOTALL)
old_chunk = old_chunk_match.group(0)

new_chunk = f"""{btn_flip_html}

        {card_back_html}

        {input_area_html}"""

# Add a bit of margin to the input-area so it looks nice below the reward buttons
new_chunk = new_chunk.replace('<div class="input-area">', '<div class="input-area" style="margin-top: 15px;">')

html = html.replace(old_chunk, new_chunk)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Reordered layout successfully.")
