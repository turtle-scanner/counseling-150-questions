import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Shuffle Button Text
html = html.replace('🔀 카드 섞기', '🎯 2027 출제 1순위 정렬')

# 2. Update shuffleCards logic to sort by 2027 Prediction
new_shuffle = """
    function shuffleCards() {
      const highYield = ['장애', '평가', '가족', '진로', '이론', '치료', '검사', '척도', 'MMPI', 'DSM', '보웬', '미누친', '벡', '합리적', '자폐', '강박', '해리', '성격'];
      
      items.sort((a, b) => {
        let aScore = Math.random(); // Add base randomness
        let bScore = Math.random();
        highYield.forEach(k => { 
          if(a.q.includes(k) || a.kw.includes(k)) aScore += 5; 
        });
        highYield.forEach(k => { 
          if(b.q.includes(k) || b.kw.includes(k)) bScore += 5; 
        });
        return bScore - aScore;
      });
      
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
      alert('🔥 2027 임용고시 출제 1순위(A급 킬러) 예측 배열로 정렬되었습니다!');
    }
"""
old_shuffle_regex = r'function shuffleCards\(\)\s*\{[\s\S]*?alert\([^\)]+\);\s*\}'
html = re.sub(old_shuffle_regex, new_shuffle.strip(), html)


# 3. Update Reward Container to 4 Anki Buttons
old_reward_container_regex = r'<div class="reward-container">[\s\S]*?</div>'
new_reward_container = """<div class="reward-container" style="display:flex; gap:8px; width:100%; margin-top:10px;">
            <button class="reward-btn" style="background:#ef4444;" onclick="handleSRS('again')">다시<br><span style="font-size:0.8rem; font-weight:400;">5분 후</span></button>
            <button class="reward-btn" style="background:#f97316;" onclick="handleSRS('hard')">어려움<br><span style="font-size:0.8rem; font-weight:400;">1일 후</span></button>
            <button class="reward-btn" style="background:#3b82f6;" onclick="handleSRS('good')">쉬움<br><span style="font-size:0.8rem; font-weight:400;">5일 후</span></button>
            <button class="reward-btn" style="background:#10b981;" onclick="handleSRS('easy')">매우 쉬움<br><span style="font-size:0.8rem; font-weight:400;">7일 후</span></button>
          </div>"""
html = re.sub(old_reward_container_regex, new_reward_container, html)


# 4. Add handleSRS logic and rename existing showReward
# The existing function is showReward(type)
html = html.replace('function showReward(type)', 'function showRewardUI(type)')

handle_srs_logic = """
    function handleSRS(level) {
      // Save interval data
      const now = new Date().getTime();
      let addMs = 0;
      if (level === 'again') addMs = 5 * 60 * 1000;
      if (level === 'hard') addMs = 1 * 24 * 60 * 60 * 1000;
      if (level === 'good') addMs = 5 * 24 * 60 * 60 * 1000;
      if (level === 'easy') addMs = 7 * 24 * 60 * 60 * 1000;
      
      let srsData = JSON.parse(localStorage.getItem('kice_srs') || '{}');
      if (items[currentIndex]) {
        srsData[items[currentIndex].kw] = now + addMs;
        localStorage.setItem('kice_srs', JSON.stringify(srsData));
      }
      
      // Trigger appropriate reward UI and audio
      if (level === 'again' || level === 'hard') {
        showRewardUI('wrong');
      } else {
        showRewardUI('right');
      }
    }
"""
html = html.replace('function showRewardUI(type)', handle_srs_logic + '\n    function showRewardUI(type)')


with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Anki SRS and 2027 Predictive Sorting applied.")
