import pytest
from report.handlers import HandlersReport


def test_handlers_report_basic():
    data = [
        ("/api/v1/auth/login/", "INFO"),
        ("/api/v1/auth/login/", "ERROR"),
        ("/api/v1/orders/", "DEBUG"),
    ]
    report = HandlersReport()
    report.process(data)

    assert report.total == 3
    assert report.data["/api/v1/auth/login/"]["INFO"] == 1
    assert report.data["/api/v1/orders/"]["DEBUG"] == 1
