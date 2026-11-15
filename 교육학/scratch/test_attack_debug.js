const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html', 'utf8');

const globalDom = {
  elements: {},
  getElementById: function(id) {
    if (!this.elements[id]) {
      this.elements[id] = {
        id: id,
        innerText: '',
        innerHTML: '',
        style: {},
        classList: { add: function() {}, remove: function() {}, contains: function() { return false; } },
        disabled: true,
        addEventListener: function() {},
        appendChild: function() {}
      };
    }
    return this.elements[id];
  },
  querySelectorAll: function() { return []; },
  querySelector: function() { return null; },
  createElement: function() { return { style: {}, innerText: '', className: '', remove: function() {} }; },
  addEventListener: function() {}
};

global.window = global;
global.window.addEventListener = function() {};
global.document = globalDom;
global.confirm = function() { return true; };
global.alert = function() {};
global.prompt = function() { return '1'; };
global.console = console;
global.AudioContext = function() {
  return {
    createOscillator: function() { return { type: '', frequency: { setValueAtTime: function() {}, exponentialRampToValueAtTime: function() {} }, connect: function() {}, start: function() {}, stop: function() {} }; },
    createGain: function() { return { gain: { setValueAtTime: function() {}, linearRampToValueAtTime: function() {}, exponentialRampToValueAtTime: function() {} }, connect: function() {} }; },
    destination: {},
    currentTime: 0
  };
};
global.webkitAudioContext = global.AudioContext;
global.requestAnimationFrame = function(cb) { setTimeout(cb, 16); };

const canvasObj = {
  width: 1160,
  height: 590,
  getBoundingClientRect: function() { return { left: 0, top: 0, width: 1160, height: 590 }; },
  getContext: function() {
    return {
      clearRect: function() {},
      beginPath: function() {},
      moveTo: function() {},
      lineTo: function() {},
      closePath: function() {},
      arc: function() {},
      fill: function() {},
      stroke: function() {},
      fillText: function() {},
      fillRect: function() {},
      strokeRect: function() {},
      measureText: function() { return { width: 10 }; },
      save: function() {},
      restore: function() {}
    };
  },
  addEventListener: function() {}
};
globalDom.elements['battleCanvas'] = canvasObj;

const scripts = [...html.matchAll(/<script[\s\S]*?>([\s\S]*?)<\/script>/gi)];
scripts.forEach((m, idx) => {
  vm.runInThisContext(m[1]);
});

// 전장 리셋
const targetProv = PROVINCES.find(p => p.id === 2);
const fromProv = getMyCapital();
resetHexBattlefield(targetProv, fromProv);

console.log('UNITS count:', UNITS.length);
const ally = UNITS.find(u => u.faction === 'ally');
const enemy = UNITS.find(u => u.faction === 'enemy');

console.log('Ally:', ally.name, 'pos:', ally.q, ally.r);
console.log('Enemy:', enemy.name, 'pos:', enemy.q, enemy.r);

// 인접 배치
ally.q = enemy.q - 1;
ally.r = enemy.r;
selectUnit(ally);

console.log('Selected unit:', sam5BattleState.selectedUnit ? sam5BattleState.selectedUnit.name : 'null');
console.log('Enemy troops BEFORE:', enemy.troops);

// 직접 공격 실행
executeDirectAttack(ally, enemy);

console.log('Enemy troops AFTER:', enemy.troops);

console.log('\n--- Testing onCmdAutoSmartAttack with Zhao Yun ---');
const zhao = UNITS.find(u => u.id === 'zhao_yun');
// 조운을 적장 옆으로 배치
zhao.q = enemy.q + 1;
zhao.r = enemy.r;
selectUnit(zhao);
console.log('Zhao pos:', zhao.q, zhao.r, 'Enemy pos:', enemy.q, enemy.r);
console.log('Enemy troops BEFORE auto attack:', enemy.troops);

onCmdAutoSmartAttack();

console.log('Enemy troops AFTER auto attack:', enemy.troops);
