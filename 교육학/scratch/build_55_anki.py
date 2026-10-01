import os, json

with open('scratch/final_55_compressed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

items_json = json.dumps(items, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>2027 KICE 초압축 55제 앙키(Anki) 모드</title>
  <!-- Confetti library -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <style>
    html, body {{ margin: 0; padding: 0; background: #0f1117; color: #e2e8f0; font-family: "Malgun Gothic", "맑은 고딕", sans-serif; -webkit-font-smoothing: antialiased; word-break: keep-all; overflow-wrap: break-word; }}
    .app-header {{ background: #161a23; padding: 15px 20px; border-bottom: 2px solid #d97706; text-align: center; }}
    .app-title {{ font-size: 1.2rem; font-weight: 800; color: #fbbf24; margin-bottom: 5px; }}
    .app-sub {{ font-size: 0.85rem; color: #94a3b8; }}
    
    .main-container {{ max-width: 600px; margin: 20px auto; padding: 0 15px; display: flex; flex-direction: column; align-items: center; padding-bottom: 50px; }}
    
    .progress-container {{ width: 100%; margin-bottom: 15px; }}
    .progress-bar {{ width: 100%; background: #1e293b; height: 8px; border-radius: 4px; overflow: hidden; }}
    .progress-fill {{ height: 100%; background: #38bdf8; width: 0%; transition: width 0.3s ease; }}
    .progress-text {{ text-align: right; font-size: 0.85rem; color: #94a3b8; margin-top: 5px; font-weight: 700; }}

    .anki-card {{ width: 100%; background: #161a24; border: 1px solid #2d3748; border-radius: 12px; padding: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.6); box-sizing: border-box; }}
    
    .card-badge {{ display: inline-block; background: #0c4a6e; color: #38bdf8; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; font-weight: 800; margin-bottom: 15px; border: 1px solid #0369a1; }}
    
    .card-q {{ font-size: 1.15rem; font-weight: 700; line-height: 1.6; color: #f1f5f9; margin-bottom: 25px; min-height: 80px; }}
    
    .input-area {{ width: 100%; margin-bottom: 20px; }}
    textarea {{ width: 100%; height: 100px; background: #0f1117; border: 1.5px solid #334155; border-radius: 8px; padding: 12px; color: #f8fafc; font-family: inherit; font-size: 1rem; resize: none; box-sizing: border-box; transition: border-color 0.2s; line-height: 1.5; }}
    textarea:focus {{ outline: none; border-color: #38bdf8; }}
    textarea::placeholder {{ color: #475569; }}

    .btn-flip {{ width: 100%; background: #d97706; color: #fff; border: none; padding: 14px; border-radius: 8px; font-size: 1.05rem; font-weight: 800; cursor: pointer; transition: background 0.2s; box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3); }}
    .btn-flip:active {{ background: #b45309; transform: translateY(2px); }}
    .btn-flip.flipped {{ background: #334155; color: #cbd5e1; box-shadow: none; }}

    .card-back {{ margin-top: 25px; padding-top: 25px; border-top: 2px dashed #334155; display: none; animation: fadeIn 0.4s ease; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(-10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    
    .answer-kw {{ font-size: 1.25rem; font-weight: 800; color: #fde047; margin-bottom: 12px; text-align: center; }}
    .answer-text {{ font-size: 1.05rem; color: #fef08a; line-height: 1.6; font-weight: 600; background: #1f2937; padding: 15px; border-radius: 8px; border-left: 4px solid #facc15; margin-bottom: 20px; }}

    .reward-btn {{ width: 100%; background: #ec4899; color: #fff; border: none; padding: 14px; border-radius: 8px; font-size: 1.05rem; font-weight: 800; cursor: pointer; transition: background 0.2s; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4); display: flex; align-items: center; justify-content: center; gap: 8px; }}
    .reward-btn:active {{ background: #be185d; transform: scale(0.98); }}

    .nav-buttons {{ width: 100%; display: flex; justify-content: space-between; margin-top: 20px; }}
    .btn-nav {{ flex: 1; background: #1e293b; color: #cbd5e1; border: 1px solid #334155; padding: 14px; border-radius: 8px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background 0.2s; }}
    .btn-nav:active {{ background: #0f1117; }}
    .btn-nav.prev {{ margin-right: 10px; }}
    .btn-nav.next {{ margin-left: 10px; background: #0369a1; color: #fff; border-color: #0284c7; }}
    .btn-nav.next:active {{ background: #0284c7; }}

    /* Reward Modal */
    .modal-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.85); display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px; animation: fadeIn 0.3s ease; }}
    .modal-content {{ background: #1e293b; border-radius: 16px; overflow: hidden; max-width: 400px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.8); border: 2px solid #ec4899; text-align: center; }}
    .modal-img {{ width: 100%; display: block; max-height: 400px; object-fit: cover; }}
    .modal-text {{ padding: 20px; }}
    .modal-title {{ font-size: 1.3rem; font-weight: 800; color: #fdf2f8; margin-bottom: 10px; }}
    .modal-msg {{ font-size: 1rem; color: #fbcfe8; margin-bottom: 20px; line-height: 1.5; }}
    .btn-close-modal {{ background: #ec4899; color: white; border: none; padding: 10px 24px; border-radius: 8px; font-weight: 800; font-size: 1rem; cursor: pointer; width: 100%; }}

  </style>
</head>
<body>

  <div class="app-header">
    <div class="app-title">🚨 2027 KICE 초압축 55제 앙키(Anki) 모드</div>
    <div class="app-sub">백지 인출 직접 타이핑 · 정답 보상 시스템 가동</div>
  </div>

  <div class="main-container">
    
    <div class="progress-container">
      <div class="progress-bar"><div class="progress-fill" id="p-fill"></div></div>
      <div class="progress-text"><span id="p-text">1</span> / 55</div>
    </div>

    <div class="anki-card">
      <div class="card-badge" id="c-badge">영역</div>
      <div class="card-q" id="c-q">문제 단서 텍스트</div>

      <div class="input-area">
        <textarea id="c-input" placeholder="여기에 정답(표제어 및 서술형 문장)을 직접 타이핑해보며 백지 인출을 연습하세요..."></textarea>
      </div>

      <button class="btn-flip" id="btn-flip" onclick="toggleFlip()">💡 정답 확인하기 (뒤집기)</button>

      <div class="card-back" id="c-back">
        <div class="answer-kw" id="c-kw">정답 표제어</div>
        <div class="answer-text" id="c-ans">공식 서술형 정답</div>
        
        <button class="reward-btn" onclick="showReward()">🎉 완벽하게 맞혔어요! (보상 받기)</button>
      </div>
    </div>

    <div class="nav-buttons">
      <button class="btn-nav prev" onclick="goPrev()">◀ 이전 카드</button>
      <button class="btn-nav next" onclick="goNext()">다음 카드 ▶</button>
    </div>

  </div>

  <!-- Reward Modal -->
  <div class="modal-overlay" id="reward-modal">
    <div class="modal-content">
      <img src="images/cheer.jpg" class="modal-img" alt="Cheering Celeb">
      <div class="modal-text">
        <div class="modal-title">🎉 정답입니다! 최고예요!</div>
        <div class="modal-msg">선생님의 노력은 절대 배신하지 않습니다!<br>올해 무조건 합격하실 거예요! 화이팅! 💖</div>
        <button class="btn-close-modal" onclick="closeReward()">닫기 (다음 문제로)</button>
      </div>
    </div>
  </div>

  <script>
    const items = {items_json};
    let currentIndex = 0;
    let isFlipped = false;

    const elBadge = document.getElementById('c-badge');
    const elQ = document.getElementById('c-q');
    const elInput = document.getElementById('c-input');
    const elFlipBtn = document.getElementById('btn-flip');
    const elBack = document.getElementById('c-back');
    const elKw = document.getElementById('c-kw');
    const elAns = document.getElementById('c-ans');
    const elPFill = document.getElementById('p-fill');
    const elPText = document.getElementById('p-text');
    const modal = document.getElementById('reward-modal');

    function renderCard(index) {{
      const item = items[index];
      elBadge.innerText = item.badge;
      elQ.innerHTML = item.q.replace(/➔/g, '<span style="color:#d97706; font-weight:bold;">➔</span>');
      elKw.innerText = item.kw;
      elAns.innerText = item.ans;
      
      // Update progress
      elPText.innerText = index + 1;
      elPFill.style.width = ((index + 1) / items.length * 100) + '%';

      // Reset state
      isFlipped = false;
      elBack.style.display = 'none';
      elFlipBtn.innerText = '💡 정답 확인하기 (뒤집기)';
      elFlipBtn.classList.remove('flipped');
      elInput.value = ''; // Clear user input
      elInput.focus();
    }}

    function toggleFlip() {{
      if(isFlipped) {{
        elBack.style.display = 'none';
        elFlipBtn.innerText = '💡 정답 확인하기 (뒤집기)';
        elFlipBtn.classList.remove('flipped');
        isFlipped = false;
      }} else {{
        elBack.style.display = 'block';
        elFlipBtn.innerText = '숨기기';
        elFlipBtn.classList.add('flipped');
        isFlipped = true;
      }}
    }}

    function showReward() {{
      modal.style.display = 'flex';
      
      // Fire confetti
      const duration = 3 * 1000;
      const animationEnd = Date.now() + duration;
      const defaults = {{ startVelocity: 30, spread: 360, ticks: 60, zIndex: 1001 }};

      function randomInRange(min, max) {{
        return Math.random() * (max - min) + min;
      }}

      const interval = setInterval(function() {{
        const timeLeft = animationEnd - Date.now();
        if (timeLeft <= 0) {{ return clearInterval(interval); }}
        const particleCount = 50 * (timeLeft / duration);
        confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }} }}));
        confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }} }}));
      }}, 250);
    }}

    function closeReward() {{
      modal.style.display = 'none';
      goNext();
    }}

    function goNext() {{
      if(currentIndex < items.length - 1) {{
        currentIndex++;
        renderCard(currentIndex);
      }} else {{
        alert('마지막 카드입니다. 1번부터 다시 시작합니다!');
        currentIndex = 0;
        renderCard(currentIndex);
      }}
    }}

    function goPrev() {{
      if(currentIndex > 0) {{
        currentIndex--;
        renderCard(currentIndex);
      }}
    }}

    // Init
    renderCard(currentIndex);
  </script>
</body>
</html>
"""

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Successfully generated Anki HTML with Rewards at {target_path}')
