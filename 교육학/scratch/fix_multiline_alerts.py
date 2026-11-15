# -*- coding: utf-8 -*-
with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 줄바꿈이 있는 쌍따옴표 alert 구문들을 백틱(`) 템플릿 리터럴로 안전하게 치환
text = text.replace(
    'alert("📦 [수송 완료]\n\n전선 기지로 군자금 200전과 군량 500석의 보급 수송을 완료했습니다!");',
    'alert(`📦 [수송 완료]\\n\\n전선 기지로 군자금 200전과 군량 500석의 보급 수송을 완료했습니다!`);'
)
text = text.replace(
    'alert("💰 [세율 조정 완료]\n\n세율을 40%로 조정하여 국고에 금 350전이 입고되었습니다.");',
    'alert(`💰 [세율 조정 완료]\\n\\n세율을 40%로 조정하여 국고에 금 350전이 입고되었습니다.`);'
)
text = text.replace(
    'alert("⚓ [누선 함선 건조 완료!]\n\n장강과 수로 전투에서 수군 공격력이 +30% 상승하고 물길 이동력이 +1칸 증가합니다!");',
    'alert(`⚓ [누선 함선 건조 완료!]\\n\\n장강과 수로 전투에서 수군 공격력이 +30% 상승하고 물길 이동력이 +1칸 증가합니다!`);'
)
text = text.replace(
    'alert("💊 [화타 명의 진료 완료!]\n\n아군 전 장수의 체력 100% 회복 및 피로도 0% 완치!");',
    'alert(`💊 [화타 명의 진료 완료!]\\n\\n아군 전 장수의 체력 100% 회복 및 피로도 0% 완치!`);'
)
text = text.replace(
    'alert("🚩 [방랑군 거병]\n\n현재 유비군은 웅대한 본거지를 거느린 정규 군벌이므로 방랑할 필요가 없습니다. 천하통일에 매진하십시오!");',
    'alert(`🚩 [방랑군 거병]\\n\\n현재 유비군은 웅대한 본거지를 거느린 정규 군벌이므로 방랑할 필요가 없습니다. 천하통일에 매진하십시오!`);'
)
text = text.replace(
    'alert(`🚩 [시나리오 ${scenNum} 선택]\n\n영웅집결 & 난세의 영웅들 시나리오가 활성화되었습니다.`);',
    'alert(`🚩 [시나리오 ${scenNum} 선택]\\n\\n영웅집결 & 난세의 영웅들 시나리오가 활성화되었습니다.`);'
)

# 파일 저장 및 전역 동기화
with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'C:/Users/LENOVO/Desktop/sam3_update.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/교육학/samgukji.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/samgukji.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Multiline alerts escaped safely!")
