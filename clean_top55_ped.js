const fs = require('fs');

// 1. Clean top55_extracted.json
const top55Path = '교육학/scratch/top55_extracted.json';
const top55Data = JSON.parse(fs.readFileSync(top55Path, 'utf8'));

function cleanText(text) {
  if (!text) return text;
  return text
    .replace(/탈숙고\(Dereflection\)/g, '탈숙고')
    .replace(/과잉주의\(Hyperreflection\)/g, '과잉주의')
    .replace(/역설적 지시\(Paradoxical Injunction \/ 증상 처방\)/g, '역설적 지시(증상 처방)')
    .replace(/역설적 지시\(Paradoxical Injunction\)/g, '역설적 지시(증상 처방)')
    .replace(/명확한 경계선\(Clear boundary\)/g, '명확한 경계선')
    .replace(/실연\(Enactment\)/g, '실연')
    .replace(/반전\(Retroflection\)/g, '반전')
    .replace(/빈 의자 기법\(Empty Chair Technique\)/g, '빈 의자 기법')
    .replace(/토막짜기\(Block Design\)/g, '토막짜기')
    .replace(/시각퍼즐\(Visual Puzzles\)/g, '시각퍼즐')
    .replace(/행렬추론\(Matrix Reasoning\)/g, '행렬추론')
    .replace(/무게비교\(Figure Weights\)/g, '무게비교')
    .replace(/미세공격\(Microaggression\)/g, '미세공격')
    .replace(/생애 주제\(Life Theme\)/g, '생애 주제')
    .replace(/진로적응도\(Career Adaptability\)/g, '진로적응도')
    .replace(/지지 제공\(Providing Support\)/g, '지지 제공')
    .replace(/다짐 받기\(Obtaining Commitment\)/g, '다짐 받기')
    .replace(/욕구\(Need\)/g, '욕구')
    .replace(/압착\(Press\)/g, '압착')
    .replace(/계측성\(Calculus\)/g, '계측성')
    .replace(/일관성\(Consistency\)/g, '일관성')
    .replace(/동일시\(Identification\)/g, '동일시')
    .replace(/좋은-나\(Good-me\)/g, '좋은-나')
    .replace(/나쁜-나\(Bad-me\)/g, '나쁜-나')
    .replace(/나-아님\(Not-me\)/g, '나-아님')
    .replace(/교사\(Teacher\)/g, '교사')
    .replace(/상담자\(Counselor\)/g, '상담자')
    .replace(/자문가\(Consultant\)/g, '자문가')
    .replace(/자극추구\(Novelty Seeking, NS\)/g, '자극추구(NS)')
    .replace(/위험회피\(Harm Avoidance, HA\)/g, '위험회피(HA)')
    .replace(/보상의존\(Reward Dependence, RD\)/g, '보상의존(RD)')
    .replace(/인내력\(Persistence, P\)/g, '인내력(P)')
    .replace(/자율성\(Self-Directedness, SD\)/g, '자율성(SD)')
    .replace(/협동성\(Cooperativeness, CO\)/g, '협동성(CO)')
    .replace(/자기초월\(Self-Transcendence, ST\)/g, '자기초월(ST)')
    .replace(/\s*\((Dereflection|Hyperreflection|Clear boundary|Enactment|Retroflection|Empty Chair Technique|Block Design|Visual Puzzles|Matrix Reasoning|Figure Weights|Microaggression|Life Theme|Career Adaptability|Providing Support|Obtaining Commitment|Need|Press|Calculus|Consistency|Identification|Good-me|Bad-me|Not-me|Teacher|Counselor|Consultant)\)/g, '');
}

top55Data.forEach(item => {
  item.question = cleanText(item.question);
  item.answer = cleanText(item.answer);
  item.clean_ans = cleanText(item.clean_ans);
  item.keyword = cleanText(item.keyword);
});
fs.writeFileSync(top55Path, JSON.stringify(top55Data, null, 2), 'utf8');
console.log('✅ top55_extracted.json cleaned');

// 2. Clean pedagogy_data.json
const pedPath = 'pedagogy_data.json';
const pedData = JSON.parse(fs.readFileSync(pedPath, 'utf8'));
pedData.domains.forEach(d => {
  d.theory = cleanText(d.theory);
  d.sub_questions = d.sub_questions.map(cleanText);
  d.compact_answers = d.compact_answers.map(cleanText);
  d.keywords = d.keywords.map(cleanText);
  d.rubric = d.rubric.map(cleanText);
});
fs.writeFileSync(pedPath, JSON.stringify(pedData, null, 2), 'utf8');
console.log('✅ pedagogy_data.json cleaned');
