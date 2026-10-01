import os, subprocess, shutil
from pypdf import PdfReader

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
comwel_dir = os.path.join(desktop, '근로복지공단_1차보완요청(10월7일기한)_완성서류모음')
os.makedirs(comwel_dir, exist_ok=True)

img1 = r'C:/Users/LENOVO/.gemini/antigravity/brain/54a65f4d-a058-4307-83a1-d8dec8bb9bb0/.user_uploaded/media_1790844623804.png'
img2 = r'C:/Users/LENOVO/.gemini/antigravity/brain/54a65f4d-a058-4307-83a1-d8dec8bb9bb0/.user_uploaded/media_1790844653387.png'

html_doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>송도봄정신건강의학과 진료기록부 전문 (공단 제출용)</title>
<style>
  @page {{ size: A4 portrait; margin: 8mm; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Malgun Gothic', '맑은 고딕', sans-serif; color: #000; margin: 0; padding: 0; text-align: center; background: #fff; }}
  .page {{ page-break-after: always; height: 280mm; display: flex; flex-direction: column; justify-content: center; align-items: center; }}
  .page:last-child {{ page-break-after: auto; }}
  img {{ max-width: 100%; max-height: 275mm; object-fit: contain; }}
</style>
</head>
<body>
  <div class="page"><img src="file:///{img1}"></div>
  <div class="page"><img src="file:///{img2}"></div>
</body>
</html>"""

html_path = os.path.join(base_dir, '송도봄_진료기록부_변환.html')
pdf_tmp = os.path.join(base_dir, 'tmp_songdo_bom.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_doc)

udir = 'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_songdo'
subprocess.run([
    edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
    '--no-pdf-header-footer', f'--print-to-pdf={pdf_tmp}', html_path
], check=True)

reader = PdfReader(pdf_tmp)
print('Songdo Bom PDF pages:', len(reader.pages))

dst_name = '12_[보완3번_의무기록]_송도봄정신건강의학과_진료기록부_전문(2026.08.31_09.01).pdf'
shutil.copyfile(pdf_tmp, os.path.join(desktop, dst_name))
shutil.copyfile(pdf_tmp, os.path.join(comwel_dir, dst_name))
print('Successfully saved Songdo Bom PDF to Desktop and Comwel folder!')
