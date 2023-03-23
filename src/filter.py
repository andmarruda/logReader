import re
from src.reader import reader

class filter:
    def __init__(self, filepath, auto=True):
        try:
            print(self.getRegEx())
            self._filepath = filepath
            self._reader = reader(self._filepath)
            self._regex = re.compile(self.getRegEx())
            self._filtered = []

            if(auto):
                self.filter()
        except re.error:
            raise Exception('Input regex is not a valid one.')

    def changePosition(self):
        self._reader

    def filter(self):
        lines = self._reader.line()
        while(lines):
            if(self.exec(lines)):
                self._filtered.append(lines)
                self._limited += 1
        self._reader.close()

    def exec(self, line):
        return self._regex.search(line)

    def getFiltered(self):
        return self._filtered