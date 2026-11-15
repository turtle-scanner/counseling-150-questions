const fs = require('fs');
const path = require('path');
const vm = require('vm');

// Read current build_master.js
let code = fs.readFileSync('build_master.js', 'utf8');

// 1. Ensure vm is required
if (!code.includes("const vm = require('vm');")) {
  code = "const vm = require('vm');\n" + code;
}

// 2. Define comprehensive English cleaner in build_master.js right after loading questionsA & questionsB
const cleanerDef = `
function cleanEnglishFullNames(text) {
  if (!text) return text;
  let res = text
    .replace(/역설적 지시\\(Paradoxical Injunction \\/ 증상 처방\\)/g, '역설적 지시(증상 처방)')
    .replace(/역설적 지시\\(Paradoxical Injunction\\)/g, '역설적 지시(증상 처방)')
    .replace(/자극추구\\(Novelty Seeking, NS\\)/g, '자극추구(NS)')
    .replace(/위험회피\\(Harm Avoidance, HA\\)/g, '위험회피(HA)')
    .replace(/보상의존\\(Reward Dependence, RD\\)/g, '보상의존(RD)')
    .replace(/인내력\\(Persistence, P\\)/g, '인내력(P)')
    .replace(/자율성\\(Self-Directedness, SD\\)/g, '자율성(SD)')
    .replace(/협동성\\(Cooperativeness, CO\\)/g, '협동성(CO)')
    .replace(/자기초월\\(Self-Transcendence, ST\\)/g, '자기초월(ST)')
    .replace(/탈숙고\\(Dereflection\\)/g, '탈숙고')
    .replace(/과잉주의\\(Hyperreflection\\)/g, '과잉주의')
    .replace(/명확한 경계선\\(Clear boundary\\)/g, '명확한 경계선')
    .replace(/실연\\(Enactment\\)/g, '실연')
    .replace(/반전\\(Retroflection\\)/g, '반전')
    .replace(/빈 의자 기법\\(Empty Chair Technique\\)/g, '빈 의자 기법')
    .replace(/생애 주제\\(Life Theme\\)/g, '생애 주제')
    .replace(/진로적응도\\(Career Adaptability\\)/g, '진로적응도')
    .replace(/토막짜기\\(Block Design\\)/g, '토막짜기')
    .replace(/시각퍼즐\\(Visual Puzzles\\)/g, '시각퍼즐')
    .replace(/행렬추론\\(Matrix Reasoning\\)/g, '행렬추론')
    .replace(/무게비교\\(Figure Weights\\)/g, '무게비교')
    .replace(/미세공격\\(Microaggression\\)/g, '미세공격')
    .replace(/계측성\\(Calculus\\)/g, '계측성')
    .replace(/일관성\\(Consistency\\)/g, '일관성')
    .replace(/동일시\\(Identification\\)/g, '동일시')
    .replace(/좋은-나\\(Good-me\\)/g, '좋은-나')
    .replace(/나쁜-나\\(Bad-me\\)/g, '나쁜-나')
    .replace(/나-아님\\(Not-me\\)/g, '나-아님')
    .replace(/교사\\(Teacher\\)/g, '교사')
    .replace(/상담자\\(Counselor\\)/g, '상담자')
    .replace(/자문가\\(Consultant\\)/g, '자문가')
    .replace(/신체증상장애\\(Somatic Symptom Disorder\\)/g, '신체증상장애')
    .replace(/질병불안장애\\(Illness Anxiety Disorder\\)/g, '질병불안장애')
    .replace(/사회적\\(실용적\\) 의사소통장애\\(Social Communication Disorder\\)/g, '사회적(실용적) 의사소통장애')
    .replace(/자폐스펙트럼장애\\(Autism Spectrum Disorder\\)/g, '자폐스펙트럼장애')
    .replace(/광장공포증\\(Agoraphobia\\)/g, '광장공포증')
    .replace(/파국적 오해석\\(Catastrophic Misinterpretation\\)/g, '파국적 오해석')
    .replace(/내부감각 노출\\(Interoceptive Exposure\\)/g, '내부감각 노출')
    .replace(/참여자적 관찰자\\(Participant Observer\\)/g, '참여자적 관찰자')
    .replace(/자아동질적\\(Ego-syntonic\\)/g, '자아동질적')
    .replace(/자아이질적\\(Ego-dystonic\\)/g, '자아이질적')
    .replace(/기질\\(Temperament\\)/g, '기질')
    .replace(/성격\\(Character\\)/g, '성격')
    .replace(/과부하\\(Overload\\)/g, '과부하')
    .replace(/외향반응성\\(Extratensive\\)/g, '외향반응성')
    .replace(/제한\\(Circumscription\\)/g, '제한')
    .replace(/타협\\(Compromise\\)/g, '타협')
    .replace(/성역할 발달\\(Sex-Role Orientation\\)/g, '성역할 발달')
    .replace(/성역할 경계선\\(Sex-Role Orientation\\)/g, '성역할 경계선')
    .replace(/핵심신념\\(Core Belief\\)/g, '핵심신념')
    .replace(/하향화살표 기법\\(Downward Arrow Technique\\)/g, '하향화살표 기법')
    .replace(/삼각관계\\(Triangulation\\)/g, '삼각관계')
    .replace(/탈삼각화\\(Detriangulation\\)/g, '탈삼각화')
    .replace(/로샤\\(Rorschach\\)/g, '로샤')
    .replace(/사비카스\\(Savickas\\)/g, '사비카스')
    .replace(/길리랜드\\(Gilliland\\)/g, '길리랜드')
    .replace(/숀 셰이\\(Shawn Shea\\)/g, '숀 셰이')
    .replace(/욕구\\(Need\\)/g, '욕구')
    .replace(/압착\\(Press\\)/g, '압착')
    .replace(/주제\\(Thema\\)/g, '주제')
    .replace(/관심\\(Concern\\)/g, '관심')
    .replace(/통제\\(Control\\)/g, '통제')
    .replace(/호기심\\(Curiosity\\)/g, '호기심')
    .replace(/자신감\\(Confidence\\)/g, '자신감')
    .replace(/지지 제공\\(Providing Support\\)/g, '지지 제공')
    .replace(/다짐 받기\\(Obtaining Commitment\\)/g, '다짐 받기');

  const termsToRemove = [
    'Dereflection', 'Hyperreflection', 'Paradoxical Injunction', 'Clear boundary',
    'Enactment', 'Retroflection', 'Empty Chair Technique', 'Life Theme',
    'Career Adaptability', 'Concern', 'Control', 'Curiosity', 'Confidence',
    'Providing Support', 'Obtaining Commitment', 'Block Design', 'Visual Puzzles',
    'Matrix Reasoning', 'Figure Weights', 'Microaggression', 'Calculus',
    'Consistency', 'Identification', 'Circumscription', 'Compromise',
    'Sex-Role Orientation', 'Core Belief', 'Downward Arrow Technique',
    'Triangulation', 'Detriangulation', 'Somatic Symptom Disorder',
    'Illness Anxiety Disorder', 'Social Communication Disorder',
    'Autism Spectrum Disorder', 'Agoraphobia', 'Catastrophic Misinterpretation',
    'Interoceptive Exposure', 'Participant Observer', 'Ego-syntonic',
    'Ego-dystonic', 'Temperament', 'Character', 'Overload', 'Extratensive',
    'Rorschach', 'Savickas', 'Gilliland', 'Shawn Shea', 'Need', 'Press',
    'Thema', 'Not-me', 'Good-me', 'Bad-me', 'Teacher', 'Counselor', 'Consultant',
    'Chronological Assessment of Suicide Events'
  ];

  termsToRemove.forEach(t => {
    res = res.split(' (' + t + ')').join('').split('(' + t + ')').join('');
  });

  return res;
}

questionsA.forEach(q => {
  q.title = cleanEnglishFullNames(q.title);
  q.content = cleanEnglishFullNames(q.content);
  q.instructions = cleanEnglishFullNames(q.instructions);
  q.answer = cleanEnglishFullNames(q.answer);
});

questionsB.forEach(q => {
  q.title = cleanEnglishFullNames(q.title);
  q.content = cleanEnglishFullNames(q.content);
  q.instructions = cleanEnglishFullNames(q.instructions);
  q.answer = cleanEnglishFullNames(q.answer);
});
`;

