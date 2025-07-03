DATA_PATH = './data/tasks.json'
TODAY = datetime.datetime.now().strftime('%x')

tasks = [
    {
        'id' : 0,
        'description' : 'feed the dog',
        'status' : 'todo',
        'createdAt' : TODAY,
        'updatedAt' : TODAY
    },
    {
        'id' : 1,
        'description' : 'clean the house',
        'status' : 'todo',
        'createdAt' : TODAY,
        'updatedAt' : TODAY
    }
]