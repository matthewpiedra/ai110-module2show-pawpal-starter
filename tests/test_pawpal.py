from pawpal_system import Task, Pet


def test_task_edit_marks_completion_status():
    task = Task(name="Walk", duration=30, priority="High", completion_status=False, time="08:00")

    task.edit(completion_status=True)

    assert task.completion_status is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Rex", species="Dog")
    task = Task(name="Walk", duration=30, priority="High", completion_status=False, time="08:00")

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1