import json, re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load source datasets
with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages_150 = json.load(f)

# Flatten 150 items
items_150 = []
for p in pages_150:
    for it in p['items']:
        items_150.append(it)

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items_203 = json.load(f)

print(f"Loaded 150 items: {len(items_150)}, 203 items: {len(items_203)}")

# Function to extract clean single-paragraph answer
def clean_answer(raw_ans):
    if not raw_ans:
        return ""
    if "🏆 [KICE 4점 만점 서술문]" in raw_ans:
        part = raw_ans.split("🏆 [KICE 4점 만점 서술문]")[1].strip()
        if "🔍" in part:
            part = part.split("🔍")[0].strip()
        return part
    # If bullet lines
    lines = [l.strip() for l in raw_ans.strip().split("\n") if l.strip()]
    # Combine lines into cohesive answer or pick best sentences
    clean_lines = []
    for l in lines:
        cleaned = re.sub(r'^\d+\.\s*', '', l)
        cleaned = re.sub(r'^\[.*?\]\s*', '', cleaned)
        clean_lines.append(cleaned)
    return " ".join(clean_lines)

# Function to clean no stars & no tildes
def clean_text(s):
    if not s:
        return ""
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    s = s.replace('*', '')
    s = s.replace('~', '-')
    return s.strip()

# Build 200 items list
# Pedagogy (교육학): 30 items
# Counsel (전공상담): 170 items
# Total: 200 items

edu_badges = ['교육과정', '교육행정', '교수학습', '교육평가', '교육심리', '교육방법·학습', '교육심리·특수']
edu_203 = [it for it in items_203 if it['badge'] in edu_badges]
counsel_203 = [it for it in items_203 if it['badge'] not in edu_badges]

print(f"Edu in 203: {len(edu_203)}, Counsel in 203: {len(counsel_203)}")

# Select top 30 education items
# Let's inspect edu_203
print("Selecting 30 education items...")
selected_edu = []
# Prune out the 3 items: e.g. 변혁적 리더십, 관료제 5대 원리, 렌줄리 SEM(압축과 중복)
skip_edu_kws = ['변혁적 리더십', '관료제 5대 원리', '렌줄리 영재성 3고리']
for it in edu_203:
    if not any(k in it['kw'] for k in skip_edu_kws):
        selected_edu.append(it)
    if len(selected_edu) == 30:
        break

if len(selected_edu) < 30:
    for it in edu_203:
        if it not in selected_edu:
            selected_edu.append(it)
        if len(selected_edu) == 30:
            break

print(f"Selected Edu count: {len(selected_edu)}")

# Select 170 counseling items
selected_counsel = counsel_203[:170]
print(f"Selected Counsel count: {len(selected_counsel)}")

total_200 = selected_edu + selected_counsel
print(f"Total 200 items prepared: {len(total_200)}")

with open('scratch/prepared_200_items.json', 'w', encoding='utf-8') as out:
    json.dump(total_200, out, ensure_ascii=False, indent=2)

print("Saved scratch/prepared_200_items.json successfully.")
