// ============================================================================
// TYPEFIGHTER — 30-DAY DAILY CONSISTENCY CALENDAR ENGINE
// ============================================================================

class CalendarTracker {
  constructor() {
    this.saveManager = window.saveManager;
  }

  getTodayString() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  recordDailyPractice() {
    const today = this.getTodayString();
    const save = window.saveManager.data;

    if (!save.practiceDaysHistory.includes(today)) {
      save.practiceDaysHistory.push(today);

      // Calculate streak
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      const yesterdayStr = `${yesterday.getFullYear()}-${String(yesterday.getMonth() + 1).padStart(2, '0')}-${String(yesterday.getDate()).padStart(2, '0')}`;

      if (save.lastPracticeDate === yesterdayStr) {
        save.dailyStreakCount += 1;
      } else if (save.lastPracticeDate !== today) {
        save.dailyStreakCount = 1;
      }
      save.lastPracticeDate = today;
      window.saveManager.save();
    }
  }

  getStreakInfo() {
    const save = window.saveManager.data;
    return {
      streakDays: save.dailyStreakCount || 0,
      totalDaysPracticed: save.practiceDaysHistory.length,
      history: save.practiceDaysHistory
    };
  }

  generateCalendarGrid(daysCount = 30) {
    const save = window.saveManager.data;
    const historySet = new Set(save.practiceDaysHistory);
    const grid = [];
    const today = new Date();

    for (let i = daysCount - 1; i >= 0; i--) {
      const d = new Date();
      d.setDate(today.getDate() - i);
      const dateStr = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
      grid.push({
        dayNumber: daysCount - i,
        date: dateStr,
        isCompleted: historySet.has(dateStr),
        isToday: i === 0
      });
    }
    return grid;
  }
}

window.calendarTracker = new CalendarTracker();
