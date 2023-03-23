from os import path

class reader:
    def __init__(self, filepath):
        if not(path.exists(filepath)):
            raise Exception('File does not exists.')

        self._file = open(filepath, 'r')
        self._filepath = filepath

    def reset(self):
        self._file.seek(0)

    def setPosition(self, position):
        self._file.seek(position)

    def line(self):
        if self._file.closed:
            self._file = open(self._filepath, 'r')

        return self._file.readline()

    def close(self):
        self._file.close()