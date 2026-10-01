import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the TTS speak function
tts_js = """
    // TTS Voice Setup
    function speakText(text) {
      if ('speechSynthesis' in window) {
        // Cancel any ongoing speech
        window.speechSynthesis.cancel();
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ko-KR';
        utterance.rate = 1.1;  // Slightly faster/upbeat
        utterance.pitch = 1.4; // Higher pitch for a brighter/cuter female voice tone
        
        // Try to force a female voice if multiple Korean voices exist
        const voices = window.speechSynthesis.getVoices();
        const koVoices = voices.filter(v => v.lang.includes('ko'));
        if (koVoices.length > 0) {
          utterance.voice = koVoices[0]; // Usually the default OS female voice (Heami/Yuna)
        }
        
        window.speechSynthesis.speak(utterance);
      }
    }
"""

# Insert TTS function at the top of the JS block
html = html.replace('const items = ', tts_js + '\n    const items = ')
html = html.replace('let items = ', tts_js + '\n    let items = ')

# Hook the speakText into showReward
html = html.replace("t.innerText = '🎉 완벽합니다! 최고예요!';", "t.innerText = '🎉 완벽합니다! 최고예요!';\n        speakText('화이팅!');")
html = html.replace("t.innerText = '🐕 괜찮아요! 토닥토닥';", "t.innerText = '🐕 괜찮아요! 토닥토닥';\n        speakText('힘내세요!');")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Voice TTS added successfully.")
