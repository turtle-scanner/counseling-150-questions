import os, subprocess, shutil
from pypdf import PdfReader

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
html_path = os.path.join(base_dir, '★[학교장앞_이의신청]_임용계약_해지_예정_통보에_대한_이의제기_및_효력정지_요구서_변귀섭.html')
pdf_tmp = os.path.join(base_dir, 'tmp_11pt_obj.pdf')

def generate_11pt_html(body_size, line_height, tbl_size, sec_size, box_size, sign_size, top_bot):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>임용계약 해지 예정 통보에 대한 정식 이의신청 및 효력정지(집행유예) 요구서 (11pt A4 1장 완성본)</title>
<style>
  @page {{ size: A4 portrait; margin: {top_bot}mm 11mm {top_bot}mm 11mm; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Batang', '바탕', 'Malgun Gothic', serif;
    color: #000; background: #fff;
    font-size: {body_size}pt; line-height: {line_height};
  }}
  .title {{
    text-align: center; font-size: 16pt; font-weight: 900;
    letter-spacing: 1px; border-bottom: 2px solid #000;
    padding-bottom: 2px; margin-bottom: 4px; font-family: 'Malgun Gothic', sans-serif;
  }}
  .table-box {{
    width: 100%; border-collapse: collapse; margin-bottom: 4px;
    font-size: {tbl_size}pt; font-family: 'Malgun Gothic', sans-serif;
  }}
  .table-box th, .table-box td {{
    border: 1px solid #333; padding: 1.5px 5px; text-align: left;
  }}
  .table-box th {{
    background: #f1f5f9; font-weight: 800; width: 17%; text-align: center;
  }}
  .sec-head {{
    font-family: 'Malgun Gothic', sans-serif; background: #0f172a;
    color: #fff; font-size: {sec_size}pt; font-weight: 800;
    padding: 1.5px 6px; margin: 3px 0 1.5px 0;
  }}
  .p-text {{
    text-align: justify; margin-bottom: 2px; text-indent: 6px;
  }}
  .highlight-warn {{
    border: 1.5px solid #dc2626; background: #fef2f2;
    padding: 3.5px 7px; margin: 2.5px 0; font-family: 'Malgun Gothic', sans-serif;
    font-size: {box_size}pt; line-height: 1.28;
  }}
  .sign-area {{
    margin-top: 4px; text-align: center; font-family: 'Malgun Gothic', sans-serif;
    font-weight: 800; font-size: {sign_size}pt; line-height: 1.35;
    border-top: 1.5px solid #000; padding-top: 3px;
  }}
</style>
</head>
<body>

<div class="title">임용계약 해지 예정 통보에 대한 정식 이의신청<br>및 효력정지(집행유예) 요구서</div>

<table class="table-box">
  <tr>
    <th>수 &nbsp; 신</th>
    <td><strong>유한공업고등학교장 (참조: 행정실장, 교감)</strong></td>
    <th>발 &nbsp; 신</th>
    <td><strong>교사 변귀섭 (전기과 / 2학년 5반 담임)</strong></td>
  </tr>
  <tr>
    <th>통보 문서</th>
    <td colspan="3"><strong>임용계약 해지 예정 통보서 (2026. 9. 29. 유한공업고등학교장 직인 발송)</strong></td>
  </tr>
  <tr>
    <th>해지 예정일</th>
    <td><strong>2026년 11월 5일자</strong></td>
    <th>산재 접수번호</th>
    <td><strong>근로복지공단 제2060-2026-4028537호 (2026. 9. 28. 접수)</strong></td>
  </tr>
</table>

<div class="sec-head">1. 이의신청의 요지 : 업무상 재해에 따른 일방적 계약해지의 위법성</div>
<div class="p-text">
  귀교가 2026년 9월 29일 자로 발송한 본인에 대한 『임용계약 해지 예정 통보서』는 <strong>근로기준법 제23조 제2항, 동법 제76조의3 제6항을 정면으로 위반한 명백한 불법·부당해고 처분</strong>인바, 이에 정식으로 이의를 제기하며 <strong>오는 2026년 11월 5일 자 계약해지 처분을 즉각 철회 또는 집행 유예할 것을 엄중히 요구</strong>합니다.
</div>

