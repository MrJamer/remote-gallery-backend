import pytest
from unittest.mock import MagicMock
from services.user_service import UserService

@pytest.fixture
def mock_user_repo():
    repo = MagicMock()
    repo.get_by_email.return_value = None
    repo.create_user.return_value = {"id": 1, "email": "test@example.com"}
    return repo

def test_create_user_success(mock_user_repo):
    service = UserService(user_repo=mock_user_repo)
    
    result = service.create_user(email="test@example.com")

    assert result["id"] == 1
    assert result["email"] == "test@example.com"
    mock_user_repo.create_user.assert_called_once()
