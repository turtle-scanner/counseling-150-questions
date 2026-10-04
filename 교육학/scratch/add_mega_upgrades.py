import json
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS for Badges, Trap Box, Category Pills, and Print Stylesheet
css_upgrades = """
    /* MEGA UPGRADES: BADGES, TRAP CLINIC, PILLS & PRINT */
    .badge-grade {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 900;
      font-size: 0.85rem;
      margin-left: 6px;
      vertical-align: middle;
    }
    .grade-s { background: #dc2626 !important; color: #fff !important; box-shadow: 0 0 8px rgba(220,38,38,0.5); }
    .grade-recent { background: #2563eb !important; color: #fff !important; }
    .grade-a { background: #059669 !important; color: #fff !important; }
    
    .category-pills-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px;
      margin: 8px 10px;
    }
    .pill-btn {
      padding: 6px 12px;
      border-radius: 20px;
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      font-size: 0.9rem;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: 'Malgun Gothic', sans-serif;
    }
    .pill-btn:hover { background: #334155; color: #f8fafc; }
    .pill-btn.active {
      background: #3b82f6 !important;
      color: #fff !important;
      border-color: #2563eb !important;
      box-shadow: 0 2px 6px rgba(59,130,246,0.4);
    }
    
    .trap-box {
      background: #2a1505 !important;
      border: 1px solid #d97706 !important;
      color: #fde68a !important;
      padding: 12px 16px !important;
      border-radius: 8px !important;
      margin-top: 14px !important;
      font-size: 1.15rem !important;
      line-height: 1.6 !important;
      text-align: left !important;
      font-family: 'Malgun Gothic', sans-serif !important;
      box-shadow: inset 0 0 10px rgba(217,119,6,0.15);
    }
    
    @media print {
      body { background: #fff !important; color: #000 !important; font-size: 9pt !important; }
      #pomodoro-bar, .controls, .category-pills-container, #dashboard, .btn-control, .app-sub, #auth-screen, .progress-container, .pagination, .kice-sheet-wrapper, .btn-flip, #hint-box, .btn-nav, .star-btn { display: none !important; }
      #mode-table { display: block !important; }
      #mode-anki { display: none !important; }
      .table-container { width: 100% !important; margin: 0 !important; box-shadow: none !important; background: #fff !important; }
      table { border-collapse: collapse !important; width: 100% !important; color: #000 !important; }
      th, td { border: 1px solid #444 !important; color: #000 !important; padding: 4px 6px !important; }
      th { background: #eee !important; color: #000 !important; font-weight: bold !important; }
      .app-title { color: #000 !important; font-size: 14pt !important; text-align: center !important; margin-bottom: 10px !important; }
      #table-body.hide-ans td:nth-child(4) > * { opacity: 1 !important; filter: none !important; }
      #table-body.hide-kw td:nth-child(2) > * { opacity: 1 !important; filter: none !important; }
    }
"""

if '/* MEGA UPGRADES: BADGES' not in html:
    html = html.replace('</style>', css_upgrades.strip() + '\n  </style>')

# 2. Add Category Pills and Print Button to HTML
pills_html = """
    <div class="category-pills-container" id="cat-pills">
      <button class="pill-btn active" onclick="filterByCategory('all')">🌟 전체 (203)</button>
      <button class="pill-btn" onclick="filterByCategory('교육')">🎓 교육학 (18)</button>
      <button class="pill-btn" onclick="filterByCategory('진로')">🧭 진로상담 (18)</button>
      <button class="pill-btn" onclick="filterByCategory('심리검사')">📊 심리검사 (22)</button>
      <button class="pill-btn" onclick="filterByCategory('가족')">👨‍👩‍👧 가족치료 (22)</button>
      <button class="pill-btn" onclick="filterByCategory('정신병리')">🧠 이상심리/DSM-5 (35)</button>
      <button class="pill-btn" onclick="filterByCategory('이론')">💡 상담이론·치료 (25)</button>
      <button class="pill-btn" onclick="filterByCategory('위기')">🚨 위기·법령·윤리 (25)</button>
    </div>
"""

if 'id="cat-pills"' not in html:
    html = html.replace('</div>\n    <div class="controls">', '</div>\n' + pills_html + '    <div class="controls">')

