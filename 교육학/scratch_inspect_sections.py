import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('index.html total length:', len(text))
print('Has <style>:', '<style>' in text)
print('Has <script>:', '<script>' in text)

# find CSS style end
style_end = text.find('</style>')
print('Style length:', style_end)

# find main body structure
body_start = text.find('<body>')
script_start = text.find('<script>')
print('Body to script length:', script_start - body_start)

# find script length
script_end = text.rfind('</script>')
print('Script length:', script_end - script_start)
