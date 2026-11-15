const fs = require('fs');

const filePath = '교육학/exam_2027_kice_ab.html';
let html = fs.readFileSync(filePath, 'utf8');

const matchA = html.match(/const examDataA = (\[[\s\S]*?\]);/);
const matchB = html.match(/const examDataB = (\[[\s\S]*?\]);/);

if (!matchA || !matchB) {
  console.error('Failed to match examDataA or examDataB');
  process.exit(1);
}

let qA = JSON.parse(matchA[1]);
let qB = JSON.parse(matchB[1]);

// Cleaning function for English full names
function cleanEnglishText(text) {
  if (!text) return text;
  
  // Specific mappings first
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
    .replace(/관심\(Concern\)/g, '관심')
    .replace(/통제\(Control\)/g, '통제')
    .replace(/호기심\(Curiosity\)/g, '호기심')
    .replace(/자신감\(Confidence\)/g, '자신감')
    .replace(/지지 제공\(Providing Support\)/g, '지지 제공')
    .replace(/다짐 받기\(Obtaining Commitment\)/g, '다짐 받기')
    .replace(/토막짜기\(Block Design\)/g, '토막짜기')
    .replace(/시각퍼즐\(Visual Puzzles\)/g, '시각퍼즐')
    .replace(/행렬추론\(Matrix Reasoning\)/g, '행렬추론')
    .replace(/무게비교\(Figure Weights\)/g, '무게비교')
    .replace(/미세공격\(Microaggression\)/g, '미세공격')
    .replace(/계측성\(Calculus\)/g, '계측성')
    .replace(/일관성\(Consistency\)/g, '일관성')
    .replace(/동일시\(Identification\)/g, '동일시')
    .replace(/제한\(Circumscription\)/g, '제한')
    .replace(/타협\(Compromise\)/g, '타협')
    .replace(/성역할 발달\(Sex-Role Orientation\)/g, '성역할 발달')
    .replace(/성역할 경계선\(Sex-Role Orientation\)/g, '성역할 경계선')
    .replace(/핵심신념\(Core Belief\)/g, '핵심신념')
    .replace(/하향화살표 기법\(Downward Arrow Technique\)/g, '하향화살표 기법')
    .replace(/하향 화살표 기법\(Downward Arrow Technique\)/g, '하향 화살표 기법')
    .replace(/삼각관계\(Triangulation\)/g, '삼각관계')
    .replace(/탈삼각화\(Detriangulation\)/g, '탈삼각화')
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
    .replace(/로샤\(Rorschach\)/g, '로샤')
    .replace(/사비카스\(Savickas\)/g, '사비카스')
    .replace(/길리랜드\(Gilliland\)/g, '길리랜드')
    .replace(/숀 셰이\(Shawn Shea\)/g, '숀 셰이')
    .replace(/욕구\(Need\)/g, '욕구')
    .replace(/압착\(Press\)/g, '압착')
    .replace(/주제\(Thema\)/g, '주제')
    .replace(/나-아님\(Not-me\)/g, '나-아님');

  // Generic removal of remaining English full names in parentheses:
  // e.g. (Dereflection), (Hyperreflection), (Paradoxical Injunction) etc.
  // but preserve standard acronyms like (VSI), (FRI), (DMDD), (ODD), (RAD), (DSED), (SUI), (BXD), (OCD), (ASD), (MMPI), (TCI), (TAT), (ZPD), (4C), (CASE), (L-r / K-r), (F-r), (RCd), (NS), (HA), (RD), (P), (SD), (CO), (ST), (es), (Adj D), (Zf)
  const fullTermsToRemove = [
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
    'Thema', 'Not-me', 'Chronological Assessment of Suicide Events'
  ];

  fullTermsToRemove.forEach(t => {
    const r = new RegExp('\\s*\\(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\)', 'g');
    res = res.replace(r, '');
  });

  return res;
}

function cleanQuestion(q) {
  q.title = cleanEnglishText(q.title);
  q.content = cleanEnglishText(q.content);
  q.instructions = cleanEnglishText(q.instructions);
  q.answer = cleanEnglishText(q.answer);
  return q;
}

qA = qA.map(cleanQuestion);
qB = qB.map(cleanQuestion);

// Specifically format B7 to strict B4 38-45 char standard with Zero English Full Names
const qB7 = qB.find(q => q.num === 7);
if (qB7) {
  qB7.answer = `[모범답안]
[사례 1] 기법은 탈숙고이며, 증상에 쏠린 과잉주의를 의도적으로 차단하고
긍정적 가치로 주의를 전환하여 문제에 대한 예기불안 악순환을 해소한다.
[사례 2] 기법은 역설적 지시(증상 처방)이며 통제 불가한 증상을 고의로
수행하게 처방하여 증상이 자발적 통제 하에 있음을 깨닫게 해 소거한다.

[KICE 4점 만점 채점 기준표]
- 탈숙고 기법 명칭 명시 및 과잉주의 차단/가치 전환 기제 서술: 2점
- 역설적 지시(증상 처방) 기법 명칭 명시: 1점
- 증상의 고의적 수행을 통해 자발적 통제 가능성을 자각시키는 메커니즘 서술: 1점`;
}

// Replace in html
html = html.replace(/const examDataA = \[[\s\S]*?\];/, 'const examDataA = ' + JSON.stringify(qA, null, 2) + ';');
html = html.replace(/const examDataB = \[[\s\S]*?\];/, 'const examDataB = ' + JSON.stringify(qB, null, 2) + ';');

fs.writeFileSync(filePath, html, 'utf8');
console.log('✅ exam_2027_kice_ab.html questions cleaned and B7 updated to B4 38-45 format!');
