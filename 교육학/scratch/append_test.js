const fs = require('fs');
let code = fs.readFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_attack_debug.js', 'utf8');

const appendTest = `
console.log('\\n--- Testing onCmdAutoSmartAttack with Zhao Yun ---');
const zhao = UNITS.find(u => u.id === 'zhao_yun');
// 조운을 적장 옆으로 배치
zhao.q = enemy.q + 1;
zhao.r = enemy.r;
selectUnit(zhao);
console.log('Zhao pos:', zhao.q, zhao.r, 'Enemy pos:', enemy.q, enemy.r);
console.log('Enemy troops BEFORE auto attack:', enemy.troops);

onCmdAutoSmartAttack();

console.log('Enemy troops AFTER auto attack:', enemy.troops);
`;

fs.writeFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_attack_debug.js', code + appendTest, 'utf8');
