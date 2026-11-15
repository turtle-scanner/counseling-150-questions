# -*- coding: utf-8 -*-
import os

runner_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\build_samguk3_war_fixed_runner.py"
with open(runner_path, "r", encoding="utf-8") as f:
    code = f.read()

old_block_start = "out_paths = ["
old_block_end = "    for p in out_paths:"
start_idx = code.find(old_block_start)
end_idx = code.find(old_block_end)

new_block = """out_paths = [
        r"C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html",
        r"C:\\Users\\LENOVO\\Desktop\\sam3_update.html",
        os.path.join(brain_dir, "samgukji_game.html"),
        r"g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\samgukji.html",
        r"g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\samgukji.html"
    ]

"""

fixed_code = code[:start_idx] + new_block + code[end_idx:]

with open(runner_path, "w", encoding="utf-8") as f:
    f.write(fixed_code)

print("Successfully fixed out_paths in runner!")
