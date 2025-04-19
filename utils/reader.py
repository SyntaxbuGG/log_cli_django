import os
from concurrent.futures import ProcessPoolExecutor
from log_reader import read_log_file
from typing import List


def check_files_exist(paths: List[str]):
    for path in paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")


def read_logs_parallel(paths: List[str]) -> List[str]:
    results = []
    with ProcessPoolExecutor() as executor:
        for data in executor.map(read_log_file, paths):
            results.extend(data)

    return results
