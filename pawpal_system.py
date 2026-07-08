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
        self.is_complete = True

    def edit_time(self, new_time: str) -> None:
        self.time = new_time

    def update_frequency(self, new_frequency: str) -> None:
        self.frequency = new_frequency


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)


class Owner:
    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.pets = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_pets(self) -> List[Pet]:
        return self.pets

    def remove_pet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_todays_schedule(self) -> List[Task]:
        all_tasks = []
        for pet in self.owner.get_all_pets():
            for task in pet.get_tasks():
                all_tasks.append(task)
        return all_tasks

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        pass

    def check_conflicts(self, tasks: List[Task]) -> bool:
        pass

    def filter_tasks(self, tasks: List[Task], priority: Optional[str] = None) -> List[Task]:
        pass

    def handle_recurring_tasks(self, tasks: List[Task]) -> List[Task]:
        pass
