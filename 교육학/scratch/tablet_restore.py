import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure anki-card and mode-anki can stretch horizontally on tablets
html = html.replace('#mode-anki { width: 100%; max-width: 600px;', '#mode-anki { width: 100%; max-width: 900px;')

tablet_css = """
    /* TABLET SPECIFIC TWEAKS (Width and Font only, keeping heights compact) */
    @media (min-width: 768px) {
      .app-title { font-size: 1.4rem; }
      .card-q { font-size: 1.3rem; }
      textarea { font-size: 1.1rem; }
      .answer-text { font-size: 1.1rem; }
      th, td { font-size: 1.15rem; padding: 15px; }
      .modal-content { max-width: 600px; }
    }
  </style>"""

# Add it back to the end of the style block if it's not there
if "TABLET SPECIFIC TWEAKS" not in html:
    html = html.replace('  </style>', tablet_css)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Tablet sizing restored.")
