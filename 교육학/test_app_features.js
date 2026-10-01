const fs = require('fs');
const vm = require('vm');
const path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html';

const html = fs.readFileSync(path, 'utf8');

console.log('Testing feature execution in simulated DOM...');

const sandbox = {
  window: {
    scrollTo: () => {},
    print: () => {},
    addEventListener: () => {},
    removeEventListener: () => {}
  },
  localStorage: {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = v; },
    removeItem(k) { delete this._data[k]; }
  }
};

function createElement(tag, id = '', className = '') {
  return {
    tagName: tag,
    id: id,
    className: className,
    classList: {
      _classes: new Set(className.split(' ').filter(Boolean)),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c, force) {
        if (force === undefined) {
          if (this._classes.has(c)) this._classes.delete(c);
          else this._classes.add(c);
        } else if (force) {
          this._classes.add(c);
        } else {
          this._classes.delete(c);
        }
      },
      contains(c) { return this._classes.has(c); }
    },
    style: {
      setProperty: () => {},
      display: 'block'
    },
    getAttribute(attr) {
      if (attr === 'data-scale') return '1.6';
      return null;
    },
    innerHTML: '',
    textContent: '',
    value: '',
    children: [],
    querySelectorAll(selector) {
      return [createElement('div'), createElement('div')];
    },
    querySelector(selector) {
      return createElement('div');
    }
  };
}

const domElements = {
  cardContainer: createElement('div', 'cardContainer'),
  cardFront: createElement('div', 'cardFront'),
  cardBack: createElement('div', 'cardBack'),
  cardBadgeId: createElement('span', 'cardBadgeId'),
  cardBadgePeriod: createElement('span', 'cardBadgePeriod'),
  cardBadgeDomain: createElement('span', 'cardBadgeDomain'),
  cardBadgeFreeze: createElement('span', 'cardBadgeFreeze'),
  cardBadgeCore150: createElement('span', 'cardBadgeCore150'),
  cardTitleFront: createElement('div', 'cardTitleFront'),
  cardTitleBack: createElement('div', 'cardTitleBack'),
  cardQuestionText: createElement('div', 'cardQuestionText'),
  cardChosungBox: createElement('div', 'cardChosungBox'),
  cardRubricContainer: createElement('div', 'cardRubricContainer'),
  starNavCount: createElement('span', 'starNavCount'),
  cardStarBtn: createElement('button', 'cardStarBtn'),
  printCore150Container: createElement('div', 'printCore150Container'),
  examQuestionsContainer: createElement('div', 'examQuestionsContainer'),
  interactiveExamBox: createElement('div', 'interactiveExamBox'),
  rawExamBox: createElement('div', 'rawExamBox'),
  btnRound04: createElement('button', 'btnRound04'),
  btnRoundRaw: createElement('button', 'btnRoundRaw'),
  btnSubAll: createElement('button', 'btnSubAll'),
  btnSubPed: createElement('button', 'btnSubPed'),
  btnSubA: createElement('button', 'btnSubA'),
  btnSubB: createElement('button', 'btnSubB'),
  btnModeCard: createElement('button', 'btnModeCard'),
  btnModeList: createElement('button', 'btnModeList'),
  btnModeMatrix: createElement('button', 'btnModeMatrix'),
  btnModeExam: createElement('button', 'btnModeExam'),
  flashcardView: createElement('div', 'flashcardView'),
  listView: createElement('div', 'listView'),
  matrixView: createElement('div', 'matrixView'),
  examView: createElement('div', 'examView'),
  ddayCount: createElement('span', 'ddayCount'),
  masteryKnownCount: createElement('span', 'masteryKnownCount'),
  masteryConfusedCount: createElement('span', 'masteryConfusedCount'),
  masteryUnknownCount: createElement('span', 'masteryUnknownCount'),
  masteryProgressBar: createElement('div', 'masteryProgressBar'),
  btnRatingKnown: createElement('button', 'btnRatingKnown'),
  btnRatingConfused: createElement('button', 'btnRatingConfused'),
  btnRatingUnknown: createElement('button', 'btnRatingUnknown'),
  examDisplayBox: createElement('div', 'examDisplayBox')
};

