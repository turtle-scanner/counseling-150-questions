import sys, json
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]
all_data = json.loads(data_str)

# Partition by domains
ped_items = [it for it in all_data if '1교시' in it['period']]
career_items = [it for it in all_data if it['domain'] == '진로상담']
test_items = [it for it in all_data if it['domain'] == '심리검사']
pers_group_items = [it for it in all_data if it['domain'] in ['성격심리', '집단상담', '대인관계']]
theory_items = [it for it in all_data if it['domain'] in ['상담이론', '상담기법']]
family_items = [it for it in all_data if it['domain'] == '가족치료']
psychopath_items = [it for it in all_data if it['domain'] == '정신병리']
crisis_behav_play_items = [it for it in all_data if it['domain'] in ['행동치료', '위기상담', '놀이치료']]
law_ethics_super_items = [it for it in all_data if it['domain'] in ['학교폭력법령', '상담윤리', '상담수퍼비전']]

print(f'Pedagogy: {len(ped_items)}')
print(f'Career: {len(career_items)}')
print(f'Test: {len(test_items)}')
print(f'Personality & Group: {len(pers_group_items)}')
print(f'Theory: {len(theory_items)}')
print(f'Family: {len(family_items)}')
print(f'Psychopathology: {len(psychopath_items)}')
print(f'Crisis, Behavior, Play: {len(crisis_behav_play_items)}')
print(f'Law, Ethics, Supervision: {len(law_ethics_super_items)}')
