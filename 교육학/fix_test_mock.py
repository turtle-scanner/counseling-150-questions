import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('test_app_features.js', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    "body: createElement('body')",
    "body: createElement('body'),\n  addEventListener: () => {},\n  removeEventListener: () => {}"
)

with open('test_app_features.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated test_app_features.js with document.addEventListener mock.')
