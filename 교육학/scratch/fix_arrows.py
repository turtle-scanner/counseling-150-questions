import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add a text formatter function right before renderCard
formatter_js = """
    function formatText(text) {
      if (!text) return '';
      let t = text.replace(/\*\*(.*?)\*\*/g, '<span style="color:#d97706; font-weight:bold;">$1</span>');
      // Replace LaTeX arrows with unicode arrows
      t = t.replace(/\$\\\\Rightarrow\$/g, '➔');
      t = t.replace(/\\\\Rightarrow/g, '➔');
      t = t.replace(/\$\\\\rightarrow\$/g, '→');
      t = t.replace(/\\\\rightarrow/g, '→');
      t = t.replace(/\$\\\\Leftrightarrow\$/g, '↔');
      t = t.replace(/\\\\Leftrightarrow/g, '↔');
      return t;
    }
"""

if "function formatText" not in html:
    html = html.replace('function renderCard(index) {', formatter_js + '\n    function renderCard(index) {')

# Apply to renderCard
html = html.replace("elBadge.innerText = item.badge;", "elBadge.innerHTML = formatText(item.badge);")
html = html.replace("elQ.innerHTML = item.q.replace(/\\*\\*(.*?)\\*\\*/g, '<span style=\"color:#d97706; font-weight:bold;\">$1</span>');", "elQ.innerHTML = formatText(item.q);")
html = html.replace("elKw.innerText = item.kw;", "elKw.innerHTML = formatText(item.kw);")
# For elAns, we don't want to break the AutoGrader logic, but wait, the AutoGrader parses `items[currentIndex].ans`.
# We just need to ensure the initial display is formatted.
# The initial display is: elAns.innerText = item.ans;
html = html.replace("elAns.innerText = item.ans;", "elAns.innerHTML = formatText(item.ans);")

# Apply to initTable
old_table_row = """html += `<tr class="table-row" id="tr-${i}">
            <td class="td-num"><b>${i+1}</b></td>
            <td><span class="td-badge">[${item.badge}]</span><br><span class="td-kw">${item.kw}</span></td>
            <td class="td-q">${item.q}</td>
            <td class="td-ans">${item.ans}</td>
          </tr>`;"""

new_table_row = """html += `<tr class="table-row" id="tr-${i}">
            <td class="td-num"><b>${i+1}</b></td>
            <td><span class="td-badge">[${formatText(item.badge)}]</span><br><span class="td-kw">${formatText(item.kw)}</span></td>
            <td class="td-q">${formatText(item.q)}</td>
            <td class="td-ans">${formatText(item.ans)}</td>
          </tr>`;"""

html = html.replace(old_table_row, new_table_row)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Arrow formatting applied.")
