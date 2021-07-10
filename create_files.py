import os


def check_files():
    if not os.path.exists('sessions'):
        os.mkdir('sessions')

    if not os.path.exists('.env'):
        file = open('.env', 'w')
        file.write('LOGIN=\n')
        file.write('PASSWORD=\n')
        file.write('SEND_ID=')
