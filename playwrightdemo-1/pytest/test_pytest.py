#fixtures
import pytest
@pytest.fixture(scope="function")#module level fixture will run once for the entire module
def preWork():
    print("This is the pre work")
    return"pass"

@pytest.fixture(scope="function")
def secondwork():
    print("This is the secondwork")
   # return"pass"
    yield  #pause the execution here and resume after the test function is executed
print("Tear down validation")

#@pytest.mark.skip(reason="test is skipped")
def test_initial_check(preWork,secondwork):
    print("This is the initial check")
    assert preWork=="pass"     #fail=fail is also  pass


@pytest.mark.skip(reason="test is skipped")
def test_secondCheck(preWork,secondwork):
    print("This is the second check")
   
