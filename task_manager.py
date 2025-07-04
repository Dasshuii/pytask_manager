from data.data_manager import load_tasks, save_tasks
from models.task import Task
import datetime

tasks = load_tasks()
TODAY = datetime.datetime.now().strftime('%x')

def add(description):
    id = len(tasks) - 1 if len(tasks) > 0 else 0
    task = Task(id, description)
    tasks.append(task.__dict__)
    save_tasks(tasks)

def update(id, description):
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            task['updatedAt'] = TODAY
            break
    save_tasks(tasks)
    
def mark_in_progress(id):
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'in-progress'
            break
    save_tasks(tasks)

def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'done'
            break
    save_tasks(tasks)

def task_list(status = None):
    print('--- TASK LIST ---')
    match status:
        case 'todo':
            for task in tasks:
                if task['status'] == 'todo':
                    print(f'{task['id']} -- {task['description']} -- {task['status']}')
        case 'in-progress':
            for task in tasks:
                if task['status'] == 'in-progress':
                    print(f'{task['id']} -- {task['description']} -- {task['status']}')
        case 'done':
            for task in tasks:
                if task['status'] == 'done':
                   print(f'{task['id']} -- {task['description']} -- {task['status']}')
        case _:
            for task in tasks:
                print(f'{task['id']} -- {task['description']} -- {task['status']}')