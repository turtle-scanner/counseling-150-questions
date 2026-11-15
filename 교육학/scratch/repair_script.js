const fs = require('fs');

const filePath = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let html = fs.readFileSync(filePath, 'utf8');

// Target corrupted part
const corrupted = `      logMessage(\`👑 [군주 변경] 이제부터 '\${name}'(으)로 천하통일을 지휘합니다!\`, 'text-yellow-300 font-black');
    }
      gameState.bgmPlaying = !gameState.bgmPlaying;`;

const fixed = `      logMessage(\`👑 [군주 변경] 이제부터 '\${name}'(으)로 천하통일을 지휘합니다!\`, 'text-yellow-300 font-black');
    }

    // ==================== 사운드 엔진 (Web Audio API) ====================
    function toggleBGM() {
      closeAllPopups();
      if (!gameState.audioCtx) {
        try { gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch(e){}
      }
      gameState.bgmPlaying = !gameState.bgmPlaying;`;

if (html.includes(corrupted)) {
  html = html.replace(corrupted, fixed);
  console.log('Successfully repaired toggleBGM header!');
} else {
  console.log('Corrupted string not found directly, checking regex...');
  // Let's do string search
  const idx = html.indexOf("gameState.bgmPlaying = !gameState.bgmPlaying;");
  console.log('Index of bgmPlaying:', idx);
  const before = html.substring(idx - 150, idx);
  console.log('Before snippet:\n', before);
  
  html = html.replace(
    /logMessage\(`👑 \[군주 변경\][^`]*`,\s*'[^']*'\);\s*\}\s*gameState\.bgmPlaying = !gameState\.bgmPlaying;/,
    fixed
  );
}

// Write back
fs.writeFileSync(filePath, html, 'utf8');

// Also update the other target files
const targetPaths = [
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

console.log('All files repaired. Now testing syntax...');
