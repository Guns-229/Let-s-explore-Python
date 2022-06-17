# content of test_plat.py
"""
pytest 
pytest -m linux

"""
import pytest

@pytest.mark.darwin
def test_if_apple_is_evil():
    pass

@pytest.mark.linux
def test_if_linux_works():
    pass

@pytest.mark.win32
def test_if_win32_crashes():
    pass

def test_runs_everywhere():
    pass