import json

from flask.testing import FlaskClient


def test_video_list(client: FlaskClient):
    ret = client.get("/video/list")
    if ret is None:
        return
    assert len(ret.json) == 3
