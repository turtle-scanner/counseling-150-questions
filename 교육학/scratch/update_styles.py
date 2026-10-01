import os

filepath = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034\2027_적중1순위_초압축_55제_암기장.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace tags to include styles
content = content.replace('<th>', '<th style="word-break: keep-all; overflow-wrap: break-word;">')
content = content.replace('<th width', '<th style="word-break: keep-all; overflow-wrap: break-word;" width')
content = content.replace('<td>', '<td style="word-break: keep-all; overflow-wrap: break-word; line-height: 1.6;">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Markdown file styles updated.')
