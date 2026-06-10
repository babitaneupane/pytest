
import pytest


@pytest.fixture(scope="session")   #session level fixture will run once for the entire session
def preSetupWork():
    print("This is the pre setup work")

    