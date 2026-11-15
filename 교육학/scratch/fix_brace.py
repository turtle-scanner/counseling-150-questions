# -*- coding: utf-8 -*-
TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("""      // 6. ⚔️ 일기토
      if (btnDuel) btnDuel.disabled = (allEnemies.length === 0);
    }
    }""", """      // 6. ⚔️ 일기토
      if (btnDuel) btnDuel.disabled = (allEnemies.length === 0);
    }""")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed extra brace.")
