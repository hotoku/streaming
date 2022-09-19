from server import app as APP
import pytest
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app():
    APP.config.update({
        "TESTING": True
    })
    yield APP


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
