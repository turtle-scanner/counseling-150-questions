import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see how setPeriodFilter is implemented
p_filter = text.find('function setPeriodFilter(')
print('setPeriodFilter:')
print(text[p_filter:p_filter+900])

# Let's see renderCardView
p_render = text.find('function renderCardView(')
print('renderCardView:')
print(text[p_render:p_render+1200])

# Let's see flipCard
p_flip = text.find('function flipCard(')
print('flipCard:')
print(text[p_flip:p_flip+600])
