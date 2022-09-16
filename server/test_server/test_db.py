from server import db


def test_random_list():
    ret = db.random_list()
    assert len(ret) == 100

    ret2 = db.random_list()
    assert len(ret2) == 100

    assert ret != ret2
