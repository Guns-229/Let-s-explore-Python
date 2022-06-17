import yaml


def pytest_generate_tests(metafunc):
    if 'testdata' in metafunc.fixturenames:
        with open("testdata.yaml", 'r') as f:
            Iterations = yaml.load(f)
            metafunc.parametrize('name, testdata',
                                 [[i, Iterations[i]] for i in Iterations])


def test_it(name, testdata):
    print(testdata)


# with open("testdata.yaml", 'r') as f:
#     Iterations = yaml.load(f)

#     print(list([[i, Iterations[i]] for i in Iterations]))
