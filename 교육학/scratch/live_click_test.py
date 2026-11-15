# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

URL = 'file:///C:/Users/LENOVO/Desktop/sam3_update.html'
errors = []

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    pg.on('pageerror', lambda e: errors.append('PAGEERROR: ' + str(e)))
    pg.on('console', lambda m: errors.append('CONSOLE.' + m.type + ': ' + m.text) if m.type in ('error',) else None)
    pg.on('dialog', lambda d: (errors.append('DIALOG: ' + d.message[:150].replace('\n', ' ')), d.accept()))
    pg.goto(URL)
    pg.wait_for_timeout(2500)

    # 어떤 요소가 화면 중앙 클릭을 가로채는지 검사
    top = pg.evaluate("""() => {
      const el = document.elementFromPoint(innerWidth/2, innerHeight/2);
      return el ? (el.tagName + '#' + el.id + '.' + (el.className||'').toString().slice(0,80)) : null;
    }""")
    print('CENTER ELEMENT:', top)

    visible_modals = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')]
      .filter(e => getComputedStyle(e).display !== 'none' && getComputedStyle(e).visibility !== 'hidden')
      .map(e => e.id)""")
    print('VISIBLE MODALS AT LOAD:', visible_modals)

    def step(name, fn):
        before = len(errors)
        try:
            fn()
        except Exception as e:
            errors.append('STEP-EXC ' + name + ': ' + str(e)[:200])
        pg.wait_for_timeout(500)
        print('STEP', name, '-> new errors:', errors[before:])

    step('click start btn', lambda: pg.click('text=게임 시작', timeout=3000))
    print('VISIBLE MODALS AFTER START:', pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')]
      .filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)"""))
    step('open military menu', lambda: pg.click('text=1. 군사', timeout=3000))
    step('click 훈련', lambda: pg.click('.koei-popup-item:has-text("훈")', timeout=3000))
    step('open military menu 2', lambda: pg.click('text=1. 군사', timeout=3000))
    step('click 전쟁', lambda: pg.click('#popup-military .koei-popup-item:has-text("4.")', timeout=3000))
    print('VISIBLE MODALS AFTER WAR:', pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')]
      .filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)"""))
    pg.screenshot(path=r'C:\Users\LENOVO\Desktop\live_test.png')
    b.close()

print('\n=== ALL ERRORS ===')
for e in errors:
    print(e)
