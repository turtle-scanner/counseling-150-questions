import re

content = open('../complete_counseling_55_builder.py', encoding='utf-8').read()

m = re.findall(r'\{\s*"domain"[^}]+"num":\s*21[^}]+}', content)
if m:
    print("Found topic 21:")
    print(m[0][:500])
else:
    # 21 주변 찾기
    pos = content.find('21')
    print("Find '21':", pos)
    idx = content.find('"num": 21')
    print("Find '\"num\": 21':", idx)
    # 정규식 검색
    matches = list(re.finditer(r'"num":\s*21\b', content))
    print("Regex matches:", matches)
    if matches:
        start = matches[0].start()
        print(content[start-50:start+300])
