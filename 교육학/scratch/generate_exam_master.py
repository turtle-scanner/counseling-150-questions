# -*- coding: utf-8 -*-
import os, sys, json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('scratch')

from test_pedagogy_data import pedagogy_essay
import build_exam_web

with open('scratch/top55_extracted.json', 'r', encoding='utf-8') as f:
    top55_data = json.load(f)

top55_items = []
for idx, item in enumerate(top55_data):
    is_ped = (item.get('type') == 'pedagogy')
    prefix = 'P' if is_ped else 'C'
    cat_name = '교육학 20선' if is_ped else '전공상담 35선'
    
    raw_kw = item.get('keyword', '')
    kws = [k.strip() for k in raw_kw.replace('➔', ',').replace('/', ',').split(',') if k.strip()]
    
    clean_a = item.get('clean_ans', item.get('answer', ''))
    clean_a = clean_a.replace('<mark style=\"background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;\">', '').replace('</mark>', '').replace('<br>', '\n').strip()
    
    top55_items.append({
        "num": idx + 1,
        "code": f"{prefix}{idx+1:02d}",
        "category": cat_name,
        "type": item.get('type'),
        "domain": item.get('domain', ''),
        "question": item.get('question', ''),
        "keywords": kws,
        "raw_keywords": raw_kw,
        "answer": clean_a
    })

data_payload = {
    "top55": top55_items,
    "pedagogy": pedagogy_essay,
    "questions_a": build_exam_web.questions_a,
    "questions_b": build_exam_web.questions_b
}

json_str = json.dumps(data_payload, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2027 KICE 임용고시 합격 마스터: 교육학 & 전공상담 풀세트</title>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg-main: #090d16;
  --bg-card: #151e2e;
  --bg-card-hover: #1b263b;
  --bg-input: #0f1624;
  --border-card: #23324a;
  --border-focus: #38bdf8;
  --text-main: #f8fafc;
  --text-sub: #94a3b8;
  --text-dim: #64748b;
  --gold: #f59e0b;
  --gold-bg: rgba(245, 158, 11, 0.12);
  --emerald: #10b981;
  --emerald-bg: rgba(16, 185, 129, 0.12);
  --sky: #38bdf8;
  --sky-bg: rgba(56, 189, 248, 0.12);
  --rose: #f43f5e;
  --rose-bg: rgba(244, 63, 94, 0.12);
  --purple: #a855f7;
  --purple-bg: rgba(168, 85, 247, 0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: 'Noto Sans KR', sans-serif;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  padding-bottom: 80px;
}

/* Header & Nav */
header.app-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(9, 13, 22, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-card);
  padding: 12px 24px;
}
.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  max-width: 1400px;
  margin: 0 auto;
}
.brand-title {
  display: flex;
  align-items: center;
  gap: 10px;
}
.brand-title h1 {
  font-size: 1.25rem;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.5px;
}
.brand-badge {
  background: var(--gold-bg);
  color: var(--gold);
  border: 1px solid var(--gold);
  font-size: 0.72rem;
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 700;
}

/* Tabs */
.tab-container {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 0;
  max-width: 1400px;
  margin: 10px auto 0 auto;
}
.tab-btn {
  background: var(--bg-card);
  color: var(--text-sub);
  border: 1px solid var(--border-card);
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.tab-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.tab-btn.active {
  background: var(--sky-bg);
  color: var(--sky);
  border-color: var(--sky);
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
}

/* Control Bar */
.control-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  max-width: 1400px;
  margin: 16px auto;
  padding: 0 24px;
}
.search-box {
  position: relative;
  flex: 1;
  max-width: 360px;
}
.search-box input {
  width: 100%;
  background: var(--bg-input);
  border: 1px solid var(--border-card);
  color: #fff;
  padding: 8px 12px 8px 36px;
  border-radius: 8px;
  font-size: 0.85rem;
  outline: none;
}
.search-box input:focus {
  border-color: var(--sky);
}
.search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 0.9rem;
}

.tool-group {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
}
.tool-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  color: var(--text-sub);
  padding: 7px 12px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}
