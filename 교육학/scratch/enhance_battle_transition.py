# -*- coding: utf-8 -*-
import os
import re

def main():
    target_path = r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html'
    with open(target_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. 출전 장수 편성 모달 제목 및 버튼 텍스트 강화
    html = html.replace('[출전 장수 편성] 침공 부대 선발', '[출전 장수 편성] 침공 부대 선발 ➔ 삼국지 V 10턴 헥스 결전')
    html = html.replace('선발 장수 출진! (전장 돌입)', '선발 장수 출진! (삼국지 5 헥스 전장 돌입)')

    # 2. 우측 패널 버튼 텍스트 강화
    panel_btn_old = """            <button onclick="openWarModal(${p.id})" class="w-full py-2 bg-gradient-to-r from-red-700 to-rose-700 hover:from-red-600 hover:to-rose-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex items-center justify-center gap-1.5 animate-pulse">
              <span>⚔️</span> 이 적 영지 즉시 침공 (전쟁 개시!)
            </button>"""

    panel_btn_new = """            <button onclick="openWarModal(${p.id})" class="w-full py-2.5 bg-gradient-to-r from-red-700 via-amber-600 to-rose-700 hover:from-red-600 hover:to-rose-500 text-yellow-100 font-black text-xs rounded-lg border-2 border-yellow-300 shadow-2xl flex items-center justify-center gap-2 animate-pulse">
              <span>⚔️</span> ${p.id}. ${p.name} (${p.ruler}군) 침공작전 개시 (출전 장수 편성)
            </button>"""

    if panel_btn_old in html:
        html = html.replace(panel_btn_old, panel_btn_new)
        print("우측 패널 침공 버튼 텍스트 보강 완료!")

    # 3. openHexBattle 렌더링 순서 최적화 (모달 open 후 캔버스 렌더링)
    hex_open_old = """      resetHexBattlefield(targetProv, fromProv, deployedOfficers);
      openModal('hex-battle-modal');
      logMessage(`⚔️ [전술 결전 돌입] ${fromProv.name}의 아군이 ${targetProv.name}의 ${targetProv.ruler}군을 상대로 10턴 헥스 결전에 돌입했습니다!`, 'text-yellow-300 font-black');"""

    hex_open_new = """      openModal('hex-battle-modal');
      resetHexBattlefield(targetProv, fromProv, deployedOfficers);
      setTimeout(() => {
        renderBattlefield();
        deselectUnit();
      }, 50);
      logMessage(`⚔️ [삼국지 5 헥스 결전 돌입] ${fromProv.name}의 아군이 ${targetProv.name}의 ${targetProv.ruler}군을 상대로 10턴 결전에 돌입했습니다!`, 'text-yellow-300 font-black');"""

    if hex_open_old in html:
        html = html.replace(hex_open_old, hex_open_new)
        print("openHexBattle 모달 오픈 및 캔버스 렌더링 순서 최적화 완료!")

    # 4. confirmOfficerDeployment에서 즉시 삼국지5 전장으로 진입하는 안내 로그 추가
    deploy_confirm_old = """        // 일반 공격 10턴 헥스 결전
        openHexBattle(deployingTargetProv, deployingFromProv, deployedOfficers);"""

    deploy_confirm_new = """        // 일반 공격 ➔ 삼국지 5 10턴 헥스 결전 전장 돌입!
        logMessage(`🚩 [선발 완료] ${deployedOfficers.map(o => o.name.split(' ')[0]).join(', ')} 장군이 출격하여 삼국지 5 전장에 포진합니다!`, 'text-yellow-300 font-black');
        openHexBattle(deployingTargetProv, deployingFromProv, deployedOfficers);"""

    if deploy_confirm_old in html:
        html = html.replace(deploy_confirm_old, deploy_confirm_new)
        print("confirmOfficerDeployment 출전 로그 보강 완료!")

    # 5. 파일 저장 및 4개 복사본 전체 동기화
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("데스크톱 파일 저장 완료!")

    for p in [r"C:\Users\LENOVO\Desktop\sam3_update.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
    print("모든 파일 및 Git 저장소 동기화 완료!")

if __name__ == "__main__":
    main()
