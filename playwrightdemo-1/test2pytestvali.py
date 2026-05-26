#fixtures
import pytest



@pytest.fixture(scope="module")#module level fixture will run once for the entire module
def test_initial_check(preSetupWork):
    print("This is the initial check")

def test_thirdcheck(preSetupWork):
    print("This is the third check")
