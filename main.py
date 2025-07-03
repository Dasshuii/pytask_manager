import json
import datetime



TASK_STATUS_TODO = 'todo'
TASK_STATUS_INPROGRESS = 'in-progress'
TASK_STATUS_DONE = 'done'

def add(task):
    tasks.append(task)
    with open(DATA_PATH, 'w') as file:
        json.dump(tasks, file)

def update(id, description):
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            break
    
def mark_in_progress(id):
    for task in tasks:
        if task['id'] == id:
            task['status'] == 'in-progress'
            break

def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['status'] == 'done'
            break

def task_list(status = ''):
    print('--- TO-DO\'s ---')
    match status:
        case TASK_STATUS_TODO:
            for task in tasks:
                if task['status'] == 'todo':
                    print(f'{task['description']} --- todo')
        case TASK_STATUS_INPROGRESS:
            for task in tasks:
                if task['status'] == 'in-progress':
                    print(f'{task['description']} --- in-progress')
        case TASK_STATUS_DONE:
            for task in tasks:
                if task['status'] == 'done':
                    print(f'{task['description']} --- done')
        case _:
            for task in tasks:
                print(f'{task['description']} --- {task['status']}')

def main():
    task_list()
    add({
        'id' : 2, 
        'description' : 'cook the lunch', 
        'status' : 'in-progress',
        'createdAt' : TODAY,
        'updatedAt' : TODAY,
        })
    update(1, 'clean the bath')
    task_list('in-progress')

    
if __name__ == '__main__':
    main()