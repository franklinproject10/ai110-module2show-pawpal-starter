"""Demo script for PawPal+ — builds a sample household and prints today's schedule."""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # 1. Create the owner
    owner = Owner("Frank")

    # 2. Create two pets
    biscuit = Pet("Biscuit", "dog", "Golden Retriever")
    rex = Pet("Rex", "dog", "Labrador")

    # 3. Add tasks with different times to each pet
    biscuit.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    biscuit.add_task(Task("Feeding", "09:00", 10, "high", "daily"))
    rex.add_task(Task("Meds", "07:30", 5, "high", "daily"))
    rex.add_task(Task("Evening walk", "18:00", 20, "medium", "daily"))

    # 4. Register the pets with the owner
    owner.add_pet(biscuit)
    owner.add_pet(rex)

    # 5. Build the scheduler (the "brain")
    scheduler = Scheduler(owner)

    # 6. Print today's schedule, grouped by pet
    print(f"=== Today's Schedule for {owner.name} ===\n")
    for pet in owner.get_all_pets():
        print(f"🐾 {pet.name} ({pet.breed}):")
        for task in pet.get_tasks():
            status = "done" if task.is_complete else "todo"
            print(f"   {task.time} — {task.description} ({task.duration} min) [{task.priority}] ({status})")
        print()  # blank line between pets

    # 7. Show the flat total from the Scheduler (proves get_todays_schedule works)
    total = scheduler.get_todays_schedule()
    print(f"Total tasks across all pets: {len(total)}")


if __name__ == "__main__":
    main()
