const fs = require('fs');
let code = fs.readFileSync('build_master.js', 'utf8');

// 1. Update CSS for .exam-instructions
const oldCss = `.exam-instructions {
  background: rgba(245, 158, 11, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: 8px;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 0.88rem;
  color: #fde68a;
}`;

const newCss = `.exam-instructions {
  background: rgba(245, 158, 11, 0.06);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-left: 4px solid var(--gold);
  border-radius: 8px;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 0.92rem;
  color: #fde68a;
  white-space: pre-wrap;
  line-height: 1.9;
  letter-spacing: -0.2px;
}`;

if (code.includes(oldCss)) {
  code = code.replace(oldCss, newCss);
  console.log('✅ CSS updated successfully');
} else {
  console.log('CSS pattern not matched directly, checking alternative');
}

// 2. Update renderExamQuestions to format instructions with clean line breaks
const oldRender = `let instHtml = '';
    if (q.instructions && q.instructions.trim()) {
      instHtml = '<div class="exam-instructions">' + q.instructions + '</div>';
    }`;

const newRender = `let instHtml = '';
    if (q.instructions && q.instructions.trim()) {
      let formattedInst = q.instructions
        .replace(/<작성 방법>/g, '<strong>&lt;작성 방법&gt;</strong>\\n')
        .replace(/[\\r\\n]+/g, '\\n')
        .replace(/\\s*(○|\\u25CB)/g, '\\n○ ')
        .trim();
      instHtml = '<div class="exam-instructions">' + formattedInst + '</div>';
    }`;

if (code.includes(oldRender)) {
  code = code.replace(oldRender, newRender);
  console.log('✅ renderExamQuestions updated successfully');
} else {
  console.log('renderExamQuestions pattern not matched');
}

fs.writeFileSync('build_master.js', code, 'utf8');
console.log('build_master.js updated!');
