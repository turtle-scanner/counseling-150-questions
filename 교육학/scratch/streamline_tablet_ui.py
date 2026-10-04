import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title in Header
html = html.replace('🚨 2027 KICE 초압축 55제', '🐢 2027 KICE 핵심 단어장 (203선)')
html = html.replace('2027 KICE 초압축 55선', '2027 KICE 핵심 단어장 (203선)')
html = html.replace('앙키 카드 모드 &amp; 전체 표 모드 지원', '1인 1계정 클라우드 보호 • 실전 4줄 B4 답안지 • 안키 분산반복')

# 2. Modern Ultra-Clean Responsive Tablet & Mobile CSS
clean_tablet_css = """
    /* --- ULTRA-CLEAN TABLET & DESKTOP STREAMLINED LAYOUT --- */
    body {
      background: #090d16 !important;
      color: #f1f5f9 !important;
      font-family: 'Malgun Gothic', '맑은 고딕', sans-serif !important;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 40px;
    }
    
    /* Top Bar: Sleek & Compact */
    .app-header {
      background: #0f172a !important;
      border-bottom: 1px solid #1e293b !important;
      padding: 10px 16px !important;
      display: flex !important;
      flex-wrap: wrap;
      justify-content: space-between !important;
      align-items: center !important;
      gap: 8px;
    }
    .app-title-area {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .app-title {
      font-size: 1.15rem !important;
      font-weight: 800 !important;
      color: #fbbf24 !important;
      margin: 0 !important;
      letter-spacing: -0.5px;
    }
    .app-sub { display: none !important; }
    
    /* Horizontal Scrollable Category Pills (Tablet Touch Optimized) */
    .category-pills-container {
      display: flex !important;
      flex-wrap: nowrap !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      gap: 8px !important;
      padding: 8px 12px !important;
      background: #090d16 !important;
      border-bottom: 1px solid #1e293b !important;
    }
    .category-pills-container::-webkit-scrollbar { display: none; }
    .pill-btn {
      flex: 0 0 auto !important;
      padding: 6px 14px !important;
      border-radius: 20px !important;
      font-size: 0.9rem !important;
      font-weight: 600 !important;
      white-space: nowrap !important;
      cursor: pointer;
    }
    
    /* Compact Streamlined Controls Bar */
    .controls {
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 6px !important;
      padding: 8px 10px !important;
      background: #0d1322 !important;
      border-bottom: 1px solid #1e293b !important;
      margin-bottom: 12px !important;
    }
    .btn-control {
      min-width: auto !important;
      padding: 6px 12px !important;
      font-size: 0.88rem !important;
      font-weight: 600 !important;
      border-radius: 6px !important;
      margin: 0 !important;
      cursor: pointer;
      display: inline-flex !important;
      align-items: center !important;
      gap: 4px !important;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3) !important;
    }
    #search-input {
      width: 130px !important;
      padding: 6px 10px !important;
      font-size: 0.88rem !important;
      border-radius: 6px !important;
      margin: 0 !important;
    }
    
    /* Dashboard: Sleek Badge Row */
    #dashboard {
      padding: 6px 12px !important;
      margin: 4px 10px 8px 10px !important;
      font-size: 0.88rem !important;
      background: #111827 !important;
      border: 1px solid #1f2937 !important;
      gap: 15px !important;
    }
    
    /* Progress Energy Bar: Compact & Prominent */
    .progress-container {
      margin: 6px 12px !important;
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
    }
    .progress-bar {
      flex: 1 !important;
      height: 10px !important;
      background: #1e293b !important;
      border-radius: 5px !important;
      border: none !important;
    }
    .progress-fill {
      background: linear-gradient(90deg, #3b82f6, #10b981) !important;
      border-radius: 5px !important;
    }
    .progress-text {
      font-size: 0.95rem !important;
      color: #38bdf8 !important;
      font-weight: 800 !important;
      white-space: nowrap !important;
    }
    
    /* Main Tablet Container: Clean & Centered */
    .main-container {
      max-width: 860px !important;
      margin: 0 auto !important;
      padding: 0 12px !important;
    }
    
    /* Anki Card Container */
    .anki-card {
      background: #111827 !important;
      border: 1px solid #1f2937 !important;
      border-radius: 12px !important;
      padding: 18px 20px !important;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5) !important;
    }
    
    /* Question text */
    .card-q, #c-q {
      font-size: 1.18rem !important;
      line-height: 1.65 !important;
      font-weight: 400 !important;
      color: #f8fafc !important;
      margin: 12px 0 16px 0 !important;
      letter-spacing: -0.2px !important;
    }
    
    /* Flip button */
    .btn-flip {
      width: 100% !important;
      padding: 12px !important;
      font-size: 1.05rem !important;
      font-weight: 700 !important;
      border-radius: 8px !important;
      margin-bottom: 12px !important;
      cursor: pointer;
    }
    
    /* B4 Answer Sheet */
    .kice-sheet-wrapper {
      margin-top: 12px !important;
      border: 2px solid #ec4899 !important;
      border-radius: 8px !important;
    }
    .kice-textarea {
      font-size: 1.1rem !important;
      line-height: 40px !important;
      padding: 0 12px !important;
    }
    
    /* Official Answer Box */
    .answer-kw {
      font-size: 1.25rem !important;
      font-weight: 800 !important;
      color: #38bdf8 !important;
      margin: 10px 0 8px 0 !important;
      text-align: left !important;
    }
    .answer-text, #c-ans {
      font-size: 1.15rem !important;
      line-height: 1.75 !important;
      font-weight: 400 !important;
      color: #fef08a !important;
      padding: 14px 16px !important;
      background: #0f172a !important;
      border-radius: 8px !important;
      border-left: 4px solid #facc15 !important;
      margin-bottom: 12px !important;
    }
    
    /* Trap Box */
    .trap-box {
      font-size: 1rem !important;
      line-height: 1.6 !important;
      padding: 10px 14px !important;
      border-radius: 8px !important;
      margin-bottom: 12px !important;
    }
    
    /* SRS Review Buttons for Tablet Touch */
    .reward-container {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 8px !important;
      margin-top: 12px !important;
    }
    .reward-btn {
      padding: 10px 6px !important;
      min-height: 48px !important;
      font-size: 0.95rem !important;
      font-weight: 700 !important;
      border-radius: 8px !important;
    }
    
    /* Table Mode Styling for Tablets */
    .table-container {
      border-radius: 10px !important;
      background: #111827 !important;
      border: 1px solid #1f2937 !important;
    }
    .table-container table td {
      padding: 12px 14px !important;
      font-size: 0.98rem !important;
      line-height: 1.6 !important;
    }
    
    /* Responsive Tablet Adjustments (iPad 768px - 1024px) */
    @media (max-width: 900px) {
      .app-header { padding: 8px 12px !important; }
      .app-title { font-size: 1.05rem !important; }
      .controls { gap: 5px !important; padding: 6px !important; }
      .btn-control { min-width: auto !important; padding: 6px 10px !important; font-size: 0.82rem !important; }
      #search-input { width: 110px !important; font-size: 0.82rem !important; padding: 5px 8px !important; }
      .card-q, #c-q { font-size: 1.1rem !important; line-height: 1.6 !important; }
      .answer-text, #c-ans { font-size: 1.05rem !important; line-height: 1.65 !important; padding: 12px !important; }
      .reward-btn { min-height: 44px !important; font-size: 0.88rem !important; padding: 8px 4px !important; }
    }
"""

# Replace existing TABLET OPTIMIZATIONS block with clean_tablet_css
html = re.sub(
    r'/\*\s*TABLET OPTIMIZATIONS\s*\*/[\s\S]*?(?=/\*\s*4-LINE OFFICIAL)',
    clean_tablet_css.strip() + '\n\n  ',
    html
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Streamlined tablet & desktop layout successfully!")
