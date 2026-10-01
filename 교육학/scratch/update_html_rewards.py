import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the image tag
html = html.replace('<img src="images/cheer.jpg" class="modal-img" alt="Cheering Celeb">', '<img src="" class="modal-img" id="reward-img" alt="Cheering Reward">')

# Add random image logic
old_js = "function showReward() {\n      modal.style.display = 'flex';"
new_js = """function showReward() {
      const rewardImages = ['images/cheer1.jpg', 'images/cheer2.jpg', 'images/cheer3.jpg'];
      const randomImg = rewardImages[Math.floor(Math.random() * rewardImages.length)];
      document.getElementById('reward-img').src = randomImg;
      modal.style.display = 'flex';"""
      
html = html.replace(old_js, new_js)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Successfully injected random reward logic.")
