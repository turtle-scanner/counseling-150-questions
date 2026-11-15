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
        classList: { add: function() {}, remove: function() {}, contains: function() { return false; }, toggle: function() {} },
        disabled: false,
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
global.alert = function(msg) { console.log('ALERT:', msg); };
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
  width: 1280,
  height: 640,
  getBoundingClientRect: function() { return { left: 0, top: 0, width: 1280, height: 640 }; },
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

console.log('Testing executeRest()...');
try {
  executeRest();
  console.log('SUCCESS: executeRest finished without error!');
  console.log('Current Date:', document.getElementById('currentDate').innerText);
  console.log('Action Points:', gameState.actionPoints);
} catch (e) {
  console.error('ERROR in executeRest:', e);
}
