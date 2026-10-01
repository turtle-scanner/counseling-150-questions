import os, subprocess, shutil
from pypdf import PdfReader, PdfWriter

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
target_dir = os.path.join(desktop, '고소장', '02_[오늘바로등기발송가능]_서울구로경찰서_형사고소장(최종완성본)')

html_src = os.path.join(target_dir, '1_[서울구로경찰서_오늘발송용]_형사고소장_김형준_원본.html')
tmp_complaint_pdf = os.path.join(base_dir, 'tmp_upgraded_complaint_0923.pdf')

udir = 'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_complaint_0923'
subprocess.run([
    edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
    '--no-pdf-header-footer', f'--print-to-pdf={tmp_complaint_pdf}', html_src
], check=True)

print('Rendered complaint pages:', len(PdfReader(tmp_complaint_pdf).pages))

# Copy standalone complaint PDFs
for name in [
    '1_[서울구로경찰서_오늘발송용]_형사고소장_김형준(모욕_상해_업무방해)_20260923.pdf',
    '1_[최종확정판_인쇄용]_서울구로경찰서_형사고소장_김형준_20260923.pdf',
    '1_[최종완성_김형준선조사요청포함]_서울구로경찰서_형사고소장_20260923.pdf',
]:
    dst = os.path.join(target_dir, name)
    try: shutil.copyfile(tmp_complaint_pdf, dst)
    except Exception as e: print('Skip standalone:', name, e)

# Merge full bundle into 고소장_9월23일-완료.pdf
pet_pdf = os.path.join(base_dir, 'tmp_pet_1aa.pdf')
ev_files = [
    tmp_complaint_pdf,
    os.path.join(target_dir, '2_[증제1호증_최종완성]_강용준_안전요원_정식목격자진술서(0923).pdf'),
    os.path.join(target_dir, '3_[증제3호증_보강]_인천힐병원_3개월진단서_소견서_초진차트_입원확인서.pdf'),
    os.path.join(target_dir, '4_[증제10호증_보강]_학교측_통화녹취_증거목록_및_요지서(0923).pdf'),
    os.path.join(target_dir, '5_[첨부증거_사진캡처모음]_카톡원본_버스기사문자_단톡방_처방전_캡처본(12장).pdf'),
    pet_pdf,
]

writer = PdfWriter()
for ef in ev_files:
    if os.path.exists(ef):
        r = PdfReader(ef)
        for p in r.pages:
            writer.add_page(p)

out_paths = [
    os.path.join(target_dir, '고소장_9월23일-완료.pdf'),
    os.path.join(target_dir, '고소장_9월23일.pdf'),
    os.path.join(target_dir, '서울구로경찰서_고소장_및_전부증거합본.pdf'),
    os.path.join(desktop, '고소장_9월23일-완료.pdf'),
]

for op in out_paths:
    try:
        with open(op, 'wb') as f:
            writer.write(f)
        print('Saved merged bundle:', op, len(writer.pages), 'pages')
    except Exception as e:
        print('Skip bundle (open):', op, e)

print('UPGRADE_COMPLETE')
