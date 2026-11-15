
    // Day Buttons Generation
    const dayPillsBox = document.getElementById('day-pills');
    const weekdaysKr = ['월', '화', '수', '목', '금', '토', '일'];
    let dayPillHtml = '<button class="tab-pill active" onclick="filterByDay(\'all\', this)">전체 Day (1~18)</button>';
    for (let d = 1; d <= 18; d++) {
      const dDate = new Date(2026, 9, 5 + (d - 1)); // Month is 0-indexed: 9 = Oct
      const mm = String(dDate.getMonth() + 1).padStart(2, '0');
      const dd = String(dDate.getDate()).padStart(2, '0');
      const w = weekdaysKr[dDate.getDay() === 0 ? 6 : dDate.getDay() - 1];
      dayPillHtml += `<button class="tab-pill" onclick="filterByDay(${d}, this)">Day ${String(d).padStart(2, '0')} (${mm}/${dd})</button>`;
    }
    dayPillsBox.innerHTML = dayPillHtml;

    // Local Storage for Checkboxes
    const STORAGE_KEY = 'kice_phase1_wordbook_checks';
    let checksData = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');

    function loadSavedChecks() {
      const chks = document.querySelectorAll('.chk-box');
      chks.forEach(chk => {
        const idx = chk.getAttribute('data-idx');
        const round = chk.getAttribute('data-round');
        if (checksData[idx] && checksData[idx]['r' + round]) {
          chk.checked = true;
        }
      });
      updateDashboard();
    }

    function handleCheckChange(chk) {
      const idx = chk.getAttribute('data-idx');
      const round = chk.getAttribute('data-round');
      if (!checksData[idx]) checksData[idx] = {};
      checksData[idx]['r' + round] = chk.checked;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(checksData));
      updateDashboard();
    }

    function updateDashboard() {
      let r1Count = 0, r2Count = 0, r3Count = 0;
      const total = 203;
      for (let i = 0; i < total; i++) {
        if (checksData[i]) {
          if (checksData[i].r1) r1Count++;
          if (checksData[i].r2) r2Count++;
          if (checksData[i].r3) r3Count++;
        }
      }
      const pct1 = Math.round((r1Count / total) * 100);
      const pct2 = Math.round((r2Count / total) * 100);
      const pct3 = Math.round((r3Count / total) * 100);

      document.getElementById('stat-r1').innerText = `${r1Count} / ${total} (${pct1}%)`;
      document.getElementById('stat-r2').innerText = `${r2Count} / ${total} (${pct2}%)`;
      document.getElementById('stat-r3').innerText = `${r3Count} / ${total} (${pct3}%)`;

      document.getElementById('fill-r1').style.width = pct1 + '%';
      document.getElementById('fill-r2').style.width = pct2 + '%';
      document.getElementById('fill-r3').style.width = pct3 + '%';
    }

    // Blind Mode
    let isBlind = false;
    function toggleBlindMode() {
      isBlind = !isBlind;
      const btn = document.getElementById('btn-toggle-blind');
      if (isBlind) {
        document.body.classList.add('blind-mode');
        btn.classList.add('active');
        btn.innerText = '👁️ 키워드 모두 보이기 (정답 확인)';
      } else {
        document.body.classList.remove('blind-mode');
        btn.classList.remove('active');
        btn.innerText = '👁️ 키워드 가리기 (블라인드 인출 테스트)';
      }
    }

    function toggleKwReveal(span) {
      if (isBlind) {
        span.classList.toggle('revealed');
      }
    }

    // Filtering Logic
    let curDay = 'all';
    let curCat = 'all';

    function filterByDay(day, btn) {
      curDay = day;
      document.querySelectorAll('#day-pills .tab-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      applyCombinedFilter();
    }

    function filterByCat(cat, btn) {
      curCat = cat;
      document.querySelectorAll('#cat-pills .tab-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      applyCombinedFilter();
    }

    function applyCombinedFilter() {
      const cards = document.querySelectorAll('.word-card');
      cards.forEach(card => {
        const cDay = card.getAttribute('data-day');
        const cCat = card.getAttribute('data-cat');
        const matchDay = (curDay === 'all' || String(cDay) === String(curDay));
        const matchCat = (curCat === 'all' || String(cCat) === String(curCat));
        if (matchDay && matchCat) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function filterUnchecked() {
      const cards = document.querySelectorAll('.word-card');
      cards.forEach(card => {
        const idx = card.getAttribute('data-idx');
        const isChecked = checksData[idx] && (checksData[idx].r1 || checksData[idx].r2 || checksData[idx].r3);
        if (!isChecked) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function resetAllFilters() {
      curDay = 'all';
      curCat = 'all';
      document.querySelectorAll('.tab-pill').forEach(b => b.classList.remove('active'));
      document.querySelector('#day-pills .tab-pill').classList.add('active');
      document.querySelector('#cat-pills .tab-pill').classList.add('active');
      applyCombinedFilter();
    }

    // Initialize
    loadSavedChecks();
  