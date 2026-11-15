const fs = require('fs');

let code = fs.readFileSync('build_master.js', 'utf8');

// 1. Update CSS
const cssSearch = '/* Exam Mode Simulation Cards */';
const idxCss = code.indexOf(cssSearch);
const endCss = code.indexOf('/* Quick Nav Bar */', idxCss);

const newCss = `/* Exam Mode Simulation Cards */
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
  font-size: 0.9rem;
  line-height: 1.6;
  color: #e2e8f0;
  white-space: pre-wrap;
  max-height: 300px;
  overflow-y: auto;
}
.exam-instructions {
  background: rgba(245, 158, 11, 0.06);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 8px 12px;
  margin: 0;
  font-size: 0.85rem;
  color: #fde68a;
  line-height: 1.6;
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
  font-size: 0.86rem;
  line-height: 1.55;
  color: #e2e8f0;
  white-space: pre-wrap;
}
.rubric-list {
  margin-top: 8px;
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

if (idxCss !== -1 && endCss !== -1) {
  code = code.slice(0, idxCss) + newCss + code.slice(endCss);
  console.log('✅ CSS updated to compact split grid');
} else {
  console.error('CSS boundaries not found');
}

// 2. Update renderExamQuestions card template
const oldCardCreation = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">' +
        '<div style="display:flex; align-items:center; gap:8px;">' +
          '<span class="badge ' + (type === 'A' ? 'badge-category' : 'badge-code') + '" style="font-size:0.85rem;">[' + type + '형 ' + q.num + '번]</span>' +
          '<span class="badge ' + (q.type === '기입형' ? 'badge-pedagogy' : 'badge-score') + '">' + q.type + '</span>' +
          '<strong style="color:#fff; font-size:1.05rem;">' + q.title + '</strong>' +
        '</div>' +
        '<span class="badge badge-score">' + q.score + '점</span>' +
      '</div>' +
      '<div class="exam-case-box">' + q.content + '</div>' +
      instHtml +
      '<div class="answer-box-wrap">' +
        '<div class="answer-box-header">' +
          '<span>✍️ B4 실전 답안 작성란 (첫 글자 입력 시 아래에 정답이 즉시 나타납니다)</span>' +
          '<span class="char-count-badge" id="counter-' + type + '-' + q.num + '">0자</span>' +
        '</div>' +
        '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. 줄당 38~45자 규격 준수 권장." oninput="handleExamInput(\\'' + type + '\\', ' + q.num + ')"></textarea>' +
        '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
          '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
          '<div class="model-answer-text">' + q.answer + '</div>' +
        '</div>' +
      '</div>';`;

const newCardCreation = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge ' + (type === 'A' ? 'badge-category' : 'badge-code') + '" style="font-size:0.8rem;">[' + type + '형 ' + q.num + '번]</span>' +
          '<span class="badge ' + (q.type === '기입형' ? 'badge-pedagogy' : 'badge-score') + '" style="font-size:0.75rem;">' + q.type + '</span>' +
          '<strong style="color:#fff; font-size:0.95rem;">' + q.title + '</strong>' +
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
            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)" oninput="handleExamInput(\\'' + type + '\\', ' + q.num + ')"></textarea>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
              '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + q.answer + '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';`;

if (code.includes(oldCardCreation)) {
  code = code.replace(oldCardCreation, newCardCreation);
  console.log('✅ renderExamQuestions updated to 2-column split grid');
} else {
  console.error('oldCardCreation pattern not matched');
}

// 3. Update renderPedagogy card template as well
const oldPedCard = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">' +
        '<div style="display:flex; align-items:center; gap:8px;">' +
          '<span class="badge badge-pedagogy" style="font-size:0.85rem;">' + d.name + ' 영역</span>' +
          '<strong style="color:#fff; font-size:1rem;">' + d.theory + '</strong>' +
        '</div>' +
        '<span class="badge badge-score">' + d.score + '점</span>' +
      '</div>' +
      '<div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:12px 16px; font-size:0.88rem; color:#e2e8f0; margin-bottom:12px;">' +
        '<strong style="color:var(--sky);">[세부 질문 4개]</strong>' +
        '<ol style="margin-left:18px; margin-top:6px;">' + subQList + '</ol>' +
      '</div>' +
      '<div class="keyword-tags" style="margin-bottom:12px;">' + kwBadges + '</div>' +
      '<div class="answer-box-wrap">' +
        '<div class="answer-box-header">' +
          '<span>✍️ B4 실전 답안 작성란 (작성 시 하단에 모범답안이 열립니다)</span>' +
          '<span class="char-count-badge" id="ped-counter-' + d.id + '">0자</span>' +
        '</div>' +
        '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)" oninput="handlePedInput(\\'' + d.id + '\\')"></textarea>' +
        '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +
          '<div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>' +
          '<div class="model-answer-text">' + compactLines + '</div>' +
          '<div class="rubric-list">' +
            '<strong>[KICE 4점 채점표]</strong>' + rubricItems +
          '</div>' +
        '</div>' +
      '</div>';`;

const newPedCard = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge badge-pedagogy" style="font-size:0.8rem;">' + d.name + ' 영역</span>' +
          '<strong style="color:#fff; font-size:0.95rem;">' + d.theory + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + d.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:10px 14px; font-size:0.85rem; color:#e2e8f0;">' +
            '<strong style="color:var(--sky);">[세부 질문 4개]</strong>' +
            '<ol style="margin-left:16px; margin-top:4px;">' + subQList + '</ol>' +
          '</div>' +
          '<div class="keyword-tags">' + kwBadges + '</div>' +
        '</div>' +
        '<div class="exam-right-col">' +
          '<div class="answer-box-wrap">' +
            '<div class="answer-box-header">' +
              '<span>✍️ B4 실전 답안 작성란 (작성 시 모범답안 자동 표시)</span>' +
              '<span class="char-count-badge" id="ped-counter-' + d.id + '">0자</span>' +
            '</div>' +
            '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)" oninput="handlePedInput(\\'' + d.id + '\\')"></textarea>' +
            '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +
              '<div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + compactLines + '</div>' +
              '<div class="rubric-list">' +
                '<strong>[KICE 4점 채점표]</strong>' + rubricItems +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';`;

if (code.includes(oldPedCard)) {
  code = code.replace(oldPedCard, newPedCard);
  console.log('✅ renderPedagogy updated to 2-column split grid');
} else {
  console.error('oldPedCard pattern not matched');
}

fs.writeFileSync('build_master.js', code, 'utf8');
console.log('build_master.js successfully updated for compact 1-screen layout!');
