# -*- coding: utf-8 -*-
import os

sam5_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji5.html"
with open(sam5_path, "r", encoding="utf-8") as f:
    text = f.read()

print("sam5 length:", len(text))

# Check sections
body_start = text.find("<body")
script_start = text.find("<script>")
script_end = text.rfind("</script>")

print("body_start:", body_start)
print("script_start:", script_start)
print("script_end:", script_end)

# Find CSS styles
style_start = text.find("<style>")
style_end = text.find("</style>")
print("CSS length:", style_end - style_start)

# Save CSS and JS parts
with open("scratch/sam5_css.txt", "w", encoding="utf-8") as f:
    f.write(text[style_start+7:style_end])

with open("scratch/sam5_body.txt", "w", encoding="utf-8") as f:
    f.write(text[body_start:script_start])

with open("scratch/sam5_script.txt", "w", encoding="utf-8") as f:
    f.write(text[script_start+8:script_end])

print("Saved parts to scratch folder!")