.tool-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.tool-btn.active-toggle {
  background: var(--rose-bg);
  border-color: var(--rose);
  color: var(--rose);
}

/* Timer Widget */
.timer-widget {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  padding: 4px 12px;
  border-radius: 8px;
}
.timer-clock {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--gold);
}

/* Progress bar */
.progress-wrap {
  max-width: 1400px;
  margin: 0 auto 16px auto;
  padding: 0 24px;
}
.progress-bar-bg {
  background: #1b263b;
  border-radius: 999px;
  height: 6px;
  overflow: hidden;
}
.progress-bar-fill {
  background: linear-gradient(90deg, var(--sky), var(--emerald));
  height: 100%;
  width: 0%;
  transition: width 0.3s ease;
}
.progress-text {
  font-size: 0.78rem;
  color: var(--text-sub);
  margin-top: 4px;
  display: flex;
  justify-content: space-between;
}

/* Content Area */
main.content-area {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
}
.tab-section {
  display: none;
}
.tab-section.active {
  display: block;
}

/* Card Styles */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
  gap: 16px;
}
@media (max-width: 768px) {
  .card-grid { grid-template-columns: 1fr; }
}

.item-card {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  padding: 18px;
  position: relative;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.item-card:hover {
  border-color: #3b4e6d;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.item-card.memorized {
  border-color: var(--emerald);
  background: rgba(16, 185, 129, 0.04);
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.badge-group {
  display: flex;
  gap: 6px;
  align-items: center;
}
.badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 6px;
}
.badge-code {
  background: #202b3d;
  color: var(--sky);
  border: 1px solid #334460;
  font-family: 'JetBrains Mono', monospace;
}
.badge-category {
  background: var(--purple-bg);
  color: var(--purple);
  border: 1px solid rgba(168, 85, 247, 0.4);
}
.badge-pedagogy {
  background: var(--sky-bg);
  color: var(--sky);
  border: 1px solid rgba(56, 189, 248, 0.4);
}
.badge-score {
  background: var(--gold-bg);
  color: var(--gold);
  border: 1px solid var(--gold);
}

.memorize-chk {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  color: var(--text-sub);
  cursor: pointer;
  user-select: none;
}
.memorize-chk input {
  cursor: pointer;
  accent-color: var(--emerald);
  width: 16px;
  height: 16px;
}

.card-question {
  font-size: 0.98rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.5;
}
.keyword-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.kw-tag {
  background: #1e293b;
  color: var(--gold);
  border: 1px solid #334155;
  font-size: 0.76rem;
  padding: 3px 8px;
  border-radius: 6px;
  font-weight: 600;
  transition: all 0.2s;
}

/* Spoiler / Blind Effect */
body.blind-mode .kw-tag {
  background: #0f172a;
  color: #0f172a;
  border-color: #334155;
  cursor: pointer;
  user-select: none;
}
body.blind-mode .kw-tag:hover,
body.blind-mode .kw-tag.revealed {
  background: #1e293b;
  color: var(--gold);
  border-color: var(--gold);
}

.compact-answer-box {
  background: #0d1422;
  border: 1px solid #202b3d;
  border-radius: 8px;
  padding: 12px;
  font-size: 0.88rem;
  line-height: 1.6;
  color: #cbd5e1;
  font-family: 'Nanum Myeongjo', serif;
  border-left: 3px solid var(--emerald);
  white-space: pre-wrap;
}

/* Exam Mode Simulation Cards */
.exam-full-card {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 14px;
  padding: 24px;
  margin-bottom: 24px;
}
.exam-case-box {
  background: #0c1320;
  border: 1px solid #23324a;
  border-left: 4px solid var(--sky);
  border-radius: 8px;
  padding: 18px;
  margin: 16px 0;
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.95rem;
  line-height: 1.8;
  color: #e2e8f0;
  white-space: pre-wrap;
}
.exam-instructions {
  background: rgba(245, 158, 11, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: 8px;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 0.88rem;
  color: #fde68a;
}
.exam-instructions ul {
  margin-left: 20px;
  margin-top: 6px;
}

/* Line-note styled textarea */
.answer-box-wrap {
  margin-top: 16px;
}
.answer-box-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  font-size: 0.82rem;
  color: var(--text-sub);
}
.char-count-badge {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: var(--sky);
}
.char-count-badge.limit-ok {
  color: var(--emerald);
}
.char-count-badge.limit-warn {
  color: var(--rose);
}

.exam-textarea {
  width: 100%;
  min-height: 140px;
  background: var(--bg-input);
  background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 100% 32px;
  line-height: 32px;
  border: 1px solid var(--border-card);
  border-radius: 8px;
  color: #fff;
  padding: 8px 14px;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 0.95rem;
  resize: vertical;
  outline: none;
}
.exam-textarea:focus {
  border-color: var(--sky);
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
}

/* Hidden Model Answer Box */
.model-answer-panel {
  display: none;
  background: #0b1524;
  border: 1px solid #1e3a5f;
  border-left: 4px solid var(--gold);
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
  animation: fadeIn 0.3s ease;
}
.model-answer-panel.show {
  display: block;
}
.model-answer-title {
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--gold);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.model-answer-text {
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.92rem;
  line-height: 1.7;
  color: #e2e8f0;
  white-space: pre-wrap;
}
.rubric-list {
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px dashed #233852;
  font-size: 0.82rem;
  color: var(--text-sub);
}
.rubric-item {
  margin-bottom: 4px;
  display: flex;
  align-items: flex-start;
  gap: 6px;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Quick Nav Bar */
.quick-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}
.quick-nav-btn {
  background: var(--bg-card);
  color: var(--text-sub);
  border: 1px solid var(--border-card);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}
.quick-nav-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.quick-nav-btn.written {
  border-color: var(--emerald);
  color: var(--emerald);
}

/* Banner */
.notice-banner {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.1), rgba(168, 85, 247, 0.1));
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
.notice-banner h3 {
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
}
.notice-banner p {
  font-size: 0.82rem;
  color: var(--text-sub);
}
</style>
</head>
<body>

