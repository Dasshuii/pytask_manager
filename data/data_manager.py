import json

DATA_PATH = './data/tasks.json'

def load_tasks():
    with open(DATA_PATH, 'r') as file:
        content = file.read().strip()
        return json.loads(content) if content else []

def save_tasks(tasks):
    with open(DATA_PATH, 'w') as file:
        json.dump(tasks, file)