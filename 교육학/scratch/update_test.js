const fs = require('fs');
let code = fs.readFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', 'utf8');

const targetCheck = `console.log('Target Enemy before attack:', enemyBefore.name, 'Troops:', enemyBefore.troops);
onCmdAutoSmartAttack();`;

const replacementCheck = `// 조운을 적장 바로 옆(거리 1칸)으로 배치하여 근접 즉시 타격 검증!
const zhao = UNITS.find(u => u.id === 'zhao_yun');
zhao.q = enemyBefore.q - 1;
zhao.r = enemyBefore.r;
console.log('Target Enemy before attack:', enemyBefore.name, 'Troops:', enemyBefore.troops);
onCmdAutoSmartAttack();`;

code = code.replace(targetCheck, replacementCheck);
fs.writeFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', code, 'utf8');
