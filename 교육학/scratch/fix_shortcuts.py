import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_listener = """// Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      // Ignore if typing in input or textarea
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
      
      // Ignore if modal is open or we are in table mode
      if (document.getElementById('add-modal') && document.getElementById('add-modal').style.display === 'flex') return;
      if (document.getElementById('reward-modal') && document.getElementById('reward-modal').style.display === 'flex') {
        // If reward modal is open, let Space or Right Arrow close it and go next
        if (e.code === 'Space' || e.code === 'ArrowRight' || e.code === 'Enter') {
          e.preventDefault();
          closeReward();
        }
        return;
      }
      if (document.getElementById('mode-anki').style.display === 'none') return;
      
      if (e.code === 'Space') {
        e.preventDefault(); // Prevent page scrolling
        toggleFlip();
      } else if (e.code === 'ArrowRight') {
        goNext();
      } else if (e.code === 'ArrowLeft') {
        goPrev();
      }
    });"""

new_listener = """// Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      // Modal handles
      if (document.getElementById('add-modal') && document.getElementById('add-modal').style.display === 'flex') return;
      if (document.getElementById('reward-modal') && document.getElementById('reward-modal').style.display === 'flex') {
        if (e.code === 'Space' || e.code === 'ArrowRight' || e.code === 'Enter') {
          e.preventDefault();
          closeReward();
        }
        return;
      }
      if (document.getElementById('mode-anki').style.display === 'none') return;

      const isTyping = ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName);
      
      // If typing, allow escape to unfocus, and allow Ctrl+Key combinations to bypass
      if (isTyping) {
        if (e.code === 'Escape') {
          document.activeElement.blur();
        }
        // If holding Ctrl, allow navigation even while typing
        if (e.ctrlKey) {
          if (e.code === 'Space' || e.code === 'Enter') {
            e.preventDefault();
            toggleFlip();
          } else if (e.code === 'ArrowRight') {
            e.preventDefault();
            goNext();
          } else if (e.code === 'ArrowLeft') {
            e.preventDefault();
            goPrev();
          }
        }
        return; // otherwise ignore normal arrows/space in textarea
      }
      
      // Normal non-typing shortcuts
      if (e.code === 'Space' || e.code === 'Enter') {
        e.preventDefault();
        toggleFlip();
      } else if (e.code === 'ArrowRight') {
        goNext();
      } else if (e.code === 'ArrowLeft') {
        goPrev();
      }
    });"""

if "const isTyping = ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName);" not in html:
    html = html.replace(old_listener, new_listener)
    # also remove the duplicate one near the top
    html = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js">[\s\S]*?</script>', '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>', html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Keyboard shortcuts upgraded.")
