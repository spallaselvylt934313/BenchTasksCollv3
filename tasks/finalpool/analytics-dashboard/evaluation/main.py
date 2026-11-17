import os

def main():
    assert os.path.exists('analytics_dashboard.py'), 'analytics_dashboard.py not found'
    assert os.path.exists('chart_generator.py'), 'chart_generator.py not found'
    assert os.path.exists('data_aggregator.py'), 'data_aggregator.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