<header class="app-header">
  <div class="header-top">
    <div class="brand-title">
      <h1>🎯 2027 KICE 임용고시 합격 마스터</h1>
      <span class="brand-badge">2027 0순위 55개 완전압축</span>
    </div>
    
    <div class="tool-group">
      <div class="timer-widget">
        <span style="font-size: 0.8rem; color: var(--text-sub);">⏱️</span>
        <span class="timer-clock" id="timer-display">60:00</span>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="toggleTimer()" id="timer-btn">시작</button>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="resetTimer(60)">60분</button>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="resetTimer(90)">90분</button>
      </div>

      <button class="tool-btn" id="blind-toggle-btn" onclick="toggleBlindMode()">
        <span>👁️</span> <span id="blind-label">키워드 가리기</span>
      </button>

      <button class="tool-btn" onclick="exportAnswers()">
        <span>📋</span> 답안 전체 복사
      </button>
    </div>
  </div>

  <div class="tab-container">
    <button class="tab-btn active" onclick="switchTab('top55')" id="tab-btn-top55">
      <span>⚡</span> 2027 핵심 55선 콤팩트 스피드 암기
    </button>
    <button class="tab-btn" onclick="switchTab('pedagogy')" id="tab-btn-pedagogy">
      <span>🎓</span> 1교시 교육학 논술 [20점]
    </button>
    <button class="tab-btn" onclick="switchTab('qa')" id="tab-btn-qa">
      <span>📘</span> 2교시 전공 A형 [40점]
    </button>
    <button class="tab-btn" onclick="switchTab('qb')" id="tab-btn-qb">
      <span>📙</span> 3교시 전공 B형 [40점]
    </button>
  </div>
</header>

<div class="control-bar" id="control-bar">
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="search-input" placeholder="이론명, 학자명, 키워드 실시간 검색..." oninput="handleSearch()">
  </div>

  <div class="tool-group" id="top55-filters">
    <button class="tool-btn active-toggle" onclick="filterTop55('all', this)">전체 55개</button>
    <button class="tool-btn" onclick="filterTop55('pedagogy', this)">교육학 20선</button>
    <button class="tool-btn" onclick="filterTop55('counseling', this)">전공상담 35선</button>
  </div>