<div class="sec-head">2. 법률적 위법 사유 및 강행규정 위반</div>
<div class="p-text">
  <strong>가. 근로기준법 제23조 제2항(해고 등의 제한) 위반 (위반 시 5년 이하 징역) :</strong><br>
  본인의 질병(F32.9, F43.2, F43.0, F41.0 및 사지 마비)은 개인 질환이 아니며, <strong>2026. 8. 28. 제주 교육여행(수학여행) 총괄 안전 인솔 공무 수행 중 발생한 명백한 ‘업무상 질병’</strong>입니다. 근로기준법 제23조 제2항은 <em>“사용자는 근로자가 업무상 부상 또는 질병의 요양을 위하여 휴업한 기간과 그 후 30일 동안은 해고하지 못한다”</em>고 규정하고 있으며, 이는 강행규정으로서 이를 위반한 해고는 <strong>사법상 절대 무효이자 형사처벌(5년 이하 징역 또는 5천만 원 이하 벌금) 대상</strong>입니다.
</div>
<div class="p-text">
  <strong>나. 귀교 스스로 통보서 제7항에서 산재 승인 시 해고 무효임을 자인 :</strong><br>
  귀교 또한 본 상병의 업무상 인과관계와 법적 효력을 인식하고 있기에, 통보서 제7항에 <em>“아울러 선생님께서 근로복지공단에 최초요양급여신청(2026.9.28.) 승인사항에 따라 계약해지 부분이 달라질 수 있는 점도 함께 알려드립니다”</em>라고 명시하였습니다. 따라서 <strong>근로복지공단의 산재 요양 승인 결정이 확정될 때까지 본 계약해지 절차는 법률상 당연히 중단·유예되어야 마땅</strong>합니다.
</div>
<div class="p-text">
  <strong>다. 공무상 재해(교육여행 인솔)로 입원 치료 중인 교원에 대한 일방적 계약해지의 부당성 및 법률 위반 :</strong><br>
  본인은 2026학년도 2학년 교육여행(수학여행) 총괄 안전 인솔 공무를 수행하던 중 발생한 중대한 사고로 인하여 현재까지 병원에 입원 치료 중인 환자입니다. <strong>학교의 공식 업무를 수행하다가 부상(정신적·신체적 상해)을 입고 병상에 누워 있는 피해 교원에게, 보호와 치료 지원은커녕 사전 협의 없이 일방적으로 학급 담임 직무를 박탈하고 실물 계약해지 통보서(등기번호: 11440-0504-3990)를 발송하여 해고를 통보하는 것은 근로기준법 제23조 제2항 및 제76조의3(불리한 처우 금지)을 정면으로 위반한 지극히 부당하고 위법한 처분</strong>입니다.
</div>

<div class="highlight-warn">
  <strong>■ 본인의 요구사항 및 향후 법적 조치 통고 :</strong><br>
  1. 귀교는 <strong>2026년 11월 5일 자 임용계약 해지 처분의 집행을 근로복지공단의 산재 요양 승인 결정 시까지 즉각 '집행 유예(효력 정지)' 처리</strong>할 것을 요구합니다.<br>
  2. 만약 귀교가 이를 무시하고 11월 5일 자로 직권 계약해지를 강행할 경우, 본인은 즉시 <strong>① 서울지방노동위원회 부당해고 구제신청, ② 서울남부고용노동지청에 학교장 및 교감 대상 근로기준법 제23조 제2항·제76조의3 위반 형사고발, ③ 서울특별시교육청 특정감사 추가 보복행위 감사 청구</strong>를 진행하여 일체의 민·형사상 책임을 끝까지 물을 것임을 엄중히 고지합니다.
</div>

<div class="sign-area">
  2026년 &nbsp;&nbsp;&nbsp; 10월 &nbsp;&nbsp;&nbsp; 01일 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 이의신청인 (교사) : &nbsp;&nbsp; <strong>변 &nbsp; 귀 &nbsp; 섭</strong> &nbsp;&nbsp; (서명 또는 인)<br>
  <span style="font-size:13pt; font-weight:900; letter-spacing:1px; display:inline-block; margin-top:2px;">유한공업고등학교장 귀하</span>
</div>

</body>
</html>
"""

# Let's test with body 11.0pt, line-height 1.30, margins 6.5mm
for b_sz in [11.0, 10.8, 10.5]:
    c = generate_11pt_html(b_sz, 1.28, 10.0, 10.8, 9.8, 10.8, 6.5)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(c)
    udir = 'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_11pt_run'
    subprocess.run([
        edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
        '--no-pdf-header-footer', f'--print-to-pdf={pdf_tmp}', html_path
    ], check=True)
    pages = len(PdfReader(pdf_tmp).pages)
    print(f'Test font {b_sz}pt -> pages: {pages}')
    if pages == 1:
        print(f'Found 1-page fit at {b_sz}pt!')
        dst_desktop = os.path.join(desktop, '★[학교장앞_이의신청서_A4한장완성본]_임용계약_해지_예정_통보에_대한_이의제기_및_효력정지_요구서_변귀섭.pdf')
        shutil.copyfile(pdf_tmp, dst_desktop)
        print('Copied to desktop successfully!')
        break
