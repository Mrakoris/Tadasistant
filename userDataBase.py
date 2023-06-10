import os


class userDataBase(object):
    def __init__(self, parent=None):
        super(self).__init__(parent)

def initFile():
    if not os.path.exists('Users.txt'):
        with open('Users.txt', 'w'):
            pass

def addUser(login: str, password: str) -> bool:
    with open('Users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0]:
            return False

    with open('Users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')
        return True
#
def getUser(login: str, password: str) -> bool:
    with open('Users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:
                return True
        return False
