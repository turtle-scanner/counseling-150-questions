import json
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract current items
m = re.search(r'let items = (\[[\s\S]*?\]);\s*// Load custom items', html)
if not m:
    print('Failed to find items array')
    exit(1)

items = json.loads(m.group(1))
print('Current items count:', len(items))

# 2. Add New Card 1: 변혁적 학습 이론 (메지로우)
card_mezirow = {
    "num": len(items) + 1,
    "badge": "교육방법·학습",
    "kw": "변혁적 학습 이론 (메지로우)",
    "q": "학습자가 기존에 무비판적으로 수용했던 신념이나 가치관인 '의미관점(Meaning Perspective)'이 기존 지식으로 해결할 수 없는 '혼란스러운 딜레마(Disorienting Dilemma)'에 직면했을 때, '비판적 반성(Critical Reflection)'을 거쳐 보다 개방적이고 통합적인 관점으로 재구성되는 학습 모형의 명칭과 3대 핵심 개념을 쓸 것.",
    "ans": "기존의 왜곡된 전제를 의식화하고 수정하는 '비판적 반성'과 대화를 통한 '합리적 담론'을 거쳐 새로운 신념 체계로 관점 전환을 이루는 메지로우(Mezirow)의 '변혁적 학습 이론'이다. (핵심 3요소: 의미관점, 혼란스러운 딜레마, 비판적 반성)"
}

# 3. Add New Card 2: 렌줄리 영재성 3고리 & 심화학습 모형(SEM)
card_renzulli = {
    "num": len(items) + 2,
    "badge": "교육심리·특수",
    "kw": "렌줄리 영재성 3고리 및 학교심화학습 모형 (SEM)",
    "q": "렌줄리(Renzulli)가 영재성을 구성하는 상호작용적 3대 요인으로 제시한 요소들과, 정규 교육과정을 넘어서는 3단계 심화학습(1단계 일반적 탐색, 2단계 집단 훈련, 3단계 실제 문제 조사·연구)으로 구성된 학교 교육과정 모형의 명칭을 쓸 것.",
    "ans": "영재성의 3대 요인인 '평균 이상의 일반 능력', '높은 창의성', '강한 과제 집착력'의 상호작용을 강조하며, 모든 학습자에게 단계별 탐구와 문제해결 기회를 제공하는 렌줄리의 '학교심화학습 모형(SEM)'이다."
}

items.append(card_mezirow)
items.append(card_renzulli)
print(f'New items count: {len(items)}')

# Serialize back
new_items_json = json.dumps(items, ensure_ascii=False)
replacement = f'let items = {new_items_json};\n      // Load custom items'
html = html[:m.start(0)] + replacement + html[m.end(0):]

# Update Title and count in HTML
html = html.replace('2027 KICE 핵심 단어장 (201선)', f'2027 KICE 핵심 단어장 ({len(items)}선)')
html = html.replace('1 / 201', f'1 / {len(items)}')

# 4. Add UI Buttons for [🔥 오답 집중], [🎲 실전 20제], [A+ / A-] Font Sizing
old_controls_btn = '<button class="btn-control" id="btn-table" onclick="switchMode(\'table\')">📑 4개씩 표 모드</button>'
new_controls_btn = """<button class="btn-control" id="btn-table" onclick="switchMode('table')">📑 4개씩 표 모드</button>
      <button class="btn-control" id="btn-wrong" onclick="toggleWrongMode()" style="background:#dc2626; border-color:#b91c1c; color:#fff;">🔥 오답 집중 모드</button>
      <button class="btn-control" id="btn-mock20" onclick="startMockTest20()" style="background:#0284c7; border-color:#0369a1; color:#fff;">🎲 실전 20제 모의고사</button>
      <div style="display:inline-flex; align-items:center; gap:3px; margin-left:5px;">
        <button class="btn-control" onclick="adjustFontSize(-0.1)" title="글자 축소" style="padding:4px 8px; font-weight:900;">A-</button>
        <button class="btn-control" onclick="adjustFontSize(0.1)" title="글자 확대" style="padding:4px 8px; font-weight:900;">A+</button>
      </div>"""

if 'btn-wrong' not in html:
    html = html.replace(old_controls_btn, new_controls_btn)

# 5. Add JavaScript logic for Wrong Mode, Mock 20 Mode, and Dynamic Font Sizing
new_js_features = """
    // --- ADVANCED STUDY FEATURES (Wrong Mode, Mock 20, Font Scaling) ---
    let isWrongMode = false;
    let isMockMode = false;

    function toggleWrongMode() {
      const btn = document.getElementById('btn-wrong');
      const srsData = JSON.parse(localStorage.getItem('kice_srs_data') || '{}');
      
      if (!isWrongMode) {
        // Filter cards that have interval <= 1 or was rated again
        const wrongItems = originalItems.filter(item => {
          const rec = srsData[item.kw];
          return rec && rec.interval <= 1;
        });
        
        if (wrongItems.length === 0) {
          alert('👏 현재 복습이 필요한 오답 카드가 없습니다! 아주 훌륭합니다.');
          return;
        }
        
        isWrongMode = true;
        isMockMode = false;
        items = wrongItems;
        btn.style.background = '#facc15';
        btn.style.color = '#000';
        btn.innerText = '🔥 오답 모드 해제 (전체 복귀)';
        alert(`🔥 취약/오답 카드 ${wrongItems.length}문항을 집중 공략합니다!`);
      } else {
        isWrongMode = false;
        items = [...originalItems];
        btn.style.background = '#dc2626';
        btn.style.color = '#fff';
        btn.innerText = '🔥 오답 집중 모드';
      }
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
    }

    function startMockTest20() {
      if (confirm('🎲 전체 203문항 중 무작위 20문항을 추출하여 실전 미니 모의고사를 시작하시겠습니까?')) {
        isMockMode = true;
        isWrongMode = false;
        
        // Shuffle and pick 20
        const shuffled = [...originalItems].sort(() => 0.5 - Math.random());
        items = shuffled.slice(0, 20);
        
        currentIndex = 0;
        renderCard(currentIndex);
        initTable();
        alert('🎯 20문항 실전 모의고사가 생성되었습니다! 1번부터 차례대로 풀며 실력을 점검해 보세요.');
      }
    }

    let currentFontScale = parseFloat(localStorage.getItem('kice_font_scale') || '1.0');
    function applyFontScale() {
      document.querySelectorAll('.card-q').forEach(el => el.style.fontSize = (1.25 * currentFontScale) + 'rem');
      document.querySelectorAll('.answer-text').forEach(el => el.style.fontSize = (1.45 * currentFontScale) + 'rem');
      document.querySelectorAll('.kice-textarea').forEach(el => el.style.fontSize = (1.25 * currentFontScale) + 'rem');
    }

    function adjustFontSize(delta) {
      currentFontScale = Math.max(0.7, Math.min(1.6, currentFontScale + delta));
      localStorage.setItem('kice_font_scale', currentFontScale.toFixed(2));
      applyFontScale();
    }
    
    // Apply initial font scale
    setTimeout(applyFontScale, 300);
"""

if 'toggleWrongMode' not in html:
    html = html.replace('// --- POMODORO LOGIC ---', new_js_features.strip() + '\n\n    // --- POMODORO LOGIC ---')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully added 2 new theory cards and 3 advanced learning features!')
