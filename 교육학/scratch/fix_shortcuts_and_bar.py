import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the Keyboard Shortcuts
old_listener_pattern = r"// Keyboard Shortcuts\s*document\.addEventListener\('keydown', function\(e\) \{[\s\S]*?\}\);"

new_listener = """// Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      if (document.getElementById('add-modal') && document.getElementById('add-modal').style.display === 'flex') return;
      if (document.getElementById('reward-modal') && document.getElementById('reward-modal').style.display === 'flex') {
        if (e.key === ' ' || e.key === 'Enter' || e.key === 'ArrowRight' || e.code === 'Space' || e.keyCode === 39 || e.keyCode === 32) {
          e.preventDefault();
          closeReward();
        }
        return;
      }
      if (document.getElementById('mode-anki').style.display === 'none') return;

      const isTyping = ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName);
      
      const isRight = e.key === 'ArrowRight' || e.code === 'ArrowRight' || e.keyCode === 39;
      const isLeft = e.key === 'ArrowLeft' || e.code === 'ArrowLeft' || e.keyCode === 37;
      const isSpace = e.key === ' ' || e.code === 'Space' || e.keyCode === 32;
      const isEnter = e.key === 'Enter' || e.code === 'Enter' || e.keyCode === 13;
      
      if (isTyping) {
        if (e.key === 'Escape' || e.keyCode === 27) {
          document.activeElement.blur();
        }
        if (e.ctrlKey) {
          if (isSpace || isEnter) {
            e.preventDefault();
            toggleFlip();
          } else if (isRight) {
            e.preventDefault();
            goNext();
          } else if (isLeft) {
            e.preventDefault();
            goPrev();
          }
        }
        return;
      }
      
      if (isSpace || isEnter) {
        e.preventDefault();
        toggleFlip();
      } else if (isRight) {
        e.preventDefault();
        goNext();
      } else if (isLeft) {
        e.preventDefault();
        goPrev();
      }
    });"""

html = re.sub(old_listener_pattern, new_listener, html)


# 2. Fix Progress Bar (Energy Bar) dynamic text and visibility
html = html.replace('<div class="progress-text"><span id="p-text">1</span> / 55</div>', '<div class="progress-text" id="p-text-container" style="font-weight:900; font-size:1.1rem; color:#fbbf24;">1 / 55</div>')

# Update JS in renderCard
html = html.replace("elPText.innerText = index + 1;", "document.getElementById('p-text-container').innerText = (index + 1) + ' / ' + items.length;")

# Make the progress bar thicker so it looks like an energy bar
css_fixes = """
    /* ENERGY BAR UPGRADES */
    .progress-container { margin: 15px 0 !important; }
    .progress-bar { height: 12px !important; border-radius: 6px !important; background: #334155 !important; border: 1px solid #1e293b !important; }
    .progress-fill { background: linear-gradient(90deg, #f59e0b, #ef4444) !important; border-radius: 6px !important; transition: width 0.3s ease !important; }
"""
if "/* ENERGY BAR UPGRADES */" not in html:
    html = html.replace('</style>', css_fixes + '\n  </style>')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Keyboard shortcuts and energy bar updated.")
