from collections import defaultdict
from typing import List, Tuple

from report.base import BaseReport


class HandlersReport(BaseReport):
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(int))
        self.total = 0

    def process(self, data: List[Tuple[str, str]]) -> None:
        for path, level in data:
            self.data[path][level] += 1
            self.total += 1

    def display(self) -> None:
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        max_path_len = (
            max((len(path) for path in self.data), default=len("HANDLER")) + 4
        )
        level_width = max(len(lvl) for lvl in levels) + 2

        print(f"Total requests: {self.total}\n")
        # Заголовок
        print(
            f"{'HANDLER':<{max_path_len}}"
            + "".join([f"{lvl:<{level_width}}" for lvl in levels])
        )
        summary = defaultdict(int)
        # Данные
        for path in sorted(self.data):
            print(f"{path:<{max_path_len}}", end="")
            for lvl in levels:
                count = self.data[path].get(lvl, 0)
                summary[lvl] += count

                print(f"{count:<{level_width}}", end="")
            print()
        # Итог
        max_path_len -= 7
        print(
            "\nTotal: "
            + max_path_len * " "
            + "".join([f"{summary[lvl]:<{level_width}}" for lvl in levels])
        )
