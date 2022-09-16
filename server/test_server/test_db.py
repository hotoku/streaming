from server import db


def test_random_list():
    ret = list(db.random_list())
    assert len(ret) == 100

    ret2 = list(db.random_list())
    assert len(ret2) == 100

    id1 = [r["id"] for r in ret]
    id2 = [r["id"] for r in ret2]
    assert not id1 == id2
