import re

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('File size (chars):', len(text))
print('allData occurrences:', len(re.findall(r'allData', text)))

views = re.findall(r'id=["\']([^"\']*[vV]iew[^"\']*)["\']', text)
print('Views found:', views)

functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', text)
print('Functions count:', len(functions))
print('Sample functions:', functions[:20])

# Check where allData is defined
all_data_pos = text.find('const allData = [')
if all_data_pos != -1:
    print('allData defined around char:', all_data_pos)
    # let's see how many items
    end_data_pos = text.find('];', all_data_pos)
    items_block = text[all_data_pos:end_data_pos]
    item_matches = re.findall(r'\{\s*id:', items_block)
    print('allData item count:', len(item_matches))
else:
    print('allData definition pattern not found directly with const allData = [')
