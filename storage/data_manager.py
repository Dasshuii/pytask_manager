import json
import os

DATA_PATH = './storage/tasks.json'

def load_tasks():
    if not os.path.exists(DATA_PATH):
        return []
    
    try:
        with open(DATA_PATH, 'r') as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, IOError) as error:
        print(f'Error loading tasks: {error}')
        return []

def save_tasks(tasks):
    try:
        with open(DATA_PATH, 'w') as file:
            json.dump(tasks, file)
    except IOError as error:
        print(f'Error saving tasks: {error}')