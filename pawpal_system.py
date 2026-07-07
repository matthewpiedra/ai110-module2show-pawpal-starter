from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    completion_status: bool

    def edit(self, name=None, duration=None, priority=None, completion_status=None):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_name(self, name):
        pass

    def add_species(self, species):
        pass
    
    def add_task(self, task):
        pass
    
    def get_task(self, name):
        pass

    def edit_task(self, task, name=None, duration=None, priority=None, completion_status=None):
        pass
    
    def remove_task(self, name):
        pass
    
    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_name(self, name):
        pass

    def add_pet(self, pet):
        pass
    
    def get_pets_tasks(self, name):
        pass


class Scheduler:
    def generate_schedule(self, owner):
        pass

    def sort_by_priority_and_duration(self, owner):
        pass

    def filter_by_time_constraints(self, owner):
        pass

    def handle_conflicts(self, owner):
        pass

    def explain_schedule(self, owner):
        pass