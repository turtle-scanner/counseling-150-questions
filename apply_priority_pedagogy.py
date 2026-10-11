# -*- coding: utf-8 -*-
import os
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")

# Let's inspect the current build_pedagogy_16_html.js to prepare our update
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add priority and priorityLabel to each topic in topicsData
priority_map = {
    1: ("1순위", "🔥 1순위 압도적 적중"),
    2: ("3순위", "📌 3순위 기본 방어"),
    3: ("2순위", "⭐ 2순위 유력 복병"),
    4: ("3순위", "📌 3순위 기본 방어"),
    5: ("1순위", "🔥 1순위 압도적 적중"),
    6: ("3순위", "📌 3순위 기본 방어"),
    7: ("2순위", "⭐ 2순위 유력 복병"),
    8: ("3순위", "📌 3순위 기본 방어"),
    9: ("1순위", "🔥 1순위 압도적 적중"),
    10: ("1순위", "🔥 1순위 연계 루브릭"),
    11: ("2순위", "⭐ 2순위 유력 복병"),
    12: ("3순위", "📌 3순위 기본 방어"),
    13: ("1순위", "🔥 1순위 압도적 적중"),
    14: ("3순위", "📌 3순위 기본 방어"),
    15: ("2순위", "⭐ 2순위 유력 복병"),
    16: ("3순위", "📌 3순위 기본 방어")
}

# Add priority fields to topicsData
for num, (p, pl) in priority_map.items():
    # find pattern for topic num
    pat = rf'num:\s*{num},'
    rep = f'num: {num},\n    priority: "{p}",\n    priorityLabel: "{pl}",'
    content = re.sub(pat, rep, content, count=1)

# Update CSS for priority badges
css_priority = """
/* Priority Badge */
.priority-badge {
  font-size: 0.74rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 4px;
  letter-spacing: -0.2px;
}
.priority-1순위 {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.35);
}
.priority-2순위 {
  background: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.35);
}
.priority-3순위 {
  background: rgba(148, 163, 184, 0.1);
  color: #94a3b8;
  border: 1px solid rgba(148, 163, 184, 0.2);
}
"""

content = content.replace("/* Keyword Tags */", css_priority + "\n/* Keyword Tags */")

# Update card top HTML to show priority badge
old_card_top = """          '<div class="card-top">' +
            '<div>' +
              '<div class="card-num">TOPIC ' + String(t.num).padStart(2, '0') + '</div>' +
              '<div class="card-title-text">' + t.title + '</div>' +
            '</div>' +
            '<span class="domain-badge">' + t.domain + '</span>' +
          '</div>' +"""

new_card_top = """          '<div class="card-top">' +
            '<div>' +
              '<div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">' +
                '<span class="card-num">TOPIC ' + String(t.num).padStart(2, '0') + '</span>' +
                '<span class="priority-badge priority-' + t.priority + '">' + t.priorityLabel + '</span>' +
              '</div>' +
              '<div class="card-title-text">' + t.title + '</div>' +
            '</div>' +
            '<span class="domain-badge">' + t.domain + '</span>' +
          '</div>' +"""

content = content.replace(old_card_top, new_card_top)

# Update nav HTML
old_nav = """<nav class="filter-nav">
  <button class="tab-btn active" onclick="filterDomain('all')">전체 16대 주제 보기</button>
  <button class="tab-btn" onclick="filterDomain('교육과정')">Ⅰ. 교육과정 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육방법')">Ⅱ. 교육방법 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육평가')">Ⅲ. 교육평가 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육행정')">Ⅳ. 교육행정 (4선)</button>
</nav>"""

new_nav = """<nav class="filter-nav">
  <button class="tab-btn active" onclick="filterDomain('top')">🔥 2027 1-2순위 초정예 집중 뷰</button>
  <button class="tab-btn" onclick="filterDomain('all')">전체 16대 주제 보기</button>
  <button class="tab-btn" onclick="filterDomain('교육과정')">Ⅰ. 교육과정 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육방법')">Ⅱ. 교육방법 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육평가')">Ⅲ. 교육평가 (4선)</button>
  <button class="tab-btn" onclick="filterDomain('교육행정')">Ⅳ. 교육행정 (4선)</button>
</nav>"""

content = content.replace(old_nav, new_nav)

# Update renderTopics function to handle 'top'
old_render = """    if (filter !== 'all' && filter !== d) return;

    const domainTopics = topics.filter(t => t.domain === d);
    if (domainTopics.length === 0) return;"""

new_render = """    let domainTopics = topics.filter(t => t.domain === d);
    if (filter === 'top') {
      domainTopics = domainTopics.filter(t => t.priority === '1순위' || t.priority === '2순위');
    } else if (filter !== 'all' && filter !== d) {
      return;
    }
    if (domainTopics.length === 0) return;"""

content = content.replace(old_render, new_render)

# Update initial call to 'top'
content = content.replace("renderTopics('all');", "renderTopics('top');")

# Ensure no tildes
content = content.replace("38~45자", "38-45자")
content = content.replace("~", "-")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] build_pedagogy_16_html.js updated with 1-2 priority features.")
