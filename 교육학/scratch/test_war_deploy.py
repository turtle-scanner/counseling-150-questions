# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

URL = 'file:///C:/Users/LENOVO/Desktop/sam3_update.html'
errors = []
dialogs = []

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    pg.on('pageerror', lambda e: errors.append('PAGEERROR: ' + str(e)))
    pg.on('console', lambda m: errors.append('CONSOLE.' + m.type + ': ' + m.text) if m.type == 'error' else None)
    pg.on('dialog', lambda d: (dialogs.append(d.message.replace('\n', ' ')[:150]), d.accept()))
    pg.goto(URL)
    pg.wait_for_timeout(1200)

    # Close intro
    pg.click('#liu-bei-intro-modal button:has-text("게임 시작")', timeout=3000)
    pg.wait_for_timeout(300)

    # Call openWarModal(10) (익주 침공)
    pg.evaluate('openWarModal(10)')
    pg.wait_for_timeout(400)
    vis1 = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)""")
    print('After openWarModal(10) -> visible modals:', vis1, 'errors:', errors)

    # Click #btn-deploy-confirm (선발 장수 출진!)
    pg.click('#btn-deploy-confirm', timeout=3000)
    pg.wait_for_timeout(500)
    vis2 = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)""")
    print('After clicking #btn-deploy-confirm -> visible modals:', vis2, 'errors:', errors, 'dialogs:', dialogs)

    # If inside hex battle modal, test clicking attack / wait / archery
    if 'hex-battle-modal' in vis2:
        units = pg.evaluate('() => sam5BattleState.units.map(u => ({id:u.id, name:u.name, side:u.side, x:u.x, y:u.y, soldiers:u.soldiers}))')
        print('Hex Battle Units:', units)
    b.close()
