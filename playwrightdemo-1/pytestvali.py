#fixtures
import pytest
@pytest.fixture(scope="module")#module level fixture will run once for the entire module
@pytest.fixture(scope="function")#function level fixture will run before each test function
def preWork():
    print("This is the pre work")


def test_initial_check(preWork):
    print("This is the initial check")

def test_secondcheck(preWork):
        print("This is the second check")