# Task Scheduler Implementation

## Problem Description
Implement a task scheduler that efficiently manages tasks with different priorities. The scheduler should support basic task management operations while maintaining optimal time complexity.

## Features
1. Add tasks with priorities (1-5, where 1 is highest)
2. Get the next highest priority task
3. Mark tasks as complete
4. Remove completed tasks
5. List all tasks in priority order

## Implementation Details

### Data Structures Used
1. **Min Heap**: For efficient priority-based task retrieval
2. **Hash Map**: For O(1) task lookups by name

### Classes
1. **Task**:
   - Properties: name, priority, created_at, completed
   - Custom comparison for heap operations

2. **TaskScheduler**:
   - Uses heap for priority management
   - Uses hash map for quick lookups
   - Maintains task order based on priority and creation time

### Time Complexity
- Add Task: O(log n)
- Get Next Task: O(1) amortized
- Complete Task: O(1)
- Remove Completed: O(n log n)
- List Tasks: O(n log n)

### Space Complexity
- O(n) where n is the number of tasks

## Edge Cases Handled
- Duplicate task names
- Invalid priorities
- Empty scheduler
- All tasks completed
- Multiple tasks with same priority

## Usage Example
```python
scheduler = TaskScheduler()
scheduler.add_task("Study DSA", 1)
scheduler.add_task("Write Code", 2)
next_task = scheduler.get_next_task()  # Returns "Study DSA"
scheduler.complete_task("Study DSA")
scheduler.remove_completed()  # Removes completed tasks
```

## Applications
- Task Management Systems
- Process Schedulers
- Event Priority Systems
- Job Queue Management
