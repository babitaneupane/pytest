import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("browser_name")