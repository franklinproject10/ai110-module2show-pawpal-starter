"""Demo script for PawPal+ — showcases the Scheduler's sorting, conflict, and filter logic."""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # Build the owner and pets
    owner = Owner("Frank")
    biscuit = Pet("Biscuit", "dog", "Golden Retriever")
    rex = Pet("Rex", "dog", "Labrador")

    # Add tasks DELIBERATELY out of order, with a time conflict at 08:00
    biscuit.add_task(Task("Evening walk", "18:00", 20, "medium", "daily"))
    biscuit.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    rex.add_task(Task("Meds", "07:30", 5, "high", "daily"))
    rex.add_task(Task("Vet appointment", "08:00", 60, "high", "none"))  # conflicts with Morning walk

    owner.add_pet(biscuit)
    owner.add_pet(rex)
    scheduler = Scheduler(owner)

    # Grab all tasks once
    all_tasks = scheduler.get_todays_schedule()

    # 1. Raw schedule (add-order — intentionally messy)
    print("=== Raw Schedule (add order) ===")
    for t in all_tasks:
        print(f"   {t.time} — {t.description} [{t.priority}]")

    # 2. Sorted schedule (chronological)
    print("\n=== Sorted Schedule (by time) ===")
    for t in scheduler.sort_by_time(all_tasks):
        print(f"   {t.time} — {t.description} [{t.priority}]")

    # 3. Conflict detection
    print("\n=== Conflict Check ===")
    print(f"   {scheduler.check_conflicts(all_tasks)}")

    # 4. Filtered view — high priority only
    print("\n=== High-Priority Tasks Only ===")
    for t in scheduler.filter_tasks(all_tasks, priority="high"):
        print(f"   {t.time} — {t.description} [{t.priority}]")


if __name__ == "__main__":
    main()
