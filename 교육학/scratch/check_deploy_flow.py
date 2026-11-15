# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('openModal officer-deploy-modal:', "openModal('officer-deploy-modal')" in html)
print('confirmOfficerDeployment calls openHexBattle:', 'openHexBattle(deployingTargetProv, deployingFromProv, deployedOfficers)' in html)
print('openWarModal calls openOfficerDeployModal:', 'openOfficerDeployModal(target, myProv, false);' in html)
