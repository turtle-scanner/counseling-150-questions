import os, subprocess, shutil
from pypdf import PdfReader

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
comwel_dir = os.path.join(desktop, '근로복지공단_1차보완요청(10월7일기한)_완성서류모음')
os.makedirs(comwel_dir, exist_ok=True)

tasks = [
    (
        os.path.join(base_dir, '10_[핵심2차가해증빙]_유한공업고등학교_임용계약_해지_예정_통보서.html'),
        os.path.join(base_dir, 'tmp_term_notice.pdf'),
        [
            os.path.join(desktop, '10_[핵심2차가해증빙]_유한공업고등학교_임용계약_해지_예정_통보서(2026.09.29발행).pdf'),
            os.path.join(comwel_dir, '10_[핵심2차가해증빙]_유한공업고등학교_임용계약_해지_예정_통보서(2026.09.29발행).pdf')
        ]
    ),
    (
        os.path.join(base_dir, '★[긴급]_학교측_보복성_계약해지_통보에_따른_요양급여_신속승인_요청서_변귀섭.html'),
        os.path.join(base_dir, 'tmp_fast_track.pdf'),
        [
            os.path.join(desktop, '★[공단제출용]_학교측_보복성_계약해지_통보에_따른_요양급여_신속승인_요청서_변귀섭.pdf'),
            os.path.join(comwel_dir, '★[공단제출용]_학교측_보복성_계약해지_통보에_따른_요양급여_신속승인_요청서_변귀섭.pdf')
        ]
    ),
    (
        os.path.join(base_dir, '★[학교장앞_이의신청]_임용계약_해지_예정_통보에_대한_이의제기_및_효력정지_요구서_변귀섭.html'),
        os.path.join(base_dir, 'tmp_school_objection.pdf'),
        [
            os.path.join(desktop, '★[학교장앞_이의신청서]_임용계약_해지_예정_통보에_대한_이의제기_및_효력정지_요구서_변귀섭.pdf')
        ]
    ),
]

for idx, (h_src, p_dst, copies) in enumerate(tasks):
    udir = f'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_term_{idx}'
    subprocess.run([
        edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
        '--no-pdf-header-footer', f'--print-to-pdf={p_dst}', h_src
    ], check=True)
    print(f'Rendered {os.path.basename(p_dst)}: {len(PdfReader(p_dst).pages)} pages')
    for cp in copies:
        try:
            shutil.copyfile(p_dst, cp)
            print(f'Copied to: {os.path.basename(cp)}')
        except Exception as e:
            print(f'Copy error {cp}: {e}')

print('ALL_DEFENSE_PDFS_GENERATED')
