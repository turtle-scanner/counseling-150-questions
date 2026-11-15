# -*- coding: utf-8 -*-
with open('g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('const rawData =')
if idx != -1:
    print("Found 'const rawData =':", idx)
    end_script = content.find('</script>', idx)
    print("End of script:", end_script)
    snippet = content[idx:idx+400]
    print(snippet)
    # rawData json parse
    import json
    # find where rawData definition ends
    semicolon = content.find(';\nlet currentTab', idx)
    if semicolon == -1:
        semicolon = content.find(';\r\nlet currentTab', idx)
    if semicolon == -1:
        semicolon = content.find('; let currentTab', idx)
    print("Semicolon pos:", semicolon)
    if semicolon != -1:
        raw_json_str = content[idx+len('const rawData ='):semicolon].strip()
        try:
            d = json.loads(raw_json_str)
            print("Successfully parsed rawData JSON!")
            print("Keys:", d.keys())
            print("top55 len:", len(d.get('top55', [])))
            print("pedagogy keys:", d.get('pedagogy', {}).keys())
            print("questions_a len:", len(d.get('questions_a', [])))
            print("questions_b len:", len(d.get('questions_b', [])))
        except Exception as e:
            print("Error parsing json:", e)
