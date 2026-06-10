import pytest

@pytest.fixture(scope="session")
def preSetupwork():
    print("I setup browser instance")


