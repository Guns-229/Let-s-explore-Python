# content of conftest.py
#
import sys
import pytest

ALL = set(["darwin", "linux", "win32"])

def pytest_runtest_setup(item):
    if isinstance(item, item.Function):
        plat = sys.platform
        if not item.get_marker(plat):
            if ALL.intersection(item.keywords):
                pytest.skip("cannot run on platform %s" %(plat))