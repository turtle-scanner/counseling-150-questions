const fs = require('fs');
const filePath = '교육학/scratch/top55_extracted.json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

let changeCount = 0;

data.forEach((item, idx) => {
  // P04: 파이나 실존적 재개념주의 (쿠레레 currere 자서전적 방법)
  if (item.id === 'P007') {
    item.question = '파이나의 실존적 재개념주의에서 제시한 쿠레레(currere) 자서전적 방법 4단계를 순서대로 제시하시오.';
    item.keyword = '소환(회상), 전진, 분석, 종합';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 소환(회상) ➔ 전진 ➔ 분석 ➔ 종합<br>과거 경험을 회상하고 미래를 전망한 뒤, 이를 분석하고 현재 의미로 종합하여 개인의 생애사적 주체성을 재구성한다.</mark>';
    item.clean_ans = '정답: 소환(회상) ➔ 전진 ➔ 분석 ➔ 종합 과거 경험을 회상하고 미래를 전망한 뒤, 이를 분석하고 현재 의미로 종합하여 개인의 생애사적 주체성을 재구성한다.';
    changeCount++;
  }

  // P18: 스크리븐(Scriven) 탈목표(목표비구속) 평가 모형
  if (item.id === 'P036') {
    item.question = '스크리븐의 탈목표(목표비구속) 평가 모형에서 평가자가 프로그램의 사전 목표에 구속되지 않고 실제 나타난 모든 부수 효과까지 평가하는 개념을 서술하시오.';
    item.keyword = '목표 비구속, 의도하지 않은 부수 효과, 탈목표 평가';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 탈목표 평가 (목표비구속 평가)<br>프로그램의 사전 의도 목표뿐만 아니라 의도하지 않은 실제 부수 효과와 잠재적 부작용까지 종합적으로 평가한다.</mark>';
    item.clean_ans = '정답: 탈목표 평가 (목표비구속 평가) 프로그램의 사전 의도 목표뿐만 아니라 의도하지 않은 실제 부수 효과와 잠재적 부작용까지 종합적으로 평가한다.';
    changeCount++;
  }

  // C33: 파괴적 기분조절부전장애(DMDD) 정식명칭 보완
  if (item.id === 'Q026') {
    item.question = '주 3회 이상의 심한 분노 발작을 보이며, 발작이 없는 평상시에도 만성적으로 성마른 기분을 유지하는 DSM-5-TR 장애 명칭을 쓰시오.';
    item.keyword = '주 3회 분노 발작, 만성 성마른 기분, 1년 이상';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 파괴적 기분조절부전장애 (DMDD)<br>심한 분노 발작과 발작 사이 평상시에도 만성적으로 성마르고 과민한 기분을 1년 이상 유지하는 것이 핵심 감별 기준이다.</mark>';
    item.clean_ans = '정답: 파괴적 기분조절부전장애 (DMDD) 심한 분노 발작과 발작 사이 평상시에도 만성적으로 성마르고 과민한 기분을 1년 이상 유지하는 것이 핵심 감별 기준이다.';
    changeCount++;
  }

  // C37: 탈억제 사회관여 장애(DSED) DSM-5-TR 정식명칭 보완
  if (item.id === 'Q031') {
    item.question = '애착 형성 결여로 인해 낯선 성인에게 주저함 없이 접근하고 과도한 친밀감을 표출하는 DSM-5-TR 아동 장애의 정식 명칭을 서술하시오.';
    item.keyword = '낯선 성인 과도 친밀, 주저함 없음, 탈억제 사회관여';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 탈억제 사회관여 장애 (DSED)<br>낯선 성인에게 주저함 없이 다가가 과도한 친밀감을 표출하며 친숙한 보호자에 대한 선택적 애착 행동이 결여된 장애이다.</mark>';
    item.clean_ans = '정답: 탈억제 사회관여 장애 (DSED) 낯선 성인에게 주저함 없이 다가가 과도한 친밀감을 표출하며 친숙한 보호자에 대한 선택적 애착 행동이 결여된 장애이다.';
    changeCount++;
  }

  // C45: 게슈탈트 융합 오타(서갈등) 수정
  if (item.id === 'Q097') {
    item.answer = item.answer.replace('서갈등', '갈등');
    item.clean_ans = item.clean_ans.replace('서갈등', '갈등');
    changeCount++;
  }

  // C54: 제1호 조치 오타(공식 공칭) 수정
  if (item.id === 'Q145') {
    item.question = '학교폭력예방법상 가해학생에게 내리는 제1호 조치 처분의 법률상 공식 명칭을 작성하시오.';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 피해학생에 대한 서면사과<br>가해학생에게 내리는 제1호 조치의 법률상 공식 명칭은 "피해학생에 대한 서면사과"이다.</mark>';
    item.clean_ans = '정답: 피해학생에 대한 서면사과 가해학생에게 내리는 제1호 조치의 법률상 공식 명칭은 "피해학생에 대한 서면사과"이다.';
    changeCount++;
  }

  // C55: 교권보호 전담 기구 오타(개관되는) 수정
  if (item.id === 'Q150') {
    item.question = '교권보호 4법에 따라 정당한 생활지도권을 보호하고 교원 교육활동 침해 시 개최·설치되는 교육지원청 전담 기구의 명칭을 작성하시오.';
    item.answer = '<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">정답: 지역교권보호위원회<br>교원의 정당한 교육활동과 생활지도권을 보장하고 침해 사안 발생 시 교육지원청 단위의 지역교권보호위원회를 개최하여 심의·의결한다.</mark>';
    item.clean_ans = '정답: 지역교권보호위원회 교원의 정당한 교육활동과 생활지도권을 보장하고 침해 사안 발생 시 교육지원청 단위의 지역교권보호위원회를 개최하여 심의·의결한다.';
    changeCount++;
  }
});

fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
console.log(`✅ Fixed and standardized ${changeCount} items in top55_extracted.json!`);
