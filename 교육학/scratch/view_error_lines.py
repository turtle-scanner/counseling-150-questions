with open('scratch/temp_script1.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

line_no = 3018
start = max(0, line_no - 30)
end = min(len(lines), line_no + 20)

for idx in range(start, end):
    print(f"{idx+1:4d}: {lines[idx]}", end='')
