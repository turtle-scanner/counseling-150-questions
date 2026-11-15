const fs = require('fs');
const filePath = '교육학/scratch/top55_extracted.json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

// 1. Update Q057 (Card C39: VSI - 토막짜기 & 시각퍼즐)
const q057 = data.find(item => item.id === 'Q057');
if (q057) {
  q057.question = 'K-WISC-V 지표 중 토막짜기와 시각퍼즐 소검사로 구성되며 시각적 세부 인지 및 공간 처리 능력을 평가하는 지표 명칭을 쓰시오.';
  q057.keyword = '시공간 지표(VSI), 토막짜기, 시각퍼즐';
  q057.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 시공간 지표 (VSI)<br>시각적 자극의 구성 및 공간적 관계 분석 능력을 평가하며, 토막짜기와 퍼즐(시각퍼즐) 2가지 핵심 소검사로 구성된다.</mark>';
  q057.clean_ans = '정답: 시공간 지표 (VSI) 시각적 자극의 구성 및 공간적 관계 분석 능력을 평가하며, 토막짜기와 퍼즐(시각퍼즐) 2가지 핵심 소검사로 구성된다.';
}

// 2. Update Q058 (Card C40: FRI - 행렬추론 & 무게비교)
const q058 = data.find(item => item.id === 'Q058');
if (q058) {
  q058.question = 'K-WISC-V 지표 중 비구어적 자극의 귀납적·연역적 규칙 추론 능력을 평가하며 행렬추론과 무게비교 소검사를 쓰는 지표 명칭을 쓰시오.';
  q058.keyword = '유동추론 지표(FRI), 행렬추론, 무게비교';
  q058.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 유동추론 지표 (FRI)<br>비구어적 자극 간의 규칙과 원리를 귀납적·연역적으로 추론하는 능력으로, 행렬추론과 무게비교 2대 핵심 소검사로 구성된다.</mark>';
  q058.clean_ans = '정답: 유동추론 지표 (FRI) 비구어적 자극 간의 규칙과 원리를 귀납적·연역적으로 추론하는 능력으로, 행렬추론과 무게비교 2대 핵심 소검사로 구성된다.';
}

fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
console.log('✅ top55_extracted.json Q057 and Q058 updated successfully!');
