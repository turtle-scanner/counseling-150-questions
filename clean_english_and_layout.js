const fs = require('fs');

// 1. Function to clean English full names while keeping acronyms
function cleanEnglishFullNames(text) {
  if (!text) return text;
  
  // List of full English terms to remove
  const fullTerms = [
    '\\(Dereflection\\)',
    '\\(Hyperreflection\\)',
    '\\(Paradoxical Injunction \\/ 증상 처방\\)',
    '\\(Paradoxical Injunction\\)',
    '\\(Clear boundary\\)',
    '\\(Enactment\\)',
    '\\(Retroflection\\)',
    '\\(Empty Chair Technique\\)',
    '\\(Life Theme\\)',
    '\\(Career Adaptability\\)',
    '\\(Providing Support\\)',
    '\\(Obtaining Commitment\\)',
    '\\(Need\\)',
    '\\(Press\\)',
    '\\(Calculus\\)',
    '\\(Consistency\\)',
    '\\(Persona\\)',
    '\\(Identification\\)',
    '\\(Good-me\\)',
    '\\(Bad-me\\)',
    '\\(Not-me\\)',
    '\\(Teacher\\)',
    '\\(Counselor\\)',
    '\\(Consultant\\)',
    '\\(Microaggression\\)',
    '\\(Block Design\\)',
    '\\(Visual Puzzles\\)',
    '\\(Matrix Reasoning\\)',
    '\\(Figure Weights\\)'
  ];

  let cleaned = text;
  // Specific replacement for Paradoxical Injunction
  cleaned = cleaned.replace(/역설적 지시\(Paradoxical Injunction \/ 증상 처방\)/g, '역설적 지시(증상 처방)');
  cleaned = cleaned.replace(/역설적 지시\(Paradoxical Injunction\)/g, '역설적 지시(증상 처방)');
  
  fullTerms.forEach(term => {
    const regex = new RegExp('\\s*' + term, 'g');
    cleaned = cleaned.replace(regex, '');
  });

  return cleaned;
}

// 2. Clean top55_extracted.json
const top55Path = '교육학/scratch/top55_extracted.json';
const top55Data = JSON.parse(fs.readFileSync(top55Path, 'utf8'));
top55Data.forEach(item => {
  item.question = cleanEnglishFullNames(item.question);
  item.answer = cleanEnglishFullNames(item.answer);
  item.clean_ans = cleanEnglishFullNames(item.clean_ans);
  item.keyword = cleanEnglishFullNames(item.keyword);
});
fs.writeFileSync(top55Path, JSON.stringify(top55Data, null, 2), 'utf8');
console.log('✅ top55 English full names cleaned');

// 3. Clean pedagogy_data.json
const pedPath = 'pedagogy_data.json';
const pedData = JSON.parse(fs.readFileSync(pedPath, 'utf8'));
pedData.domains.forEach(d => {
  d.theory = cleanEnglishFullNames(d.theory);
  d.sub_questions = d.sub_questions.map(cleanEnglishFullNames);
  d.compact_answers = d.compact_answers.map(cleanEnglishFullNames);
  d.keywords = d.keywords.map(cleanEnglishFullNames);
  d.rubric = d.rubric.map(cleanEnglishFullNames);
});
fs.writeFileSync(pedPath, JSON.stringify(pedData, null, 2), 'utf8');
console.log('✅ pedagogy_data.json English full names cleaned');

// 4. Update build_master.js to clean questionsA and questionsB on load
let masterCode = fs.readFileSync('build_master.js', 'utf8');

// Insert clean function right after loading questionsA & questionsB
const hookStr = `const questionsA = JSON.parse(matchA[1]);
const questionsB = JSON.parse(matchB[1]);`;

