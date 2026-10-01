import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update goPrev and goNext for seamless looping
old_go_next = """function goNext() {
      if(currentIndex < items.length - 1) {
        currentIndex++;
        renderCard(currentIndex);
      } else {
        alert('마지막 카드입니다. 1번으로 돌아갑니다.');
        currentIndex = 0;
        renderCard(currentIndex);
      }
    }"""
    
new_go_next = """function goNext() {
      if(currentIndex < items.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0; // loop to start
      }
      renderCard(currentIndex);
    }"""

old_go_prev = """function goPrev() {
      if(currentIndex > 0) {
        currentIndex--;
        renderCard(currentIndex);
      }
    }"""

new_go_prev = """function goPrev() {
      if(currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = items.length - 1; // loop to end
      }
      renderCard(currentIndex);
    }"""

# Since spacing might vary, I'll use regex for replacement to be safe, or just replace the bodies
html = re.sub(r'function goNext\(\)\s*\{[\s\S]*?\}', new_go_next, html, count=1)
html = re.sub(r'function goPrev\(\)\s*\{[\s\S]*?\}', new_go_prev, html, count=1)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Looping logic applied.")
