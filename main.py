# Task Manager - Custom Queue


# Insert task into queue
def insert(queue, task):
    queue.append(task)

# Remove first task from queue
def extract(queue):
    if not is_empty(queue):
        return queue.pop(0)
    return None

# Peek at first task without removing
def peek(queue):
    if not is_empty(queue):
        return queue[0]
    return None

# Check if queue is empty
def is_empty(queue):
    return len(queue) == 0

# Complete the task with highest priority (lowest value)
def complete_next_task(queue):
    if is_empty(queue):
        print("No tasks to complete.")
        return

    highest = min(queue, key=lambda t: t["priority"])
    print(f"\n✅ Completed Task: {highest['title']} (Duration: {highest['duration']} mins, Priority: {highest['priority']})")
    queue.remove(highest)

# Binary Search for a task by title (after sorting by title)
def search_for_task(queue, title):
    sorted_tasks = sorted(queue, key=lambda t: t["title"])
    low = 0
    high = len(sorted_tasks) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_tasks[mid]["title"] == title:
            print(f"\n🔍 Task Found: {sorted_tasks[mid]}")
            return
        elif sorted_tasks[mid]["title"] < title:
            low = mid + 1
        else:
            high = mid - 1

    print("\n❌ Task not found.")

# Sort tasks by duration (ascending)
def sort_tasks(queue):
    return sorted(queue, key=lambda t: t["duration"])


# Main Program

task_queue = []
num_tasks = int(input("Enter number of tasks: "))

for i in range(num_tasks):
    print(f"\n--- Task {i + 1} ---")
    title = input("Title: ")
    duration = int(input("Duration (in minutes): "))
    priority = int(input("Priority (lower = higher priority): "))

    task = {
        "title": title,
        "duration": duration,
        "priority": priority
    }

    insert(task_queue, task)


print("\n📋 All Tasks:")
for task in task_queue:
    print(task)


complete_next_task(task_queue)


search_title = input("\nEnter task title to search for: ")
search_for_task(task_queue, search_title)


print("\n🕒 Tasks sorted by duration:")
sorted_tasks = sort_tasks(task_queue)
for task in sorted_tasks:
    print(task)
