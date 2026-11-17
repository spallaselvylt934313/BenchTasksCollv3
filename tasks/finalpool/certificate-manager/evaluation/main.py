import os

def main():
    assert os.path.exists('cert_generator.py'), 'cert_generator.py not found'
    assert os.path.exists('cert_validator.py'), 'cert_validator.py not found'
    assert os.path.exists('cert_storage.py'), 'cert_storage.py not found'
    assert os.path.exists('cert_manager.py'), 'cert_manager.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
