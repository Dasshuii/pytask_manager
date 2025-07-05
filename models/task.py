import datetime

class Task:
    def __init__(self, id, description, status = 'todo', createdAt = None, updatedAt = None):
        now = datetime.datetime.now().strftime('%x')
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt or now
        self.updatedAt = updatedAt or now
    
    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Task(
            id = data['id'],
            description = data['description'],
            status = data['status'],
            createdAt = data['createdAt'],
            updatedAt = data['updatedAt']
        )

    def __str__(self):
        return f'{self.id} - {self.description} - {self.status}'
