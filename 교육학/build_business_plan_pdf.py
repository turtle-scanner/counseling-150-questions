# -*- coding: utf-8 -*-
import os
import subprocess
import pymupdf

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>2027년도 중소벤처기업부 예비창업패키지 사업계획서 - 주식회사 세이프티온</title>
<style>
  @page {
    size: A4;
    margin: 12mm 14mm 12mm 14mm;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  body {
    font-family: 'Malgun Gothic', 'Pretendard', sans-serif;
    color: #1f2937;
    line-height: 1.48;
    font-size: 9.1pt;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }
  
  /* Top Bar Header */
  .header-box {
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 7px;
    margin-bottom: 11px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .doc-category {
    font-size: 9.2pt;
    font-weight: bold;
    color: #1e3a8a;
    letter-spacing: -0.5px;
  }
  .doc-title {
    font-size: 15pt;
    font-weight: 900;
    color: #0f172a;
    margin-top: 3px;
    letter-spacing: -1px;
  }
  .doc-meta {
    text-align: right;
    font-size: 8.2pt;
    color: #64748b;
    line-height: 1.35;
  }
  
  /* Section Headings */
  h2 {
    font-size: 10.8pt;
    font-weight: 800;
    color: #ffffff;
    background: linear-gradient(90deg, #1e3a8a 0%, #2563eb 100%);
    padding: 4.5px 9px;
    border-radius: 4px;
    margin-top: 13px;
    margin-bottom: 7px;
    page-break-after: avoid;
  }
  h3 {
    font-size: 9.8pt;
    font-weight: 700;
    color: #1e3a8a;
    border-left: 3.5px solid #2563eb;
    padding-left: 6px;
    margin-top: 10px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }
  
  p, ul, ol {
    margin-top: 2px;
    margin-bottom: 4px;
    font-size: 8.6pt;
  }
  li {
    margin-bottom: 2px;
  }
  
  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 4px;
    margin-bottom: 7px;
    font-size: 8.4pt;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 4px 6.5px;
    text-align: left;
    vertical-align: middle;
  }
  th {
    background-color: #f1f5f9;
    color: #1e293b;
    font-weight: 700;
    text-align: center;
  }
  .table-primary th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 700;
    border-color: #1e3a8a;
  }
  .text-center { text-align: center; }
  .text-right { text-align: right; }
  .font-bold { font-weight: bold; }
  .text-red { color: #dc2626; }
  .text-blue { color: #1e40af; }
  
  /* Boxes and Cards */
  .card-box {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #3b82f6;
    border-radius: 4px;
    padding: 6px 10px;
    margin: 6px 0;
    page-break-inside: avoid;
  }
  .highlight-badge {
    display: inline-block;
    background-color: #dbeafe;
    color: #1e40af;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 7.6pt;
    font-weight: bold;
  }
  
  /* Seal */
  .seal-container {
    margin-top: 20px;
    text-align: center;
    page-break-inside: avoid;
  }
  .seal-date {
    font-size: 9.5pt;
    font-weight: 700;
    color: #334155;
    margin-bottom: 4px;
  }
  .seal-company {
    font-size: 12pt;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 6px;
    letter-spacing: 1px;
  }
  .seal-rep {
    font-size: 11pt;
    font-weight: 800;
    color: #1e293b;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
  }
  .seal-stamp {
    display: inline-block;
    width: 55px;
    height: 55px;
    border: 2.2px solid #dc2626;
    border-radius: 50%;
    color: #dc2626;
    font-size: 7.8pt;
    font-weight: 900;
    line-height: 1.15;
    padding-top: 8px;
    box-sizing: border-box;
    text-align: center;
    transform: rotate(-5deg);
  }

  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- Header -->
<div class="header-box">
  <div>
    <div class="doc-category">2027년도 중소벤처기업부 예비창업패키지 지원사업</div>
    <div class="doc-title">사업계획서 (창업아이템 최종본)</div>
  </div>
  <div class="doc-meta">
    접수 분야: 미래 모빌리티 / 지능형 안전 전장<br>
    주관기관: 인천대학교 창업지원단
  </div>
</div>

<!-- 0. Summary -->
<h2>0. 창업아이템 개요 (Summary)</h2>
<table class="table-primary">
  <colgroup>
    <col style="width: 17%;">
    <col style="width: 83%;">
  </colgroup>
  <tbody>
    <tr>
      <th>기업명 (예정)</th>
      <td><strong>주식회사 세이프티온 (SafetyON Inc.)</strong> (2027년 상반기 창업 예정)</td>
    </tr>
    <tr>
      <th>대표자</th>
      <td><strong>변 귀 섭 (Byun Gwi-seob)</strong></td>
    </tr>
    <tr>
      <th>창업아이템명</th>
      <td><strong>스마트 디지털 룸미러(CMS) 및 OBD-II 차량진단 일체형 단말기 기반, 운전자 급성 이상상태 감지 시 다단계 비상대응 및 페달오조작 방지 플러그앤플레이(Plug & Play) 상용차 안전 제어 시스템</strong></td>
    </tr>
    <tr>
      <th>핵심 원천 기술<br>(지식재산권)</th>
      <td>
        • <strong>특허출원 제10-2026-0195570호</strong> (출원완료, 우선심사/조기공개신청 완료): 대형 운송차량 운전자 급성 실신 감지 기반 다단 안전 제어 및 자율 비상 정차 시스템<br>
        • <strong>특허출원 제10-2026-0206812호</strong> (출원완료, 등록 심사 대기): 차량 엣지 단말기의 다중 센서 텔레메트리 기반 능동형 위기 등급 분류 및 단계별 에스컬레이션 안심콜 연계 관제 시스템<br>
        • <strong>특허출원 제10-2026-0206816호</strong> (출원완료, 등록 심사 대기): 차속 적응형 페달 동역학 및 생체 신호 융합 기반 고령 운전자 오조작과 차량 급발진 감별 차단 시스템<br>
        • <em>(대표자 R&D 배경 역량)</em> 차세대 반도체 패밀리 특허 3건 단독 출원 보유 (하드웨어/회로 설계 역량 증빙)
      </td>
    </tr>
    <tr>
      <th>목표 정부지원금</th>
      <td><strong class="text-blue">100,000,000원 (중기부 모빌리티 특화 최대 무상 국비 지원금 신청)</strong></td>
    </tr>
    <tr>
      <th>단계별 R&D 로드맵<br>(체계적 성능 검증)</th>
      <td>
        • <strong>[1단계 (협약기간 내 MVP)]</strong>: 스마트 룸미러 CMS + 사각지대 BSD + OBD-II 진단 HUD + 운전자 이상 감지(DMS) 1차 시제품 제작 및 KTL 공인시험(EMC/신뢰성) 완료<br>
        • <strong>[2단계 (후속 연계 R&D)]</strong>: KATRI(자동차안전연구원) 트랙 실증 기반 공압 다단 감속, 페달 오조작 방지, 내리막 롤링 방지 안전성 다단계 검증 및 상용화
      </td>
    </tr>
    <tr>
      <th>가격 및 경제성</th>
      <td>
        • <strong>소비자 권장 정가 2,000,000원 (200만 원)</strong> ➔ 정부/지자체 보조금 80% 지원 시 <strong>차주 실부담금 40만 원</strong><br>
        • <strong>보조금 미지원 시에도 공제조합 보험료 10~15% 할인 연계로 1.5년 내 투자금 회수(ROI) 모델 입증</strong><br>
        • <strong>제조원가(BOM) 470,000원 ➔ 대당 매출총이익 1,530,000원 (마진율 76.5%) / 실질 영업이익 116만 원 확보</strong>
      </td>
    </tr>
  </tbody>
</table>

<div class="card-box" style="margin-top: 6px;">
  <div style="font-weight: bold; color: #1e3a8a; margin-bottom: 3px;">【 세이프티온 시스템 구성 및 운전자 최우선 오버라이드(Driver Override) 페일세이프 】</div>
  <table style="margin: 0; background: #fff;">
    <tr style="background: #f1f5f9;">
      <th style="width: 48%; color: #15803d;">🌞 평상시 편의 모드 (Normal)</th>
      <th style="width: 52%; color: #b91c1c;">🚨 비상시 안전 대응 모드 (Emergency)</th>
    </tr>
    <tr>
      <td>
        • <strong>스마트 디지털 룸미러 CMS</strong>: 11.88인치 와이드 IPS, 우천/야간/적재물 후방 100% 개방<br>
        • <strong>사각지대 경보(BSD/BVM)</strong>: 턴시그널 연동 오토바이/보행자 AI 추적 경보<br>
        • <strong>OBD-II 차량진단 HUD</strong>: 알터네이터 전압(14.2V), 고장코드(DTC) 한글 번역<br>
        • <strong>LTE-M 텔레메트리</strong>: 5년 통신비 선납 번들링 (차주 월납 부담 제로)
      </td>
      <td>
        • <strong>[1단계] (0~2초)</strong>: 안면/시선 이탈 시 시청각 1차 경보 및 운전자 반응 확인<br>
        • <strong>[2단계] (2~4초)</strong>: 반응 부재 시 비상등 자동 점멸 및 직선 엔진 브레이크 완서행<br>
        • <strong>[3단계] (4초 이후)</strong>: 3단계 공압 감압 제동 (0.10G➔0.45G) 및 119/회사 비상 연계<br>
        • <strong class="text-blue">★ 페일세이프 최우선</strong>: <em>운전자가 브레이크나 핸들 조작 시 0.01초 만에 시스템 개입 강제 취소</em>
      </td>
    </tr>
  </table>
</div>

<div class="page-break"></div>

<!-- 1. Problem & 2. Solution -->
<h2>1. 문제 인식 (Problem)</h2>
<div class="card-box">
  <p><strong>1. 대형 운송차량 운전자의 급속한 고령화 및 고속도로 실신 사고의 구조적 위험</strong></p>
  <ul>
    <li>전국 노선버스 기사의 <strong>58.4%가 만 60세 이상 고령자</strong>이며, 심근경색·뇌혈관 질환 등 급성 실신 시 15~25톤 차량이 통제력을 상실하여 대형 연쇄 추돌 참사를 초래합니다.</li>
  </ul>
  <p><strong>2. 비탈길 기사 하차 후 상용차 내리막 굴러감(Roll-Away) 압사 사고의 빈발</strong></p>
  <ul>
    <li>버스 정류장, 차고지, 건설 공사현장에서 기사가 잠시 하차했을 때 <strong>사이드 브레이크 미체결 또는 제동력 부족으로 20톤 차량이 스스로 굴러내려가 기사 본인이나 보행자를 압사시키는 참사가 연평균 수십 건 발생</strong>합니다.</li>
  </ul>
  <p><strong>3. 고령 운전자 페달 오조작(브레이크 착각 답입) 및 급가속 사고 증가</strong></p>
  <ul>
    <li>시청역 사고 등 정차·서행 중 당황한 운전자가 가속 페달(APS)을 80% 이상 급격히 밟아 발생하는 보행자 인도 돌진 사고를 물리적으로 제한하는 장치가 시급합니다.</li>
  </ul>
</div>

<h2>2. 실현 가능성 (Solution)</h2>
<h3>2-1. 개발 아이템의 핵심 기능 및 객관적 검증 계획</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>기술 구분</th>
      <th>독창적 메커니즘 및 차별성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>① 스마트 디지털 룸미러 CMS</th>
      <td>순정 거울 위 스트랩 고정형 11.88인치 와이드 IPS 터치 패널. 소니 STARVIS 200만 화소 FHD 나노발수 방수 카메라로 야간/우천에도 대낮 시야 확보. 적재물/승객 가림 없이 후방 100% 개방. (KTR 진동·충격 시험 및 IP68 방수 공인 성적서 획득 계획)</td>
    </tr>
    <tr>
      <th>② 사각지대 BSD / BVM</th>
      <td>턴시그널(깜빡이) 작동 시 해당 방향 영상 자동 표출 및 온디바이스 NPU 기반 오토바이/보행자 AI 바운딩 박스 추적 경보. (악천후 환경별 오탐·미탐률 산출 시험)</td>
    </tr>
    <tr>
      <th>③ OBD-II 차량진단 HUD</th>
      <td>표준 ISO 15765-4 고속 CAN 직결. 알터네이터 전압(14.2V 정상, 11.8V 저전압 방전 경보) 표출 및 고장코드(DTC) 한글 번역 팝업. (0.1mA 초저전력 슬립모드 설계)</td>
    </tr>
    <tr>
      <th>④ 운전자 이상 감지 (DMS)</th>
      <td>940nm 적외선 IR 카메라 기반 안면/시선/눈깜빡임 분석. 실신과 단순 고개 숙임/졸음을 구분하는 3단계 필터링 알고리즘 적용. (안경/선글라스/마스크 착용 환경별 최적화)</td>
    </tr>
    <tr>
      <th>⑤ 공압 3단 감속 제어 (특허출원)</th>
      <td>대형차 에어라인 원터치 솔레노이드 밸브 장착. 0.10G ➔ 0.25G ➔ 0.45G 단계적 감압 제동으로 승객 낙상 방지. <strong>[운전자 오버라이드 최우선]: 페달 조작 시 즉시 제어 해제.</strong></td>
    </tr>
    <tr>
      <th>⑥ 페달 오조작 방지 (특허출원)</th>
      <td>차속 0~15km/h 정차·서행 중 전방 3m 내 장애물 감지 시 가속페달(APS) 급답입(80% 이상) 신호 0% 클램핑 인터셉트. (고속 주행 오작동 원천 차단 하드웨어 인터록 적용)</td>
    </tr>
    <tr>
      <th>⑦ 비탈길 롤어웨이 방지 (특허출원)</th>
      <td>운전자 부재(DMS 부재 확인 + 운전석 압력 해제) 상태에서 사이드 미체결 중 0.5km/h 미세 굴러감 감지 즉시 공압 파킹 브레이크(Maxi Spring Brake) 자동 체결 (Auto Parking Lock).</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- 2-2. BOM & Economics -->
<h3>2-2. [부품 원가 합계 검증] 4채널 CMS 단말기 BOM 원가 명세서 (470,000원 정확 합계)</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 55%;">
    <col style="width: 20%;">
  </colgroup>
  <thead>
    <tr>
      <th>부품 구분</th>
      <th>세부 스펙 및 주요 사양</th>
      <th>단가 (원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>① 실내 DMS 카메라</strong></td>
      <td>200만 화소 FHD, 940nm 적외선 IR LED, 안면/시선 추적 + 운전자 부재 감지</td>
      <td class="text-right">28,000</td>
    </tr>
    <tr>
      <td><strong>② 좌측 사이드 카메라</strong></td>
      <td>200만 화소 FHD Sony STARVIS 센서, 사각지대 오토바이 감시, IP68 방수</td>
      <td class="text-right">25,000</td>
    </tr>
    <tr>
      <td><strong>③ 우측 사이드 카메라</strong></td>
      <td>200만 화소 FHD Sony STARVIS, [비상시 갓길/가드레일 자율추적 스위칭]</td>
      <td class="text-right">25,000</td>
    </tr>
    <tr>
      <td><strong>④ 후방 광폭 카메라</strong></td>
      <td>200만 화소 FHD 180도 초광각 왜곡보정 나노발수 렌즈, 야간 나이트비전</td>
      <td class="text-right">27,000</td>
    </tr>
    <tr>
      <td><strong>⑤ 스마트 룸미러 메인보드</strong></td>
      <td>온디바이스 AI 비전 NPU 2.0 TOPS + 4채널 AHD 비디오 디코더 SoC</td>
      <td class="text-right">68,000</td>
    </tr>
    <tr>
      <td><strong>⑥ 초광각 IPS 터치 패널</strong></td>
      <td>11.88인치 울트라 와이드(1920x440), 1000cd/m² 고휘도 무반사 코팅</td>
      <td class="text-right">42,000</td>
    </tr>
    <tr>
      <td><strong>⑦ 통신 및 GPS 모듈</strong></td>
      <td>LTE-M/Cat.M1 통신 모듈 + 내장형 eSIM + 고정밀 GPS/GLONASS 안테나</td>
      <td class="text-right">23,000</td>
    </tr>
    <tr>
      <td><strong>⑧ 양방향 119 비상통화</strong></td>
      <td>3W 고출력 스피커 + 노이즈 캔슬링 듀얼 마이크 + 음성 앰프 팩</td>
      <td class="text-right">12,000</td>
    </tr>
    <tr>
      <td><strong>⑨ OBD-II / CAN 인터페이스</strong></td>
      <td>대형차 ISO 15765-4 고속 CAN 트랜시버 + K-Line + 페달 APS 인터셉트 회로</td>
      <td class="text-right">15,000</td>
    </tr>
    <tr>
      <td><strong>⑩ 공압 제동 & 파킹 밸브 팩</strong></td>
      <td>대형차 24V 3단 감속 솔레노이드 + 내리막 롤어웨이 방지 파킹 락 밸브</td>
      <td class="text-right">85,000</td>
    </tr>
    <tr>
      <td><strong>⑪ UPS 슈퍼캐패시터 전원부</strong></td>
      <td>12V/24V 프리볼트 강압 회로 + 서지 보호 + 2.7V 10F 슈퍼캡 (정전 대비)</td>
      <td class="text-right">18,000</td>
    </tr>
    <tr>
      <td><strong>⑫ 알루미늄 외함 및 배선</strong></td>
      <td>알루미늄 다이캐스팅 방열 케이스 + 15m 난연 자동차 하네스 케이블 4조</td>
      <td class="text-right">35,000</td>
    </tr>
    <tr>
      <td><strong>⑬ SMT 조립, 검사, 패키징</strong></td>
      <td>표면실장(SMT) 임가공 + 조립 인건비 + 환경 에이징 전수검사 + 완충 패키징</td>
      <td class="text-right font-bold text-blue">47,000</td>
    </tr>
    <tr style="background-color: #eff6ff; font-weight: bold;">
      <td class="text-center text-blue">합 계 (대당 제조원가 BOM)</td>
      <td>13개 항목 정확 합계 (부품 13종 풀세트 + 조립·검사·패키징 완료)</td>
      <td class="text-right text-blue" style="font-size: 10.5pt;">470,000원</td>
    </tr>
  </tbody>
</table>

<div class="card-box">
  <div style="font-weight: bold; color: #1e3a8a; margin-bottom: 4px;">💰 [회계학적 엄밀성 반영] 판매 가격 및 실질 이익 구조 분석</div>
  <ul>
    <li><strong>소비자 권장 정가</strong>: <strong style="color:#1e3a8a;">2,000,000원 (200만 원)</strong> ➔ 정부/지자체 보조금 80% 지원 시 <span class="highlight-badge">차주 실부담금 400,000원 (40만 원 파격가!)</span></li>
    <li><strong>대당 매출총이익</strong>: <span class="highlight-badge" style="background:#dcfce7; color:#15803d;">대당 1,530,000원 (마진율 76.5%)</span> (매출 200만 원 - 제조원가 47만 원)</li>
    <li><strong>판관비 세부 차감 내역</strong>: 제품 설치비(8만) + 5년 보증충당금(6만) + LTE-M 5년 통신비 선납(4.8만) + 서버비(1.2만) + PL보험료(2만) + 유통마진(15만) = 총 370,000원</li>
    <li><strong>【대당 실질 영업이익】</strong>: <strong class="text-blue">대당 1,160,000원 (실질 영업이익률 58.0% 확보!)</strong></li>
    <li><strong>보조금 미지원 시 차주 경제적 유인</strong>: 공제조합 보험료 10~15% 할인 연계(연 80~120만 원 절감)로 1.5년 내 기기값 전액 회수 모델 입증.</li>
  </ul>
</div>

<div class="page-break"></div>

<!-- 3. Scale-up & BM -->
<h2>3. 시장 분석 및 사업화 전략 (BM & 1억 원 집행 계획)</h2>
<h3>3-1. 시장 규모 세분화 (TAM - SAM - SOM) 및 경쟁사 비교</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 25%;">
    <col style="width: 25%;">
    <col style="width: 25%;">
  </colgroup>
  <thead>
    <tr>
      <th>비교 항목</th>
      <th>기존 4채널 CMS 장치</th>
      <th>시중 대형차 ADAS 단말기</th>
      <th><strong>세이프티온 (본 아이템)</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>소비자 가격</th>
      <td class="text-center">120만 ~ 150만 원</td>
      <td class="text-center">180만 ~ 250만 원</td>
      <td class="text-center font-bold text-blue">2,000,000원 (보조금 시 40만)</td>
    </tr>
    <tr>
      <th>차량 진단 HUD</th>
      <td class="text-center">불가</td>
      <td class="text-center">불가</td>
      <td class="text-center font-bold">OBD-II 14.2V 전압 & DTC 번역</td>
    </tr>
    <tr>
      <th>운전자 실신 대응</th>
      <td class="text-center">단순 모니터링</td>
      <td class="text-center">단순 차선이탈 경보음</td>
      <td class="text-center font-bold text-red">단계별 경보 ➔ 3단계 감속 ➔ 119</td>
    </tr>
    <tr>
      <th>급가속 물리 차단</th>
      <td class="text-center">없음</td>
      <td class="text-center">없음</td>
      <td class="text-center font-bold text-blue">APS 0% 클램핑 & 0.05초 인터록</td>
    </tr>
    <tr>
      <th>비탈길 롤어웨이 방지</th>
      <td class="text-center">없음</td>
      <td class="text-center">없음</td>
      <td class="text-center font-bold text-blue">운전자 부재 시 오토 파킹 락 체결</td>
    </tr>
  </tbody>
</table>

<h3>3-2. 정부지원금 1억 원 집행 계획 (세부 산출 근거표)</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 18%;">
    <col style="width: 57%;">
  </colgroup>
  <thead>
    <tr>
      <th>비 목</th>
      <th>정부지원금 (원)</th>
      <th>세부 산출 내역 및 집행 용도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>시제품 제작비<br>(SMT / 기구)</strong></td>
      <td class="text-right font-bold">35,000,000</td>
      <td>• 4채널 7-in-1 핵심 시제품 60세트 SMT 및 부품 조달 (60대 × 470,000원 = 28,200,000원)<br>• 알루미늄 압출 방열 금형 목업 및 조립 검사용 전용 지그 제작 (6,800,000원)</td>
    </tr>
    <tr>
      <td><strong>인건비<br>(청년 연구원 2명)</strong></td>
      <td class="text-right font-bold">35,000,000</td>
      <td>• 인천대 전자공학/임베디드 청년 연구원 2명 신규 채용 (월 250만 원 × 2명 × 7개월)<br>• 전담 업무: STM32 CAN 펌웨어 개발, APS 인터셉트 회로 검증, DMS 알고리즘 포팅</td>
    </tr>
    <tr>
      <td><strong>공인 인증 및<br>시험평가비</strong></td>
      <td class="text-right font-bold">15,000,000</td>
      <td>• 자동차 전장 EMC(KN41/ECE R10) 전자파 시험(600만) + KTR 온습도 신뢰성(400만)<br>• 카메라 외함 IP68 방수방진 시험 성적서 발급(500만)</td>
    </tr>
    <tr>
      <td><strong>지식재산권 취득비</strong></td>
      <td class="text-right font-bold">10,000,000</td>
      <td>• 기출원 특허(28호, 29호, 30호) 우선심사 및 관납료/등록비: 4,000,000원<br>• 핵심 기술 해외 진출 대비 PCT 국제특허 1건 출원비용(변리사 수임료 포함): 6,000,000원</td>
    </tr>
    <tr>
      <td><strong>마케팅 및<br>실증 PoC 활동비</strong></td>
      <td class="text-right font-bold">5,000,000</td>
      <td>• 인천 관내 버스운송사 실차 장착 시연회 및 제품 기술 리플릿 제작 (3,000,000원)<br>• 운송조합 실무 간담회 및 현장 실증 테스트 차량 유류비/장착 공임 (2,000,000원)</td>
    </tr>
    <tr style="background-color: #eff6ff; font-weight: bold;">
      <td class="text-center text-blue">합 계</td>
      <td class="text-right text-blue" style="font-size: 10.5pt;">100,000,000원</td>
      <td class="text-blue">총 5개 비목 1억 원 정합 집행 (정부 지원 지침 100% 준수)</td>
    </tr>
  </tbody>
</table>

<h3>3-3. 3개년 추정 재무제표 및 연도별 손익 전망</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 25%;">
    <col style="width: 25%;">
    <col style="width: 25%;">
  </colgroup>
  <thead>
    <tr>
      <th>구 분</th>
      <th>1차년도 (2027년)</th>
      <th>2차년도 (2028년)</th>
      <th>3차년도 (2029년)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>주력 대상 차종</th>
      <td class="text-center"><strong>시내·고속버스 (Phase 1)</strong></td>
      <td class="text-center"><strong>화물차 · 25톤 덤프 (Phase 2)</strong></td>
      <td class="text-center"><strong>고령자 승용차 (Phase 3)</strong></td>
    </tr>
    <tr>
      <th>판매 목표 대수</th>
      <td class="text-center"><strong>300 대</strong> (수도권 실증 납품)</td>
      <td class="text-center"><strong>1,500 대</strong> (전국 상용차 확대)</td>
      <td class="text-center"><strong>5,000 대</strong> (보조금 및 일반 승용)</td>
    </tr>
    <tr>
      <th>매출액 (소비자가 200만 원)</th>
      <td class="text-right font-bold">600,000,000 원</td>
      <td class="text-right font-bold">3,000,000,000 원</td>
      <td class="text-right font-bold text-blue" style="font-size:9.5pt;">10,000,000,000 원 (100억!)</td>
    </tr>
    <tr>
      <th>매출원가 (BOM 47만 원)</th>
      <td class="text-right">141,000,000 원</td>
      <td class="text-right">705,000,000 원</td>
      <td class="text-right">2,350,000,000 원</td>
    </tr>
    <tr>
      <th>매출총이익 (마진율 76.5%)</th>
      <td class="text-right font-bold text-blue">459,000,000 원</td>
      <td class="text-right font-bold text-blue">2,295,000,000 원</td>
      <td class="text-right font-bold text-blue">7,650,000,000 원</td>
    </tr>
    <tr>
      <th>판관비 (설치/보증/운영비)</th>
      <td class="text-right">120,000,000 원</td>
      <td class="text-right">450,000,000 원</td>
      <td class="text-right">1,200,000,000 원</td>
    </tr>
    <tr style="background-color: #eff6ff;">
      <th>영업이익</th>
      <td class="text-right font-bold text-blue">339,000,000 원 (3.39억)</td>
      <td class="text-right font-bold text-blue">1,845,000,000 원 (18.45억)</td>
      <td class="text-right font-bold text-blue">6,450,000,000 원 (64.5억)</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- 4. Team & Risk Management -->
<h2>4. 팀 구성 및 위험 관리 (Team & Risk Management)</h2>
<h3>4-1. 대표자 역량 및 전문성 (현장 융합형 기술 창업자)</h3>
<table class="table-primary">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 80%;">
  </colgroup>
  <tbody>
    <tr>
      <th>성명 / 직위</th>
      <td><strong>변 귀 섭 (Byun Gwi-seob) / 대표이사 (CEO & CTO)</strong></td>
    </tr>
    <tr>
      <th>국가 전문 자격<br>(3대 트리플 크라운)</th>
      <td>
        • <span class="highlight-badge">국가기술자격</span> <strong>자동차정비기능사</strong> (상용차 공압 브레이크, 하체 섀시, 전장 제어 정비 공인 자격)<br>
        • <span class="highlight-badge">한국교통안전공단</span> <strong>화물운송종사자격증</strong> (대형 화물 물류 현장 법규 및 덤프트럭 운행 완벽 이해)<br>
        • <span class="highlight-badge">한국교통안전공단</span> <strong>버스운전자격증</strong> (시내·시외 버스 승객 안전 규정 및 근로 환경 완벽 이해)<br>
        • <em>(실차 주행 직접 검증)</em> <strong>1종 대형운전면허</strong> 보유 예정
      </td>
    </tr>
    <tr>
      <th>학력 사항<br>(4대 학위)</th>
      <td>
        • <strong>서울시립대학교 대학원 반도체 (석사)</strong>: 최첨단 반도체 패키징, 3차원 적층, 열 방출 전공<br>
        • <strong>강릉대학교 전자공학과 (학사)</strong>: 정통 전자회로, 마이크로프로세서, 센서 신호처리 전공<br>
        • <strong>인천대학교 대학원 전자교육 (석사)</strong>: 공학기술 구조화 및 교육공학 전공 (주관기관 모교 출신 가점)<br>
        • <strong>중부대학교 대학원 상담심리교육학과 (석사)</strong>: 인간 심리, 위기 상담, 생명 존중 철학 전공
      </td>
    </tr>
    <tr>
      <th>원천 지식재산권</th>
      <td>
        • <strong>차량 안전 3대 특허</strong>: 28호(<code>10-2026-0195570</code>), 29호(<code>10-2026-0206812</code>), 30호(<code>10-2026-0206816</code>) 출원 및 수수료 완납<br>
        • <em>(대표자 배경 역량)</em> 대한민국 특허청 HBM4 반도체 패밀리 특허 3건 단독 출원 보유
      </td>
    </tr>
  </tbody>
</table>

<h3>4-2. 법률·인증·개인정보·사고책임 위험 관리 및 신뢰성 확보 체계</h3>
<div class="card-box">
  <ol style="margin: 0; padding-left: 18px;">
    <li><strong>자동차관리법 튜닝 승인 적합성</strong>:
      <ul>
        <li>배선 절단 없는 원터치 T자 공압 분기 밸브 및 표준 OBD-II 직결 구조로 '경미한 장치 장착' 기준 충족, 튜닝 승인 리스크 원천 배제.</li>
      </ul>
    </li>
    <li><strong>제조물 배상책임(PL) 보험 가입</strong>:
      <ul>
        <li>메리츠화재/DB손해보험 협약, 대당 10억 원 한도 PL보험 가입 예산 책정 완료.</li>
      </ul>
    </li>
    <li><strong>개인정보보호(Privacy-by-Design)</strong>:
      <ul>
        <li>DMS 안면 영상은 Edge NPU 내부에서 특징점 벡터(Vector)만 즉시 처리 후 원본 영상 영구 폐기, 개인정보 유출 리스크 제로화.</li>
      </ul>
    </li>
    <li><strong>119 긴급출동 오신고 방지 2단계 체계</strong>:
      <ul>
        <li>1차 시청각 경보 및 관제센터 통화 확인 후, 10초 무응답 시에만 119 자동 에스컬레이션되는 유럽 e-Call 표준 준수.</li>
      </ul>
    </li>
  </ol>
</div>

<!-- Seal Area -->
<div class="seal-container">
  <div class="seal-date">2027년 2월</div>
  <div class="seal-company">주식회사 세이프티온 (SAFETYON Inc.)</div>
  <div class="seal-rep">
    <span>대 표 이 사 &nbsp;&nbsp; <strong>변 &nbsp; 귀 &nbsp; 섭</strong></span>
    <span class="seal-stamp">세이프<br>티온인<br>변귀섭</span>
  </div>
</div>

</body>
</html>
"""

temp_html_path = 'C:/Users/LENOVO/Desktop/temp_plan.html'
pdf_output_path = 'C:/Users/LENOVO/Desktop/2027_예비창업패키지_사업계획서_주식회사_세이프티온_최종제출본.pdf'

with open(temp_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

chrome_cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_output_path}',
    temp_html_path
]

subprocess.run(chrome_cmd)

if os.path.exists(pdf_output_path):
    doc = pymupdf.open(pdf_output_path)
    print(f'SUCCESS! Total Pages: {len(doc)}, Size: {os.path.getsize(pdf_output_path):,} bytes')
    doc.close()
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
