from os import path
from src.filter import filter

class reader:
    def __init__(self, filepath):
        if not(path.exists(filepath)):
            raise Exception('File does not exists.')

        self._file = open(filepath, 'r')
        self._filter = []

    def __any_filter_match(self, line):
        for f in self._filter:
            if f.exec(line):
                return True

        return False

    def __readingLines(self, filter=None, use_filters=False):
        lines = self._file.readlines()
        list = []
        for line in lines:
            if filter is not None and filter.exec(line):
                list.append(line)

            if use_filters and self.__any_filter_match(line):
                list.append(line)

            if filter is None and use_filters is False:
                list.append(line)

        return list

    def toList(self):
        return self.__readingLines()

    def isFilter(self, input_filter):
        if not (isinstance(input_filter, filter)):
            raise Exception('Need to be a filter class to be setted over here.')

    def set_filter(self, filter):
        self.isFilter(filter)
        self._filter.append(filter)
        return self

    def getByFilter(self, filter):
        self.isFilter(filter)
        return self.__readingLines(filter)

    def filter_all(self):
        return self.__readingLines(use_filters=True)