**b. Design changes**

- After AI review of the skeleton, I added `priority` to the `Task` class — it
  was missing from my initial brainstorm but the README mentioned it three times
  as a core constraint. I also upgraded `remove_task()` and `remove_pet()` to use
  a defensive guard (`if task in self.tasks`) rather than calling `.remove()`
  directly, after deciding that a pet owner clicking "remove" on a missing task
  should never crash the app.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- My scheduler considers three constraints: time (HH:MM ordering via
  `sort_by_time`), priority level (high/medium/low via `filter_tasks`), and
  scheduling conflicts (exact same-time collisions via `check_conflicts`). I also
  implemented frequency-based recurrence (`handle_recurring_tasks`) using
  `timedelta` to compute the next occurrence date.
- I prioritized time-ordering first because a schedule that isn't chronological
  is useless to a pet owner regardless of priority levels. Conflict detection came
  second because double-booking is the most common real-world mistake. Priority
  filtering came third as a "focus view" for busy days.

**b. Tradeoffs**

- My conflict detection (`check_conflicts`) only flags tasks that share an _exact_
  start time (e.g., two tasks both at 08:00). It does NOT detect overlapping
  durations — a 30-minute walk starting at 08:00 and a task at 08:15 actually
  clash, but my scheduler won't warn about it because their start times differ.
- This tradeoff is reasonable for a lightweight pet-care app: it catches the most
  common and obvious scheduling mistake (double-booking the same slot) with simple,
  fast logic, while avoiding the added complexity of parsing durations and computing
  time ranges. If the app grew, I would upgrade to interval-overlap detection.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI tools at every phase: brainstorming class attributes from user actions
  (Phase 1), generating class skeletons from my UML (Phase 1), implementing method
  bodies one class at a time (Phase 2), writing the Streamlit UI wiring (Phase 3),
  and generating the initial test suite (Phase 5).
- The most effective prompts were scoped and specific — asking for one class at a
  time rather than the whole file at once. Prompts that included my existing design
  decisions ("use @dataclass for Task and Pet, plain classes for Owner and
  Scheduler") produced cleaner output than open-ended requests.

**b. Judgment and verification**

- When the AI generated the Scheduler skeleton, it typed `-> bool` as the return
  type for `check_conflicts`. I changed it to `-> str` because I had decided the
  method should return a human-readable warning message rather than a bare
  True/False — a string is directly displayable in the Streamlit UI without
  extra logic. I verified this by checking that `st.warning(conflict_msg)` worked
  cleanly in `app.py` without any additional formatting step.
- I also rejected the AI's first attempt to write all four classes in one shot
  (it accidentally overwrote `app.py`). After that I scoped every AI request to
  one class or method at a time and always ran `python -m pytest` after each
  change to verify nothing broke.

---

## 4. Testing and Verification

**a. What you tested**

- I tested six behaviors: task completion (mark_complete flips the flag), task
  addition (add_task grows the list), sorting correctness (scrambled tasks come
  back chronological, empty list returns empty), filtering by priority (only
  matching tasks returned, verified with `all()`), conflict detection (flags a
  clash AND stays quiet on a clean schedule), and recurrence logic (daily task
  spawns a fresh incomplete copy; "none"-frequency task is correctly skipped).
- These tests matter because they cover both the happy path and discriminating
  edge cases — proving the logic actually decides correctly, not just that it
  returns the right answer by luck on the most obvious input.

**b. Confidence**

- 4/5. All six tests pass and cover every algorithm plus key edge cases (empty
  lists, one-off tasks, conflict-free schedules). The one gap is time-overlap
  detection — a 30-minute task at 08:00 overlapping a task at 08:15 is not
  flagged, and there are no multi-pet integration tests verifying the Scheduler
  collects correctly across three or more pets. Those would be my next tests.

---

## 5. Reflection

**a. What went well**

- The "CLI-first" workflow was the most valuable habit of the project. By building
  and verifying every method in the terminal before touching the Streamlit UI, I
  always knew whether a bug was in the logic layer or the display layer — never
  both at once. The six automated tests made Phase 3 UI wiring stress-free because
  I already trusted the backend completely.

**b. What you would improve**

- I would add a `due_date` field to `Task` from the start, so recurring tasks
  track real calendar dates rather than just spawning undated copies. I would also
  build the `filter_tasks` and `sort_by_time` calls into `get_todays_schedule`
  directly, so the Scheduler always returns a sorted, filtered list by default
  instead of requiring callers to chain the methods manually.

**c. Key takeaway**

- The most important thing I learned is that user actions reveal class
  responsibilities — you discover what objects you need by asking "what does the
  user need to do?" first, not by inventing classes and hoping they fit.
