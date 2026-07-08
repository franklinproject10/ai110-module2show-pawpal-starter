"""Automated tests for PawPal+ core behaviors and scheduling algorithms."""

from pawpal_system import Task, Pet, Owner, Scheduler


# ---------- Phase 2: core behaviors ----------

def test_task_completion():
    """Calling mark_complete() flips is_complete from False to True."""
    task = Task("Morning walk", "08:00", 30, "high", "daily")
    assert task.is_complete is False
    task.mark_complete()
    assert task.is_complete is True


def test_add_task_increases_count():
    """Adding a task to a pet increases that pet's task count by one."""
    pet = Pet("Biscuit", "dog", "Golden Retriever")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Feeding", "09:00", 10, "high", "daily"))
    assert len(pet.get_tasks()) == 1


# ---------- Phase 4: scheduling algorithms ----------

def test_sort_by_time_orders_chronologically():
    """sort_by_time returns tasks earliest-first, and handles an empty list."""
    scheduler = Scheduler(Owner("Frank"))
    tasks = [
        Task("Evening walk", "18:00", 20, "medium", "daily"),
        Task("Meds", "07:30", 5, "high", "daily"),
        Task("Morning walk", "08:00", 30, "high", "daily"),
    ]
    ordered = scheduler.sort_by_time(tasks)
    assert [t.time for t in ordered] == ["07:30", "08:00", "18:00"]
    # edge case: empty list should return empty, not crash
    assert scheduler.sort_by_time([]) == []


def test_filter_tasks_by_priority():
    """filter_tasks(priority='high') returns only — and all — high-priority tasks."""
    scheduler = Scheduler(Owner("Frank"))
    tasks = [
        Task("Morning walk", "08:00", 30, "high", "daily"),
        Task("Feeding", "09:00", 10, "high", "daily"),
        Task("Play", "17:00", 15, "low", "daily"),
    ]
    result = scheduler.filter_tasks(tasks, priority="high")
    assert len(result) == 2
    assert all(t.priority == "high" for t in result)


def test_check_conflicts_flags_and_clears():
    """check_conflicts warns on a shared time and reports clean otherwise."""
    scheduler = Scheduler(Owner("Frank"))
    clashing = [
        Task("Walk", "08:00", 30, "high", "daily"),
        Task("Vet", "08:00", 20, "high", "none"),
    ]
    assert "08:00" in scheduler.check_conflicts(clashing)
    clean = [
        Task("Walk", "08:00", 30, "high", "daily"),
        Task("Feed", "09:00", 10, "high", "daily"),
    ]
    assert scheduler.check_conflicts(clean) == "No conflicts detected."


def test_recurring_task_spawns_next_occurrence():
    """A completed daily task recurs; a completed 'none' task does not."""
    scheduler = Scheduler(Owner("Frank"))
    daily = Task("Morning walk", "08:00", 30, "high", "daily")
    oneoff = Task("Vet visit", "14:00", 60, "high", "none")
    daily.mark_complete()
    oneoff.mark_complete()
    next_ones = scheduler.handle_recurring_tasks([daily, oneoff])
    assert len(next_ones) == 1              # only the daily task recurs
    assert next_ones[0].is_complete is False  # fresh copy, reset for next time