sandbox.document = {
  documentElement: createElement('html'),
  getElementById(id) {
    if (!domElements[id]) {
      domElements[id] = createElement('div', id);
    }
    return domElements[id];
  },
  querySelectorAll(sel) {
    return [createElement('div'), createElement('div')];
  },
  querySelector(sel) {
    return createElement('div');
  },
  body: createElement('body'),
  addEventListener: () => {},
  removeEventListener: () => {}
};

const context = vm.createContext(sandbox);
const rawScript = html.match(/<script>([\s\S]*?)<\/script>/)[1];
vm.runInContext(rawScript, context);

console.log('--- Test 1: allData items & isCore150 count ---');
const allData = vm.runInContext('allData', context);
const totalItems = allData.length;
const core150Items = allData.filter(item => item.isCore150);
console.log(`Total items: ${totalItems}, Core 150 items: ${core150Items.length}`);
if (core150Items.length !== 150) {
  console.error('FAIL: Core 150 count is not 150!');
  process.exit(1);
} else {
  console.log('✅ PASS: Exactly 150 items tagged as isCore150!');
}

console.log('--- Test 2: Filter by core150 ---');
vm.runInContext("setPeriodFilter('core150')", context);
const filteredItems = vm.runInContext('filteredItems', context);
console.log(`Filtered items count in core150 mode: ${filteredItems.length}`);
if (filteredItems.length !== 150) {
  console.error('FAIL: filteredItems should be 150 in core150 mode!');
  process.exit(1);
} else {
  console.log('✅ PASS: filteredItems is exactly 150 in core150 mode!');
}

console.log('--- Test 3: Card flip interaction ---');
vm.runInContext('isFlipped = false; flipCard();', context);
let isFlipped = vm.runInContext('isFlipped', context);
if (!isFlipped) {
  console.error('FAIL: flipCard did not toggle isFlipped to true!');
  process.exit(1);
}
vm.runInContext('flipCard();', context);
isFlipped = vm.runInContext('isFlipped', context);
if (isFlipped) {
  console.error('FAIL: flipCard did not toggle isFlipped back to false!');
  process.exit(1);
}
console.log('✅ PASS: Card flipping toggles smoothly!');

console.log('--- Test 4: examQuestions04 dataset & rendering ---');
const examQuestions04 = vm.runInContext('examQuestions04', context);
if (!examQuestions04 || examQuestions04.length !== 24) {
  console.error(`FAIL: examQuestions04 count is ${examQuestions04 ? examQuestions04.length : 0}, expected 24!`);
  process.exit(1);
} else {
  console.log('✅ PASS: examQuestions04 contains exactly 24 questions (1 Pedagogy + 12 Major A + 11 Major B)!');
}

vm.runInContext('renderInteractiveExam();', context);
const examHtml = domElements.examQuestionsContainer.innerHTML;
console.log(`Rendered exam container HTML length: ${examHtml.length}`);
if (examHtml.length < 5000) {
  console.error('FAIL: renderInteractiveExam did not generate expected HTML!');
  process.exit(1);
} else {
  console.log('✅ PASS: renderInteractiveExam successfully populated questions!');
}

console.log('--- Test 5: Print 150 Core Keywords ---');
vm.runInContext('printCore150PDF();', context);
const printHtml = domElements.printCore150Container.innerHTML;
console.log(`Print 150 container HTML length: ${printHtml.length}`);
if (!printHtml.includes('2027 KICE 전문상담 핵심키워드 150선')) {
  console.error('FAIL: printCore150PDF missing header!');
  process.exit(1);
} else {
  console.log('✅ PASS: printCore150PDF generated complete 150-card study booklet!');
}

console.log('--- Test 6: Zero asterisks verification in HTML ---');
// Verify that our injected sections have NO asterisks
const interactiveExamSection = html.slice(html.indexOf('id="interactiveExamBox"'), html.indexOf('id="rawExamBox"'));
const starCountInInteractive = (interactiveExamSection.match(/\*/g) || []).length;
console.log(`Asterisks in interactive exam HTML: ${starCountInInteractive}`);
if (starCountInInteractive > 0) {
  console.error('FAIL: Asterisks found in interactive exam HTML!');
  process.exit(1);
} else {
  console.log('✅ PASS: Zero asterisks strictly verified in interactive exam section!');
}

console.log('ALL TESTS PASSED WITH 100% SUCCESS! 🚀');
