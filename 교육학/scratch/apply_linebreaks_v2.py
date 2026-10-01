import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS to respect line breaks (\n) natively via pre-wrap
prewrap_css = """
    /* ENABLE NEWLINES */
    .answer-text, .card-q, .td-ans, .td-q, .kice-textarea { 
      white-space: pre-wrap !important; 
    }
"""
if "/* ENABLE NEWLINES */" not in html:
    html = html.replace('</style>', prewrap_css + '\n  </style>')

# 2. Add an item pre-processor during initialization to automatically insert \n after Korean sentence endings
init_logic = """
      // AUTO-FORMAT SENTENCE BREAKS
      items.forEach(item => {
        item.q = item.q.replace(/([가-힣](?:다|임|함|요)\\.)\\s+/g, '$1\\n');
        item.ans = item.ans.replace(/([가-힣](?:다|임|함|요)\\.)\\s+/g, '$1\\n');
      });
"""
if "AUTO-FORMAT SENTENCE BREAKS" not in html:
    html = html.replace('setTimeout(() => { originalItems = [...items]; }, 500);', init_logic + '\n      setTimeout(() => { originalItems = [...items]; }, 500);')

# 3. Fix the Auto-Grader to use tokens
# Let's extract the exact old code snippet
old_autograder = """        const words = officialAnswer.split(' ');
        let highlightedAns = '';
        words.forEach(word => {
          const cleanWord = word.replace(/[.,!?()]/g, '');
          if (cleanWord.length > 1 && userAnswer.includes(cleanWord)) {
            highlightedAns += `<span style="color:#4ade80; font-weight:800;">${word}</span> `;
          } else if (cleanWord.length <= 1) {
            highlightedAns += `${word} `;
          } else {
            highlightedAns += `<span style="color:#f87171; text-decoration:underline;">${word}</span> `;
          }
        });"""

new_autograder = """        const tokens = officialAnswer.split(/(\\s+)/);
        let highlightedAns = '';
        tokens.forEach(word => {
          if (word.trim() === '') {
            highlightedAns += word;
            return;
          }
          const cleanWord = word.replace(/[.,!?()]/g, '');
          if (cleanWord.length > 1 && userAnswer.includes(cleanWord)) {
            highlightedAns += `<span style="color:#4ade80; font-weight:800;">${word}</span>`;
          } else if (cleanWord.length <= 1) {
            highlightedAns += `${word}`;
          } else {
            highlightedAns += `<span style="color:#f87171; text-decoration:underline;">${word}</span>`;
          }
        });"""

# Use simple string replace
if "officialAnswer.split(' ')" in html:
    html = html.replace(old_autograder, new_autograder)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Line break logic implemented securely.")
