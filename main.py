from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner(name="Alex")

dog = Pet(name="Rex", species="Dog")
cat = Pet(name="Whiskers", species="Cat")

dog.add_task(Task(name="Walk", duration=30, priority="High", completion_status=False, time="08:00"))
dog.add_task(Task(name="Feed", duration=10, priority="Medium", completion_status=False, time="09:00"))
cat.add_task(Task(name="Litter Box", duration=15, priority="High", completion_status=False, time="08:15"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)

print("Today's Schedule")
for task in schedule:
    print(f"- {task.time} {task.name} ({task.priority}, {task.duration} min)")