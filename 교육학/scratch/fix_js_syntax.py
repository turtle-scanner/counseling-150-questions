import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The correct block
correct_block = """    function goNext() {
      if(currentIndex < items.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0; // loop to start
      }
      renderCard(currentIndex);
    }

    function goPrev() {
      if(currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = items.length - 1; // loop to end
      }
      renderCard(currentIndex);
    }

"""

# We need to replace from 'function goNext()' up to '// TABLE LOGIC'
html = re.sub(r'function goNext\(\) \{[\s\S]*?// TABLE LOGIC', correct_block + '    // TABLE LOGIC', html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Syntax errors fixed.")