// Insert cleaner definition if not present
if (!code.includes('function cleanEnglishFullNames(')) {
  const insertTarget = 'const questionsB = JSON.parse(matchB[1]);';
  code = code.replace(insertTarget, insertTarget + '\n' + cleanerDef);
}

// 3. Compact CSS
const cssTarget = '/* Exam Mode Simulation Cards */';
const cssEndTarget = '/* Quick Nav Bar */';

const newCompactCss = `/* Exam Mode Simulation Cards */
.exam-full-card {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  padding: 14px 18px;
  margin-bottom: 14px;
}
.exam-split-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
  align-items: start;
}
@media (min-width: 960px) {
  .exam-split-grid {
    grid-template-columns: 1.15fr 1fr;
  }
}
.exam-left-col {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.exam-right-col {
  display: flex;
  flex-direction: column;
}
.exam-case-box {
  background: #0c1320;
  border: 1px solid #23324a;
  border-left: 3px solid var(--sky);
  border-radius: 8px;
  padding: 10px 14px;
  margin: 0;
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.88rem;
  line-height: 1.58;
  color: #e2e8f0;
  white-space: pre-wrap;
  max-height: 260px;
  overflow-y: auto;
}
.exam-instructions {
  background: rgba(245, 158, 11, 0.06);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 8px 12px;
  margin: 0;
  font-size: 0.82rem;
  color: #fde68a;
  line-height: 1.5;
}
.exam-instructions ul {
  margin-left: 16px;
  margin-top: 4px;
}

/* Line-note styled textarea */
.answer-box-wrap {
  margin-top: 0;
}
.answer-box-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
  font-size: 0.78rem;
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
  height: 76px;
  min-height: 76px;
  background: var(--bg-input);
  background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 100% 24px;
  line-height: 24px;
  border: 1px solid var(--border-card);
  border-radius: 8px;
  color: #fff;
  padding: 6px 12px;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 0.88rem;
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
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 10px 14px;
  margin-top: 8px;
  max-height: 280px;
  overflow-y: auto;
  animation: fadeIn 0.25s ease;
}
.model-answer-panel.show {
  display: block;
}
.model-answer-title {
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--gold);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.model-answer-text {
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.85rem;
  line-height: 1.52;
  color: #e2e8f0;
  white-space: pre-wrap;
}
.rubric-list {
  margin-top: 6px;
  padding-top: 6px;
  border-top: 1px dashed #233852;
  font-size: 0.78rem;
  color: var(--text-sub);
}
.rubric-item {
  margin-bottom: 3px;
  display: flex;
  align-items: flex-start;
  gap: 6px;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-3px); }
  to { opacity: 1; transform: translateY(0); }
}

`;

