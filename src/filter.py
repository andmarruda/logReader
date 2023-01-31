import re

class filter:
    def __init__(self, regex):
        try:
            self._regex = re.compile(regex)
        except re.error:
            raise Exception('Input regex is not a valid one.')

    def exec(self, line):
        return self._regex.search(line)