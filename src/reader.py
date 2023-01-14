from os import path

class reader:
    def __init__(self, filepath):
        if not(path.exists(filepath)):
            raise Exception('File does not exists.')

        self._file = open(filepath, 'r')

    def toList(self):
        self._lines = self._file.readlines()
        list = []
        for line in self._lines:
            list.append(line)

        return list