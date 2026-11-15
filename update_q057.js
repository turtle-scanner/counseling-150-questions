const fs = require('fs');
const filePath = '교육학/scratch/top55_extracted.json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

// Find Q057
const target = data.find(item => item.id === 'Q057');
if (target) {
  target.question = 'K-WISC-V 지표 중 토막짜기와 시각퍼즐 소검사로 구성되며 시각적 세부 인지 및 공간 처리 능력을 평가하는 지표 명칭을 쓰시오.';
  target.keyword = '시공간 처리, 시각퍼즐, 토막짜기';
  target.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 시공간 지표 (VSI)<br>시각적 자극의 구성 및 공간적 관계 분석 능력을 평가하며, 토막짜기와 퍼즐(시각퍼즐) 2가지 핵심 소검사로 구성된다.</mark>';
  target.clean_ans = '정답: 시공간 지표 (VSI) 시각적 자극의 구성 및 공간적 관계 분석 능력을 평가하며, 토막짜기와 퍼즐(시각퍼즐) 2가지 핵심 소검사로 구성된다.';
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
  console.log('✅ top55_extracted.json Q057 updated successfully!');
} else {
  console.error('Q057 not found in top55_extracted.json');
}
