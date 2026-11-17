import os

def main():
    assert os.path.exists('monitor.py'), 'monitor.py not found'
    assert os.path.exists('checker.py'), 'checker.py not found'
    assert os.path.exists('alerter.py'), 'alerter.py not found'
    assert os.path.exists('reporter.py'), 'reporter.py not found'
    assert os.path.exists('config.py'), 'config.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
