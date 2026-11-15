const fs = require('fs');

const filePath = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let html = fs.readFileSync(filePath, 'utf8');

// The marker where sam5_script starts
const sam5Marker = '// ==================== 🔥 삼국지 5 헥스 전장 스크립트 임베딩 ====================';
const idx = html.indexOf(sam5Marker);

if (idx === -1) {
  console.error('sam5Marker not found!');
  process.exit(1);
}

const mainPart = html.substring(0, idx);
let sam5Part = html.substring(idx);

console.log('Replacing gameState and duelState in sam5Part...');

// Replace gameState with sam5BattleState in sam5Part
sam5Part = sam5Part.replace(/\bgameState\b/g, 'sam5BattleState');

// Replace duelState with sam5DuelState in sam5Part
sam5Part = sam5Part.replace(/\bduelState\b/g, 'sam5DuelState');

// Combine back
html = mainPart + sam5Part;

// Write back to all target files
const targetPaths = [
  'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html',
  'C:\\Users\\LENOVO\\Desktop\\sam3_update.html',
  'g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\samgukji.html',
  'g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\samgukji.html'
];

targetPaths.forEach(p => {
  try {
    fs.writeFileSync(p, html, 'utf8');
    console.log('Updated:', p);
  } catch(e) {
    console.error('Failed:', p, e.message);
  }
});

console.log('Finished renaming conflicts. Now testing syntax...');
