from abc import ABC, abstractmethod
from typing import List


class BaseReport(ABC):
    @abstractmethod
    def process(self, data: List[str]) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass
