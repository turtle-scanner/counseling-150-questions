import re

def check_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        nums = re.findall(r'\"num\":\s*(\d+)', text)
        print(path, 'total items:', len(nums))
        if nums:
            print('  first 5 nums:', nums[:5], 'last 5 nums:', nums[-5:])
    except Exception as e:
        print(path, 'error:', e)

check_file(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html')
check_file(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html')
check_file(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\2027_KICE_300개_핵심단어장_앱.html')
check_file(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\index.html')
