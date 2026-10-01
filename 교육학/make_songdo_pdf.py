import os, base64, subprocess, shutil
from pypdf import PdfReader

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
comwel_dir = os.path.join(desktop, '근로복지공단_1차보완요청(10월7일기한)_완성서류모음')

img1_path = r'C:/Users/LENOVO/.gemini/antigravity/brain/54a65f4d-a058-4307-83a1-d8dec8bb9bb0/.user_uploaded/media_1790844623804.png'
img2_path = r'C:/Users/LENOVO/.gemini/antigravity/brain/54a65f4d-a058-4307-83a1-d8dec8bb9bb0/.user_uploaded/media_1790844653387.png'

with open(img1_path, 'rb') as f:
    b64_1 = base64.b64encode(f.read()).decode('utf-8')
with open(img2_path, 'rb') as f:
    b64_2 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>송도봄정신건강의학과 진료기록부 전문</title>
<style>
  @page {{ size: A4 portrait; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #fff; }}
  .page {{ page-break-after: always; width: 210mm; height: 297mm; display: flex; justify-content: center; align-items: center; overflow: hidden; }}
  .page:last-child {{ page-break-after: auto; }}
  img {{ width: 100%; height: 100%; object-fit: contain; }}
</style>
</head>
<body>
  <div class="page"><img src="data:image/png;base64,{b64_1}"></div>
  <div class="page"><img src="data:image/png;base64,{b64_2}"></div>
</body>
</html>"""

html_file = os.path.join(base_dir, 'songdo_b64.html')
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

pdf_tmp = os.path.join(base_dir, 'tmp_songdo_b64.pdf')
udir = 'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_songdo_b64'
subprocess.run([
    edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
    '--no-pdf-header-footer', f'--print-to-pdf={pdf_tmp}', html_file
], check=True)

reader = PdfReader(pdf_tmp)
print('Generated Songdo Bom PDF pages:', len(reader.pages))

out_name = '12_[보완3번_의무기록]_송도봄정신건강의학과_진료기록부_전문(2026.08.31_09.01).pdf'
shutil.copyfile(pdf_tmp, os.path.join(desktop, out_name))
shutil.copyfile(pdf_tmp, os.path.join(comwel_dir, out_name))
print('SUCCESS_SONGDO_BOM_PDF')
