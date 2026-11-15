# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

URL = 'file:///C:/Users/LENOVO/Desktop/sam3_update.html'
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    pg.goto(URL)
    pg.wait_for_timeout(400)

    res = pg.evaluate("""() => {
      initHexBattleUnits(PROVINCES[9], PROVINCES[7]);
      const RULER_BOSSES = ['조조', '원소', '손책', '손권', '유표', '유장', '장로', '마등', '공손찬', '동탁', '여포', '장각', '사마의'];
      const realBoss = UNITS.find(u => u.faction === "enemy" && RULER_BOSSES.some(r => (u.name && u.name.includes(r)) || (u.fullName && u.fullName.includes(r))));
      return {
        realBoss: realBoss ? { name: realBoss.name, fullName: realBoss.fullName } : null,
        matches: UNITS.filter(u => u.faction === "enemy").map(u => ({
          name: u.name,
          fullName: u.fullName,
          matchedRuler: RULER_BOSSES.filter(r => (u.name && u.name.includes(r)) || (u.fullName && u.fullName.includes(r)))
        }))
      };
    }""")
    print('Check real boss logic:', res)
    b.close()
