from abc import ABC, abstractmethod


class DataCaptureInterface(ABC):

    @abstractmethod
    def less(self, x) -> int:
        """Returns Numbers lower than target number"""

    @abstractmethod
    def greater(self, x) -> int:
        """Returns Numbers greater than target number"""

    @abstractmethod
    def between(self, x) -> int:
        """Returns Numbers between a range of numbers"""
    