import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = {
    'getMaxDeployableCount': 'function getMaxDeployableCount' in text,
    'deploy_levels_scale': 'if (maxLvl >= 50) return 6;' in text and 'if (maxLvl >= 10) return 4;' in text,
    'lubu_lv10': "name: '여포 (봉선)'" in text and "level: 10" in text,
    'sunce_lv10': "name: '손책 (백부)'" in text and "level: 10" in text,
    'hwangchung_archer': "id: 'huang_zhong'" in text and "신궁" in text,
    'go_baduk_encirclement': '바둑의 3면 포위 일제합공' in text and 'getSurroundingUnits' in text,
    'anhaeng_long_range': 'arcRange: 4' in text and 'onCmdArchery' in text,
    'auto_switch_anhaeng': "u.formation = 'anhaeng'" in text,
    'ally_depot_tile_8': '🌾 아군 군량고!' in text and 'terrain === 8' in text,
    'enemy_depot_guard': "role: 'guard_depot'" in text and '군량고 철통 수비대장' in text,
    'ally_depot_raider': "role: 'raider'" in text and '아군 군량고 우회 기습' in text,
    'triggerAllySupplyRaid': 'function triggerAllySupplyRaid' in text,
    'triggerSupplyRaid': 'function triggerSupplyRaid' in text
}

print("=== FINAL VERIFICATION CHECKS ===")
all_pass = True
for k, v in checks.items():
    print(f"[{'PASS' if v else 'FAIL'}] {k}")
    if not v:
        all_pass = False

print(f"Overall Result: {'ALL PASS!' if all_pass else 'SOME FAILED'}")
