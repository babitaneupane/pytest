#fixtures
import pytest



@pytest.fixture(scope="module")#module level fixture will run once for the entire module
#@pytest.fixture(scope="session")#session level fixture will run once for the entire session
#@pytest.fixture(scope="function")#function level fixture will run once for each test function
def preSetupWork():
    print("This is the pre work")
def test_initial_check(preSetupWork):
    print("This is the initial check")

def test_thirdcheck(preSetupWork):
    print("This is the third check")
