import os, json

with open('scratch/final_55_compressed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

items_json = json.dumps(items, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>2027 KICE 초압축 55제</title>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <style>
    html, body {{ margin: 0; padding: 0; background: #0f1117; color: #e2e8f0; font-family: "Malgun Gothic", "맑은 고딕", sans-serif; -webkit-font-smoothing: antialiased; word-break: keep-all; overflow-wrap: break-word; }}
    
    .app-header {{ background: #161a23; padding: 15px 20px; border-bottom: 2px solid #d97706; text-align: center; }}
    .app-title {{ font-size: 1.2rem; font-weight: 800; color: #fbbf24; margin-bottom: 5px; }}
    .app-sub {{ font-size: 0.85rem; color: #94a3b8; }}
    
    .controls {{ display: flex; justify-content: center; gap: 10px; margin: 20px 0; padding: 0 15px; flex-wrap: wrap; }}
    .btn-control {{ background: #1e293b; border: 1.5px solid #3b82f6; color: #93c5fd; padding: 10px 20px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: 0.2s; flex: 1; min-width: 120px; }}
    .btn-control.active {{ background: #3b82f6; color: #fff; }}
    .btn-print {{ background: #10b981; border-color: #059669; color: #fff; }}

    .main-container {{ max-width: 800px; margin: 0 auto; padding: 0 15px 50px 15px; display: flex; flex-direction: column; align-items: center; }}
    
    /* ANKI MODE */
    #mode-anki {{ width: 100%; max-width: 600px; display: block; }}
    .progress-container {{ width: 100%; margin-bottom: 15px; }}
    .progress-bar {{ width: 100%; background: #1e293b; height: 8px; border-radius: 4px; overflow: hidden; }}
    .progress-fill {{ height: 100%; background: #38bdf8; width: 0%; transition: width 0.3s ease; }}
    .progress-text {{ text-align: right; font-size: 0.85rem; color: #94a3b8; margin-top: 5px; font-weight: 700; }}

    .anki-card {{ width: 100%; background: #161a24; border: 1px solid #2d3748; border-radius: 12px; padding: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.6); box-sizing: border-box; }}
    .card-badge {{ display: inline-block; background: #0c4a6e; color: #38bdf8; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; font-weight: 800; margin-bottom: 15px; border: 1px solid #0369a1; }}
    .card-q {{ font-size: 1.15rem; font-weight: 700; line-height: 1.6; color: #f1f5f9; margin-bottom: 25px; min-height: 80px; }}
    
    .input-area {{ width: 100%; margin-bottom: 20px; }}
    textarea {{ width: 100%; height: 100px; background: #0f1117; border: 1.5px solid #334155; border-radius: 8px; padding: 12px; color: #f8fafc; font-family: inherit; font-size: 1rem; resize: none; box-sizing: border-box; line-height: 1.5; }}
    textarea:focus {{ outline: none; border-color: #38bdf8; }}

    .btn-flip {{ width: 100%; background: #d97706; color: #fff; border: none; padding: 14px; border-radius: 8px; font-size: 1.05rem; font-weight: 800; cursor: pointer; transition: background 0.2s; box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3); }}
    .btn-flip.flipped {{ background: #334155; color: #cbd5e1; box-shadow: none; }}

    .card-back {{ margin-top: 25px; padding-top: 25px; border-top: 2px dashed #334155; display: none; animation: fadeIn 0.4s ease; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(-10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    .answer-kw {{ font-size: 1.25rem; font-weight: 800; color: #fde047; margin-bottom: 12px; text-align: center; }}
    .answer-text {{ font-size: 1.05rem; color: #fef08a; line-height: 1.6; font-weight: 600; background: #1f2937; padding: 15px; border-radius: 8px; border-left: 4px solid #facc15; margin-bottom: 20px; }}
    
    .reward-container {{ display: flex; gap: 10px; width: 100%; }}
    .reward-btn {{ flex: 1; color: #fff; border: none; padding: 12px; border-radius: 8px; font-size: 0.95rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }}
    .reward-btn.wrong {{ background: #64748b; }}
    .reward-btn.right {{ background: #ec4899; }}
    .reward-btn:active {{ transform: scale(0.98); }}

    .nav-buttons {{ width: 100%; display: flex; justify-content: space-between; margin-top: 20px; gap: 10px; }}
    .btn-nav {{ flex: 1; background: #1e293b; color: #cbd5e1; border: 1px solid #334155; padding: 14px; border-radius: 8px; font-size: 1rem; font-weight: 700; cursor: pointer; }}
    .btn-nav.next {{ background: #0369a1; color: #fff; border-color: #0284c7; }}

    /* TABLE MODE */
    #mode-table {{ width: 100%; display: none; }}
    .table-container {{ background: #11141d; border: 1.5px solid #2d3748; border-radius: 8px; overflow-x: auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 10pt; min-width: 600px; }}
    th {{ background: #161a24; color: #fbbf24; border: 1px solid #283042; padding: 10px; font-weight: 800; text-align: center; }}
    td {{ border: 1px solid #222938; padding: 12px; line-height: 1.6; vertical-align: top; }}
    tr.table-row {{ display: none; }}
    tr.table-row.active-page {{ display: table-row; }}
    
    .table-nav {{ display: flex; justify-content: space-between; align-items: center; margin-top: 15px; gap: 10px; }}
    .page-info {{ color: #94a3b8; font-weight: 700; white-space: nowrap; }}

    /* Reward Modal */
    .modal-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.85); display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px; animation: fadeIn 0.3s ease; }}
    .modal-content {{ background: #1e293b; border-radius: 16px; overflow: hidden; max-width: 400px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.8); border: 2px solid #ec4899; text-align: center; }}
    .modal-img {{ width: 100%; display: block; max-height: 400px; object-fit: cover; }}
    .modal-text {{ padding: 20px; }}
    .modal-title {{ font-size: 1.3rem; font-weight: 800; color: #fdf2f8; margin-bottom: 10px; }}
    .modal-msg {{ font-size: 1rem; color: #fbcfe8; margin-bottom: 20px; line-height: 1.5; }}
    .btn-close-modal {{ background: #ec4899; color: white; border: none; padding: 10px 24px; border-radius: 8px; font-weight: 800; font-size: 1rem; cursor: pointer; width: 100%; }}

    /* PRINT STYLES */
    @media print {{
      body {{ background: #fff; color: #000; font-size: 11pt; }}
      .app-header, .controls, #mode-anki, .table-nav {{ display: none !important; }}
      #mode-table {{ display: block !important; width: 100%; max-width: none; }}
      .table-container {{ border: none; box-shadow: none; overflow: visible; }}
      table {{ border: 2px solid #000; width: 100%; page-break-inside: auto; }}
      tr {{ page-break-inside: avoid; page-break-after: auto; }}
      tr.table-row {{ display: table-row !important; }} /* SHOW ALL ROWS */
      th {{ background: #f0f0f0 !important; color: #000 !important; border: 1px solid #000; }}
      td {{ border: 1px solid #000 !important; color: #000 !important; }}
      .td-badge {{ color: #555 !important; border: none !important; padding: 0 !important; display: inline; margin-right: 5px; }}
      .td-kw {{ color: #000 !important; font-weight: bold; }}
      .td-q, .td-ans {{ color: #000 !important; }}
    }}
  </style>
</head>
<body>

  <div class="app-header">
    <div class="app-title">🚨 2027 KICE 초압축 55제</div>
    <div class="app-sub">앙키 카드 모드 &amp; 전체 표 모드 지원</div>
  </div>

  <div class="controls">
    <button class="btn-control active" id="btn-anki" onclick="switchMode('anki')">🃏 앙키 카드 모드</button>
    <button class="btn-control" id="btn-table" onclick="switchMode('table')">📋 6개씩 표 모드</button>
    <button class="btn-control btn-print" onclick="window.print()">🖨️ 인쇄하기 (전체)</button>
  </div>

  <div class="main-container">
    
    <!-- ANKI MODE -->
    <div id="mode-anki">
      <div class="progress-container">
        <div class="progress-bar"><div class="progress-fill" id="p-fill"></div></div>
        <div class="progress-text"><span id="p-text">1</span> / 55</div>
      </div>

      <div class="anki-card">
        <div class="card-badge" id="c-badge">영역</div>
        <div class="card-q" id="c-q">문제 단서 텍스트</div>

        <div class="input-area">
          <textarea id="c-input" placeholder="여기에 정답을 직접 타이핑해보세요..."></textarea>
        </div>

        <button class="btn-flip" id="btn-flip" onclick="toggleFlip()">💡 정답 확인하기 (뒤집기)</button>

        <div class="card-back" id="c-back">
          <div class="answer-kw" id="c-kw">정답 표제어</div>
          <div class="answer-text" id="c-ans">공식 서술형 정답</div>
          <div class="reward-container">
            <button class="reward-btn wrong" onclick="showReward('wrong')">❌ 아쉬워요 (위로 받기)</button>
            <button class="reward-btn right" onclick="showReward('right')">⭕ 완벽해요 (보상 받기)</button>
          </div>
        </div>
      </div>

      <div class="nav-buttons">
        <button class="btn-nav prev" onclick="goPrev()">◀ 이전 카드</button>
        <button class="btn-nav next" onclick="goNext()">다음 카드 ▶</button>
      </div>
    </div>

    <!-- TABLE MODE -->
    <div id="mode-table">
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th width="5%">No</th>
              <th width="20%">영역 및 표제어</th>
              <th width="40%">실전 단서 (핵심 키워드)</th>
              <th width="35%">공식 정답</th>
            </tr>
          </thead>
          <tbody id="table-body">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>
      <div class="table-nav">
        <button class="btn-nav prev" onclick="goPrevPage()">◀ 이전 6개</button>
        <span class="page-info" id="t-page">페이지 1 / 10</span>
        <button class="btn-nav next" onclick="goNextPage()">다음 6개 ▶</button>
      </div>
    </div>

  </div>

  <!-- Reward Modal -->
  <div class="modal-overlay" id="reward-modal">
    <div class="modal-content">
      <img src="" class="modal-img" id="reward-img" alt="Cheering Reward">
      <div class="modal-text">
        <div class="modal-title" id="reward-title">🎉 정답입니다! 최고예요!</div>
        <div class="modal-msg" id="reward-msg">선생님의 노력은 배신하지 않습니다!<br>올해 무조건 합격하실 거예요! 💖</div>
        <button class="btn-close-modal" onclick="closeReward()">닫기 (다음 문제로)</button>
      </div>
    </div>
  </div>

  <script>
    const items = {items_json};
    
    // ANKI STATE
    let currentIndex = 0;
    let isFlipped = false;

    // TABLE STATE
    let tablePage = 0;
    const itemsPerPage = 6;
    const totalPages = Math.ceil(items.length / itemsPerPage);

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

    // UI SWITCHER
    function switchMode(mode) {{
      if(mode === 'anki') {{
        document.getElementById('mode-anki').style.display = 'block';
        document.getElementById('mode-table').style.display = 'none';
        document.getElementById('btn-anki').classList.add('active');
        document.getElementById('btn-table').classList.remove('active');
      }} else {{
        document.getElementById('mode-anki').style.display = 'none';
        document.getElementById('mode-table').style.display = 'block';
        document.getElementById('btn-anki').classList.remove('active');
        document.getElementById('btn-table').classList.add('active');
      }}
    }}

    // ANKI LOGIC
    function renderCard(index) {{
      const item = items[index];
      elBadge.innerText = item.badge;
      elQ.innerHTML = item.q.replace(/➔/g, '<span style="color:#d97706; font-weight:bold;">➔</span>');
      elKw.innerText = item.kw;
      elAns.innerText = item.ans;
      
      elPText.innerText = index + 1;
      elPFill.style.width = ((index + 1) / items.length * 100) + '%';

      isFlipped = false;
      elBack.style.display = 'none';
      elFlipBtn.innerText = '💡 정답 확인하기 (뒤집기)';
      elFlipBtn.classList.remove('flipped');
      elInput.value = '';
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

    function goNext() {{
      if(currentIndex < items.length - 1) {{
        currentIndex++;
        renderCard(currentIndex);
      }} else {{
        alert('마지막 카드입니다. 1번으로 돌아갑니다.');
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

    // TABLE LOGIC
    function initTable() {{
      const tbody = document.getElementById('table-body');
      let html = '';
      items.forEach((item, i) => {{
        html += `<tr class="table-row" id="tr-${{i}}">
          <td class="td-num"><b>${{i+1}}</b></td>
          <td><span class="td-badge">[${{item.badge}}]</span><br><span class="td-kw">${{item.kw}}</span></td>
          <td class="td-q">${{item.q}}</td>
          <td class="td-ans">${{item.ans}}</td>
        </tr>`;
      }});
      tbody.innerHTML = html;
      updateTablePagination();
    }}

    function updateTablePagination() {{
      for(let i=0; i<items.length; i++) {{
        const tr = document.getElementById(`tr-${{i}}`);
        if(i >= tablePage * itemsPerPage && i < (tablePage + 1) * itemsPerPage) {{
          tr.classList.add('active-page');
        }} else {{
          tr.classList.remove('active-page');
        }}
      }}
      document.getElementById('t-page').innerText = `페이지 ${{tablePage + 1}} / ${{totalPages}}`;
    }}

    function goNextPage() {{
      if(tablePage < totalPages - 1) {{
        tablePage++;
        updateTablePagination();
        window.scrollTo(0, 0);
      }}
    }}

    function goPrevPage() {{
      if(tablePage > 0) {{
        tablePage--;
        updateTablePagination();
        window.scrollTo(0, 0);
      }}
    }}

    // REWARD LOGIC
    function showReward(type) {{
      const t = document.getElementById('reward-title');
      const m = document.getElementById('reward-msg');
      
      if(type === 'right') {{
        const rewardImages = ['images/cheer1.jpg', 'images/cheer2.jpg'];
        const randomImg = rewardImages[Math.floor(Math.random() * rewardImages.length)];
        document.getElementById('reward-img').src = randomImg;
        
        t.innerText = '🎉 완벽합니다! 최고예요!';
        m.innerHTML = '선생님의 노력은 절대 배신하지 않습니다!<br>이 기세로 2027 합격까지 화이팅! 💖';
        document.querySelector('.modal-content').style.borderColor = '#ec4899';
        
        // Fire confetti
        const duration = 2 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = {{ startVelocity: 30, spread: 360, ticks: 60, zIndex: 1001 }};
        function randomInRange(min, max) {{ return Math.random() * (max - min) + min; }}
        const interval = setInterval(function() {{
          const timeLeft = animationEnd - Date.now();
          if (timeLeft <= 0) {{ return clearInterval(interval); }}
          const particleCount = 50 * (timeLeft / duration);
          confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }} }}));
          confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }} }}));
        }}, 250);
      }} else {{
        document.getElementById('reward-img').src = 'images/cheer3.jpg';
        t.innerText = '🐕 괜찮아요! 토닥토닥';
        m.innerHTML = '틀린 부분은 지금 확실히 잡으면 됩니다!<br>다시 한번 눈도장 찍고 다음으로 넘어가요! 🐾';
        document.querySelector('.modal-content').style.borderColor = '#38bdf8';
      }}
      
      modal.style.display = 'flex';
    }}

    function closeReward() {{
      modal.style.display = 'none';
      goNext();
    }}

    // INIT
    renderCard(currentIndex);
    initTable();
  </script>
</body>
</html>
"""

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully generated unified UI with Right/Wrong rewards')
