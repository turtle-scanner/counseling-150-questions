import json

with open('clean_b8_b11.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('b8_b11_clean.txt', 'w', encoding='utf-8') as out:
    for q in data:
        qid = q['id']
        title = q['title']
        content = q['content']
        inst = q['instructions']
        ans = q['answer']
        out.write(f"[{qid}]\nTITLE: {title}\nCONTENT:\n{content}\nINSTRUCTIONS:\n{inst}\nANSWER:\n{ans}\n" + "="*50 + "\n")

print("SUCCESSFULLY EXPORTED")
