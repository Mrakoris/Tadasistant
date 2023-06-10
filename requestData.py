import os


class requestData(object):
    def __init__(self, parent=None):
        super(self).__init__(parent)


def initFileRequest():
    if not os.path.exists('userActions.txt'):
        with open('userActions.txt', 'w'):
            pass


def reQuest(login: str, request: str) -> bool:

    with open('userActions.txt', 'a') as f:
        f.write(f'{login}:{request}\n')
        return True
