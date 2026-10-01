import os, subprocess, shutil
from pypdf import PdfReader, PdfWriter

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

base_dir = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학'
desktop = r'C:\Users\LENOVO\Desktop'
folder = os.path.join(desktop, '근로복지공단_1차보완요청(10월7일기한)_완성서류모음')
os.makedirs(folder, exist_ok=True)

html_qna = os.path.join(base_dir, '사실관계확인서_정신질병_전문항완성본_문1_문126_변귀섭.html')
html_rep = os.path.join(base_dir, '재해발생_상세_경위서_변귀섭_20260924.html')
html_pet = os.path.join(base_dir, '국민신문고_서울시교육청_특정감사청구_접수확인서_1AA26091083217.html')

tmp_qna_pdf = os.path.join(base_dir, 'tmp_qna_1aa.pdf')
tmp_rep_pdf = os.path.join(base_dir, 'tmp_rep_1aa.pdf')
tmp_pet_pdf = os.path.join(base_dir, 'tmp_pet_1aa.pdf')

for idx, (h_path, p_path) in enumerate([(html_qna, tmp_qna_pdf), (html_rep, tmp_rep_pdf), (html_pet, tmp_pet_pdf)]):
    udir = f'C:/Users/LENOVO/AppData/Local/Temp/edge_tmp_1aa_{idx}'
    subprocess.run([
        edge_path, '--headless', '--disable-gpu', f'--user-data-dir={udir}',
        '--no-pdf-header-footer', f'--print-to-pdf={p_path}', h_path
    ], check=True)

for t in [
    os.path.join(desktop, '9_[추가공적증빙]_국민신문고_서울특별시교육청_특정감사청구_접수확인서(신청번호_1AA-2609-1083217).pdf'),
    os.path.join(folder, '9_[추가공적증빙]_국민신문고_서울특별시교육청_특정감사청구_접수확인서(신청번호_1AA-2609-1083217).pdf'),
]:
    try: shutil.copyfile(tmp_pet_pdf, t)
    except: pass

for t in [
    os.path.join(desktop, '★[문1~문126_전문항완벽수록_최종본]_정신과표준문답서(사실관계확인서)_변귀섭.pdf'),
    os.path.join(desktop, '1_[보완1번_사실관계확인서]_정신과표준문답서_변귀섭(최종완성본).pdf'),
    os.path.join(folder, '1_[보완1번_문1~문126전문항완성본]_사실관계확인서(정신질병)_정신과표준문답서_변귀섭.pdf'),
]:
    try: shutil.copyfile(tmp_qna_pdf, t)
    except: pass

for t in [
    os.path.join(desktop, '8-2_[보완8번_상세경위서]_재해발생_상세_경위서_변귀섭(1장완성본).pdf'),
    os.path.join(folder, '8-2_[보완8번_상세경위서]_재해발생_상세_경위서_변귀섭(1장완성본).pdf'),
]:
    try: shutil.copyfile(tmp_rep_pdf, t)
    except: pass

plan_pdf = os.path.join(folder, '8-1_[보완8번_직무및일정증빙]_2026학년도_2학년_교육여행_계획서(공문_제10564호).pdf')
writer = PdfWriter()
for src in [tmp_qna_pdf, tmp_rep_pdf, tmp_pet_pdf, plan_pdf]:
    if os.path.exists(src):
        for page in PdfReader(src).pages:
            writer.add_page(page)

for bt in [
    os.path.join(desktop, '★[산재보험_필승완성본]_정신과표준문답서(문1~126)_상세경위서_교육여행공문증거_통합본(변귀섭).pdf'),
    os.path.join(folder, '0_[필승통합본]_정신과표준문답서(문1~126)_상세경위서_교육여행공문증거_통합본(변귀섭).pdf'),
]:
    try:
        with open(bt, 'wb') as f: writer.write(f)
    except: pass
print('SUCCESS_1AA')
