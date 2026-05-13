import pytest
from epc.db import EPCRepository


@pytest.fixture
def repo(tmp_path):
    return EPCRepository(db_path=str(tmp_path / "test.db"))


def test_attach_ue_raises_if_already_attached(repo):
    repo.attach_ue(1)

    with pytest.raises(ValueError, match="already attached"):
        repo.attach_ue(1)


def test_detach_ue_removes_it(repo):
    repo.attach_ue(1)
    repo.detach_ue(1)

    assert not repo.ue_exists(1)

