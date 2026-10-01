import os
with open('scratch/build_complete_200_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines[-8] = "target_path = r'G:\\\´ ��라δ�x\\ANTI GRAVITY\\전문상담쟄욥고시\\kice-300-wordbook\\kice_150_core_table_a4.html'\n"
with open('scratch/build_complete_200_app.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)