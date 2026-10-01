import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Go Youn-jung images
old_images = r"const rewardImages = \['images/cheer1\.jpg',\s*'images/cheer2\.jpg'\];"
new_images = "const rewardImages = ['images/go1.png', 'images/go2.jpg', 'images/go3.png', 'images/go4.jpg', 'images/go5.jpg'];"
html = re.sub(old_images, new_images, html)

# 2. Update TTS parameters (faster and prettier/higher pitch)
# Assuming the existing code is:
# utterance.rate = 1.1;
# utterance.pitch = 1.4;
html = html.replace("utterance.rate = 1.1;", "utterance.rate = 1.3;")
html = html.replace("utterance.pitch = 1.4;", "utterance.pitch = 1.7;")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Go Youn-jung images and TTS updated.")