const cleanHook = `const questionsA = JSON.parse(matchA[1]);
const questionsB = JSON.parse(matchB[1]);

function cleanEnglish(str) {
  if (!str) return str;
  return str
    .replace(/역설적 지시\\(Paradoxical Injunction \\/ 증상 처방\\)/g, '역설적 지시(증상 처방)')
    .replace(/역설적 지시\\(Paradoxical Injunction\\)/g, '역설적 지시(증상 처방)')
    .replace(/\\s*\\((Dereflection|Hyperreflection|Clear boundary|Enactment|Retroflection|Empty Chair Technique|Life Theme|Career Adaptability|Providing Support|Obtaining Commitment|Need|Press|Calculus|Consistency|Persona|Identification|Good-me|Bad-me|Not-me|Teacher|Counselor|Consultant|Microaggression|Block Design|Visual Puzzles|Matrix Reasoning|Figure Weights)\\)/g, '');
}

questionsA.forEach(q => {
  q.title = cleanEnglish(q.title);
  q.content = cleanEnglish(q.content);
  q.instructions = cleanEnglish(q.instructions);
  q.answer = cleanEnglish(q.answer);
});

questionsB.forEach(q => {
  q.title = cleanEnglish(q.title);
  q.content = cleanEnglish(q.content);
  q.instructions = cleanEnglish(q.instructions);
  q.answer = cleanEnglish(q.answer);
});`;

if (masterCode.includes(hookStr)) {
  masterCode = masterCode.replace(hookStr, cleanHook);
  console.log('✅ Added English cleaner hook in build_master.js');
}

// 5. Update renderExamQuestions card layout to 2-column split grid
const startCardStr = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'`;

const endCardStr = `        '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
          '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
          '<div class="model-answer-text">' + q.answer + '</div>' +
        '</div>' +
      '</div>';`;

const idxStart = masterCode.indexOf(startCardStr);
const idxEnd = masterCode.indexOf(endCardStr, idxStart);

if (idxStart !== -1 && idxEnd !== -1) {
  const newCardHtml = `    card.innerHTML = 
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
            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)" oninput="handleExamInput(\\'' + type + '\\', ' + q.num + ')"></textarea>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
              '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + q.answer + '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';`;

  masterCode = masterCode.slice(0, idxStart) + newCardHtml + masterCode.slice(idxEnd + endCardStr.length);
  console.log('✅ renderExamQuestions updated to 2-column split grid');
} else {
  console.log('Card template bounds not found, checking alternatives...');
}

// 6. Update renderPedagogy card layout to 2-column split grid
const startPedStr = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'`;

const endPedStr = `        '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +
          '<div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>' +
          '<div class="model-answer-text">' + compactLines + '</div>' +
          '<div class="rubric-list">' +
            '<strong>[KICE 4점 채점표]</strong>' + rubricItems +
          '</div>' +
        '</div>' +
      '</div>';`;

const idxPedStart = masterCode.indexOf(startPedStr);
const idxPedEnd = masterCode.indexOf(endPedStr, idxPedStart);

if (idxPedStart !== -1 && idxPedEnd !== -1) {
  const newPedHtml = `    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge badge-pedagogy" style="font-size:0.78rem;">' + d.name + ' 영역</span>' +
          '<strong style="color:#fff; font-size:0.92rem;">' + d.theory + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + d.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:10px 14px; font-size:0.85rem; color:#e2e8f0;">' +
            '<strong style="color:var(--sky);">[세부 질문 4개]</strong>' +
            '<ol style="margin-left:16px; margin-top:4px; line-height:1.6;">' + subQList + '</ol>' +
          '</div>' +
          '<div class="keyword-tags" style="margin-top:6px;">' + kwBadges + '</div>' +
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

  masterCode = masterCode.slice(0, idxPedStart) + newPedHtml + masterCode.slice(idxPedEnd + endPedStr.length);
  console.log('✅ renderPedagogy updated to 2-column split grid');
}

fs.writeFileSync('build_master.js', masterCode, 'utf8');
console.log('build_master.js successfully refined!');
