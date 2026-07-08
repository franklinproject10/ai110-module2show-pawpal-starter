"""Automated tests for PawPal+ core behaviors."""

from pawpal_system import Task, Pet


def test_task_completion():
    """Calling mark_complete() flips is_complete from False to True."""
    # Arrange: a fresh task starts incomplete
    task = Task("Morning walk", "08:00", 30, "high", "daily")
    assert task.is_complete is False  # before

    # Act: complete it
    task.mark_complete()

    # Assert: it is now complete
    assert task.is_complete is True   # after


def test_add_task_increases_count():
    """Adding a task to a pet increases that pet's task count by one."""
    # Arrange: a fresh pet has no tasks
    pet = Pet("Biscuit", "dog", "Golden Retriever")
    assert len(pet.get_tasks()) == 0  # before

    # Act: add one task
    task = Task("Feeding", "09:00", 10, "high", "daily")
    pet.add_task(task)

    # Assert: the pet now has exactly one task
    assert len(pet.get_tasks()) == 1  # after