const idxCssStart = code.indexOf(cssTarget);
const idxCssEnd = code.indexOf(cssEndTarget, idxCssStart);
if (idxCssStart !== -1 && idxCssEnd !== -1) {
  code = code.slice(0, idxCssStart) + newCompactCss + code.slice(idxCssEnd);
}

// 4. Replace renderPedagogy function implementation
const pedFuncStart = 'function renderPedagogy() {';
const pedFuncEnd = 'function handlePedInput(domainId) {';

const idxPedStart = code.indexOf(pedFuncStart);
const idxPedEnd = code.indexOf(pedFuncEnd, idxPedStart);

const newRenderPedagogy = `function renderPedagogy() {
  const ped = rawData.pedagogy;
  if (!ped || !ped.domains) return;

  const container = document.getElementById('ped-domain-cards');
  if (!container) return;
  container.innerHTML = '';

  ped.domains.forEach(d => {
    const card = document.createElement('div');
    card.className = 'exam-full-card';
    card.id = 'ped-card-' + d.id;

    const subQList = d.sub_questions.map(q => '<li style="margin-bottom:4px;">' + q + '</li>').join('');
    const kwBadges = d.keywords.map(kw => '<span class="kw-tag">' + kw + '</span>').join('');
    const compactLines = d.compact_answers.join('\\n');
    const rubricItems = d.rubric.map(r => '<div class="rubric-item"><span>✓</span><span>' + r + '</span></div>').join('');

    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge badge-pedagogy" style="font-size:0.78rem;">' + d.name + ' 영역</span>' +
          '<strong style="color:#fff; font-size:0.92rem;">' + d.theory + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + d.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:10px 14px; font-size:0.84rem; color:#e2e8f0; max-height:260px; overflow-y:auto;">' +
            '<strong style="color:var(--sky); font-size:0.82rem;">[세부 질문 4개]</strong>' +
            '<ol style="margin-left:16px; margin-top:4px; line-height:1.5;">' + subQList + '</ol>' +
          '</div>' +
          '<div class="keyword-tags" style="margin-top:4px;">' + kwBadges + '</div>' +
        '</div>' +
        '<div class="exam-right-col">' +
          '<div class="answer-box-wrap">' +
            '<div class="answer-box-header">' +
              '<span>✍️ B4 실전 답안 작성란 (작성 시 모범답안 즉시 표시)</span>' +
              '<span class="char-count-badge" id="ped-counter-' + d.id + '">0자</span>' +
            '</div>' +
            '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)"></textarea>' +
            '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +
              '<div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + compactLines + '</div>' +
              '<div class="rubric-list">' +
                '<strong>[KICE 4점 채점표]</strong>' + rubricItems +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    container.appendChild(card);

    // Event listener for input
    const ta = card.querySelector('#ped-input-' + d.id);
    if (ta) {
      ta.addEventListener('input', () => handlePedInput(d.id));
    }
  });
}

`;