</div>

<div class="progress-wrap" id="progress-wrap">
  <div class="progress-bar-bg">
    <div class="progress-bar-fill" id="progress-fill"></div>
  </div>
  <div class="progress-text">
    <span id="progress-label">암기 완료: 0 / 55개 (0%)</span>
    <span>한국교육과정평가원(KICE) 7개년 정식 공인 키워드 100% 탑재</span>
  </div>
</div>

<main class="content-area">

  <!-- ==================== TAB 1: TOP 55 COMPACT DRILL ==================== -->
  <section class="tab-section active" id="sec-top55">
    <div class="notice-banner">
      <div>
        <h3>⚡ 2027 KICE 영구 동결 55개 핵심 출제 풀 스피드 마스터</h3>
        <p>기출 7개년 전수 분석 완료! 우측 상단 '키워드 가리기'를 켜고 능동적 인출(Active Recall) 훈련을 진행하세요.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--gold); font-weight: 700;">
        교육학 20선 + 전공상담 35선 = 총 55개
      </div>
    </div>

    <div class="card-grid" id="top55-grid">
      <!-- Generated by JS -->
    </div>
  </section>

  <!-- ==================== TAB 2: PEDAGOGY ESSAY ==================== -->
  <section class="tab-section" id="sec-pedagogy">
    <div class="notice-banner">
      <div>
        <h3>🎓 1교시 교육학 논술 모의고사 [총점 20점 만점 / 16개 세부 소문항 규격]</h3>
        <p>2026 소진 이론 완전 배제! 2027 0순위 4대 영역(교육과정·교육방법·교육평가·교육행정) 16개 세부 발문 실전 시험지</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--sky); font-weight: 700;">
        시험 시간: 60분 (B4 답안지 1페이지)
      </div>
    </div>

    <div class="exam-full-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <h2 style="font-size:1.15rem; color:#fff;" id="ped-title"></h2>
        <span class="badge badge-score">20점 만점</span>
      </div>
      
      <div class="exam-case-box" id="ped-case"></div>

      <div class="exam-instructions">
        <strong>&lt;작성 방법 및 채점 지침&gt;</strong>
        <ul>
          <li>논술의 내용: 교육과정(4점), 교육방법(4점), 교육평가(4점), 교육행정(4점) 총 16점</li>
          <li>논술의 구성 및 표현: 논술의 체계(서론·본론·결론 결속성) 및 분량·맞춤법 4점</li>
          <li>반드시 KICE 공인 용어로 서술하고, B4 답안지 기준 1줄당 38~45자 규격을 준수할 것.</li>
        </ul>
      </div>

      <div id="ped-domain-cards">
        <!-- Rendered by JS -->
      </div>
    </div>
  </section>

  <!-- ==================== TAB 3: SPECIALTY A ==================== -->
  <section class="tab-section" id="sec-qa">
    <div class="notice-banner">
      <div>
        <h3>📘 2교시 전공상담 A형 실전 모의고사 [12문항 / 40점 만점]</h3>
        <p>기입형 1~4번 (각 2점) + 서술형 5~12번 (각 4점). 답안을 입력하면 하단에 KICE 4점 만점 모범답안이 즉시 열립니다.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--purple); font-weight: 700;">
        시험 시간: 90분
      </div>
    </div>

    <div class="quick-nav" id="quick-nav-a"></div>
    <div id="qa-container"></div>
  </section>

  <!-- ==================== TAB 4: SPECIALTY B ==================== -->
  <section class="tab-section" id="sec-qb">
    <div class="notice-banner">
      <div>
        <h3>📙 3교시 전공상담 B형 실전 모의고사 [11문항 / 40점 만점]</h3>
        <p>기입형 1~2번 (각 2점) + 서술형 3~11번 (각 4점). 80% 이상 복합형 킬러 문항으로 구성되었습니다.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--gold); font-weight: 700;">
        시험 시간: 90분
      </div>
    </div>

    <div class="quick-nav" id="quick-nav-b"></div>
    <div id="qb-container"></div>
  </section>

</main>

<script>
const rawData = ''' + json_str + ''';

