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

    res = pg.evaluate("""() => {
      sam5BattleState.battleOver = false;
      initHexBattleUnits(PROVINCES[9], PROVINCES[7]);
      
      // Defeat 1 normal enemy: 군량도위
      const depot = UNITS.find(u => u.name.includes('군량도위'));
      depot.troops = 0;
      depot.defeated = true;

      checkVictoryCondition();
      const stateAfterDepot = sam5BattleState.battleOver;

      // Defeat boss: 장위 (장로는 군주지만 장위는 부하)
      const boss = UNITS.find(u => u.isBoss);
      boss.troops = 0;
      boss.defeated = true;
      checkVictoryCondition();
      const stateAfterNonRulerBoss = sam5BattleState.battleOver;

      // Now defeat ALL remaining enemies
      UNITS.forEach(u => { if (u.faction === 'enemy') { u.troops = 0; u.defeated = true; } });
      checkVictoryCondition();
      const stateAfterAllDefeated = sam5BattleState.battleOver;

      return {
        stateAfterDepot,
        stateAfterNonRulerBoss,
        stateAfterAllDefeated
      };
    }""")
    print('Victory test result:', res)
    b.close()
