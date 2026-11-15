const fs = require('fs');
let code = fs.readFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', 'utf8');

const targetStr = `console.log('Target Enemy before attack:', enemyBefore.name, 'Troops:', enemyBefore.troops);
onCmdAutoSmartAttack();`;

const newStr = `const distCalc = getHexDistance(zhao.q, zhao.r, enemyBefore.q, enemyBefore.r);
console.log('Zhao pos:', zhao.q, zhao.r, 'Enemy pos:', enemyBefore.q, enemyBefore.r, 'Distance:', distCalc);
console.log('Target Enemy before attack:', enemyBefore.name, 'Troops:', enemyBefore.troops);
onCmdAutoSmartAttack();`;

code = code.replace(targetStr, newStr);
fs.writeFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', code, 'utf8');
