import argparse

parser = argparse.ArgumentParser(
    prog = 'pytask.py',
    description = 'Never forget what to do',
)

subparsers = parser.add_subparsers(dest = 'action', required = True)

# Action 'add'
parser_add = subparsers.add_parser('add', help = 'Add new Task.')
parser_add.add_argument('description', help = 'Task\'s description', type = str)

# Action 'update'
parser_update = subparsers.add_parser('update', help = 'Update task by id.')
parser_update.add_argument('id', help = 'id of the task to update', type = int)
parser_update.add_argument('description', help = 'New task description', type = str)

# Action 'delete'
parser_delete = subparsers.add_parser('delete', help = 'Delete task by id.')
parser_delete.add_argument('id', help = 'id of the task to delete', type = int)

# Action 'mark-in-progress'
parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help = 'Change task status to in-progress.')
parser_mark_in_progress.add_argument('id', help = 'task id to change status to in-progress', type = int)

# Action 'mark-done'
parser_mark_done = subparsers.add_parser('mark-done', help = 'Change task status to done.')
parser_mark_done.add_argument('id', help = 'task id to change status to done', type = int)

# Action 'list'
parser_list = subparsers.add_parser('list', help = 'List task by status.')
parser_list.add_argument('status', help = 'status to filter tasks', type = str, choices = ['done', 'todo', 'in-progress', 'all'])


