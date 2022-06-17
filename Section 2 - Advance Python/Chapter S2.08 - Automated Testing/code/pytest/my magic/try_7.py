import pytest
import allure 


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append(([x[1] for x in items]))
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")

scenario1 = ('basic', {'attribute': 'value'})
scenario2 = ('advanced', {'attribute': 'value2'})

class TestSampleWithScenarios:
    
    def __init__(self):
        scenarios = [scenario1, scenario2]

    @pytest.allure.feature(scenarios[0][0])
    def test_demo1(self, attribute):
        assert isinstance(attribute, str)

    @pytest.allure.feature(scenarios[1][0])
    def test_demo2(self, attribute):
        assert isinstance(attribute, str)