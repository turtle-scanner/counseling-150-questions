import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make containers wider for tablet
html = html.replace('.main-container { max-width: 800px;', '.main-container { max-width: 1100px;')
html = html.replace('#mode-anki { width: 100%; max-width: 600px;', '#mode-anki { width: 100%; max-width: 900px;')

# Make textarea larger and font bigger
html = html.replace('textarea { width: 100%; height: 100px;', 'textarea { width: 100%; height: 180px; font-size: 1.15rem;')

# Make question text bigger
html = html.replace('.card-q { font-size: 1.15rem;', '.card-q { font-size: 1.35rem;')

# Make flip button bigger
html = html.replace('.btn-flip { width: 100%; background: #d97706; color: #fff; border: none; padding: 14px; border-radius: 8px; font-size: 1.05rem;', '.btn-flip { width: 100%; background: #d97706; color: #fff; border: none; padding: 20px; border-radius: 8px; font-size: 1.25rem;')

# Add responsive CSS at the end of the style block
responsive_css = """
    /* TABLET SPECIFIC TWEAKS */
    @media (min-width: 768px) {
      .app-title { font-size: 1.6rem; }
      .btn-control { font-size: 1.1rem; padding: 14px 25px; }
      .reward-btn { padding: 18px; font-size: 1.2rem; }
      th, td { font-size: 11pt; padding: 15px; }
      .modal-content { max-width: 600px; }
      .modal-title { font-size: 1.6rem; }
      .modal-msg { font-size: 1.2rem; }
    }
  </style>"""

html = html.replace('  </style>', responsive_css)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Tablet sizing applied successfully.")
