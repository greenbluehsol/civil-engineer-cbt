(function () {
  const STORAGE_KEY_ANSWERS = "civil_cbt_user_answers_v1";
  const STORAGE_KEY_BOOKMARKS = "civil_cbt_bookmarks_v1";

  let examsData = window.EXAMS_DATA || {};
  let sessionsList = [];
  let currentSessionId = "2022_2";
  let currentMode = "study"; // "study" | "quiz"
  let currentSubject = "all"; // "all" | "응용역학" | "철근콘크리트 및 강구조" | "wrong" | "bookmarked"
  let searchQuery = "";
  let searchAllSessions = false;
  let showOrigImage = true;

  // User state: { "2022_2_1": 4, ... }
  let userAnswers = loadJson(STORAGE_KEY_ANSWERS, {});
  // Bookmarks: { "2022_2_1": true, ... }
  let userBookmarks = loadJson(STORAGE_KEY_BOOKMARKS, {});
  // Whether quiz has been submitted/graded for a session: { "2022_2": true }
  let sessionGraded = {};

  function loadJson(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function saveJson(key, val) {
    try {
      localStorage.setItem(key, JSON.stringify(val));
    } catch (e) {}
  }

  function qKey(sid, qnum) {
    return `${sid}_${qnum}`;
  }

  function formatMarkdownAndMath(text) {
    if (!text) return "<p>해설 데이터를 불러오는 중입니다.</p>";
    // Escape basic HTML entities except math
    let safe = text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    // Bold **text**
    safe = safe.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

    // Convert lines into paragraphs / lists
    const lines = safe.split(/\r?\n/);
    let html = "";
    let inList = false;

    for (let rawLine of lines) {
      const line = rawLine.trim();
      if (!line) {
        if (inList) {
          html += "</ul>";
          inList = false;
        }
        continue;
      }
      if (/^[-•*]\s+/.test(line)) {
        if (!inList) {
          html += "<ul>";
          inList = true;
        }
        html += `<li>${line.replace(/^[-•*]\s+/, "")}</li>`;
      } else {
        if (inList) {
          html += "</ul>";
          inList = false;
        }
        html += `<p>${line}</p>`;
      }
    }
    if (inList) html += "</ul>";
    return html;
  }

  function triggerKaTeX(container) {
    if (typeof renderMathInElement === "function") {
      try {
        renderMathInElement(container, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "\\[", right: "\\]", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\(", right: "\\)", display: false }
          ],
          throwOnError: false
        });
      } catch (e) {
        console.warn("KaTeX render error:", e);
      }
    }
  }

  function init() {
    sessionsList = Object.values(examsData)
      .map((d) => d.session)
      .sort((a, b) => (a.date < b.date ? 1 : -1));

    if (sessionsList.length > 0 && !examsData[currentSessionId]) {
      currentSessionId = sessionsList[0].id;
    }

    bindEvents();
    renderSidebar();
    updatePdfLinks();
    renderAll();
  }

  function bindEvents() {
    document.getElementById("sidebarToggle").addEventListener("click", () => {
      document.getElementById("sidebar").classList.toggle("open");
    });

    document.getElementById("modeStudyBtn").addEventListener("click", () => {
      setMode("study");
    });
    document.getElementById("modeQuizBtn").addEventListener("click", () => {
      setMode("quiz");
    });

    document.querySelectorAll(".subj-tab").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".subj-tab").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        currentSubject = btn.dataset.subject;
        renderQuestionsAndOmr();
      });
    });

    const searchInput = document.getElementById("searchInput");
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.trim();
      renderQuestionsAndOmr();
    });

    const searchAllBtn = document.getElementById("searchAllSessionsBtn");
    searchAllBtn.addEventListener("click", () => {
      searchAllSessions = !searchAllSessions;
      searchAllBtn.classList.toggle("active", searchAllSessions);
      renderQuestionsAndOmr();
    });

    document.getElementById("toggleOrigImage").addEventListener("change", (e) => {
      showOrigImage = e.target.checked;
      renderQuestionsAndOmr();
    });

    document.getElementById("resetSessionQuizBtn").addEventListener("click", () => {
      if (!confirm("현재 회차의 풀이 기록을 초기화하시겠습니까?")) return;
      const qs = examsData[currentSessionId]?.questions || [];
      qs.forEach((q) => {
        delete userAnswers[qKey(currentSessionId, q.qnum)];
      });
      delete sessionGraded[currentSessionId];
      saveJson(STORAGE_KEY_ANSWERS, userAnswers);
      renderAll();
    });

    document.getElementById("gradeAllBtn").addEventListener("click", () => {
      const curQs = examsData[currentSessionId]?.questions || [];
      const solvedInCur = curQs.filter((q) => userAnswers[qKey(currentSessionId, q.qnum)]).length;
      
      if (!sessionGraded[currentSessionId]) {
        if (solvedInCur < curQs.length) {
          if (!confirm(`총 ${curQs.length}문항 중 ${solvedInCur}문항만 답안을 선택했습니다.\n답안을 제출하고 채점하시겠습니까?`)) {
            return;
          }
        }
        sessionGraded[currentSessionId] = true;
      } else {
        // Toggle view
        sessionGraded[currentSessionId] = true;
      }
      renderAll();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    document.getElementById("filterBookmarkBtn").addEventListener("click", () => {
      document.querySelectorAll(".subj-tab").forEach((b) => b.classList.remove("active"));
      document.getElementById("tabBookmarkOnly").classList.add("active");
      currentSubject = "bookmarked";
      renderQuestionsAndOmr();
    });

    // Modal close
    document.getElementById("modalBackdrop").addEventListener("click", closeModal);
    document.getElementById("modalCloseBtn").addEventListener("click", closeModal);
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        closeModal();
        closeMobileOmr();
      }
    });

    // Mobile Bottom Bar Events
    const mBtnSidebar = document.getElementById("mBtnSidebar");
    if (mBtnSidebar) {
      mBtnSidebar.addEventListener("click", () => {
        document.getElementById("sidebar").classList.toggle("open");
      });
    }

    const mBtnMode = document.getElementById("mBtnMode");
    if (mBtnMode) {
      mBtnMode.addEventListener("click", () => {
        setMode(currentMode === "study" ? "quiz" : "study");
      });
    }

    const mBtnOmr = document.getElementById("mBtnOmr");
    if (mBtnOmr) {
      mBtnOmr.addEventListener("click", () => {
        openMobileOmr();
      });
    }

    const mBtnTop = document.getElementById("mBtnTop");
    if (mBtnTop) {
      mBtnTop.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }

    const closeMobileOmrBtn = document.getElementById("closeMobileOmrBtn");
    if (closeMobileOmrBtn) {
      closeMobileOmrBtn.addEventListener("click", closeMobileOmr);
    }
    const mobileOmrBackdrop = document.getElementById("mobileOmrBackdrop");
    if (mobileOmrBackdrop) {
      mobileOmrBackdrop.addEventListener("click", closeMobileOmr);
    }
  }

  function openMobileOmr() {
    renderMobileOmrPanel();
    document.getElementById("mobileOmrSheet").classList.add("open");
  }

  function closeMobileOmr() {
    document.getElementById("mobileOmrSheet").classList.remove("open");
  }

  function setMode(mode) {
    currentMode = mode;
    document.getElementById("modeStudyBtn").classList.toggle("active", mode === "study");
    document.getElementById("modeQuizBtn").classList.toggle("active", mode === "quiz");
    document.getElementById("scoreBanner").classList.toggle("hidden", mode !== "quiz");
    const mModeText = document.getElementById("mBtnModeText");
    if (mModeText) {
      mModeText.textContent = mode === "study" ? "CBT 모드" : "해설 모드";
    }
    renderQuestionsAndOmr();
  }

  function renderSidebar() {
    const container = document.getElementById("sessionList");
    container.innerHTML = "";

    // Group by year
    const byYear = {};
    sessionsList.forEach((s) => {
      if (!byYear[s.year]) byYear[s.year] = [];
      byYear[s.year].push(s);
    });

    Object.keys(byYear)
      .sort((a, b) => b - a)
      .forEach((year) => {
        const yLabel = document.createElement("div");
        yLabel.className = "year-group-label";
        yLabel.textContent = `${year}년도 기출문제`;
        container.appendChild(yLabel);

        byYear[year].forEach((s) => {
          const btn = document.createElement("button");
          btn.className = "session-item" + (s.id === currentSessionId ? " active" : "");
          btn.innerHTML = `
            <span>${s.year}년 ${s.round}</span>
            <span class="session-date">${s.date}</span>
          `;
          btn.addEventListener("click", () => {
            currentSessionId = s.id;
            searchAllSessions = false;
            document.getElementById("searchAllSessionsBtn").classList.remove("active");
            document.getElementById("sidebar").classList.remove("open");
            renderSidebar();
            updatePdfLinks();
            renderAll();
            window.scrollTo({ top: 0, behavior: "smooth" });
          });
          container.appendChild(btn);
        });
      });
  }

  function updatePdfLinks() {
    const s = examsData[currentSessionId]?.session;
    if (!s) return;
    document.getElementById("studentPdfLink").href = `pdfs/${s.id}_student.pdf`;
    document.getElementById("teacherPdfLink").href = `pdfs/${s.id}_teacher.pdf`;
  }

  function getFilteredQuestions() {
    let pool = [];
    if (searchAllSessions || (currentSubject === "bookmarked" && searchAllSessions)) {
      sessionsList.forEach((s) => {
        const qs = examsData[s.id]?.questions || [];
        pool = pool.concat(qs);
      });
    } else {
      pool = examsData[currentSessionId]?.questions || [];
    }

    return pool.filter((q) => {
      const key = qKey(q.session_id, q.qnum);
      if (currentSubject === "응용역학" && q.subject !== "응용역학") return false;
      if (currentSubject === "철근콘크리트 및 강구조" && q.subject !== "철근콘크리트 및 강구조") return false;
      if (currentSubject === "bookmarked" && !userBookmarks[key]) return false;
      if (currentSubject === "wrong") {
        const uAns = userAnswers[key];
        if (!uAns || uAns === q.answer) return false;
      }

      if (searchQuery) {
        const qLower = searchQuery.toLowerCase();
        const numMatch = `${q.qnum}` === qLower || `${q.qnum}번` === qLower;
        const stemMatch = (q.stem || "").toLowerCase().includes(qLower);
        const topicMatch = (q.topic || "").toLowerCase().includes(qLower);
        const expMatch = (q.explanation || "").toLowerCase().includes(qLower);
        const choiceMatch = (q.choices || []).some((c) => (c || "").toLowerCase().includes(qLower));
        if (!numMatch && !stemMatch && !topicMatch && !expMatch && !choiceMatch) {
          return false;
        }
      }
      return true;
    });
  }

  function updateGlobalStats() {
    let totalCount = 0;
    let solvedCount = 0;
    let correctCount = 0;
    let bookmarkedCount = 0;

    sessionsList.forEach((s) => {
      const qs = examsData[s.id]?.questions || [];
      totalCount += qs.length;
      qs.forEach((q) => {
        const key = qKey(s.id, q.qnum);
        if (userAnswers[key]) {
          solvedCount++;
          if (userAnswers[key] === q.answer) correctCount++;
        }
        if (userBookmarks[key]) bookmarkedCount++;
      });
    });

    document.getElementById("statTotal").textContent = `${totalCount}문항`;
    document.getElementById("statSolved").textContent = `${solvedCount} / ${totalCount}`;
    const acc = solvedCount > 0 ? Math.round((correctCount / solvedCount) * 100) : 0;
    document.getElementById("statAccuracy").textContent = `${acc}%`;
    document.getElementById("statBookmarked").textContent = `${bookmarkedCount}`;

    // Also update current session quiz banner
    const curQs = examsData[currentSessionId]?.questions || [];
    const isGraded = currentMode === "study" || !!sessionGraded[currentSessionId];
    const solvedInCur = curQs.filter((q) => userAnswers[qKey(currentSessionId, q.qnum)]).length;

    let c1 = 0, c4 = 0;
    curQs.forEach((q) => {
      const uAns = userAnswers[qKey(currentSessionId, q.qnum)];
      if (uAns === q.answer) {
        if (q.qnum <= 20) c1++;
        else c4++;
      }
    });
    const s1Score = c1 * 5;
    const s4Score = c4 * 5;
    const avgScore = (s1Score + s4Score) / 2;

    const gradeBtn = document.getElementById("gradeAllBtn");

    if (isGraded) {
      document.getElementById("scoreSubj1").textContent = `${c1} / 20 (${s1Score}점)`;
      document.getElementById("scoreSubj4").textContent = `${c4} / 20 (${s4Score}점)`;
      let statusText = "합격 🎉";
      if (s1Score < 40 || s4Score < 40) statusText = "과락 탈락 ⚠️ (40점 미만)";
      else if (avgScore < 60) statusText = "불합격 (평균 60점 미만)";
      document.getElementById("scoreTotalAvg").textContent = `${avgScore.toFixed(1)}점 (${statusText})`;
      if (gradeBtn) {
        gradeBtn.textContent = "✅ 채점 완료 (정답·해설 공개 중)";
        gradeBtn.classList.remove("pulse-btn");
      }
    } else {
      document.getElementById("scoreSubj1").textContent = `답안 마킹: ${curQs.slice(0, 20).filter(q => userAnswers[qKey(currentSessionId, q.qnum)]).length} / 20`;
      document.getElementById("scoreSubj4").textContent = `답안 마킹: ${curQs.slice(20, 40).filter(q => userAnswers[qKey(currentSessionId, q.qnum)]).length} / 20`;
      document.getElementById("scoreTotalAvg").textContent = `풀이 진행 중 (${solvedInCur}/${curQs.length} 완료)`;
      if (gradeBtn) {
        gradeBtn.textContent = `📝 답안 제출 및 전체 채점하기 (${solvedInCur}/${curQs.length})`;
        gradeBtn.classList.add("pulse-btn");
      }
    }
  }

  function renderAll() {
    const s = examsData[currentSessionId]?.session;
    if (s) {
      document.getElementById("currentSessionTitle").textContent = searchAllSessions
        ? "전회차 통합 검색 결과 (2018~2022년)"
        : `토목기사 ${s.title}`;
    }
    renderQuestionsAndOmr();
    updateGlobalStats();
  }

  function renderQuestionsAndOmr() {
    const container = document.getElementById("questionsContainer");
    const filtered = getFilteredQuestions();
    document.getElementById("currentQuestionCount").textContent = `${filtered.length}문항`;

    const s = examsData[currentSessionId]?.session;
    if (s) {
      document.getElementById("currentSessionTitle").textContent = searchAllSessions
        ? `전회차 통합 검색 (${filtered.length}문항)`
        : `토목기사 ${s.title}`;
    }

    container.innerHTML = "";

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="question-card" style="text-align:center; padding: 48px 20px; color:#64748b;">
          <h3 style="margin-bottom:8px; color:#334155;">조건에 맞는 문항이 없습니다.</h3>
          <p>검색어나 과목 필터를 변경해 보세요.</p>
        </div>
      `;
    } else {
      const circleSymbols = ["①", "②", "③", "④"];

      filtered.forEach((q) => {
        const key = qKey(q.session_id, q.qnum);
        const uAns = userAnswers[key];
        const isBookmarked = !!userBookmarks[key];
        const isStudy = currentMode === "study";
        const isGraded = isStudy || !!sessionGraded[q.session_id];
        const isRevealed = isGraded;
        const sessObj = examsData[q.session_id]?.session;

        const card = document.createElement("article");
        let cardClass = "question-card";
        if (isGraded && uAns) {
          cardClass += uAns === q.answer ? " solved-correct" : " solved-wrong";
        }
        card.className = cardClass;
        card.id = `qcard-${q.session_id}-${q.qnum}`;

        const subjBadgeClass = q.qnum <= 20 ? "subj-1" : "subj-4";
        const subjLabel = q.qnum <= 20 ? "1과목 · 응용역학" : "4과목 · 철근콘크리트 및 강구조";

        const choicesHtml = [0, 1, 2, 3]
          .map((idx) => {
            const cNum = idx + 1;
            const cText = q.choices && q.choices[idx] ? q.choices[idx] : `선지 ${cNum} (상단 원본 도면/수식 참조)`;
            let btnClass = "choice-btn";
            if (isGraded) {
              if (cNum === q.answer) {
                btnClass += " is-answer";
              } else if (uAns === cNum && uAns !== q.answer) {
                btnClass += " user-wrong";
              }
            } else {
              // Quiz mode before submission: only show user selected state
              if (uAns === cNum) {
                btnClass += " user-selected";
              }
            }
            return `
              <button class="${btnClass}" data-cnum="${cNum}">
                <span class="choice-num">${cNum}</span>
                <span class="choice-text">${cText}</span>
              </button>
            `;
          })
          .join("");

        card.innerHTML = `
          <div class="q-header">
            <div class="q-badges">
              <span class="q-num-badge">${q.qnum}번</span>
              <span class="q-subj-badge ${subjBadgeClass}">${subjLabel}</span>
              ${q.topic ? `<span class="q-topic-badge"># ${q.topic}</span>` : ""}
              <span class="q-session-tag">${sessObj ? sessObj.title : q.session_id}</span>
            </div>
            <div class="q-actions">
              <button class="bookmark-btn ${isBookmarked ? "active" : ""}" data-action="bookmark">
                ${isBookmarked ? "★ 북마크됨" : "☆ 북마크"}
              </button>
            </div>
          </div>

          <div class="q-stem">${q.qnum}. ${q.stem}</div>

          ${
            showOrigImage
              ? `
            <div class="q-orig-image-wrap">
              <img src="${q.image}" alt="${q.qnum}번 원본 문제 이미지" loading="eager" data-zoom-src="${q.image}" onerror="this.onerror=null; this.src='${q.image}';" />
              <div class="img-zoom-hint">🔍 이미지를 클릭하면 원본 크기로 확대됩니다 (도면·수식 선지 포함)</div>
            </div>
          `
              : ""
          }

          <div class="q-choices">
            ${choicesHtml}
          </div>

          <div class="q-explanation-wrap">
            ${
              !isGraded
                ? `<div style="font-size:13px; color:#64748b; padding: 4px 0;">🔒 답안을 모두 푼 후 상단 <strong>[📝 답안 제출 및 전체 채점하기]</strong> 버튼을 누르면 정답과 해설이 공개됩니다.</div>`
                : ""
            }
            <div class="q-explanation ${isRevealed ? "" : "hidden"}">
              <div class="exp-answer-line">
                <span>정답 : ${circleSymbols[q.answer - 1]} (${q.answer}번)</span>
                ${
                  uAns
                    ? `<span style="color:${uAns === q.answer ? "#16a34a" : "#dc2626"}; font-size:13.5px;">
                        [내 선택: ${circleSymbols[uAns - 1]} → ${uAns === q.answer ? "정답입니다! 🎯" : "오답입니다 ❌"}]
                      </span>`
                    : ""
                }
              </div>
              <div class="exp-body">
                ${formatMarkdownAndMath(q.explanation)}
              </div>
            </div>
          </div>
        `;

        // Event listeners on card
        card.querySelector('[data-action="bookmark"]').addEventListener("click", () => {
          if (userBookmarks[key]) delete userBookmarks[key];
          else userBookmarks[key] = true;
          saveJson(STORAGE_KEY_BOOKMARKS, userBookmarks);
          renderQuestionsAndOmr();
          updateGlobalStats();
        });

        const revealBtn = card.querySelector('[data-action="reveal"]');
        if (revealBtn) {
          revealBtn.addEventListener("click", () => {
            revealedQuizExplanations[key] = true;
            renderQuestionsAndOmr();
          });
        }

        card.querySelectorAll(".choice-btn").forEach((cBtn) => {
          cBtn.addEventListener("click", () => {
            const selected = parseInt(cBtn.dataset.cnum, 10);
            if (userAnswers[key] === selected) {
              // Click again to unselect if not graded
              if (!isGraded) delete userAnswers[key];
            } else {
              userAnswers[key] = selected;
            }
            saveJson(STORAGE_KEY_ANSWERS, userAnswers);
            renderQuestionsAndOmr();
            updateGlobalStats();
          });
        });

        const imgEl = card.querySelector("img[data-zoom-src]");
        if (imgEl) {
          imgEl.addEventListener("click", () => {
            openModal(imgEl.dataset.zoomSrc);
          });
        }

        container.appendChild(card);
      });
    }

    renderOmrPanel();
    triggerKaTeX(container);
  }

  function renderOmrPanel() {
    const grid1 = document.getElementById("omrGrid1");
    const grid4 = document.getElementById("omrGrid4");
    grid1.innerHTML = "";
    grid4.innerHTML = "";

    const curQs = examsData[currentSessionId]?.questions || [];
    const isGraded = currentMode === "study" || !!sessionGraded[currentSessionId];

    curQs.forEach((q) => {
      const key = qKey(currentSessionId, q.qnum);
      const uAns = userAnswers[key];
      const isBm = !!userBookmarks[key];

      const btn = document.createElement("button");
      let cls = "omr-cell";
      if (uAns) {
        if (isGraded) {
          cls += uAns === q.answer ? " correct" : " wrong";
        } else {
          cls += " selected";
        }
      }
      if (isBm) cls += " bookmarked";
      btn.className = cls;
      btn.textContent = q.qnum;
      btn.title = uAns ? `${q.qnum}번 (선택: ${uAns}번)` : `${q.qnum}번 문항으로 이동`;

      btn.addEventListener("click", () => {
        const target = document.getElementById(`qcard-${currentSessionId}-${q.qnum}`);
        if (target) {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          // Reset filter to 'all' if hidden
          currentSubject = "all";
          document.querySelectorAll(".subj-tab").forEach((b) => {
            b.classList.toggle("active", b.dataset.subject === "all");
          });
          renderQuestionsAndOmr();
          setTimeout(() => {
            const el = document.getElementById(`qcard-${currentSessionId}-${q.qnum}`);
            if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
          }, 50);
        }
      });

      if (q.qnum <= 20) grid1.appendChild(btn);
      else grid4.appendChild(btn);
    });

    renderMobileOmrPanel();
  }

  function renderMobileOmrPanel() {
    const grid1 = document.getElementById("mobileOmrGrid1");
    const grid4 = document.getElementById("mobileOmrGrid4");
    if (!grid1 || !grid4) return;
    grid1.innerHTML = "";
    grid4.innerHTML = "";

    const curQs = examsData[currentSessionId]?.questions || [];
    const isGraded = currentMode === "study" || !!sessionGraded[currentSessionId];

    curQs.forEach((q) => {
      const key = qKey(currentSessionId, q.qnum);
      const uAns = userAnswers[key];
      const isBm = !!userBookmarks[key];

      const btn = document.createElement("button");
      let cls = "omr-cell";
      if (uAns) {
        if (isGraded) {
          cls += uAns === q.answer ? " correct" : " wrong";
        } else {
          cls += " selected";
        }
      }
      if (isBm) cls += " bookmarked";
      btn.className = cls;
      btn.textContent = q.qnum;

      btn.addEventListener("click", () => {
        closeMobileOmr();
        const target = document.getElementById(`qcard-${currentSessionId}-${q.qnum}`);
        if (target) {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          currentSubject = "all";
          document.querySelectorAll(".subj-tab").forEach((b) => {
            b.classList.toggle("active", b.dataset.subject === "all");
          });
          renderQuestionsAndOmr();
          setTimeout(() => {
            const el = document.getElementById(`qcard-${currentSessionId}-${q.qnum}`);
            if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
          }, 50);
        }
      });

      if (q.qnum <= 20) grid1.appendChild(btn);
      else grid4.appendChild(btn);
    });
  }

  function openModal(src) {
    const modal = document.getElementById("imageModal");
    const img = document.getElementById("modalImg");
    img.src = src;
    modal.classList.remove("hidden");
  }

  function closeModal() {
    document.getElementById("imageModal").classList.add("hidden");
  }

  window.addEventListener("DOMContentLoaded", init);
})();