# Add Print button in controls
print_btn_html = '<button class="btn-control" onclick="printSummaryA4()" style="background:#059669; border-color:#047857; color:#fff;">🖨️ A4 요약집 인쇄</button>'
if 'printSummaryA4()' not in html:
    html = html.replace('<!-- Actions -->', '<!-- Actions -->\n      ' + print_btn_html)
    if 'printSummaryA4()' not in html:
        html = html.replace('onclick="openAddCardModal()"', 'onclick="openAddCardModal()" style="background:#8b5cf6;"')
        html = html.replace('</button>\n      <button class="btn-control" id="btn-table"', '</button>\n      ' + print_btn_html + '\n      <button class="btn-control" id="btn-table"')

# 3. Add Trap Box to Card Back
trap_html = '<div class="trap-box" id="c-trap" style="display:none;"></div>'
if 'id="c-trap"' not in html:
    html = html.replace('<div class="answer-box">', trap_html + '\n            <div class="answer-box">')

# 4. Inject Smart JS Logic for Grades, Trap Clinic, Category Filtering, and A4 Printing
mega_js_logic = """
    // --- MEGA UPGRADES LOGIC: GRADES, TRAP CLINIC, CATEGORY FILTER, A4 PRINT ---
    
    // High-yield S-grade killer keywords for 2027
    const S_GRADE_KEYWORDS = [
      '백워드', '영속적 이해', '스킬벡', '타바', '워커', '정교화', 'ZPD', '도덕적 리더십',
      '강박장애', '강박성', '반응성 애착', '탈억제', '신체증상', '질병불안', '공황장애', '광장공포증',
      'SUI', 'BXD', 'THD', 'RCd', 'CASE', '숀 셰이', '안전계획서', '보웬', '삼각관계', '탈삼각화',
      '탈숙고', '역설적 의도', '미세공격', '사비카스', '갓프레드슨', '학폭법', '변혁적 학습', '렌줄리'
    ];

    function getGradeInfo(item) {
      const kw = item.kw;
      const num = item.num;
      if (S_GRADE_KEYWORDS.some(k => kw.includes(k))) {
        return { text: '2027 S급 킬러', css: 'grade-s' };
      } else if (num >= 92 && num <= 121) {
        return { text: 'DSM-5-TR 핵심', css: 'grade-recent' };
      } else if (num >= 32 && num <= 46) {
        return { text: 'MMPI-2-RF 기출', css: 'grade-recent' };
      } else {
        return { text: 'A급 필수표제어', css: 'grade-a' };
      }
    }

    function getTrapTip(item) {
      const kw = item.kw;
      if (kw.includes('백워드')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 타일러 모형(수업 후 평가)과 혼동 주의! 반드시 <b>\"평가 계획이 수업 활동 설계보다 선행하여 일관성을 확보함\"</b>을 명시해야 만점이 인정됩니다.';
      } else if (kw.includes('영속적 이해')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 단순 지식 암기가 아님! 6대 측면 중 <b>\"적용(새 맥락 활용)\"</b>과 <b>\"감정이입(타인 세계관 공감)\"</b>을 정확한 학술명으로 서술해야 채점표에 부합합니다.';
      } else if (kw.includes('강박장애')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 강박성 성격장애(OCPD)와 감별 필수! 강박장애(OCD)는 증상에 고통을 느끼는 <b>\"자아이질적(Ego-dystonic)\"</b> 특성이며 의례적 중화행동이 존재합니다.';
      } else if (kw.includes('강박성')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 강박장애(OCD)와 감별 필수! 강박성 성격장애는 완벽주의를 옳다고 여기는 <b>\"자아동질적(Ego-syntonic)\"</b> 특성이며 명확한 강박사고/강박행동이 없습니다.';
      } else if (kw.includes('반응성 애착')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 탈억제 사회관여 장애(DSED)와 구별 필수! RAD는 성인 양육자에게 안락을 구하지 않는 <b>\"정서적 억제 및 위축\"</b>이 핵심 진단 기준입니다.';
      } else if (kw.includes('탈억제')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 반응성 애착장애(RAD)와 구별 필수! DSED는 낯선 성인에 대해 정상적 경계선 없이 <b>\"무분별한 친밀성 및 접근\"</b>을 보이는 외현화 양상입니다.';
      } else if (kw.includes('신체증상')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 질병불안장애와 구별 필수! 신체증상장애는 <b>\"실제 고통스러운 신체 증상이 존재\"</b>하며 그에 대해 파국적 불안을 느끼는 장애입니다.';
      } else if (kw.includes('질병불안')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 신체증상장애와 구별 필수! 질병불안장애는 <b>\"실제 신체 증상은 없거나 매우 경미함\"</b>에도 불구하고 불치병에 걸렸다는 집착에 사로잡힙니다.';
      } else if (kw.includes('탈숙고')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 프랑클의 <b>\"역설적 의도\"</b>와 혼동 금지! 불안 증상을 의도적으로 원하게 하는 것은 역설적 의도이며, 주의를 외부 의미로 돌리는 것은 <b>\"탈숙고\"</b>입니다.';
      } else if (kw.includes('CASE') || kw.includes('셰이')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 숀 셰이(Shawn Shea)의 4개 시간적 국면 순서 엄수! <b>\"현재 사건(48h) ➔ 최근 사건(2개월) ➔ 과거 사건(생애) ➔ 즉각적 사건(상담실 면담)\"</b>을 정확히 나열해야 4점 만점입니다.';
      } else if (kw.includes('안전계획서')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 단순 비밀유지가 아님! 자살 위험 도구(약물, 흉기 등)의 <b>\"물리적 즉각 제거\"</b>와 보호자 및 전문기관 비상연락망 작성을 필수로 언급해야 합니다.';
      } else if (kw.includes('보웬') || kw.includes('삼각관계')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 단순 가족 갈등이 아님! <b>\"부부 간 미분화 불안을 해소하기 위해 취약한 제3자(자녀)를 끌어들임\"</b>과 상담자의 <b>\"탈삼각화 중립성\"</b>을 반드시 서술해야 합니다.';
      } else if (kw.includes('미세공격')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 미세공격의 3대 하위유형(미세모욕, 미세폭행, 미세무효화) 중 숨은 비하 칭찬은 <b>\"미세모욕\"</b>이며, 감정을 과민반응으로 치부하는 것은 <b>\"미세무효화\"</b>입니다.';
      } else if (kw.includes('정교화')) {
        return '⚠️ <b>[KICE 감점 방지 함정]</b> 라이겔루스의 7대 교수전략 중 망각 방지는 <b>\"요약자\"</b>이며, 개념들 간의 연계성 조망은 <b>\"종합자\"</b>입니다. 두 개념을 절대 뒤바꿔 쓰지 마세요!';
      } else {
        return `💡 <b>[KICE 채점 핵심]</b> 채점관은 표제어인 <b>\"${kw}\"</b>의 정식 학술 명칭과 작동 원리 및 교육적·임상적 의의가 4줄 안에 명확히 연결되어 있는지를 집중 채점합니다.`;
      }
    }

    let currentSelectedCategory = 'all';

    function filterByCategory(category) {
      currentSelectedCategory = category;
      
      // Update pill buttons visual state
      document.querySelectorAll('.pill-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.innerText.includes(category === 'all' ? '전체' : category)) {
          btn.classList.add('active');
        }
      });

      if (category === 'all') {
        items = [...originalItems];
      } else {
        items = originalItems.filter(item => {
          const badge = item.badge || '';
          const kw = item.kw || '';
          if (category === '교육') return badge.includes('교육') || badge.includes('교수');
          if (category === '진로') return badge.includes('진로');
          if (category === '심리검사') return badge.includes('검사');
          if (category === '가족') return badge.includes('가족');
          if (category === '정신병리') return badge.includes('병리') || badge.includes('이상') || kw.includes('장애');
          if (category === '이론') return badge.includes('이론') || badge.includes('행동') || badge.includes('성격');
          if (category === '위기') return badge.includes('위기') || badge.includes('법령') || badge.includes('윤리');
          return badge.includes(category);
        });
      }

      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
    }

    function printSummaryA4() {
      // Ensure all answers and keywords are visible before printing
      document.getElementById('table-body').classList.remove('hide-ans');
      document.getElementById('table-body').classList.remove('hide-kw');
      
      // If in Anki mode, switch to table mode for full printout
      if (document.getElementById('mode-anki').style.display !== 'none') {
        switchMode('table');
      }
      
      setTimeout(() => {
        window.print();
      }, 300);
    }
"""

if 'function getGradeInfo' not in html:
    html = html.replace('// --- ADVANCED STUDY FEATURES', mega_js_logic.strip() + '\n\n    // --- ADVANCED STUDY FEATURES')

# 5. Update renderCard to apply Grade Badges and Trap Box
old_render_badge = "elBadge.innerHTML = formatText(item.badge);"
new_render_badge = """const grade = getGradeInfo(item);
        elBadge.innerHTML = `<span style="font-weight:bold;">${formatText(item.badge)}</span> <span class="badge-grade ${grade.css}">${grade.text}</span>`;
        
        // Trap Box update
        const trapEl = document.getElementById('c-trap');
        if (trapEl) {
          trapEl.innerHTML = getTrapTip(item);
          trapEl.style.display = 'block';
        }"""

html = html.replace(old_render_badge, new_render_badge)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected all 4 mega upgrades!")
