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
    pg.wait_for_timeout(200)

    # Trigger training -> promotion modal appears
    pg.evaluate('executeTraining()')
    vis_immediately = pg.evaluate("""() => getComputedStyle(document.getElementById('troop-promotion-modal')).display""")
    print('Immediately after executeTraining -> promo modal display:', vis_immediately)

    # Wait 1.5s -> should auto-disappear!
    pg.wait_for_timeout(1500)
    vis_after_1500ms = pg.evaluate("""() => getComputedStyle(document.getElementById('troop-promotion-modal')).display""")
    print('After 1.5s -> promo modal display:', vis_after_1500ms)

    # Trigger training again -> click button to close immediately
    pg.evaluate('executeTraining()')
    pg.wait_for_timeout(100)
    pg.click('#troop-promotion-modal button')
    vis_after_click = pg.evaluate("""() => getComputedStyle(document.getElementById('troop-promotion-modal')).display""")
    print('After button click -> promo modal display:', vis_after_click)
    b.close()
