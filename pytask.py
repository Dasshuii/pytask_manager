from managers.task_manager import add, update, delete, mark_status, task_list
from cli import parser
from tools import valid_str
import sys

def main():
    args = parser.parse_args()
    
    match args.action:
        case 'add':
            description = args.description.strip()
            if valid_str(description):
                print('Invalid description. Try again.')
                sys.exit(1)
            add(args.description)
            print('Task added succesfully.')
        case 'update':
            description = args.description.strip()
            if valid_str(description):
                print('Invalid description. Try again.')
                sys.exit(1)
            update(args.id, args.description)
            print('Task updated succesfully')
        case 'delete':
            delete(args.id)
            print('Task deleted succesfully')
        case 'list':
            task_list(args.status)
        case 'mark-in-progress':
            mark_status(args.id, 'in-progress')
            print('Task status updated succesfully')
        case 'mark-done':
            mark_status(args.id, 'done')
            print('Task status updated succesfully')
        case '_':
            print('Invalid action. Try again.')

if __name__ == '__main__':
    main()