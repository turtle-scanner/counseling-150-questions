const fs = require('fs');

const code = fs.readFileSync('scratch/extracted_script_2.js', 'utf8');
const lines = code.split('\n');

lines.forEach((line, idx) => {
  if (line.includes('let gameState =') || line.includes('const gameState =') || line.includes('var gameState =')) {
    console.log(`Line ${idx + 1}: ${line}`);
  }
});
