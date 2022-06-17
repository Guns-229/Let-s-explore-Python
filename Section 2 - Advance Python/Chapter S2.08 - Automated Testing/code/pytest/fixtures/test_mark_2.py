"""
pytest -sv  -m "parez" test_mark_1.py 

"""


import pytest

@pytest.fixture
def i_set_things_up(request):
    projector = {'status': 'doing fine',
                 'flashing': "dicts can't flash!"}
    def fin():
        projector['status'] = 'torn down by finalizer!'
    request.addfinalizer(fin)
    return projector

@pytest.mark.shssael
@pytest.mark.parez
def test_nothing(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'


@pytest.mark.joy
def test_really_nothing(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'

@pytest.mark.joy
def test_really_really_nothing(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'
