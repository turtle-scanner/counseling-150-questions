const vm = require('vm');
const fs = require('fs');
const path = require('path');

// 1. Load Data
const top55Raw = JSON.parse(fs.readFileSync(path.join(__dirname, '교육학/scratch/top55_extracted.json'), 'utf8'));
const pedData = JSON.parse(fs.readFileSync(path.join(__dirname, 'pedagogy_data.json'), 'utf8'));
const examHtml = fs.readFileSync(path.join(__dirname, '교육학/exam_2027_kice_ab.html'), 'utf8');

const matchA = examHtml.match(/const examDataA = (\[[\s\S]*?\]);/);
const matchB = examHtml.match(/const examDataB = (\[[\s\S]*?\]);/);

if (!matchA || !matchB) {
  console.error('Failed to extract examDataA or examDataB');
  process.exit(1);
}

const questionsA = JSON.parse(matchA[1]);
const questionsB = JSON.parse(matchB[1]);

function cleanEnglishFullNames(text) {
  if (!text) return text;
  let res = text
    .replace(/역설적 지시\(Paradoxical Injunction \/ 증상 처방\)/g, '역설적 지시(증상 처방)')
    .replace(/역설적 지시\(Paradoxical Injunction\)/g, '역설적 지시(증상 처방)')
    .replace(/자극추구\(Novelty Seeking, NS\)/g, '자극추구(NS)')
    .replace(/위험회피\(Harm Avoidance, HA\)/g, '위험회피(HA)')
    .replace(/보상의존\(Reward Dependence, RD\)/g, '보상의존(RD)')
    .replace(/인내력\(Persistence, P\)/g, '인내력(P)')
    .replace(/자율성\(Self-Directedness, SD\)/g, '자율성(SD)')
    .replace(/협동성\(Cooperativeness, CO\)/g, '협동성(CO)')
    .replace(/자기초월\(Self-Transcendence, ST\)/g, '자기초월(ST)')
    .replace(/탈숙고\(Dereflection\)/g, '탈숙고')
    .replace(/과잉주의\(Hyperreflection\)/g, '과잉주의')
    .replace(/명확한 경계선\(Clear boundary\)/g, '명확한 경계선')
    .replace(/실연\(Enactment\)/g, '실연')
    .replace(/반전\(Retroflection\)/g, '반전')
    .replace(/빈 의자 기법\(Empty Chair Technique\)/g, '빈 의자 기법')
    .replace(/생애 주제\(Life Theme\)/g, '생애 주제')
    .replace(/진로적응도\(Career Adaptability\)/g, '진로적응도')
    .replace(/토막짜기\(Block Design\)/g, '토막짜기')
    .replace(/시각퍼즐\(Visual Puzzles\)/g, '시각퍼즐')
    .replace(/행렬추론\(Matrix Reasoning\)/g, '행렬추론')
    .replace(/무게비교\(Figure Weights\)/g, '무게비교')
    .replace(/미세공격\(Microaggression\)/g, '미세공격')
    .replace(/계측성\(Calculus\)/g, '계측성')
    .replace(/일관성\(Consistency\)/g, '일관성')
    .replace(/동일시\(Identification\)/g, '동일시')
    .replace(/좋은-나\(Good-me\)/g, '좋은-나')
    .replace(/나쁜-나\(Bad-me\)/g, '나쁜-나')
    .replace(/나-아님\(Not-me\)/g, '나-아님')
    .replace(/교사\(Teacher\)/g, '교사')
    .replace(/상담자\(Counselor\)/g, '상담자')
    .replace(/자문가\(Consultant\)/g, '자문가')
    .replace(/신체증상장애\(Somatic Symptom Disorder\)/g, '신체증상장애')
    .replace(/질병불안장애\(Illness Anxiety Disorder\)/g, '질병불안장애')
    .replace(/사회적\(실용적\) 의사소통장애\(Social Communication Disorder\)/g, '사회적(실용적) 의사소통장애')
    .replace(/자폐스펙트럼장애\(Autism Spectrum Disorder\)/g, '자폐스펙트럼장애')
    .replace(/광장공포증\(Agoraphobia\)/g, '광장공포증')
    .replace(/파국적 오해석\(Catastrophic Misinterpretation\)/g, '파국적 오해석')
    .replace(/내부감각 노출\(Interoceptive Exposure\)/g, '내부감각 노출')
    .replace(/참여자적 관찰자\(Participant Observer\)/g, '참여자적 관찰자')
    .replace(/자아동질적\(Ego-syntonic\)/g, '자아동질적')
    .replace(/자아이질적\(Ego-dystonic\)/g, '자아이질적')
    .replace(/기질\(Temperament\)/g, '기질')
    .replace(/성격\(Character\)/g, '성격')
    .replace(/과부하\(Overload\)/g, '과부하')
    .replace(/외향반응성\(Extratensive\)/g, '외향반응성')
    .replace(/제한\(Circumscription\)/g, '제한')
    .replace(/타협\(Compromise\)/g, '타협')
    .replace(/성역할 발달\(Sex-Role Orientation\)/g, '성역할 발달')
    .replace(/성역할 경계선\(Sex-Role Orientation\)/g, '성역할 경계선')
    .replace(/핵심신념\(Core Belief\)/g, '핵심신념')
    .replace(/하향화살표 기법\(Downward Arrow Technique\)/g, '하향화살표 기법')
    .replace(/삼각관계\(Triangulation\)/g, '삼각관계')
    .replace(/탈삼각화\(Detriangulation\)/g, '탈삼각화')
    .replace(/로샤\(Rorschach\)/g, '로샤')
    .replace(/사비카스\(Savickas\)/g, '사비카스')
    .replace(/길리랜드\(Gilliland\)/g, '길리랜드')
    .replace(/숀 셰이\(Shawn Shea\)/g, '숀 셰이')
    .replace(/욕구\(Need\)/g, '욕구')
    .replace(/압착\(Press\)/g, '압착')
    .replace(/주제\(Thema\)/g, '주제')
    .replace(/관심\(Concern\)/g, '관심')
    .replace(/통제\(Control\)/g, '통제')
    .replace(/호기심\(Curiosity\)/g, '호기심')
    .replace(/자신감\(Confidence\)/g, '자신감')
    .replace(/지지 제공\(Providing Support\)/g, '지지 제공')
    .replace(/다짐 받기\(Obtaining Commitment\)/g, '다짐 받기');

  const termsToRemove = [
    'Dereflection', 'Hyperreflection', 'Paradoxical Injunction', 'Clear boundary',
    'Enactment', 'Retroflection', 'Empty Chair Technique', 'Life Theme',
    'Career Adaptability', 'Concern', 'Control', 'Curiosity', 'Confidence',
    'Providing Support', 'Obtaining Commitment', 'Block Design', 'Visual Puzzles',
    'Matrix Reasoning', 'Figure Weights', 'Microaggression', 'Calculus',
    'Consistency', 'Identification', 'Circumscription', 'Compromise',
    'Sex-Role Orientation', 'Core Belief', 'Downward Arrow Technique',
    'Triangulation', 'Detriangulation', 'Somatic Symptom Disorder',
    'Illness Anxiety Disorder', 'Social Communication Disorder',
    'Autism Spectrum Disorder', 'Agoraphobia', 'Catastrophic Misinterpretation',
    'Interoceptive Exposure', 'Participant Observer', 'Ego-syntonic',
    'Ego-dystonic', 'Temperament', 'Character', 'Overload', 'Extratensive',
    'Rorschach', 'Savickas', 'Gilliland', 'Shawn Shea', 'Need', 'Press',
    'Thema', 'Not-me', 'Good-me', 'Bad-me', 'Teacher', 'Counselor', 'Consultant',
    'Chronological Assessment of Suicide Events'
  ];

  termsToRemove.forEach(t => {
    res = res.split(' (' + t + ')').join('').split('(' + t + ')').join('');
  });

  return res;
}

