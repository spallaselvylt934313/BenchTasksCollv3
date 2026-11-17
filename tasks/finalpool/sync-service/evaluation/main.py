import os

def main():
    assert os.path.exists('sync_service.py'), 'sync_service.py not found'
    assert os.path.exists('data_validator.py'), 'data_validator.py not found'
    assert os.path.exists('conflict_resolver.py'), 'conflict_resolver.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
