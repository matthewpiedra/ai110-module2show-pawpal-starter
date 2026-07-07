# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Actions needed (for example):
  - adding a pet
  - scheduling a walk
  - display today's tasks
  - adding a task
  - editing a task by adding a duration and priority
- Briefly describe your initial UML design:
  - Task class: represents a task with attributes for name (string), duration (int), and priority (string) (High, Medium, Low). Methods including creating and editing tasks.
  - Owner class: represents a user with attributes for name (string), a list of tasks (Task objects), and a list of pets (Pet objects). Methods include adding and removing tasks and adding and removing pets and adding name.
  - Pet class: represents a pet with attributes for name (string), species (string) (Dog, Cat, Other). Methods include adding name and species.
  - Scheduler pure method class: responsible for generating a daily schedule based on the tasks of the owner and pet. Methods include sorting tasks by priority and duration, filtering tasks based on time constraints, and handling conflicts between overlapping tasks, and explaining the reasoning behind the schedule.
- What classes did you include, and what responsibilities did you assign to each?
  - I included a Task class to represent individual tasks, an Owner class to manage the user's information and their associated tasks, a Pet class to represent the pet's information, and a Scheduler class to handle the logic of generating a daily schedule based on the tasks and constraints provided by the owner and pet.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
