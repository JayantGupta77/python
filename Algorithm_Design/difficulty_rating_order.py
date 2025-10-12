def sort_by_difficulty_dict(tasks):
    
    sorted_tasks = sorted(tasks, key=lambda task: task["difficulty_level"], reverse=True)
    
    return sorted_tasks

tasks_data = [
    {"name": "Setup Database", "difficulty_level": 7, "category": "Backend"},
    {"name": "Login Form", "difficulty_level": 3, "category": "Frontend"},
    {"name": "Implement AI Model", "difficulty_level": 10, "category": "Data Science"},
    {"name": "Fix Typo", "difficulty_level": 1, "category": "Documentation"},
    {"name": "API Endpoint", "difficulty_level": 6, "category": "Backend"},
]

sorted_by_difficulty = sort_by_difficulty_dict(tasks_data)

print("Tasks Sorted by Difficulty (Most Difficult First):")
for task in sorted_by_difficulty:
    print(f"  Level {task['difficulty_level']}: {task['name']}")