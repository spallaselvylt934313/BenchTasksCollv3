import os

def main():
    assert os.path.exists('cache_optimizer.py'), 'cache_optimizer.py not found'
    assert os.path.exists('eviction_policy.py'), 'eviction_policy.py not found'
    assert os.path.exists('monitor.py'), 'monitor.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
