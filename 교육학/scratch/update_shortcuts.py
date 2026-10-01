import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Javascript for keyboard shortcuts
shortcut_js = """
    // Keyboard Shortcuts
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
    });
"""

# Insert right before </script>
html = html.replace('</script>', shortcut_js + '\n</script>')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Keyboard shortcuts added!")
