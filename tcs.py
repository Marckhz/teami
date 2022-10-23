from dto.data_capture_dto import DataCaptureDTO
from operations.stats_op import Stats
import random
import logging
import coloredlogs
from rich.console import Console

console = Console()

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)

class DataCapture():

    def __init__(self) -> None:
        self.collection = {}
        self.m_list = None
        self.data = DataCaptureDTO()
        self.max_value = 0

    def add(self, x: int) -> None:
        self.data.value = x
        if self.data.value > self.max_value:
            self.max_value = self.data.value
        val = self.collection.get(self.data.value)
        if not val:
            self.collection[x] = str(self.data.value)
        else:
            self.collection[x] = f'{val}{x}'

    def build_stats(self) -> Stats:
        if not self.collection:
            return Stats(collection={}, max_value=0)
        return Stats(collection=self.collection, max_value=self.max_value)


if __name__ == "__main__":
    capture = DataCapture()
    logger.info("Generating Seed")
    for n in range(1000):
        rn = random.randint(0,1000)
        capture.add(rn)
    logger.info("Finish seed")
    logger.info("Building")
    stats = capture.build_stats()
    x = stats.less(11)[:5]
    y = stats.between(10,100)[:5]
    z = stats.greater(50)[:5]
    
    console.print(f"[red]Greater [white]{z}")
    console.print(f"[green]Lower [white]{x}")
    console.print(f"[yellow]Between [white]{y}")
  