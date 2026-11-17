import os

def main():
    assert os.path.exists('parser.py'), 'parser.py not found'
    assert os.path.exists('analyzer.py'), 'analyzer.py not found'
    assert os.path.exists('reporter.py'), 'reporter.py not found'
    assert os.path.exists('utils.py'), 'utils.py not found'
    assert os.path.exists('requirements.txt'), 'requirements.txt not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
