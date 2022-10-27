
from interface.data_capture_interface import DataCaptureInterface


class Stats(DataCaptureInterface):

    def __init__(self, collection: dict, total: int) -> None:

        self.collection = collection
        self.total = total

    def less(self, x: int) -> int:
        """Returns quantity of numbers less than target"""
        res = self.collection[x]
        res = res.get('less', 0)
        return res

    def greater(self, x: int) -> int:
        """Returns quantity of numbers greater than target"""
        res = self.collection[x]
        res = res.get('greater', 0)
        return res

    def between(self, x: int, y: int) -> int:
        """Returns quantity of numbers between than target"""
        if x > y:
            raise ValueError("start can't be greater than end")  
        elif x < 0 or y < 0:
            raise ValueError("wrong index")
        less = self.collection[x]
        less = less.get('less')
        greater = self.collection[x]
        greater = greater.get('greater')

        if not less or not greater:
            return 0
         
        res = self.total - less - greater
        return res