import re

log_pattern = re.compile(
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL).*?(?P<path>/[^\s]+)/?"
)

# все данные лог
# log_pattern = re.compile(
#     r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
#     r"(?P<module>[\w.]+):\s*"
#     r"(?:"
#     r"(?:GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS|Internal Server Error:)?\s+(?P<path>/[^\s]+)"
#     r")?"
# )


def parse_line(line: str):
    match = log_pattern.search(line)

    if not match:
        return None

    path = match.group("path")
    level = match.group("level")

    # все данные
    # module = match.group("module")
    # if path is None:
    #     path = f"{module}"

    return path, level


def read_log_file(file_path: str):
    results = []

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                results.append(parsed)

    return results
