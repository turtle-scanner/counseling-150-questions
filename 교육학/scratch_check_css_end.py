import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_banner = text.find('.exam-header-banner')
pos_style_end = text.find('</style>', pos_banner)
print('Length between banner and </style>:', pos_style_end - pos_banner)
print(text[pos_style_end-1000:pos_style_end])
