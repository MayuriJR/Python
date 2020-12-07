
class SearchData(object):

    def __init__(self):
        self._indicator = 0
        self._middle_interval = 15
        self._big_interval = 60
        self._position = {}

    def search(self, line_data: list) -> dict:
        self._position.clear()
        self._position[1] = line_data[2: 5]
        if self._indicator % self._middle_interval == 0:
            self._position[2] = line_data[7: 9]
        if self._indicator % self._big_interval == 0:
            self._position[3] = line_data[10: 12]
        self._indicator += 1
        return self._position

