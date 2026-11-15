# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

URL = 'file:///C:/Users/LENOVO/Desktop/sam3_update.html'
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    pg.on('dialog', lambda d: d.accept())
    pg.goto(URL)
    pg.wait_for_timeout(800)
    pg.click('#liu-bei-intro-modal button:has-text("게임 시작")')
    pg.wait_for_timeout(300)

    # Trigger Duel Battle directly
    pg.evaluate("""() => {
      openDuelFightModal(
        { name: '위연', war: 91, hp: 100, avatar: '⚔️' },
        { name: '장료', war: 101, hp: 100, avatar: '👹', isBoss: false, troops: 3500 }
      );
    }""")
    pg.wait_for_timeout(400)
    vis_duel = pg.evaluate("""() => getComputedStyle(document.getElementById('duelModal')).display""")
    print('1. Duel modal opened:', vis_duel)

    # Force victory via endDuelBattle('victory', 'test')
    pg.evaluate("endDuelBattle('victory', '테스트')")
    pg.wait_for_timeout(300)

    log_content = pg.evaluate("() => document.getElementById('duelNarrative').innerText")
    print('2. Narrative content after victory:\n', log_content[:200])

    # Check visible display immediately
    vis_immediately = pg.evaluate("""() => getComputedStyle(document.getElementById('duelModal')).display""")
    print('3. Duel modal display immediately after victory:', vis_immediately)

    # Wait 2.2s -> should auto-close!
    pg.wait_for_timeout(2200)
    vis_after_2s = pg.evaluate("""() => getComputedStyle(document.getElementById('duelModal')).display""")
    print('4. Duel modal display after 2.2s (auto-close):', vis_after_2s)

    b.close()
