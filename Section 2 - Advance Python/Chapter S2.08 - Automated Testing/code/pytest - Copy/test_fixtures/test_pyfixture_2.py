#test_pyfixture_1.py
import pytest

class MyTester(object):
    def __init__(self, request, arg=["var0", "var1"]):
        self.request = request
        self.arg = arg
        # self.use_arg_to_init_logging_part()

    def showArgs(self):
        return("args", self.arg)

    def showRequest(self):
        print ("req", self.request)


@pytest.fixture
def tester(request):
    """Create tester object"""
    return MyTester(request.param)


class TestIt:
    @pytest.mark.parametrize('tester', [['var1', 'var2'], ['var3', 'var4']], indirect=True)
    def test_tc1(self, tester):
       print(tester.showArgs())
       assert 1