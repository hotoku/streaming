import pytest
from xprocess import ProcessStarter
from flask import Flask
from flask.testing import FlaskClient

import sys
open("/tmp/hoge", "w").write(str(sys.path))

from server import app as APP




@pytest.fixture
def app():
    APP.config.update({
        "TESTING": True
    })
    yield APP


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def server(xprocess):
    server_name = "myserver"

    class Starter(ProcessStarter):
        pattern = r"Running on http:"  # type: ignore
        timeout = 2
        terminate_on_interrupt = True
        args = ["python",
                "-m", "server"]  # type: ignore
    logfile = xprocess.ensure(server_name, Starter)
    yield dict(url="http://localhost", logfile=logfile)

    xprocess.getinfo(server_name).terminate()
