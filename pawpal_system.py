from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    completion_status: bool
    time: str

    def edit(self, name=None, duration=None, priority=None, time=None, completion_status=None):
        """Update only the fields that were passed a non-None value."""
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority
        if time is not None:
            self.time = time
        if completion_status is not None:
            self.completion_status = completion_status


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def edit_name(self, name):
        """Rename this pet."""
        self.name = name

    def edit_species(self, species):
        """Change this pet's species."""
        self.species = species

    def add_task(self, task):
        """Append a task to this pet's task list."""
        self.tasks.append(task)

    def get_task(self, name):
        """Return the task with the given name, or None if not found."""
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def edit_task(self, name, new_name=None, duration=None, priority=None, completion_status=None):
        """Find a task by name and apply the given edits to it."""
        task = self.get_task(name)
        if task is not None:
            task.edit(name=new_name, duration=duration, priority=priority, completion_status=completion_status)

    def remove_task(self, name):
        """Remove the task with the given name, if it exists."""
        task = self.get_task(name)
        if task is not None:
            self.tasks.remove(task)

    def get_tasks(self):
        """Return this pet's list of tasks."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def edit_name(self, name):
        """Rename this owner."""
        self.name = name

    def add_pet(self, pet):
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def get_pet(self, name):
        """Return the pet with the given name, or None if not found."""
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def remove_pet(self, name):
        """Remove the pet with the given name, if it exists."""
        pet = self.get_pet(name)
        if pet is not None:
            self.pets.remove(pet)

    def get_pets_tasks(self, name):
        """Return the task list for the pet with the given name, or an empty list if not found."""
        pet = self.get_pet(name)
        if pet is not None:
            return pet.get_tasks()
        return []


class Scheduler:
    PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}

    def generate_schedule(self, owner):
        """Filter, deconflict, and sort an owner's tasks into a final daily schedule."""
        tasks = self.filter_by_time_constraints(owner)
        tasks = self.handle_conflicts_list(tasks)
        tasks = self.sort_by_priority_and_duration_list(tasks)
        return tasks

    def _all_tasks(self, owner):
        """Flatten and return every task across all of an owner's pets."""
        tasks = []
        for pet in owner.pets:
            tasks.extend(pet.get_tasks())
        return tasks

    def sort_by_priority_and_duration(self, owner):
        """Return an owner's tasks sorted by priority, then duration."""
        return self.sort_by_priority_and_duration_list(self._all_tasks(owner))

    def sort_by_priority_and_duration_list(self, tasks):
        """Sort a list of tasks by priority (High to Low), then by duration ascending."""
        return sorted(tasks, key=lambda task: (self.PRIORITY_ORDER.get(task.priority, len(self.PRIORITY_ORDER)), task.duration))

    def filter_by_time_constraints(self, owner):
        """Return an owner's tasks excluding any already marked complete."""
        return [task for task in self._all_tasks(owner) if not task.completion_status]

    def handle_conflicts(self, owner):
        """Return an owner's tasks with time-overlapping conflicts resolved."""
        return self.handle_conflicts_list(self._all_tasks(owner))

    def _time_window(self, task):
        """Return a task's (start, end) datetimes derived from its time and duration."""
        start = datetime.strptime(task.time, "%H:%M")
        end = start + timedelta(minutes=task.duration)
        return start, end

    def _overlaps(self, task, other):
        """Return True if two tasks' time windows intersect."""
        start, end = self._time_window(task)
        other_start, other_end = self._time_window(other)
        return start < other_end and other_start < end

    def _conflicts_with_kept(self, task, kept_tasks):
        """Return True if a task overlaps with any task already kept."""
        for kept_task in kept_tasks:
            if self._overlaps(task, kept_task):
                return True
        return False

    def _by_priority_then_start_time(self, task):
        """Return the sort key used to resolve conflicts: priority rank, then start time."""
        priority_rank = self.PRIORITY_ORDER.get(task.priority, len(self.PRIORITY_ORDER))
        start_time, _ = self._time_window(task)
        return priority_rank, start_time

    def handle_conflicts_list(self, tasks):
        """Greedily keep the highest-priority, earliest non-overlapping tasks from a list."""
        tasks_by_priority = sorted(tasks, key=self._by_priority_then_start_time)

        kept_tasks = []
        for task in tasks_by_priority:
            if not self._conflicts_with_kept(task, kept_tasks):
                kept_tasks.append(task)

        return kept_tasks
