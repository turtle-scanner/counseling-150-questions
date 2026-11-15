# -*- coding: utf-8 -*-
import os
import json
import base64
import re

def build():
    print("=== 삼국지 3 정통 시나리오 선택 & 군주 얼굴 100% 매칭 빌드 시작 ===")

    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")
    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    # 방금 크롭한 삼국지 3 8대 군주 얼굴 읽기
    s3_faces_path = os.path.join(brain_dir, "portraits_s3_extracted", "s3_faces.json")
    with open(s3_faces_path, "r", encoding="utf-8") as f:
        s3_faces = json.load(f)

    # 초상화 딕셔너리 통합
    all_portraits = dict(assets["portraits"])
    all_portraits.update(s3_faces)
    # 유비 최우선 매칭: liubei_s3 -> liubei
    all_portraits["liubei"] = s3_faces["liubei_s3"]
    all_portraits["caocao_s3"] = s3_faces["caocao_s3"]
    all_portraits["sunquan_s3"] = s3_faces["sunquan_s3"]
    all_portraits["yuanshao_s3"] = s3_faces["yuanshao_s3"]
    all_portraits["liuzhang_s3"] = s3_faces["liuzhang_s3"]
    all_portraits["mateng_s3"] = s3_faces["mateng_s3"]
    all_portraits["zhanglu_s3"] = s3_faces["zhanglu_s3"]
    all_portraits["liubiao_s3"] = s3_faces["liubiao_s3"]

    map_b64 = assets["map_b64"]
    portraits_json = json.dumps(all_portraits)

    # 기존 최신 소스코드 가져오기
    master_src_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    with open(master_src_path, "r", encoding="utf-8") as f:
        src = f.read()

    # 인라인 초상화 태그 생성 헬퍼
    def get_img_tag(key, name, extra_class=""):
        b64 = all_portraits.get(key, all_portraits.get("liubei", ""))
        return f'<img src="{b64}" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow {extra_class}" alt="{name}">'

    # 1. 원작 스크린샷 100% 동일: 시나리오 선택 & 설정 & 군주 선택 오프닝 모달
    # media_1793683121813_a4e2994a.png (시나리오 선택 창)
    # media_1793683169122_2f71c798.png (환경 설정 창)
    # media_1793683139288_5478174f.png (정통 8대 군주 얼굴 창)
    new_opening_modal = f"""
  <!-- ==================== 🔥 [정통 코에이 삼국지 III] 시나리오 & 군주 선택 오프닝 ==================== -->
  <div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] flex items-center justify-center p-3 bg-black/95">
    <div class="koei-box w-full max-w-4xl p-5 rounded-lg shadow-2xl border-4 border-amber-400 max-h-[96vh] flex flex-col justify-between overflow-y-auto">
      
      <!-- 상단 원작 타이틀 및 결정/중지 버튼 -->
      <div class="border-b-2 border-amber-400 pb-2 mb-3 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="text-2xl">👑</span>
          <div>
            <h1 class="text-base font-black text-yellow-300 text-pixel tracking-wide">
              삼국지 III (三國志 III) : 시나리오 및 군주 선택
            </h1>
            <div class="text-[11px] text-amber-200" id="intro-status-summary">
              선택 시나리오 : <span id="summary-scenario-text" class="text-yellow-300 font-bold">194년 11월 군웅 중원에서 싸우고 조조 세력을 신장시키다</span> | 
              선택 군주 : <span id="summary-ruler-text" class="text-emerald-300 font-black">유비 (형주 8번)</span>
            </div>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="confirmIntroStart()" class="px-5 py-2 bg-gradient-to-r from-emerald-700 to-green-600 hover:from-emerald-600 hover:to-green-500 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow-xl flex items-center gap-1 animate-pulse">
            <span>⚔️</span> 결 정 (게임 시작)
          </button>
          <button onclick="closeModal('intro-ruler-select-modal')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded border border-slate-600">
            중 지
          </button>
        </div>
      </div>

      <!-- 1단계: 원작 6대 시나리오 선택 박스 (media_1793683121813_a4e2994a.png 100% 동일) -->
      <div class="mb-3 bg-blue-950/90 border-2 border-amber-500/80 rounded p-3">
        <div class="text-xs text-amber-300 font-bold mb-2 flex items-center justify-between border-b border-blue-800 pb-1">
          <span>📜 시나리오를 선택해 주십시오 (클릭하여 변경):</span>
          <span class="text-slate-400 text-[11px]">코에이 정통 6대 역사 연표</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-1.5 text-xs font-mono" id="scenario-list-box">
          <div onclick="selectScenario(1, 189, 12, '189년 12월 동탁이 소제를 퇴폐시켜 낙양 불타오르다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300" id="scen-1">
            <span>1. 189년 12월 동탁이 소제를 퇴폐시켜 낙양 불타오르다</span>
            <span class="text-[10px] text-amber-400">반동탁</span>
          </div>
          <div onclick="selectScenario(2, 194, 11, '194년 11월 군웅 중원에서 싸우고 조조 세력을 신장시키다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-amber-950/80 border-yellow-400 text-yellow-200 ring-2 ring-yellow-400 font-bold" id="scen-2">
            <span>2. 194년 11월 군웅 중원에서 싸우고 조조 세력을 신장시키다</span>
            <span class="text-[10px] text-yellow-300">★군웅할거</span>
          </div>
          <div onclick="selectScenario(3, 201, 10, '201년 10월 하북에는 폭풍이 일어나고 형주에는 봄이 오다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300" id="scen-3">
            <span>3. 201년 10월 하북에는 폭풍이 일어나고 형주에는 봄이 오다</span>
            <span class="text-[10px] text-cyan-300">관도대전</span>
          </div>
          <div onclick="selectScenario(4, 208, 9, '208년 9월 와룡공명 적벽에서 동풍을 부르다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300" id="scen-4">
            <span>4. 208년 9월 와룡공명 적벽에서 동풍을 부르다</span>
            <span class="text-[10px] text-red-300">적벽대전</span>
          </div>
          <div onclick="selectScenario(5, 221, 4, '221년 4월 후한이 멸망하고 삼국시대 시작되다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300" id="scen-5">
            <span>5. 221년 4월 후한이 멸망하고 삼국시대 시작되다</span>
            <span class="text-[10px] text-emerald-300">삼국정립</span>
          </div>
          <div onclick="selectScenario(6, 235, 2, '235년 2월 강유에게 후사를 부탁하고 거성 떨어지다')" class="scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300" id="scen-6">
            <span>6. 235년 2월 강유에게 후사를 부탁하고 거성 떨어지다</span>
            <span class="text-[10px] text-purple-300">출사표</span>
          </div>
        </div>
      </div>

      <!-- 2단계: 환경 설정 바 (media_1793683169122_2f71c798.png 100% 동일) -->
      <div class="mb-3 bg-blue-950/80 border border-blue-700 p-2.5 rounded grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
        <!-- 게임 레벨 -->
        <div class="flex flex-col gap-1">
          <span class="text-amber-300 font-bold">게임 레벨 :</span>
          <div class="flex gap-1">
            <button onclick="setIntroDifficulty('easy')" id="btn-diff-easy" class="px-2 py-0.5 rounded text-[11px] bg-slate-900 border border-slate-600 text-slate-300">초급</button>
            <button onclick="setIntroDifficulty('normal')" id="btn-diff-normal" class="px-2 py-0.5 rounded text-[11px] bg-slate-900 border border-slate-600 text-slate-300">중급</button>
            <button onclick="setIntroDifficulty('hard')" id="btn-diff-hard" class="px-2 py-0.5 rounded text-[11px] bg-red-900 border-2 border-red-500 text-yellow-200 font-black shadow ring-1 ring-red-400">🔥 상급</button>
          </div>
        </div>
        <!-- 게임 모드 -->
        <div class="flex flex-col gap-1">
          <span class="text-amber-300 font-bold">게임 모드 :</span>
          <div class="flex gap-1">
            <button class="px-2 py-0.5 rounded text-[11px] bg-blue-900 border border-blue-400 text-cyan-200 font-bold">사실 모드</button>
            <button class="px-2 py-0.5 rounded text-[11px] bg-slate-900 border border-slate-600 text-slate-400">가상 모드</button>
          </div>
        </div>
        <!-- 전쟁 연출 -->
        <div class="flex flex-col gap-1">
          <span class="text-amber-300 font-bold">전쟁 (헥스 전장) :</span>
          <div class="flex gap-1">
            <button class="px-2 py-0.5 rounded text-[11px] bg-red-900 border border-red-400 text-yellow-200 font-bold">본 다</button>
            <button class="px-2 py-0.5 rounded text-[11px] bg-slate-900 border border-slate-600 text-slate-400">안본다</button>
          </div>
        </div>
        <!-- 소리 음향 -->
        <div class="flex flex-col gap-1">
          <span class="text-amber-300 font-bold">BGM / 효과음 :</span>
          <div class="flex gap-1">
            <button onclick="toggleBGM()" class="px-2 py-0.5 rounded text-[11px] bg-emerald-900 border border-emerald-400 text-yellow-200 font-bold">ON (재생)</button>
            <button onclick="toggleBGM()" class="px-2 py-0.5 rounded text-[11px] bg-slate-900 border border-slate-600 text-slate-400">OFF</button>
          </div>
        </div>
      </div>

      <!-- 3단계: 정통 12군주 선택 그리드 (유비 최우선 1번 & 100% 인라인 Base64 도트 초상화!) -->
      <div>
        <div class="text-xs text-amber-300 font-bold mb-2 flex items-center justify-between">
          <span>🚩 플레이할 군주를 선택하십시오 (유비 최우선 & 코에이 정통 도트 초상화 100% 매칭):</span>
          <span class="text-cyan-300 text-[11px]">클릭 시 해당 군주로 본거지와 장수 자동 세팅</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2">
          <!-- 1. 유비 (최우선 배치! 원작 스크린샷 media_1793683139288_5478174f.png 초록 타일 유비) -->
          <div onclick="selectIntroRuler('유비', 8, 'liubei_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-amber-950/80 border-yellow-400 ring-2 ring-yellow-400 shadow-xl" id="card-유비">
            {get_img_tag("liubei_s3", "유비", "ring-2 ring-emerald-500")}
            <div class="font-black text-xs text-yellow-200">1. 유비 (현덕)</div>
            <div class="text-[10px] text-emerald-300 font-bold bg-emerald-950/90 px-2 py-0.5 rounded border border-emerald-600 mt-1">형주 (8번)</div>
          </div>

          <!-- 2. 조조 (원작 파랑 타일 조조) -->
          <div onclick="selectIntroRuler('조조', 13, 'caocao_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-조조">
            {get_img_tag("caocao_s3", "조조", "ring-1 ring-blue-500")}
            <div class="font-black text-xs text-white">2. 조조 (맹덕)</div>
            <div class="text-[10px] text-blue-300 font-bold bg-blue-950/90 px-2 py-0.5 rounded border border-blue-600 mt-1">낙양 (13번)</div>
          </div>

          <!-- 3. 손권/손책 (원작 주황 타일 손권) -->
          <div onclick="selectIntroRuler('손책', 7, 'sunquan_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-손책">
            {get_img_tag("sunquan_s3", "손책", "ring-1 ring-orange-500")}
            <div class="font-black text-xs text-white">3. 손책 / 손권</div>
            <div class="text-[10px] text-orange-300 font-bold bg-orange-950/90 px-2 py-0.5 rounded border border-orange-600 mt-1">노강/양주 (7번)</div>
          </div>

          <!-- 4. 원소 (원작 올리브 타일 원소) -->
          <div onclick="selectIntroRuler('원소', 2, 'yuanshao_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-원소">
            {get_img_tag("yuanshao_s3", "원소", "ring-1 ring-yellow-500")}
            <div class="font-black text-xs text-white">4. 원소 (본초)</div>
            <div class="text-[10px] text-yellow-300 font-bold bg-yellow-950/90 px-2 py-0.5 rounded border border-yellow-600 mt-1">남피/기주 (2번)</div>
          </div>

          <!-- 5. 유장 (원작 보라 타일 유장) -->
          <div onclick="selectIntroRuler('유장', 10, 'liuzhang_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-유장">
            {get_img_tag("liuzhang_s3", "유장", "ring-1 ring-purple-500")}
            <div class="font-black text-xs text-white">5. 유장 (계옥)</div>
            <div class="text-[10px] text-purple-300 font-bold bg-purple-950/90 px-2 py-0.5 rounded border border-purple-600 mt-1">성도/익주 (10번)</div>
          </div>

          <!-- 6. 마등 (원작 청록 타일 마등) -->
          <div onclick="selectIntroRuler('마등', 11, 'mateng_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-마등">
            {get_img_tag("mateng_s3", "마등", "ring-1 ring-teal-500")}
            <div class="font-black text-xs text-white">6. 마등 (수성)</div>
            <div class="text-[10px] text-teal-300 font-bold bg-teal-950/90 px-2 py-0.5 rounded border border-teal-600 mt-1">서량/량주 (11번)</div>
          </div>

          <!-- 7. 장노 (원작 녹색 타일 장노) -->
          <div onclick="selectIntroRuler('장노', 10, 'zhanglu_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-장노">
            {get_img_tag("zhanglu_s3", "장노", "ring-1 ring-green-500")}
            <div class="font-black text-xs text-white">7. 장노 (공기)</div>
            <div class="text-[10px] text-green-300 font-bold bg-green-950/90 px-2 py-0.5 rounded border border-green-600 mt-1">한중 (10번)</div>
          </div>

          <!-- 8. 유표 (원작 민트 타일 유표) -->
          <div onclick="selectIntroRuler('유표', 8, 'liubiao_s3')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-유표">
            {get_img_tag("liubiao_s3", "유표", "ring-1 ring-cyan-500")}
            <div class="font-black text-xs text-white">8. 유표 (경승)</div>
            <div class="text-[10px] text-cyan-300 font-bold bg-cyan-950/90 px-2 py-0.5 rounded border border-cyan-600 mt-1">양양 (8번)</div>
          </div>

          <!-- 9. 여포 -->
          <div onclick="selectIntroRuler('여포', 6, 'lubu')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-여포">
            {get_img_tag("lubu", "여포", "ring-1 ring-rose-500")}
            <div class="font-black text-xs text-white">9. 여포 (봉선)</div>
            <div class="text-[10px] text-rose-300 font-bold bg-rose-950/90 px-2 py-0.5 rounded border border-rose-600 mt-1">복양/연주 (6번)</div>
          </div>

          <!-- 10. 공손찬 -->
          <div onclick="selectIntroRuler('공손찬', 1, 'gongsongzan')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-공손찬">
            {get_img_tag("gongsongzan", "공손찬", "ring-1 ring-amber-500")}
            <div class="font-black text-xs text-white">10. 공손찬 (백규)</div>
            <div class="text-[10px] text-amber-300 font-bold bg-amber-950/90 px-2 py-0.5 rounded border border-amber-600 mt-1">북평/유주 (1번)</div>
          </div>

          <!-- 11. 원술 -->
          <div onclick="selectIntroRuler('원술', 3, 'yuanshu')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-원술">
            {get_img_tag("yuanshu", "원술", "ring-1 ring-pink-500")}
            <div class="font-black text-xs text-white">11. 원술 (공로)</div>
            <div class="text-[10px] text-pink-300 font-bold bg-pink-950/90 px-2 py-0.5 rounded border border-pink-600 mt-1">완/예주 (3번)</div>
          </div>

          <!-- 12. 공융 -->
          <div onclick="selectIntroRuler('공융', 3, 'gongyong')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-공융">
            {get_img_tag("gongyong", "공융", "ring-1 ring-lime-500")}
            <div class="font-black text-xs text-white">12. 공융 (문거)</div>
            <div class="text-[10px] text-lime-300 font-bold bg-lime-950/90 px-2 py-0.5 rounded border border-lime-600 mt-1">북해/청주 (3번)</div>
          </div>
        </div>
      </div>

    </div>
  </div>
"""

    # 2. 시나리오 선택 스크립트 로직
    scenario_js = """
    // ==================== 🔥 원작 시나리오 1~6 선택 엔진 ====================
    let selectedScenarioId = 2;
    let selectedScenarioYear = 194;
    let selectedScenarioMonth = 11;
    let selectedScenarioTitle = '194년 11월 군웅 중원에서 싸우고 조조 세력을 신장시키다';

    function selectScenario(id, year, month, title) {
      selectedScenarioId = id;
      selectedScenarioYear = year;
      selectedScenarioMonth = month;
      selectedScenarioTitle = title;

      for (let i = 1; i <= 6; i++) {
        const item = document.getElementById('scen-' + i);
        if (item) {
          if (i === id) {
            item.className = 'scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-amber-950/80 border-yellow-400 text-yellow-200 ring-2 ring-yellow-400 font-bold';
          } else {
            item.className = 'scenario-item p-2 rounded border cursor-pointer transition flex items-center justify-between bg-blue-900/40 border-blue-700 hover:bg-blue-800 text-slate-300';
          }
        }
      }

      document.getElementById('summary-scenario-text').innerText = title;
      gameState.year = year;
      gameState.month = month;
      const yearEl = document.getElementById('year-val');
      const monthEl = document.getElementById('month-val');
      if (yearEl) yearEl.innerText = `${year}년`;
      if (monthEl) monthEl.innerText = `${month}월`;

      playTone(440, 0.1, 'sine', 0.15);
    }
"""

    # 3. 기존 인트로 모달 교체
    pattern_old_intro = r'<!-- ==================== 🔥 \[오프닝\] 12대 군주 선택[\s\S]*?</div>\s+</div>\s+</div>'
    if re.search(pattern_old_intro, src):
        src = re.sub(pattern_old_intro, new_opening_modal.strip(), src)
        print("Successfully replaced intro modal with authentic Scenario & S3 Face selector!")
    else:
        # Fallback replacement
        idx = src.find('<div id="intro-ruler-select-modal"')
        if idx != -1:
            idx2 = src.find('<!-- ==================== 🔥 삼국지 V', idx)
            if idx2 != -1:
                src = src[:idx] + new_opening_modal + "\n" + src[idx2:]
                print("Successfully replaced intro modal via index find!")

    # 4. JS 스크립트에 scenario_js 추가
    src = src.replace("</script>\n</body>", f"\n{scenario_js}\n</script>\n</body>")

    # 5. PORTRAITS 딕셔너리에 새 얼굴들 반영
    src = src.replace("__PORTRAITS_JSON__", portraits_json)
    src = src.replace("__LIUBEI_B64__", all_portraits["liubei"])

    # 6. 대상 파일들에 최종 배포
    target_paths = [
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in target_paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(src)
            print(f"Generated: {p} ({len(src):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 모든 시나리오 & 얼굴 매칭 완료! ===")

if __name__ == "__main__":
    build()
