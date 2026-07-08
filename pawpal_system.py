from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    is_complete: bool = False

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.is_complete = True

    def edit_time(self, new_time: str) -> None:
        """Change the task's scheduled time."""
        self.time = new_time

    def update_frequency(self, new_frequency: str) -> None:
        """Change how often the task recurs."""
        self.frequency = new_frequency


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet if present."""
        if task in self.tasks:
            self.tasks.remove(task)


class Owner:
    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.pets = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list."""
        self.pets.append(pet)

    def get_all_pets(self) -> List[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner if present."""
        if pet in self.pets:
            self.pets.remove(pet)


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_todays_schedule(self) -> List[Task]:
        """Collect and return every task across all the owner's pets."""
        all_tasks = []
        for pet in self.owner.get_all_pets():
            for task in pet.get_tasks():
                all_tasks.append(task)
        return all_tasks

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return tasks ordered chronologically by their HH:MM time."""
        return sorted(tasks, key=lambda task: task.time)

    def check_conflicts(self, tasks: List[Task]) -> bool:
        pass

    def filter_tasks(
        self,
        tasks: List[Task],
        priority: Optional[str] = None,
        only_incomplete: bool = False,
    ) -> List[Task]:
        """Return tasks narrowed by optional priority and/or incomplete status."""
        result = tasks
        if priority is not None:
            result = [task for task in result if task.priority == priority]
        if only_incomplete:
            result = [task for task in result if not task.is_complete]
        return result

    def handle_recurring_tasks(self, tasks: List[Task]) -> List[Task]:
        pass
