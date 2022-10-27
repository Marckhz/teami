from dto.data_capture_dto import DataCaptureDTO
from operations.stats_op import Stats
import random
import logging
import coloredlogs
from rich.console import Console
from collections import defaultdict

console = Console()

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

class DataCapture():

    def __init__(self) -> None:

        self.collection = defaultdict(int)
        [self.collection[i] for i in range(1000)]
        self.data = DataCaptureDTO()
        self.count = 0

    def add(self, x: int) -> None:
        """Adds a Number to the collection and counter
        
        Parameters
        ----------
        x: int
            A value to be added

        Raises
        -------
            ValueError
        
        Returns
        -------
        None

        """
        self.data.value = x
        self.collection[x] += 1
        self.count += 1

    def build_stats(self) -> Stats:
        """Algorithm to make the ordenation

        Steps:
            Take the total times add has been called as that is the number of elements added.
            Then, Create a new dict with the default values
            after that, have the less as zero and assign
            total - the current value
            update base and total
            increase base plus the current value of key
            and decrease the total via the current value of key
        
        """
        d = defaultdict(dict)
        base = 0
        total = self.count
        for key, value in self.collection.items():
            d[key]['count'] = value
            d[key]['less'] = base
            d[key]['greater'] = total -value
            base += value 
            total -= value
        return Stats(collection=d, total=self.count)

if __name__ == "__main__":
    capture = DataCapture()
    logger.info("Generating Seed")
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    
    stats = capture.build_stats()
    console.print(stats.greater(4))
    console.print(stats.less(4))
    console.print(stats.between(3,6))
    console.print(stats.between(11,12))
    console.print(stats.between(-1, 12))