if (idxPedStart !== -1 && idxPedEnd !== -1) {
  code = code.slice(0, idxPedStart) + newRenderPedagogy + code.slice(idxPedEnd);
}

// 5. Replace renderExamQuestions function implementation
const examFuncStart = 'function renderExamQuestions(type) {';
const examFuncEnd = 'function handleExamInput(type, num) {';

const idxExamStart = code.indexOf(examFuncStart);
const idxExamEnd = code.indexOf(examFuncEnd, idxExamStart);

const newRenderExamQuestions = `function renderExamQuestions(type) {
  const container = document.getElementById('q' + type.toLowerCase() + '-container');
  const navContainer = document.getElementById('quick-nav-' + type.toLowerCase());
  const questions = (type === 'A') ? rawData.questions_a : rawData.questions_b;

  if (!container || !navContainer) return;
  container.innerHTML = '';
  navContainer.innerHTML = '';

  questions.forEach(q => {
    // Nav Button
    const navBtn = document.createElement('button');
    navBtn.className = 'quick-nav-btn';
    navBtn.id = 'nav-btn-' + type + '-' + q.num;
    navBtn.innerText = q.num + '번';
    navBtn.onclick = () => {
      const el = document.getElementById('exam-card-' + type + '-' + q.num);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    };
    navContainer.appendChild(navBtn);

    // Question Card
    const card = document.createElement('div');
    card.className = 'exam-full-card';
    card.id = 'exam-card-' + type + '-' + q.num;

    let instHtml = '';
    if (q.instructions && q.instructions.trim()) {
      const parts = q.instructions.split('○').map(p => p.trim()).filter(Boolean);
      let contentHtml = '<strong style="color:var(--gold); display:block; margin-bottom:6px; font-size:0.82rem;">&lt;작성 방법&gt;</strong>';
      parts.forEach(p => {
        if (!p.includes('<작성 방법>')) {
          contentHtml += '<div style="margin-bottom:6px; line-height:1.5;">○ ' + p + '</div>';
        }
      });
      instHtml = '<div class="exam-instructions">' + contentHtml + '</div>';
    }

    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge ' + (type === 'A' ? 'badge-category' : 'badge-code') + '" style="font-size:0.78rem;">[' + type + '형 ' + q.num + '번]</span>' +
          '<span class="badge ' + (q.type === '기입형' ? 'badge-pedagogy' : 'badge-score') + '" style="font-size:0.75rem;">' + q.type + '</span>' +
          '<strong style="color:#fff; font-size:0.92rem;">' + q.title + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + q.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div class="exam-case-box">' + q.content + '</div>' +
          instHtml +
        '</div>' +
        '<div class="exam-right-col">' +
          '<div class="answer-box-wrap">' +
            '<div class="answer-box-header">' +
              '<span>✍️ B4 실전 답안 작성란 (입력 시 모범답안 즉시 표시)</span>' +
              '<span class="char-count-badge" id="counter-' + type + '-' + q.num + '">0자</span>' +
            '</div>' +
            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)"></textarea>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
              '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + q.answer + '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    container.appendChild(card);

    // Event listener for input
    const ta = card.querySelector('#input-' + type + '-' + q.num);
    if (ta) {
      ta.addEventListener('input', () => handleExamInput(type, q.num));
    }
  });
}

`;

if (idxExamStart !== -1 && idxExamEnd !== -1) {
  code = code.slice(0, idxExamStart) + newRenderExamQuestions + code.slice(idxExamEnd);
}

// 6. Ensure syntax validation uses vm.Script
const oldValMatch = /const scriptMatch = htmlTemplate\.match\(\/<script>([\s\S]*?)<\/script>\);[\s\S]*?process\.exit\(1\);\s*\}\s*\}/;
const newValReplacement = `const scriptMatch = htmlTemplate.match(/<script>([\\s\\S]*?)<\\/script>/);
if (scriptMatch) {
  try {
    new vm.Script(scriptMatch[1]);
    console.log('✅ JAVASCRIPT SYNTAX VALIDATED PERFECTLY! Zero errors!');
  } catch (err) {
    console.error('❌ JS Syntax Error detected:', err);
    process.exit(1);
  }
}`;

code = code.replace(oldValMatch, newValReplacement);

fs.writeFileSync('build_master.js', code, 'utf8');
console.log('🚀 build_master.js updated with compact 2-split layout and robust listeners!');
