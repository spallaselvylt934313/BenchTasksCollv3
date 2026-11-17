import os

def main():
    assert os.path.exists('survey_builder.py'), 'survey_builder.py not found'
    assert os.path.exists('response_analyzer.py'), 'response_analyzer.py not found'
    assert os.path.exists('question_types.py'), 'question_types.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
