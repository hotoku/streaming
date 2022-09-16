import pytest
from xprocess import ProcessStarter
from flask import Flask
from flask.testing import FlaskClient

import server as _server


@pytest.fixture
def app():
    app = _server.app
    app.config.update({
        "TESTING": True
    })
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def server(xprocess):
    port = 8080
    server_name = "myserver"

    class Starter(ProcessStarter):
        pattern = r"Running on http:"  # type: ignore
        timeout = 2
        terminate_on_interrupt = True
        args = ["python",
                "-m", "di_predict", "server",
                "--port", port]  # type: ignore
    logfile = xprocess.ensure(server_name, Starter)
    yield dict(url="http://localhost", port=port, logfile=logfile)

    xprocess.getinfo(server_name).terminate()
