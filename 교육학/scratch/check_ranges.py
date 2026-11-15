import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

def find_range(func_name, next_marker):
    p1 = text.find(func_name)
    if p1 == -1:
        print(f"NOT FOUND: {func_name}")
        return
    p2 = text.find(next_marker, p1)
    print(f"{func_name} -> {next_marker}: {p1} to {p2} (len: {p2 - p1})")

find_range('function openOfficerDeployModal', 'function confirmOfficerDeployment')
find_range('function initHexBattleUnits', 'function renderBattlefield')
find_range('function updateActionCommands', 'function onCmdAttack')
find_range('function executeSkillAction', 'function calculateCombatDamage')
find_range('function calculateCombatDamage', 'function applyDamage')
find_range('function runEnemyAI', 'function finishFullTurn')
find_range('function triggerSupplyRaid', 'function checkTreasureDiscovery')
