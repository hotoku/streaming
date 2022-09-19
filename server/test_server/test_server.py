from flask.testing import FlaskClient


def test_video_list(client: FlaskClient):
    ret = client.get("/video/list")
    assert ret.json is not None and len(ret.json) == 100

    ret2 = client.get("/video/list?num=20")
    assert ret2.json is not None and len(ret2.json) == 20