// State
let currentTab = 'top55';
let blindMode = false;
let currentFilter = 'all';
let searchQuery = '';
let timeLeft = 60 * 60;
let timerRunning = false;
let timerInterval = null;

// Initialize
window.addEventListener('DOMContentLoaded', () => {
  renderTop55();
  renderPedagogy();
  renderExamQuestions('A');
  renderExamQuestions('B');
  updateProgress();
  loadAllSavedAnswers();
  updateTimerDisplay();
});

// Tab Switcher
function switchTab(tab) {
  currentTab = tab;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
  
  document.getElementById(	ab-btn-).classList.add('active');
  document.getElementById(sec-).classList.add('active');

  const top55Filters = document.getElementById('top55-filters');
  const progressWrap = document.getElementById('progress-wrap');
  if (tab === 'top55') {
    top55Filters.style.display = 'flex';
    progressWrap.style.display = 'block';
  } else {
    top55Filters.style.display = 'none';
    progressWrap.style.display = 'none';
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Blind Mode Toggle
function toggleBlindMode() {
  blindMode = !blindMode;
  document.body.classList.toggle('blind-mode', blindMode);
  const btn = document.getElementById('blind-toggle-btn');
  const label = document.getElementById('blind-label');
  if (blindMode) {
    btn.classList.add('active-toggle');
    label.innerText = '키워드 공개하기';
  } else {
    btn.classList.remove('active-toggle');
    label.innerText = '키워드 가리기';
  }
}

// Render Top55 Cards
function renderTop55() {
  const container = document.getElementById('top55-grid');
  container.innerHTML = '';

  const filtered = rawData.top55.filter(item => {
    const matchFilter = (currentFilter === 'all') || 
                        (currentFilter === 'pedagogy' && item.type === 'pedagogy') ||
                        (currentFilter === 'counseling' && item.type !== 'pedagogy');
    
    const q = searchQuery.toLowerCase();
    const matchSearch = !q || 
                        item.question.toLowerCase().includes(q) ||
                        item.raw_keywords.toLowerCase().includes(q) ||
                        item.answer.toLowerCase().includes(q) ||
                        item.code.toLowerCase().includes(q);

    return matchFilter && matchSearch;
  });

  filtered.forEach(item => {
    const isMemorized = localStorage.getItem(	op55_chk_) === 'true';
    const card = document.createElement('div');
    card.className = item-card ;
    card.id = 	op55-card-;

    const kwTags = item.keywords.map(kw => <span class="kw-tag" onclick="this.classList.toggle('revealed')"></span>).join('');

    card.innerHTML = 
      <div class="card-top">
        <div class="badge-group">
          <span class="badge badge-code"></span>
          <span class="badge "></span>
        </div>
        <label class="memorize-chk">
          <input type="checkbox"  onchange="toggleMemorized('', this.checked)">
          외웠어요
        </label>
      </div>

      <div class="card-question"></div>

      <div class="keyword-tags">
        
      </div>

      <div class="compact-answer-box"></div>
    ;
    container.appendChild(card);
  });
}

function filterTop55(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll('#top55-filters .tool-btn').forEach(b => b.classList.remove('active-toggle'));
  btn.classList.add('active-toggle');
  renderTop55();
}

function handleSearch() {
  searchQuery = document.getElementById('search-input').value.trim();
  renderTop55();
}

function toggleMemorized(code, checked) {
  localStorage.setItem(	op55_chk_, checked);
  const card = document.getElementById(	op55-card-);
  if (card) {
    card.classList.toggle('memorized', checked);
  }
  updateProgress();
}

function updateProgress() {
  const total = rawData.top55.length;
  let count = 0;
  rawData.top55.forEach(i => {
    if (localStorage.getItem(	op55_chk_) === 'true') count++;
  });
  const pct = Math.round((count / total) * 100);
  document.getElementById('progress-fill').style.width = ${pct}%;
  document.getElementById('progress-label').innerText = 암기 완료:  / 개 (%);
}

// Render Pedagogy Essay
function renderPedagogy() {
  const ped = rawData.pedagogy;
  document.getElementById('ped-title').innerText = ped.title;
  document.getElementById('ped-case').innerText = ped.case;

  const container = document.getElementById('ped-domain-cards');
  container.innerHTML = '';

  ped.domains.forEach(d => {
    const card = document.createElement('div');
    card.style.background = '#111827';
    card.style.border = '1px solid #1f2937';
    card.style.borderRadius = '10px';
    card.style.padding = '18px';
    card.style.marginTop = '16px';

    const subQList = d.sub_questions.map(q => <li style="margin-bottom:6px;"></li>).join('');
    const kwBadges = d.keywords.map(kw => <span class="kw-tag"></span>).join('');
    const compactLines = d.compact_answers.join('\n');
    const rubricItems = d.rubric.map(r => <div class="rubric-item"><span>✓</span><span></span></div>).join('');

    card.innerHTML = 
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="badge badge-pedagogy" style="font-size:0.85rem;"> 영역</span>
          <strong style="color:#fff; font-size:1rem;"></strong>
        </div>
        <span class="badge badge-score">점</span>
      </div>

      <div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:12px 16px; font-size:0.88rem; color:#e2e8f0; margin-bottom:12px;">
        <strong style="color:var(--sky);">[세부 질문 4개]</strong>
        <ol style="margin-left:18px; margin-top:6px;">
          
        </ol>
      </div>

      <div class="keyword-tags" style="margin-bottom:12px;">
        
      </div>

      <div class="answer-box-wrap">
        <div class="answer-box-header">
          <span>✍️ B4 실전 답안 작성란 (작성 시 하단에 모범답안이 열립니다)</span>
          <span class="char-count-badge" id="ped-counter-">0자</span>
        </div>
        <textarea 
          class="exam-textarea" 
          id="ped-input-" 
          placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)"
          oninput="handlePedInput('')"
        ></textarea>

        <div class="model-answer-panel" id="ped-ans-">
          <div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>
          <div class="model-answer-text"></div>
          <div class="rubric-list">
            <strong>[KICE 4점 채점표]</strong>
            
          </div>
        </div>
      </div>
    ;
    container.appendChild(card);
  });
}

function handlePedInput(domainId) {
  const txt = document.getElementById(ped-input-);
  const counter = document.getElementById(ped-counter-);
  const ansPanel = document.getElementById(ped-ans-);
  
  const val = txt.value;
  counter.innerText = ${val.length}자;
  if (val.length > 0) {
    ansPanel.classList.add('show');
    localStorage.setItem(kice_ped_, val);
  } else {
    ansPanel.classList.remove('show');
    localStorage.removeItem(kice_ped_);
  }
}

// Render Specialty Questions (A & B)
function renderExamQuestions(type) {
  const container = document.getElementById(q-container);
  const navContainer = document.getElementById(quick-nav-);
  const questions = (type === 'A') ? rawData.questions_a : rawData.questions_b;

  container.innerHTML = '';
  navContainer.innerHTML = '';

  questions.forEach(q => {
    // Quick Nav button
    const navBtn = document.createElement('button');
    navBtn.className = 'quick-nav-btn';
    navBtn.id = 
av-btn--;
    navBtn.innerText = ${q.num}번;
    navBtn.onclick = () => {
      document.getElementById(exam-card--).scrollIntoView({ behavior: 'smooth' });
    };
    navContainer.appendChild(navBtn);

    // Full Card
    const card = document.createElement('div');
    card.className = 'exam-full-card';
    card.id = exam-card--;

    let instHtml = '';
    if (q.instructions && q.instructions.trim()) {
      instHtml = <div class="exam-instructions"></div>;
    }

    card.innerHTML = 
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="badge " style="font-size:0.85rem;">[형 번]</span>
          <span class="badge "></span>
          <strong style="color:#fff; font-size:1.05rem;"></strong>
        </div>
        <span class="badge badge-score">점</span>
      </div>

      <div class="exam-case-box"></div>
      

      <div class="answer-box-wrap">
        <div class="answer-box-header">
          <span>✍️ B4 실전 답안 작성란 (첫 글자 입력 시 아래에 정답이 즉시 나타납니다)</span>
          <span class="char-count-badge" id="counter--">0자</span>
        </div>
        <textarea 
          class="exam-textarea" 
          id="input--" 
          placeholder="여기에 답안을 직접 입력하세요. 줄당 38~45자 규격 준수 권장."
          oninput="handleExamInput('', )"
        ></textarea>

        <div class="model-answer-panel" id="ansbox--">
          <div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>
          <div class="model-answer-text"></div>
        </div>
      </div>
    ;
    container.appendChild(card);
  });
}

function handleExamInput(type, num) {
  const textarea = document.getElementById(input--);
  const ansBox = document.getElementById(nsbox--);
  const counter = document.getElementById(counter--);
  const navBtn = document.getElementById(
av-btn--);

  const val = textarea.value;
  counter.innerText = ${val.length}자;

  if (val.trim().length > 0) {
    ansBox.classList.add('show');
    if (navBtn) navBtn.classList.add('written');
    localStorage.setItem(kice_ans__, val);
  } else {
    ansBox.classList.remove('show');
    if (navBtn) navBtn.classList.remove('written');
    localStorage.removeItem(kice_ans__);
  }
}

// Load Saved Answers
function loadAllSavedAnswers() {
  // Pedagogy
  rawData.pedagogy.domains.forEach(d => {
    const saved = localStorage.getItem(kice_ped_);
    if (saved) {
      const txt = document.getElementById(ped-input-);
      if (txt) {
        txt.value = saved;
        handlePedInput(d.id);
      }
    }
  });

  // A and B
  ['A', 'B'].forEach(type => {
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    list.forEach(q => {
      const saved = localStorage.getItem(kice_ans__);
      if (saved) {
        const txt = document.getElementById(input--);
        if (txt) {
          txt.value = saved;
          handleExamInput(type, q.num);
        }
      }
    });
  });
}

// Timer Functions
function updateTimerDisplay() {
  const m = Math.floor(timeLeft / 60);
  const s = timeLeft % 60;
  const disp = ${String(m).padStart(2, '0')}:;
  const clock = document.getElementById('timer-display');
  clock.innerText = disp;
  if (timeLeft <= 300) {
    clock.style.color = 'var(--rose)';
  } else {
    clock.style.color = 'var(--gold)';
  }
}

function toggleTimer() {
  if (timerRunning) {
    clearInterval(timerInterval);
    timerRunning = false;
    document.getElementById('timer-btn').innerText = '재개';
  } else {
    timerRunning = true;
    document.getElementById('timer-btn').innerText = '일시정지';
    timerInterval = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        alert('시험 시간이 종료되었습니다!');
      }
    }, 1000);
  }
}

