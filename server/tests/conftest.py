import pytest

from server.app import make_app
from aiohttp.test_utils import TestClient


@pytest.fixture
async def client(loop, test_client):
    app = make_app()
    return await test_client(app)
