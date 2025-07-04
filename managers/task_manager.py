from storage.data_manager import load_tasks, save_tasks
from models.task import Task
import datetime

tasks = [Task.from_dict(task) for task in load_tasks()]

def _save():
    save_tasks([task.to_dict() for task in tasks])

def _find_task(id):
    return next((task for task in tasks if task['id'] == id))

def _get_next_id():
    return max((task['id'] for task in tasks), default = - 1) + 1

def add(description):
    task = Task(id = _get_next_id(), description = description)
    tasks.append(task)
    _save()

def update(id, description):
    task = _find_task(id)
    if task:
        task['description'] = description
        task['updatedAt'] = datetime.datetime.now().strftime('%x')
        _save()

def mark_status(id, status):
    task = _find_task()
    if task:
        task['status'] = status
        task['updatedAt'] = datetime.datetime.now().strftime('%x')
        _save()

def mark_in_progress(id):
    mark_status(id, 'in-progress')

def mark_done(id):
    mark_status(id, 'done')

def task_list(status = None):
    print('--- TASK LIST ---')
    for task in tasks:
        if not status or task['status'] == status:
            print(task)