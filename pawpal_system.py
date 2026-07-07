from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: str

    def edit(self, name=None, duration=None, priority=None):
        pass


@dataclass
class Pet:
    name: str
    species: str

    def add_name(self, name):
        pass

    def add_species(self, species):
        pass


@dataclass
class Owner:
    name: str
    tasks: list[Task] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_name(self, name):
        pass

    def add_task(self, task):
        pass

    def edit_task(self, task, name=None, duration=None, priority=None):
        pass
    
    def remove_task(self, task):
        pass

    def add_pet(self, pet):
        pass


class Scheduler:
    def generate_schedule(self, owner):
        pass

    def sort_by_priority_and_duration(self, tasks):
        pass

    def filter_by_time_constraints(self, tasks):
        pass

    def handle_conflicts(self, tasks):
        pass

    def explain_schedule(self, schedule):
        pass