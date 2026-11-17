import os

def main():
    assert os.path.exists('scheduler.py'), 'scheduler.py not found'
    assert os.path.exists('task_queue.py'), 'task_queue.py not found'
    assert os.path.exists('monitor.py'), 'monitor.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