questionsA.forEach(q => {
  q.title = cleanEnglishFullNames(q.title);
  q.content = cleanEnglishFullNames(q.content);
  q.instructions = cleanEnglishFullNames(q.instructions);
  q.answer = cleanEnglishFullNames(q.answer);
});

questionsB.forEach(q => {
  q.title = cleanEnglishFullNames(q.title);
  q.content = cleanEnglishFullNames(q.content);
  q.instructions = cleanEnglishFullNames(q.instructions);
  q.answer = cleanEnglishFullNames(q.answer);
});


// 2. Format Top55
const top55Formatted = top55Raw.map((item, idx) => {
  const isPed = item.type === 'pedagogy';
  const prefix = isPed ? 'P' : 'C';
  const category = isPed ? '교육학 20선' : '전공상담 35선';

  const rawKw = item.keyword || '';
  const kws = rawKw.replace(/➔/g, ',').replace(/\//g, ',').split(',')
    .map(k => k.trim())
    .filter(k => k.length > 0);

  let cleanAns = item.clean_ans || item.answer || '';
  cleanAns = cleanAns
    .replace(/<mark style="[^"]*">/g, '')
    .replace(/<\/mark>/g, '')
    .replace(/<br>/g, '\n')
    .trim();

  return {
    num: idx + 1,
    code: `${prefix}${String(idx + 1).padStart(2, '0')}`,
    category,
    type: item.type,
    domain: item.domain || '',
    question: item.question || '',
    keywords: kws,
    raw_keywords: rawKw,
    answer: cleanAns
  };
});

const payload = {
  top55: top55Formatted,
  pedagogy: pedData,
  questions_a: questionsA,
  questions_b: questionsB
};

const jsonStr = JSON.stringify(payload);

// 3. Assemble HTML
const htmlTemplate = `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2027 KICE 임용고시 합격 마스터: 교육학 & 전공상담 풀세트</title>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg-main: #090d16;
  --bg-card: #151e2e;
  --bg-card-hover: #1b263b;
  --bg-input: #0f1624;
  --border-card: #23324a;
  --border-focus: #38bdf8;
  --text-main: #f8fafc;
  --text-sub: #94a3b8;
  --text-dim: #64748b;
  --gold: #f59e0b;
  --gold-bg: rgba(245, 158, 11, 0.12);
  --emerald: #10b981;
  --emerald-bg: rgba(16, 185, 129, 0.12);
  --sky: #38bdf8;
  --sky-bg: rgba(56, 189, 248, 0.12);
  --rose: #f43f5e;
  --rose-bg: rgba(244, 63, 94, 0.12);
  --purple: #a855f7;
  --purple-bg: rgba(168, 85, 247, 0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: 'Noto Sans KR', sans-serif;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  padding-bottom: 80px;
}

/* Header & Nav */
header.app-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(9, 13, 22, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-card);
  padding: 12px 24px;
}
.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  max-width: 1400px;
  margin: 0 auto;
}
.brand-title {
  display: flex;
  align-items: center;
  gap: 10px;
}
.brand-title h1 {
  font-size: 1.25rem;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.5px;
}
.brand-badge {
  background: var(--gold-bg);
  color: var(--gold);
  border: 1px solid var(--gold);
  font-size: 0.72rem;
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 700;
}

/* Tabs */
.tab-container {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 0;
  max-width: 1400px;
  margin: 10px auto 0 auto;
}
.tab-btn {
  background: var(--bg-card);
  color: var(--text-sub);
  border: 1px solid var(--border-card);
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.tab-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.tab-btn.active {
  background: var(--sky-bg);
  color: var(--sky);
  border-color: var(--sky);
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
}

/* Control Bar */
.control-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  max-width: 1400px;
  margin: 16px auto;
  padding: 0 24px;
}
.search-box {
  position: relative;
  flex: 1;
  max-width: 360px;
}
.search-box input {
  width: 100%;
  background: var(--bg-input);
  border: 1px solid var(--border-card);
  color: #fff;
  padding: 8px 12px 8px 36px;
  border-radius: 8px;
  font-size: 0.85rem;
  outline: none;
}
.search-box input:focus {
  border-color: var(--sky);
}
.search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 0.9rem;
}

.tool-group {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
}
.tool-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  color: var(--text-sub);
  padding: 7px 12px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}
.tool-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.tool-btn.active-toggle {
  background: var(--rose-bg);
  border-color: var(--rose);
  color: var(--rose);
}

/* Timer Widget */
.timer-widget {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  padding: 4px 12px;
  border-radius: 8px;
}
.timer-clock {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--gold);
}

/* Progress bar */
.progress-wrap {
  max-width: 1400px;
  margin: 0 auto 16px auto;
  padding: 0 24px;
}
.progress-bar-bg {
  background: #1b263b;
  border-radius: 999px;
  height: 6px;
  overflow: hidden;
}
.progress-bar-fill {
  background: linear-gradient(90deg, var(--sky), var(--emerald));
  height: 100%;
  width: 0%;
  transition: width 0.3s ease;
}
.progress-text {
  font-size: 0.78rem;
  color: var(--text-sub);
  margin-top: 4px;
  display: flex;
  justify-content: space-between;
}

/* Content Area */
main.content-area {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
}
.tab-section {
  display: none;
}
.tab-section.active {
  display: block;
}

/* Card Styles */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
  gap: 16px;
}
@media (max-width: 768px) {
  .card-grid { grid-template-columns: 1fr; }
}

.item-card {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  padding: 18px;
  position: relative;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.item-card:hover {
  border-color: #3b4e6d;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.item-card.memorized {
  border-color: var(--emerald);
  background: rgba(16, 185, 129, 0.04);
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.badge-group {
  display: flex;
  gap: 6px;
  align-items: center;
}
.badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 6px;
}
.badge-code {
  background: #202b3d;
  color: var(--sky);
  border: 1px solid #334460;
  font-family: 'JetBrains Mono', monospace;
}
.badge-category {
  background: var(--purple-bg);
  color: var(--purple);
  border: 1px solid rgba(168, 85, 247, 0.4);
}
.badge-pedagogy {
  background: var(--sky-bg);
  color: var(--sky);
  border: 1px solid rgba(56, 189, 248, 0.4);
}
.badge-score {
  background: var(--gold-bg);
  color: var(--gold);
  border: 1px solid var(--gold);
}

.memorize-chk {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  color: var(--text-sub);
  cursor: pointer;
  user-select: none;
}
.memorize-chk input {
  cursor: pointer;
  accent-color: var(--emerald);
  width: 16px;
  height: 16px;
}

.card-question {
  font-size: 0.98rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.5;
}
.keyword-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.kw-tag {
  background: #1e293b;
  color: var(--gold);
  border: 1px solid #334155;
  font-size: 0.76rem;
  padding: 3px 8px;
  border-radius: 6px;
  font-weight: 600;
  transition: all 0.2s;
}

/* Spoiler / Blind Effect */
body.blind-mode .kw-tag {
  background: #0f172a !important;
  color: #0f172a !important;
  border-color: #334155 !important;
  cursor: pointer;
  user-select: none;
}
body.blind-mode .kw-tag:hover,
body.blind-mode .kw-tag.revealed {
  background: #1e293b !important;
  color: var(--gold) !important;
  border-color: var(--gold) !important;
}

.compact-answer-box {
  background: #0d1422;
  border: 1px solid #202b3d;
  border-radius: 8px;
  padding: 12px;
  font-size: 0.88rem;
  line-height: 1.6;
  color: #cbd5e1;
  font-family: 'Nanum Myeongjo', serif;
  border-left: 3px solid var(--emerald);
  white-space: pre-wrap;
}

/* Exam Mode Simulation Cards */
.exam-full-card {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  padding: 14px 18px;
  margin-bottom: 14px;
}
.exam-split-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
  align-items: start;
}
@media (min-width: 960px) {
  .exam-split-grid {
    grid-template-columns: 1.15fr 1fr;
  }
}
.exam-left-col {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.exam-right-col {
  display: flex;
  flex-direction: column;
}
.exam-case-box {
  background: #0c1320;
  border: 1px solid #23324a;
  border-left: 3px solid var(--sky);
  border-radius: 8px;
  padding: 10px 14px;
  margin: 0;
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.88rem;
  line-height: 1.58;
  color: #e2e8f0;
  white-space: pre-wrap;
  max-height: 260px;
  overflow-y: auto;
}
.exam-instructions {
  background: rgba(245, 158, 11, 0.06);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 8px 12px;
  margin: 0;
  font-size: 0.82rem;
  color: #fde68a;
  line-height: 1.5;
}
.exam-instructions ul {
  margin-left: 16px;
  margin-top: 4px;
}

/* Line-note styled textarea */
.answer-box-wrap {
  margin-top: 0;
}
.answer-box-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
  font-size: 0.78rem;
  color: var(--text-sub);
}
.char-count-badge {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: var(--sky);
}
.char-count-badge.limit-ok {
  color: var(--emerald);
}
.char-count-badge.limit-warn {
  color: var(--rose);
}

.exam-textarea {
  width: 100%;
  height: 76px;
  min-height: 76px;
  background: var(--bg-input);
  background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 100% 24px;
  line-height: 24px;
  border: 1px solid var(--border-card);
  border-radius: 8px;
  color: #fff;
  padding: 6px 12px;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 0.88rem;
  resize: vertical;
  outline: none;
}
.exam-textarea:focus {
  border-color: var(--sky);
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
}

/* Hidden Model Answer Box */
.model-answer-panel {
  display: none;
  background: #0b1524;
  border: 1px solid #1e3a5f;
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 10px 14px;
  margin-top: 8px;
  max-height: 280px;
  overflow-y: auto;
  animation: fadeIn 0.25s ease;
}
.model-answer-panel.show {
  display: block;
}
.model-answer-title {
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--gold);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.model-answer-text {
  font-family: 'Nanum Myeongjo', serif;
  font-size: 0.85rem;
  line-height: 1.52;
  color: #e2e8f0;
  white-space: pre-wrap;
}
.rubric-list {
  margin-top: 6px;
  padding-top: 6px;
  border-top: 1px dashed #233852;
  font-size: 0.78rem;
  color: var(--text-sub);
}
.rubric-item {
  margin-bottom: 3px;
  display: flex;
  align-items: flex-start;
  gap: 6px;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-3px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Quick Nav Bar */
.quick-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}
.quick-nav-btn {
  background: var(--bg-card);
  color: var(--text-sub);
  border: 1px solid var(--border-card);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}
.quick-nav-btn:hover {
  background: var(--bg-card-hover);
  color: #fff;
}
.quick-nav-btn.written {
  border-color: var(--emerald);
  color: var(--emerald);
}

/* Banner */
.notice-banner {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.1), rgba(168, 85, 247, 0.1));
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
.notice-banner h3 {
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
}
.notice-banner p {
  font-size: 0.82rem;
  color: var(--text-sub);
}

/* Print Modal Styles */
.print-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(4px);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.print-modal-overlay.active {
  display: flex;
}
.print-modal-card {
  background: #111827;
  border: 1px solid #334155;
  border-radius: 14px;
  width: 100%;
  max-width: 520px;
  padding: 24px;
  color: #f8fafc;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  animation: fadeIn 0.2s ease;
}
.print-modal-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
  border-bottom: 1px solid #1e293b;
  padding-bottom: 12px;
}
.print-modal-group {
  margin-bottom: 16px;
}
.print-modal-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: #94a3b8;
  margin-bottom: 8px;
  display: block;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.print-option-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 8px;
  margin-bottom: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.88rem;
}
.print-option-row:hover {
  background: #273549;
  border-color: #475569;
}
.print-option-row input[type="radio"],
.print-option-row input[type="checkbox"] {
  accent-color: #38bdf8;
  width: 18px;
  height: 18px;
  cursor: pointer;
}
.print-modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
  border-top: 1px solid #1e293b;
  padding-top: 16px;
}
.btn-print-confirm {
  background: #f59e0b;
  color: #000;
  font-weight: 800;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}
.btn-print-confirm:hover {
  background: #d97706;
}
.btn-print-cancel {
  background: #334155;
  color: #f8fafc;
  font-weight: 600;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
}
.btn-print-cancel:hover {
  background: #475569;
}

/* Screen hidden elements for print */
.print-page-header,
.print-paper-answer {
  display: none;
}

/* ================== A4 PRINT OPTIMIZATIONS ================== */
@media print {
  @page {
    size: A4 portrait;
    margin: 12mm 10mm 12mm 10mm;
  }
  
  *, *::before, *::after {
    box-shadow: none !important;
    text-shadow: none !important;
  }
  
  html, body {
    background: #ffffff !important;
    color: #0f172a !important;
    font-size: 9pt !important;
    line-height: 1.45 !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
  }

  .app-header,
  .control-bar,
  .progress-wrap,
  .tool-group,
  .timer-widget,
  .quick-nav,
  .notice-banner,
  .no-print,
  #blind-toggle-btn,
  .search-box,
  #top55-filters,
  .char-count-badge,
  .memorize-chk,
  .print-modal-overlay,
  .answer-box-header {
    display: none !important;
  }

  main.content-area {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Print Section Scopes */
  body.print-scope-full #sec-top55 {
    display: none !important;
  }
  body.print-scope-full #sec-pedagogy,
  body.print-scope-full #sec-qa,
  body.print-scope-full #sec-qb {
    display: block !important;
  }
  body.print-scope-full #sec-qa,
  body.print-scope-full #sec-qb {
    page-break-before: always !important;
    break-before: page !important;
  }

  body.print-scope-top55 #sec-top55 {
    display: block !important;
  }
  body.print-scope-top55 #sec-pedagogy,
  body.print-scope-top55 #sec-qa,
  body.print-scope-top55 #sec-qb {
    display: none !important;
  }

  body.print-scope-current .tab-section:not(.active) {
    display: none !important;
  }
  body.print-scope-current .tab-section.active {
    display: block !important;
  }

  /* Formal Print Page Header */
  .print-page-header {
    display: block !important;
    border-bottom: 2px solid #0f172a !important;
    padding-bottom: 6px !important;
    margin-bottom: 12px !important;
    page-break-after: avoid !important;
  }
  .print-page-header h2 {
    font-size: 13pt !important;
    font-weight: 900 !important;
    color: #0f172a !important;
    margin: 0 0 2px 0 !important;
  }
  .print-page-header p {
    font-size: 8.5pt !important;
    color: #475569 !important;
    margin: 0 !important;
  }

  /* Full Question Cards on Paper */
  .exam-full-card {
    background: #ffffff !important;
    border: 1px solid #94a3b8 !important;
    border-radius: 4px !important;
    padding: 10px 12px !important;
    margin-bottom: 12px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  .exam-split-grid {
    display: block !important;
  }
  .exam-left-col {
    width: 100% !important;
  }
  .exam-right-col {
    width: 100% !important;
    margin-top: 8px !important;
  }

  .exam-case-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-left: 3px solid #0284c7 !important;
    border-radius: 4px !important;
    padding: 8px 12px !important;
    font-size: 9pt !important;
    line-height: 1.5 !important;
    max-height: none !important;
    overflow: visible !important;
    white-space: pre-wrap !important;
  }

  .exam-instructions {
    background: #fefce8 !important;
    color: #713f12 !important;
    border: 1px solid #fde047 !important;
    border-left: 3px solid #ca8a04 !important;
    border-radius: 4px !important;
    padding: 6px 10px !important;
    margin-top: 6px !important;
    font-size: 8.5pt !important;
    line-height: 1.4 !important;
  }
  .exam-instructions strong {
    color: #713f12 !important;
  }

  .exam-textarea {
    display: none !important;
  }

  /* Print Paper Answer Layout */
  .print-paper-answer {
    display: block !important;
    margin-top: 6px !important;
  }
  
  .print-written-text {
    display: none;
    font-family: 'Nanum Myeongjo', serif;
    font-size: 9pt;
    line-height: 1.55;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 8px 12px;
    background: #fff;
    min-height: 50px;
    white-space: pre-wrap;
  }
  body.print-with-user .print-written-text {
    display: block !important;
  }
  
  .print-blank-lines {
    display: block;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 10px;
    background: #ffffff;
  }
  body.print-with-user .print-blank-lines {
    display: none !important;
  }
  .p-line {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    color: #94a3b8;
    line-height: 22px;
    border-bottom: 1px solid #e2e8f0;
    padding: 2px 0;
  }
  .p-line:last-child {
    border-bottom: none;
  }

  /* Model Answer on Paper */
  .model-answer-panel {
    display: none !important;
  }
  body.print-with-answers .model-answer-panel {
    display: block !important;
    background: #f0fdf4 !important;
    border: 1px solid #86efac !important;
    border-left: 3px solid #16a34a !important;
    border-radius: 4px !important;
    padding: 8px 12px !important;
    margin-top: 8px !important;
    color: #14532d !important;
    max-height: none !important;
    overflow: visible !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .model-answer-title {
    color: #15803d !important;
    font-size: 8.5pt !important;
    font-weight: 800 !important;
  }
  .model-answer-text {
    color: #14532d !important;
    font-size: 8.8pt !important;
    line-height: 1.5 !important;
  }
  .rubric-list {
    border-top: 1px dashed #86efac !important;
    color: #166534 !important;
    font-size: 8pt !important;
  }

  /* Badges */
  .badge {
    border: 1px solid #94a3b8 !important;
    color: #0f172a !important;
    background: #f1f5f9 !important;
    font-size: 7.5pt !important;
    padding: 1px 6px !important;
  }
  .badge-category, .badge-pedagogy {
    background: #e0f2fe !important;
    color: #0369a1 !important;
    border-color: #7dd3fc !important;
  }
  .badge-score {
    background: #fef3c7 !important;
    color: #b45309 !important;
    border-color: #fcd34d !important;
  }
  .kw-tag {
    background: #f8fafc !important;
    color: #0284c7 !important;
    border: 1px solid #cbd5e1 !important;
    font-size: 7.5pt !important;
    padding: 1px 5px !important;
  }

  /* TOP 55 Cards in Print */
  .card-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
  }
  .item-card {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 4px !important;
    padding: 8px 10px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    gap: 6px !important;
  }
  .card-question {
    color: #0f172a !important;
    font-size: 8.8pt !important;
  }
  .compact-answer-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 2px solid #10b981 !important;
    font-size: 8.3pt !important;
    padding: 6px 8px !important;
  }
}

</style>
</head>
<body>

<header class="app-header">
  <div class="header-top">
    <div class="brand-title">
      <h1>🎯 2027 KICE 임용고시 합격 마스터</h1>
      <span class="brand-badge">2027 0순위 55개 완전압축</span>
    </div>
    
    <div class="tool-group">
      <div class="timer-widget">
        <span style="font-size: 0.8rem; color: var(--text-sub);">⏱️</span>
        <span class="timer-clock" id="timer-display">60:00</span>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="toggleTimer()" id="timer-btn">시작</button>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="resetTimer(60)">60분</button>
        <button class="tool-btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="resetTimer(90)">90분</button>
      </div>

      <button class="tool-btn" id="blind-toggle-btn" onclick="toggleBlindMode()">
        <span>👁️</span> <span id="blind-label">키워드 가리기</span>
      </button>

            <button class="tool-btn" onclick="openPrintModal()" style="background: var(--gold); color: #000; font-weight: 800; border-color: var(--gold);">
        <span>🖨️</span> A4 인쇄 / PDF
      </button>

      <button class="tool-btn" onclick="exportAnswers()">
        <span>📋</span> 답안 전체 복사
      </button>
    </div>
  </div>

  <div class="tab-container">
    <button class="tab-btn active" onclick="switchTab('top55')" id="tab-btn-top55">
      <span>⚡</span> 2027 핵심 55선 콤팩트 스피드 암기
    </button>
    <button class="tab-btn" onclick="switchTab('pedagogy')" id="tab-btn-pedagogy">
      <span>🎓</span> 1교시 교육학 논술 [20점]
    </button>
    <button class="tab-btn" onclick="switchTab('qa')" id="tab-btn-qa">
      <span>📘</span> 2교시 전공 A형 [40점]
    </button>
    <button class="tab-btn" onclick="switchTab('qb')" id="tab-btn-qb">
      <span>📙</span> 3교시 전공 B형 [40점]
    </button>
  </div>
</header>

<!-- ================== PRINT CONFIG MODAL ================== -->
<div class="print-modal-overlay" id="print-modal">
  <div class="print-modal-card">
    <div class="print-modal-title">
      <span>🖨️</span> A4 인쇄 및 PDF 저장 설정
    </div>

    <div class="print-modal-group">
      <span class="print-modal-label">인쇄 대상 선택</span>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="full" checked>
        <div>
          <strong>📑 1~3교시 실전 모의고사 풀세트 전체 (추천)</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">1교시 교육학 + 2교시 전공 A형 + 3교시 전공 B형 (각 교시별 페이지 자동 분할)</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="current">
        <div>
          <strong>📄 현재 열려 있는 탭만 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">현재 화면에서 선택된 특정 교시 또는 탭만 집중 인쇄</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="top55">
        <div>
          <strong>⚡ 2027 핵심 55선 콤팩트 암기장 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">교육학 20선 + 전공상담 35선 2열 인쇄용 카드 요약집</div>
        </div>
      </label>
    </div>

    <div class="print-modal-group">
      <span class="print-modal-label">출력 옵션 선택</span>
      <label class="print-option-row">
        <input type="checkbox" id="print-opt-answers" checked>
        <div>
          <strong>🏆 KICE 4점 만점 모범답안 및 채점기준표 포함</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">체크 해제 시 실제 시험장용 '빈 답안 작성란'으로 인쇄됩니다.</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="checkbox" id="print-opt-user">
        <div>
          <strong>✍️ 내가 웹에서 직접 작성한 답안 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">웹페이지 답안란에 입력해 둔 내용을 그대로 종이에 인쇄합니다.</div>
        </div>
      </label>
    </div>

    <div class="print-modal-actions">
      <button class="btn-print-cancel" onclick="closePrintModal()">닫기</button>
      <button class="btn-print-confirm" onclick="executePrint()">
        <span>🖨️</span> A4 인쇄 시작 (미리보기)
      </button>
    </div>
  </div>
</div>


<div class="control-bar" id="control-bar">
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="search-input" placeholder="이론명, 학자명, 키워드 실시간 검색..." oninput="handleSearch()">
  </div>

  <div class="tool-group" id="top55-filters">
    <button class="tool-btn active-toggle" onclick="filterTop55('all', this)">전체 55개</button>
    <button class="tool-btn" onclick="filterTop55('pedagogy', this)">교육학 20선</button>
    <button class="tool-btn" onclick="filterTop55('counseling', this)">전공상담 35선</button>
  </div>
</div>

<div class="progress-wrap" id="progress-wrap">
  <div class="progress-bar-bg">
    <div class="progress-bar-fill" id="progress-fill"></div>
  </div>
  <div class="progress-text">
    <span id="progress-label">암기 완료: 0 / 55개 (0%)</span>
    <span>한국교육과정평가원(KICE) 7개년 정식 공인 키워드 100% 탑재</span>
  </div>
</div>

<main class="content-area">

  <!-- ==================== TAB 1: TOP 55 COMPACT DRILL ==================== -->
  <section class="tab-section active" id="sec-top55">
    <div class="print-page-header">
      <h2>2027 KICE 중등임용 전문상담 & 교육학 영구동결 핵심 55선 암기장</h2>
      <p>한국교육과정평가원(KICE) 7개년 기출 검증 공인 키워드 100% 수록 | 2열 콤팩트 스피드 암기</p>
    </div>
    <div class="notice-banner">
      <div>
        <h3>⚡ 2027 KICE 영구 동결 55개 핵심 출제 풀 스피드 마스터</h3>
        <p>기출 7개년 전수 분석 완료! 우측 상단 '키워드 가리기'를 켜고 능동적 인출(Active Recall) 훈련을 진행하세요.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--gold); font-weight: 700;">
        교육학 20선 + 전공상담 35선 = 총 55개
      </div>
    </div>

    <div class="card-grid" id="top55-grid"></div>
  </section>

  <!-- ==================== TAB 2: PEDAGOGY ESSAY ==================== -->
  <section class="tab-section" id="sec-pedagogy">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>1교시 교육학 논술 [배점 20점 만점 / 시험시간 60분]</p>
    </div>
    <div class="notice-banner">
      <div>
        <h3>🎓 1교시 교육학 논술 모의고사 [총점 20점 만점 / 16개 세부 소문항 규격]</h3>
        <p>2026 소진 이론 완전 배제! 2027 0순위 4대 영역(교육과정·교육방법·교육평가·교육행정) 16개 세부 발문 실전 시험지</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--sky); font-weight: 700;">
        시험 시간: 60분 (B4 답안지 1페이지)
      </div>
    </div>

    <div class="exam-full-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <h2 style="font-size:1.15rem; color:#fff;" id="ped-title"></h2>
        <span class="badge badge-score">20점 만점</span>
      </div>
      
      <div class="exam-case-box" id="ped-case"></div>

      <div class="exam-instructions">
        <strong>&lt;작성 방법 및 채점 지침&gt;</strong>
        <ul>
          <li>논술의 내용: 교육과정(4점), 교육방법(4점), 교육평가(4점), 교육행정(4점) 총 16점</li>
          <li>논술의 구성 및 표현: 논술의 체계(서론·본론·결론 결속성) 및 분량·맞춤법 4점</li>
          <li>반드시 KICE 공인 용어로 서술하고, B4 답안지 기준 1줄당 38~45자 규격을 준수할 것.</li>
        </ul>
      </div>

      <div id="ped-domain-cards"></div>
    </div>
  </section>

  <!-- ==================== TAB 3: SPECIALTY A ==================== -->
  <section class="tab-section" id="sec-qa">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>2교시 전공상담 A형 [12문항 40점 만점 / 시험시간 90분]</p>
    </div>
    <div class="notice-banner">
      <div>
        <h3>📘 2교시 전공상담 A형 실전 모의고사 [12문항 / 40점 만점]</h3>
        <p>기입형 1~4번 (각 2점) + 서술형 5~12번 (각 4점). 답안을 입력하면 하단에 KICE 4점 만점 모범답안이 즉시 열립니다.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--purple); font-weight: 700;">
        시험 시간: 90분
      </div>
    </div>

    <div class="quick-nav" id="quick-nav-a"></div>
    <div id="qa-container"></div>
  </section>

  <!-- ==================== TAB 4: SPECIALTY B ==================== -->
  <section class="tab-section" id="sec-qb">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>3교시 전공상담 B형 [11문항 40점 만점 / 시험시간 90분]</p>
    </div>
    <div class="notice-banner">
      <div>
        <h3>📙 3교시 전공상담 B형 실전 모의고사 [11문항 / 40점 만점]</h3>
        <p>기입형 1~2번 (각 2점) + 서술형 3~11번 (각 4점). 80% 이상 복합형 킬러 문항으로 구성되었습니다.</p>
      </div>
      <div style="font-size: 0.85rem; color: var(--gold); font-weight: 700;">
        시험 시간: 90분
      </div>
    </div>

    <div class="quick-nav" id="quick-nav-b"></div>
    <div id="qb-container"></div>
  </section>

</main>

<script>
const rawData = ${jsonStr};

// State
let currentTab = 'top55';
let blindMode = false;
let currentFilter = 'all';
let searchQuery = '';
let timeLeft = 60 * 60;
let timerRunning = false;
let timerInterval = null;

// Initialize
window.addEventListener('DOMContentLoaded', () => {
  renderTop55();
  renderPedagogy();
  renderExamQuestions('A');
  renderExamQuestions('B');
  updateProgress();
  loadAllSavedAnswers();
  updateTimerDisplay();
});

// Tab Switcher
function switchTab(tab) {
  currentTab = tab;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
  
  const targetBtn = document.getElementById('tab-btn-' + tab);
  const targetSec = document.getElementById('sec-' + tab);
  if (targetBtn) targetBtn.classList.add('active');
  if (targetSec) targetSec.classList.add('active');

  const top55Filters = document.getElementById('top55-filters');
  const progressWrap = document.getElementById('progress-wrap');
  if (tab === 'top55') {
    if (top55Filters) top55Filters.style.display = 'flex';
    if (progressWrap) progressWrap.style.display = 'block';
  } else {
    if (top55Filters) top55Filters.style.display = 'none';
    if (progressWrap) progressWrap.style.display = 'none';
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Blind Mode Toggle
function toggleBlindMode() {
  blindMode = !blindMode;
  document.body.classList.toggle('blind-mode', blindMode);
  const btn = document.getElementById('blind-toggle-btn');
  const label = document.getElementById('blind-label');
  if (blindMode) {
    if (btn) btn.classList.add('active-toggle');
    if (label) label.innerText = '키워드 공개하기';
  } else {
    if (btn) btn.classList.remove('active-toggle');
    if (label) label.innerText = '키워드 가리기';
  }
}

// Render Top55 Cards
function renderTop55() {
  const container = document.getElementById('top55-grid');
  if (!container) return;
  container.innerHTML = '';

  const filtered = rawData.top55.filter(item => {
    const matchFilter = (currentFilter === 'all') || 
                        (currentFilter === 'pedagogy' && item.type === 'pedagogy') ||
                        (currentFilter === 'counseling' && item.type !== 'pedagogy');
    
    const q = searchQuery.toLowerCase();
    const matchSearch = !q || 
                        item.question.toLowerCase().includes(q) ||
                        item.raw_keywords.toLowerCase().includes(q) ||
                        item.answer.toLowerCase().includes(q) ||
                        item.code.toLowerCase().includes(q);

    return matchFilter && matchSearch;
  });

  filtered.forEach(item => {
    const isMemorized = localStorage.getItem('top55_chk_' + item.code) === 'true';
    const card = document.createElement('div');
    card.className = 'item-card ' + (isMemorized ? 'memorized' : '');
    card.id = 'top55-card-' + item.code;

    const kwTags = item.keywords.map(kw => '<span class="kw-tag" onclick="this.classList.toggle(\\'revealed\\')">' + kw + '</span>').join('');

    card.innerHTML = 
      '<div class="card-top">' +
        '<div class="badge-group">' +
          '<span class="badge badge-code">' + item.code + '</span>' +
          '<span class="badge ' + (item.type === 'pedagogy' ? 'badge-pedagogy' : 'badge-category') + '">' + item.category + '</span>' +
        '</div>' +
        '<label class="memorize-chk">' +
          '<input type="checkbox" ' + (isMemorized ? 'checked' : '') + ' onchange="toggleMemorized(\\'' + item.code + '\\', this.checked)">' +
          '외웠어요' +
        '</label>' +
      '</div>' +
      '<div class="card-question">' + item.question + '</div>' +
      '<div class="keyword-tags">' + kwTags + '</div>' +
      '<div class="compact-answer-box">' + item.answer + '</div>';

    container.appendChild(card);
  });
}

function filterTop55(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll('#top55-filters .tool-btn').forEach(b => b.classList.remove('active-toggle'));
  btn.classList.add('active-toggle');
  renderTop55();
}

function handleSearch() {
  searchQuery = document.getElementById('search-input').value.trim();
  renderTop55();
}

function toggleMemorized(code, checked) {
  localStorage.setItem('top55_chk_' + code, checked);
  const card = document.getElementById('top55-card-' + code);
  if (card) {
    card.classList.toggle('memorized', checked);
  }
  updateProgress();
}

function updateProgress() {
  const total = rawData.top55.length;
  let count = 0;
  rawData.top55.forEach(i => {
    if (localStorage.getItem('top55_chk_' + i.code) === 'true') count++;
  });
  const pct = Math.round((count / total) * 100);
  const fill = document.getElementById('progress-fill');
  const label = document.getElementById('progress-label');
  if (fill) fill.style.width = pct + '%';
  if (label) label.innerText = '암기 완료: ' + count + ' / ' + total + '개 (' + pct + '%)';
}

// Render Pedagogy Essay
function renderPedagogy() {
  const ped = rawData.pedagogy;
  if (!ped || !ped.domains) return;

    const pedTitleEl = document.getElementById('ped-title');
  const pedCaseEl = document.getElementById('ped-case');
  if (pedTitleEl) pedTitleEl.innerText = ped.title || '2027학년도 중등교사 임용후보자 선정경쟁시험 1교시 교육학 논술';
  if (pedCaseEl) pedCaseEl.innerText = ped.case || '';

  const container = document.getElementById('ped-domain-cards');
  if (!container) return;
  container.innerHTML = '';

  ped.domains.forEach(d => {
    const card = document.createElement('div');
    card.className = 'exam-full-card';
    card.id = 'ped-card-' + d.id;

    const subQList = d.sub_questions.map(q => '<li style="margin-bottom:4px;">' + q + '</li>').join('');
    const kwBadges = d.keywords.map(kw => '<span class="kw-tag">' + kw + '</span>').join('');
    const compactLines = d.compact_answers.join('\\n');
    const rubricItems = d.rubric.map(r => '<div class="rubric-item"><span>✓</span><span>' + r + '</span></div>').join('');

    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge badge-pedagogy" style="font-size:0.78rem;">' + d.name + ' 영역</span>' +
          '<strong style="color:#fff; font-size:0.92rem;">' + d.theory + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + d.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; padding:10px 14px; font-size:0.84rem; color:#e2e8f0; max-height:260px; overflow-y:auto;">' +
            '<strong style="color:var(--sky); font-size:0.82rem;">[세부 질문 4개]</strong>' +
            '<ol style="margin-left:16px; margin-top:4px; line-height:1.5;">' + subQList + '</ol>' +
          '</div>' +
          '<div class="keyword-tags" style="margin-top:4px;">' + kwBadges + '</div>' +
        '</div>' +
        '<div class="exam-right-col">' +
          '<div class="answer-box-wrap">' +
            '<div class="answer-box-header">' +
              '<span>✍️ B4 실전 답안 작성란 (작성 시 모범답안 즉시 표시)</span>' +
              '<span class="char-count-badge" id="ped-counter-' + d.id + '">0자</span>' +
            '</div>' +
            '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)"></textarea>' +
            '<div class="print-paper-answer">' +
              '<div class="print-written-text" id="ped-print-user-' + d.id + '"></div>' +
              '<div class="print-blank-lines">' +
                '<div class="p-line">1. ________________________________________________________________</div>' +
                '<div class="p-line">2. ________________________________________________________________</div>' +
                '<div class="p-line">3. ________________________________________________________________</div>' +
                '<div class="p-line">4. ________________________________________________________________</div>' +
              '</div>' +
            '</div>' +
            '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +
              '<div class="model-answer-title">🏆 KICE 공인 4점 만점 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + compactLines + '</div>' +
              '<div class="rubric-list">' +
                '<strong>[KICE 4점 채점표]</strong>' + rubricItems +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    container.appendChild(card);

    // Event listener for input
    const ta = card.querySelector('#ped-input-' + d.id);
    if (ta) {
      ta.addEventListener('input', () => handlePedInput(d.id));
    }
  });
}

function handlePedInput(domainId) {
  const txt = document.getElementById('ped-input-' + domainId);
  const counter = document.getElementById('ped-counter-' + domainId);
  const ansPanel = document.getElementById('ped-ans-' + domainId);
  
  if (!txt) return;
  const val = txt.value;
  if (counter) counter.innerText = val.length + '자';

  if (ansPanel) {
    if (val.length > 0) {
      ansPanel.classList.add('show');
      localStorage.setItem('kice_ped_' + domainId, val);
    } else {
      ansPanel.classList.remove('show');
      localStorage.removeItem('kice_ped_' + domainId);
    }
  }
}

// Render Specialty Questions (A & B)
function renderExamQuestions(type) {
  const container = document.getElementById('q' + type.toLowerCase() + '-container');
  const navContainer = document.getElementById('quick-nav-' + type.toLowerCase());
  const questions = (type === 'A') ? rawData.questions_a : rawData.questions_b;

  if (!container || !navContainer) return;
  container.innerHTML = '';
  navContainer.innerHTML = '';

  questions.forEach(q => {
    // Nav Button
    const navBtn = document.createElement('button');
    navBtn.className = 'quick-nav-btn';
    navBtn.id = 'nav-btn-' + type + '-' + q.num;
    navBtn.innerText = q.num + '번';
    navBtn.onclick = () => {
      const el = document.getElementById('exam-card-' + type + '-' + q.num);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    };
    navContainer.appendChild(navBtn);

    // Question Card
    const card = document.createElement('div');
    card.className = 'exam-full-card';
    card.id = 'exam-card-' + type + '-' + q.num;

    let instHtml = '';
    if (q.instructions && q.instructions.trim()) {
      const parts = q.instructions.split('○').map(p => p.trim()).filter(Boolean);
      let contentHtml = '<strong style="color:var(--gold); display:block; margin-bottom:6px; font-size:0.82rem;">&lt;작성 방법&gt;</strong>';
      parts.forEach(p => {
        if (!p.includes('<작성 방법>')) {
          contentHtml += '<div style="margin-bottom:6px; line-height:1.5;">○ ' + p + '</div>';
        }
      });
      instHtml = '<div class="exam-instructions">' + contentHtml + '</div>';
    }

    card.innerHTML = 
      '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">' +
        '<div style="display:flex; align-items:center; gap:6px;">' +
          '<span class="badge ' + (type === 'A' ? 'badge-category' : 'badge-code') + '" style="font-size:0.78rem;">[' + type + '형 ' + q.num + '번]</span>' +
          '<span class="badge ' + (q.type === '기입형' ? 'badge-pedagogy' : 'badge-score') + '" style="font-size:0.75rem;">' + q.type + '</span>' +
          '<strong style="color:#fff; font-size:0.92rem;">' + q.title + '</strong>' +
        '</div>' +
        '<span class="badge badge-score" style="font-size:0.75rem;">' + q.score + '점</span>' +
      '</div>' +
      '<div class="exam-split-grid">' +
        '<div class="exam-left-col">' +
          '<div class="exam-case-box">' + q.content + '</div>' +
          instHtml +
        '</div>' +
        '<div class="exam-right-col">' +
          '<div class="answer-box-wrap">' +
            '<div class="answer-box-header">' +
              '<span>✍️ B4 실전 답안 작성란 (입력 시 모범답안 즉시 표시)</span>' +
              '<span class="char-count-badge" id="counter-' + type + '-' + q.num + '">0자</span>' +
            '</div>' +
            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)"></textarea>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +
              '<div class="model-answer-title">🏆 KICE 만점 공식 모범답안 및 채점기준</div>' +
              '<div class="model-answer-text">' + q.answer + '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';

    container.appendChild(card);

    // Event listener for input
    const ta = card.querySelector('#input-' + type + '-' + q.num);
    if (ta) {
      ta.addEventListener('input', () => handleExamInput(type, q.num));
    }
  });
}

function handleExamInput(type, num) {
  const textarea = document.getElementById('input-' + type + '-' + num);
  const ansBox = document.getElementById('ansbox-' + type + '-' + num);
  const counter = document.getElementById('counter-' + type + '-' + num);
  const navBtn = document.getElementById('nav-btn-' + type + '-' + num);

  if (!textarea) return;
  const val = textarea.value;
  if (counter) counter.innerText = val.length + '자';

  if (val.trim().length > 0) {
    if (ansBox) ansBox.classList.add('show');
    if (navBtn) navBtn.classList.add('written');
    localStorage.setItem('kice_ans_' + type + '_' + num, val);
  } else {
    if (ansBox) ansBox.classList.remove('show');
    if (navBtn) navBtn.classList.remove('written');
    localStorage.removeItem('kice_ans_' + type + '_' + num);
  }
}

// Load Saved Answers
function loadAllSavedAnswers() {
  if (rawData.pedagogy && rawData.pedagogy.domains) {
    rawData.pedagogy.domains.forEach(d => {
      const saved = localStorage.getItem('kice_ped_' + d.id);
      if (saved) {
        const txt = document.getElementById('ped-input-' + d.id);
        if (txt) {
          txt.value = saved;
          handlePedInput(d.id);
        }
      }
    });
  }

  ['A', 'B'].forEach(type => {
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    if (list) {
      list.forEach(q => {
        const saved = localStorage.getItem('kice_ans_' + type + '_' + q.num);
        if (saved) {
          const txt = document.getElementById('input-' + type + '-' + q.num);
          if (txt) {
            txt.value = saved;
            handleExamInput(type, q.num);
          }
        }
      });
    }
  });
}

// Timer Functions
function updateTimerDisplay() {
  const m = Math.floor(timeLeft / 60);
  const s = timeLeft % 60;
  const disp = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  const clock = document.getElementById('timer-display');
  if (clock) {
    clock.innerText = disp;
    clock.style.color = (timeLeft <= 300) ? 'var(--rose)' : 'var(--gold)';
  }
}

function toggleTimer() {
  const btn = document.getElementById('timer-btn');
  if (timerRunning) {
    clearInterval(timerInterval);
    timerRunning = false;
    if (btn) btn.innerText = '재개';
  } else {
    timerRunning = true;
    if (btn) btn.innerText = '일시정지';
    timerInterval = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        alert('시험 시간이 종료되었습니다!');
      }
    }, 1000);
  }
}

function resetTimer(mins) {
  clearInterval(timerInterval);
  timerRunning = false;
  timeLeft = mins * 60;
  updateTimerDisplay();
  const btn = document.getElementById('timer-btn');
  if (btn) btn.innerText = '시작';
}

// Export Answers to Clipboard
function exportAnswers() {
  let text = '=== [2027 KICE 임용고시 작성 답안 모음] ===\\n\\n';
  
  text += '--- [1교시 교육학 논술] ---\\n';
  if (rawData.pedagogy && rawData.pedagogy.domains) {
    rawData.pedagogy.domains.forEach(d => {
      const ans = localStorage.getItem('kice_ped_' + d.id) || '(미작성)';
      text += '[' + d.name + ' 영역 (' + d.theory + ')]:\\n' + ans + '\\n\\n';
    });
  }

  ['A', 'B'].forEach(type => {
    text += '\\n--- [전공 ' + type + '형] ---\\n';
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    if (list) {
      list.forEach(q => {
        const ans = localStorage.getItem('kice_ans_' + type + '_' + q.num) || '(미작성)';
        text += '[' + q.num + '번 (' + q.type + ' ' + q.score + '점)]:\\n' + ans + '\\n\\n';
      });
    }
  });

  navigator.clipboard.writeText(text).then(() => {
    alert('작성하신 모든 답안이 클립보드에 복사되었습니다! 메모장이나 한글 파일에 붙여넣기 하실 수 있습니다.');
  }).catch(() => {
    alert('클립보드 복사에 실패했습니다. 권한을 확인해주세요.');
  });
}

// Print Functions
function openPrintModal() {
  const modal = document.getElementById('print-modal');
  if (modal) modal.classList.add('active');
}

function closePrintModal() {
  const modal = document.getElementById('print-modal');
  if (modal) modal.classList.remove('active');
}

function executePrint() {
  const scopeEl = document.querySelector('input[name="print-scope"]:checked');
  const scope = scopeEl ? scopeEl.value : 'full';
  const includeAnswers = document.getElementById('print-opt-answers').checked;
  const includeUser = document.getElementById('print-opt-user').checked;

  // Sync all user inputs to print-written-text boxes
  if (rawData.pedagogy && rawData.pedagogy.domains) {
    rawData.pedagogy.domains.forEach(d => {
      const ta = document.getElementById('ped-input-' + d.id);
      const pu = document.getElementById('ped-print-user-' + d.id);
      if (ta && pu) pu.innerText = ta.value || '';
    });
  }

  ['A', 'B'].forEach(type => {
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    if (list) {
      list.forEach(q => {
        const ta = document.getElementById('input-' + type + '-' + q.num);
        const pu = document.getElementById('print-user-' + type + '-' + q.num);
        if (ta && pu) pu.innerText = ta.value || '';
      });
    }
  });

  // Apply print classes to body
  document.body.classList.remove('print-scope-full', 'print-scope-current', 'print-scope-top55', 'print-with-answers', 'print-with-user');

  document.body.classList.add('print-scope-' + scope);
  if (includeAnswers) document.body.classList.add('print-with-answers');
  if (includeUser) document.body.classList.add('print-with-user');

  closePrintModal();

  setTimeout(() => {
    window.print();
  }, 150);
}

// Reset print classes after printing
window.addEventListener('afterprint', () => {
  document.body.classList.remove('print-scope-full', 'print-scope-current', 'print-scope-top55', 'print-with-answers', 'print-with-user');
});

</script>
</body>
</html>`;

// 4. Validate script syntax
const scriptMatch = htmlTemplate.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
  try {
    new vm.Script(scriptMatch[1]);
    console.log('✅ JAVASCRIPT SYNTAX VALIDATED PERFECTLY! Zero errors!');
  } catch (err) {
    console.error('❌ JS Syntax Error detected:', err);
    process.exit(1);
  }
}

// 5. Write to targets
const targets = [
  path.join(__dirname, 'exam_master_2027.html'),
  path.join(__dirname, '교육학/exam_master_2027.html'),
  path.join(__dirname, '../전문상담임용고시/exam_master_2027.html')
];

targets.forEach(t => {
  try {
    fs.mkdirSync(path.dirname(t), { recursive: true });
    fs.writeFileSync(t, htmlTemplate, 'utf8');
    console.log(`✅ File written to: ${t} (${htmlTemplate.length.toLocaleString()} bytes)`);
  } catch (e) {
    console.error(`Failed to write to ${t}:`, e.message);
  }
});

console.log('🎉 ALL EXAM MASTER TARGETS CREATED AND VALIDATED!');
