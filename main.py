from task_manager import add, update, mark_in_progress, mark_done, task_list
import datetime
from data.data_manager import load_tasks

def main():
    task_list()
    mark_done(0)
    task_list()
    mark_in_progress(0)
    task_list()

if __name__ == '__main__':
    main()