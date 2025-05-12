import pytest

from flask_login import current_user
from app import create_app
from app.plugins import db
from app.auth import Users, USER, ACTIVE


@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.testing = True

    client = app.test_client()
    yield client


def test_home_page(client):
    response = client.get("/")
    assert b"Let's start with Python & Flask" in response.data
