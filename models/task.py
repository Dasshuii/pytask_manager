import datetime

TODAY = datetime.datetime.now().strftime('%x')

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = 'todo'
        self.createdAt = TODAY
        self.updatedAt = TODAY
    
    def task_info(self):
        return f'{self.id} -- {self.description} -- {self.status}'