function resetTimer(mins) {
  clearInterval(timerInterval);
  timerRunning = false;
  timeLeft = mins * 60;
  updateTimerDisplay();
  document.getElementById('timer-btn').innerText = '시작';
}

// Export Answers to Clipboard
function exportAnswers() {
  let text = '=== [2027 KICE 임용고시 작성 답안 모음] ===\\n\\n';
  
  text += '--- [1교시 교육학 논술] ---\\n';
  rawData.pedagogy.domains.forEach(d => {
    const ans = localStorage.getItem(kice_ped_) || '(미작성)';
    text += [ 영역 ()]:\\n\\n\\n;
  });

  ['A', 'B'].forEach(type => {
    text += \\n--- [전공 형] ---\\n;
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    list.forEach(q => {
      const ans = localStorage.getItem(kice_ans__) || '(미작성)';
      text += [번 ( 점)]\\n\\n\\n;
    });
  });

  navigator.clipboard.writeText(text).then(() => {
    alert('작성하신 모든 답안이 클립보드에 복사되었습니다! 메모장이나 한글 파일에 붙여넣기 하실 수 있습니다.');
  }).catch(() => {
    alert('클립보드 복사에 실패했습니다. 권한을 확인해주세요.');
  });
}
</script>
</body>
</html>
'''

# Write to both target paths
target_paths = [
    r"G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\exam_master_2027.html",
    r"G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\exam_master_2027.html"
]

for p in target_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated: {p} ({len(html_content):,} bytes)")

print("ALL TARGET FILES GENERATED SUCCESSFULLY!")
