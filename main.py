import argparse
from report_registry import get_report_class
from utils.reader import check_files_exist, read_logs_parallel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log_files", nargs="+")
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    check_files_exist(args.log_files)


    report_cls = get_report_class(args.report)
    if not report_cls:
        print(f"Report '{args.report}' not found.")
        return

    parsed_data = read_logs_parallel(args.log_files)
    # print(parsed_data)
    report = report_cls()
    report.process(parsed_data)
    report.display()


if __name__ == "__main__":
    main()
