import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Test client fixture."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_user():
    """Sample user data fixture."""
    return {
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    }