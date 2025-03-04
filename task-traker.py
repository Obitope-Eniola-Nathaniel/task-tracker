import sys
import json
import datetime


# using now() to get current time
current_time = str(datetime.datetime.now())
status = ['todo', 'in-progress', 'done']


tasks = []

try:
    # First Read the Json File
    with open('task.json') as f:
        tasks = json.load(f)
except json.JSONDecodeError:
    tasks = []  
except FileNotFoundError:
    # Create One if it doesnt Exit
    with open('task.json', 'w') as f:
        json.dump(tasks, f)

try:
    # Get the first Argv
    action = sys.argv[1]
except IndexError:
    print('Missing Argv')


# Print Error if the arg is less than 2
if len(sys.argv) < 2:
    print("MisUsage: add 'Task Title")
    sys.exit(1)
# Print the List of Tasks
elif action == 'list' and len(sys.argv) == 2:
    for task in tasks:
        print(f'{task['id']}: {task["description"]} - status: {task["status"]}')
# Display Status of the Todo
elif action == 'list' and len(sys.argv) == 3:
    description = sys.argv[2]
    for task in tasks:
        if task['status'] == description:
            print(f'{task['id']}: {task["description"]} - status: {task["status"]}')
# Add Task 
elif action == 'add' and len(sys.argv) == 3:
    try:
        description = sys.argv[2]
    except IndexError:
        print('Missing Arg! Try Again')
        sys.exit(1)
    # task Id
    task_id = len(tasks) + 1
    # Increase the task Id if it already Exit
    for task in tasks:
        if task['id'] == task_id:
            task_id = task_id + 1

    task = {
        'id': task_id,
        'description':  description,
        'status': status[0],
        'createdAt': current_time,
        'updatedAt': ''
    }
    tasks.append(task)
    # Write the tasks into JSON
    with open('task.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task added successfully (ID: {task_id})")
elif action == 'update' and len(sys.argv) == 4:

    # Get the Description and the task Id
    description = sys.argv[3]
    task_no = int(sys.argv[2])

    for i, task in enumerate(tasks):
        # print(task)
        if task_no == task['id']:
            task["description"] = description
            task["updatedAt"] = current_time
            print(f'{i+1}-{task['description']} is Updated')
       
    with open('task.json', 'w') as f:
        json.dump(tasks, f)
elif action == 'mark-in-progress' and len(sys.argv) == 2:
    # Get the Description and the task Id
    task_no = int(sys.argv[2])

    for i, task in enumerate(tasks):
    # print(task)
        if task_no == task['id']:
            task["status"] = status[1]
            print(f'{i+1}-{task['description']} is {task["status"]}')
    with open('task.json', 'w') as f:
        json.dump(tasks, f)
elif action == 'mark-done' and len(sys.argv) == 2:
    # Get the Description and the task Id
    task_no = int(sys.argv[2])

    for i, task in enumerate(tasks):
    # print(task)
        if task_no == task['id']:
            task["status"] = status[2]
            print(f'{i+1}-{task['description']} is {task["status"]}')
    with open('task.json', 'w') as f:
        json.dump(tasks, f)
elif action == 'delete':
    task_no = int(sys.argv[2])

    # Check the task id with the task in the array!
    for i, task in enumerate(tasks):
        # print(task)
        if task_no == task['id']:
            del tasks[i]
            print(f'{i}-{task['description']} is deleted')
      
            
    with open('task.json', 'w') as f:
        json.dump(tasks, f)

else:
    print("not running- error: Check the User Instruction")
