import pytest
from unittest.mock import MagicMock
from services.collection_service import CollectionService

@pytest.fixture
def mock_collection_repo():
    repo = MagicMock()
    repo.create_collection.return_value = {"name": "My Gallery", "owner_id": 1}
    return repo

def test_create_collection(mock_collection_repo):
    service = CollectionService(collection_repo=mock_collection_repo)
    
    result = service.create_collection(name="My Gallery", owner_id=1)

    assert result["name"] == "My Gallery"
    assert result["owner_id"] == 1
    mock_collection_repo.create_collection.assert_called_once()
