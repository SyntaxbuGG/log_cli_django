from report.handlers import HandlersReport

REPORTS = {"handlers": HandlersReport}


def get_report_class(name: str):
    return REPORTS.get(name)
