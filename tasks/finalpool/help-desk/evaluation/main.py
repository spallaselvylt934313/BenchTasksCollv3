import os

def main():
    assert os.path.exists('help_desk.py'), 'help_desk.py not found'
    assert os.path.exists('ticket_handler.py'), 'ticket_handler.py not found'
    assert os.path.exists('response_templates.py'), 'response_templates.py not found'
    print('Tests passed')

if __name__ == '__main__':
    main()
