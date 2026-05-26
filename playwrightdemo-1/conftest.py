
import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("This is the pre setup work")