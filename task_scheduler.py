"""
Problem: Task Scheduler

Design a task scheduler that can:
1. Add tasks with priorities
2. Execute the highest priority task
3. List all tasks
4. Mark tasks as complete
5. Remove completed tasks

The scheduler should use a priority queue (heap) for efficient task management.

Example:
scheduler.add_task("Study DSA", 3)
scheduler.add_task("Write Code", 2)
scheduler.add_task("System Design", 1)
scheduler.get_next_task()  # Returns "Study DSA" (highest priority)
scheduler.list_tasks()     # Shows remaining tasks in priority order
"""

import heapq
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    name: str
    priority: int
    created_at: datetime
    completed: bool = False
    
    def __lt__(self, other):
        # Higher priority (lower number) comes first
        # If priorities are equal, older task comes first
        if self.priority == other.priority:
            return self.created_at < other.created_at
        return self.priority < other.priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []  # heap of tasks
        self.task_map = {}  # name -> Task mapping for O(1) lookups
    
    def add_task(self, name: str, priority: int) -> bool:
        """Add a new task with given priority (1 highest, 5 lowest)."""
        if name in self.task_map:
            return False  # Task already exists
        
        if not (1 <= priority <= 5):
            return False  # Invalid priority
        
        task = Task(name, priority, datetime.now())
        heapq.heappush(self.tasks, task)
        self.task_map[name] = task
        return True
    
    def get_next_task(self) -> Optional[str]:
        """Get the name of highest priority task that's not completed."""
        # Remove completed tasks from the top
        while self.tasks and self.tasks[0].completed:
            heapq.heappop(self.tasks)
        
        return self.tasks[0].name if self.tasks else None
    
    def complete_task(self, name: str) -> bool:
        """Mark a task as completed."""
        if name not in self.task_map:
            return False
        
        self.task_map[name].completed = True
        return True
    
    def remove_completed(self) -> int:
        """Remove all completed tasks and return count of removed tasks."""
        initial_size = len(self.tasks)
        
        # Rebuild heap without completed tasks
        self.tasks = [task for task in self.tasks if not task.completed]
        heapq.heapify(self.tasks)
        
        # Update task map
        self.task_map = {task.name: task for task in self.tasks}
        
        return initial_size - len(self.tasks)
    
    def list_tasks(self) -> List[tuple[str, int, bool]]:
        """Return list of (name, priority, completed) sorted by priority."""
        return sorted(
            [(task.name, task.priority, task.completed) for task in self.tasks],
            key=lambda x: (x[1], x[0])  # Sort by priority, then name
        )

def test_task_scheduler():
    scheduler = TaskScheduler()
    
    print("Test 1: Adding Tasks")
    print("Adding Study DSA (Priority 1):", scheduler.add_task("Study DSA", 1))
    print("Adding Write Code (Priority 2):", scheduler.add_task("Write Code", 2))
    print("Adding System Design (Priority 1):", scheduler.add_task("System Design", 1))
    print("Adding Invalid Priority Task:", scheduler.add_task("Invalid", 6))
    print("Adding Duplicate Task:", scheduler.add_task("Study DSA", 3))
    print("-" * 50)
    
    print("\nTest 2: Listing Tasks")
    tasks = scheduler.list_tasks()
    for name, priority, completed in tasks:
        print(f"Task: {name}, Priority: {priority}, Completed: {completed}")
    print("-" * 50)
    
    print("\nTest 3: Getting Next Task")
    print("Next task:", scheduler.get_next_task())  # Should be either Study DSA or System Design
    print("-" * 50)
    
    print("\nTest 4: Completing Tasks")
    print("Completing Study DSA:", scheduler.complete_task("Study DSA"))
    print("Completing Invalid Task:", scheduler.complete_task("Invalid Task"))
    print("Next task after completion:", scheduler.get_next_task())
    print("-" * 50)
    
    print("\nTest 5: Removing Completed Tasks")
    removed = scheduler.remove_completed()
    print(f"Removed {removed} completed tasks")
    tasks = scheduler.list_tasks()
    print("\nRemaining tasks:")
    for name, priority, completed in tasks:
        print(f"Task: {name}, Priority: {priority}, Completed: {completed}")

if __name__ == "__main__":
    test_task_scheduler()
