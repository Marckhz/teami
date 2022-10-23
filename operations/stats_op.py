
from interface.data_capture_interface import DataCaptureInterface



class Stats(DataCaptureInterface):

    def __init__(self, collection: dict, max_value: int) -> None:
        self.collection = collection
        self.max_value = max_value

    def less(self, x: int) -> list:
        if not self.collection:
            return []
        res = []
        if x > self.max_value:
            x = self.max_value + 1
        for n in range(x):
            val = self.__retrieve(n)
            if val:
                res.append(val)
        return res

    def greater(self, x: int) -> list:
        if not self.collection:
            return []
        if  x > self.max_value:
            return []
        res = []
        x = x + 1
        for n in range(x, self.max_value+1):
            val = self.__retrieve(n)
            if val:
                res.append(val)
        return res

    def __retrieve(self, n) -> str:
        current = self.collection.get(n)
        if current:
            return current

    def between(self, x: int, y: int) -> list:
        if not self.collection:
            return []
        if x > y:
            raise ValueError("start can't be greater than end")    
        elif x > self.max_value and y > self.max_value:
            return []
        res = []
        for n in range(x+1, y):
            val = self.__retrieve(n)
            if val:
                res.append(val)
        return res