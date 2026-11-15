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

    # 1. Test Sango Modal
    pg.click('button:has-text("삼고초려")')
    pg.wait_for_timeout(300)
    vis_sango = pg.evaluate("() => getComputedStyle(document.getElementById('sango-modal')).display")
    print('1. Sango modal opened:', vis_sango)

    # Step 1 click
    pg.click('#sango-action-buttons button')
    pg.wait_for_timeout(200)
    print('2. After Sango Step 1 -> stage:', pg.evaluate('() => sangoStage'))

    # Step 2 click
    pg.click('#sango-action-buttons button')
    pg.wait_for_timeout(200)
    print('3. After Sango Step 2 -> stage:', pg.evaluate('() => sangoStage'))

    # Step 3 click -> Recruit Zhuge Liang!
    pg.click('#sango-action-buttons button')
    pg.wait_for_timeout(300)
    zhuge = pg.evaluate("() => MY_OFFICERS.find(o => o.name.includes('제갈량'))")
    print('4. Zhuge Liang recruited:', zhuge['name'], 'INT:', zhuge['int'], 'title:', zhuge['title'])

    # Close Sango modal
    pg.click('#sango-modal button:has-text("닫기")')
    pg.wait_for_timeout(200)

    # 2. Test CheckVictoryCondition with non-boss defeat
    # Initialize Hex Units
    pg.evaluate("initHexBattleUnits(PROVINCES[9], PROVINCES[7])")
    # Defeat a normal enemy unit (e.g. 군량도위)
    pg.evaluate("""() => {
      const normalEnemy = UNITS.find(u => u.faction === 'enemy' && !u.name.includes('조조') && !u.name.includes('원소'));
      if (normalEnemy) {
        normalEnemy.troops = 0;
        normalEnemy.defeated = true;
      }
      checkVictoryCondition();
    }""")
    battleOver = pg.evaluate("() => sam5BattleState.battleOver")
    print('5. Battle over after defeating normal enemy (should be False):', battleOver)

    b.close()
