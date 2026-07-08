# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Sample Output

```
=== Today's Schedule for Frank ===

Biscuit (Golden Retriever):
   08:00 - Morning walk (30 min) [high] (todo)
   09:00 - Feeding (10 min) [high] (todo)

Rex (Labrador):
   07:30 - Meds (5 min) [high] (todo)
   18:00 - Evening walk (20 min) [medium] (todo)

Total tasks across all pets: 4
```

## Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
============================= test session starts =============================
collected 6 items

tests/test_pawpal.py::test_task_completion PASSED                        [ 16%]
tests/test_pawpal.py::test_add_task_increases_count PASSED               [ 33%]
tests/test_pawpal.py::test_sort_by_time_orders_chronologically PASSED    [ 50%]
tests/test_pawpal.py::test_filter_tasks_by_priority PASSED               [ 66%]
tests/test_pawpal.py::test_check_conflicts_flags_and_clears PASSED       [ 83%]
tests/test_pawpal.py::test_recurring_task_spawns_next_occurrence PASSED  [100%]
============================== 6 passed in 0.05s ==============================
```

**Confidence Level:** 4/5 stars - All six tests pass, covering every scheduling algorithm plus core behaviors and key edge cases (empty lists, none-frequency tasks, conflict-free schedules). One star held back because time-overlap conflicts and multi-pet integration flows are not yet tested.

## Smarter Scheduling

| Feature | Method(s) | Notes |
| --- | --- | --- |
| Task sorting | `Scheduler.sort_by_time()` | Chronological order using lexicographic HH:MM comparison |
| Filtering | `Scheduler.filter_tasks()` | By priority and/or incomplete status |
| Conflict handling | `Scheduler.check_conflicts()` | Flags tasks sharing an exact start time |
| Recurring tasks | `Scheduler.handle_recurring_tasks()` | Spawns next occurrence via timedelta (daily/weekly) |

## Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Run `python main.py` to see the CLI demo with sorting, conflict detection, and filtering.
2. Open `pawpal_system.py` to review the four core classes: Task, Pet, Owner, Scheduler.
3. Run `pytest` to verify all six automated tests pass.
4. Launch the Streamlit UI with `streamlit run app.py` to interact with the app.
5. Add a pet and tasks, then view the generated daily schedule with conflict warnings.

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or link to a demo video here -->
