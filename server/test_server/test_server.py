from flask.testing import FlaskClient


def test_video_list(client: FlaskClient):
    ret = client.get("/video/list")
    assert len(ret.json) == 100

    ret2 = client.get("/video/list?num=20")
    assert len(ret2.json) == 20
