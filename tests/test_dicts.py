import pytest
from utils import dicts


@pytest.fixture
def data_fixture():
    return {'vcs': 'mercurial', 'git': 'Hub', 'hello': 'world'}


def test_get_val(data_fixture):
    assert dicts.get_val(data_fixture, 'vcs') == 'mercurial'
    assert dicts.get_val(data_fixture, 'yes') == 'git'
    assert dicts.get_val(data_fixture, 'yes', 'not_git') == 'not_git'
