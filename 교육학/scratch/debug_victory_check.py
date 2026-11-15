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
    pg.wait_for_timeout(500)

    debug_info = pg.evaluate("""() => {
      initHexBattleUnits(PROVINCES[9], PROVINCES[7]);
      const enemies = UNITS.filter(u => u.faction === 'enemy');
      const boss = UNITS.find(u => u.isBoss);
      
      // Let's inspect checkVictoryCondition source code in runtime
      const cvSrc = checkVictoryCondition.toString();

      return {
        enemiesCount: enemies.length,
        enemiesNames: enemies.map(u => ({ name: u.name, isBoss: u.isBoss, troops: u.troops })),
        bossName: boss ? boss.name : null,
        cvSrcSnippet: cvSrc.slice(0, 500)
      };
    }""")
    print('Debug info:', debug_info)
    b.close()
