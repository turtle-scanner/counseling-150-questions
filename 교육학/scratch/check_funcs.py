import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

funcs = [
    'function getMaxDeployableCount',
    'function openOfficerDeployModal',
    'function renderDeployOfficerList',
    'function toggleDeployOfficer',
    'function initHexBattleUnits',
    'function calculateCombatDamage',
    'function executeSkillAction',
    'function updateActionCommands',
    'function runEnemyAI',
    'function finishFullTurn',
    'function renderBattlefield',
    'function triggerSupplyRaid'
]

for fn in funcs:
    print(fn, ':', fn in text)
