import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Global Toggle Buttons for TTS and Cloze Mode
buttons_html = """
      <button class="btn-control" id="btn-tts" onclick="toggleAutoTTS()" style="background:#1e293b; color:#cbd5e1;">🔊 자동 낭독 (OFF)</button>
      <button class="btn-control" id="btn-cloze" onclick="toggleClozeMode()" style="background:#1e293b; color:#cbd5e1;">🕳️ 빈칸 뚫기 (OFF)</button>
"""
if "btn-tts" not in html:
    html = html.replace('<button class="btn-control" id="btn-starmode"', buttons_html + '\n      <button class="btn-control" id="btn-starmode"')


# 2. Add Hint Box and Hint Button
hint_ui = """
            <div id="hint-box" style="display:none; background:#1e293b; color:#fbbf24; padding:10px; border-radius:6px; margin-bottom:10px; font-weight:800; font-size:1.05rem; text-align:center; border: 1px dashed #f59e0b; box-shadow: 0 4px 6px rgba(0,0,0,0.3);"></div>
            <div style="text-align:right; margin-bottom:4px; padding-right:5px;">
              <button onclick="showChosungHint()" style="background:#f59e0b; color:white; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; margin-right:5px; box-shadow:0 2px 4px rgba(0,0,0,0.2);">💡 초성 힌트</button>
"""
# Replace the existing div for the mic button to inject the hint box and button
html = re.sub(r'<div style="text-align:right; margin-bottom:4px; padding-right:5px;">', hint_ui, html)


# 3. Add Javascript Logic for all 3 features
logic_js = """
    // --- MEMORY UPGRADES LOGIC ---
    let isAutoTTS = false;
    let isClozeMode = false;
    
    function toggleAutoTTS() {
      isAutoTTS = !isAutoTTS;
      const btn = document.getElementById('btn-tts');
      if (isAutoTTS) {
        btn.style.background = '#8b5cf6';
        btn.style.color = '#fff';
        btn.innerText = '🔊 자동 낭독 (ON)';
        if (items[currentIndex]) speakTextClean(items[currentIndex].q);
      } else {
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '🔊 자동 낭독 (OFF)';
        window.speechSynthesis.cancel();
      }
    }
    
    function speakTextClean(text) {
      if (!text) return;
      // Remove symbols and markdown that shouldn't be read aloud
      let clean = text.replace(/\\*\\*/g, '').replace(/\\$/g, '').replace(/\\\\Rightarrow/g, '다음으로').replace(/➔/g, '다음으로');
      speakText(clean);
    }
    
    function toggleClozeMode() {
      isClozeMode = !isClozeMode;
      const btn = document.getElementById('btn-cloze');
      if (isClozeMode) {
        btn.style.background = '#ec4899';
        btn.style.color = '#fff';
        btn.innerText = '🕳️ 빈칸 뚫기 (ON)';
      } else {
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '🕳️ 빈칸 뚫기 (OFF)';
      }
      renderCard(currentIndex);
    }
    
    function generateCloze(text) {
      let words = text.split(' ');
      let candidates = [];
      for(let i=0; i<words.length; i++) {
        let w = words[i].replace(/[.,!?()]/g, '');
        // Pick words longer than 1 character that aren't typical sentence endings
        if(w.length >= 2 && !w.endsWith('임') && !w.endsWith('함')) {
          candidates.push(i);
        }
      }
      candidates.sort(() => 0.5 - Math.random());
      let selected = candidates.slice(0, Math.min(3, Math.max(1, Math.floor(candidates.length / 3))));
      
      let result = [];
      for(let i=0; i<words.length; i++) {
        if(selected.includes(i)) {
          result.push('[        ?        ]');
        } else {
          result.push(words[i]);
        }
      }
      return result.join(' ');
    }
    
    function getChosung(str) {
      const cho = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"];
      let result = "";
      for(let i=0; i<str.length; i++) {
        let code = str.charCodeAt(i) - 44032;
        if(code > -1 && code < 11172) {
          result += cho[Math.floor(code/588)];
        } else {
          result += str.charAt(i);
        }
      }
      return result;
    }
    
    function showChosungHint() {
      if(!items[currentIndex]) return;
      const hintBox = document.getElementById('hint-box');
      hintBox.style.display = 'block';
      hintBox.innerText = getChosung(items[currentIndex].ans);
    }
    // -----------------------------
"""

if "function toggleAutoTTS()" not in html:
    html = html.replace('function renderCard(index) {', logic_js + '\n    function renderCard(index) {')


# 4. Integrate into renderCard()
# Hide hint box, trigger TTS, and apply cloze logic on card render
render_card_updates = """
        document.getElementById('hint-box').style.display = 'none';
        
        if (isAutoTTS) {
          setTimeout(() => speakTextClean(item.q), 300); // slight delay so it feels natural
        }
        
        if (isClozeMode) {
          elInput.value = generateCloze(item.ans);
        } else {
          elInput.value = '';
        }
"""
html = html.replace("elInput.value = '';", render_card_updates)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("All 3 Memory Upgrades Applied.")
