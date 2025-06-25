import pytest
from unittest.mock import MagicMock
from services.image_service import ImageService

@pytest.fixture
def mock_image_repo():
    repo = MagicMock()
    repo.add_image.return_value = {"filename": "img.png", "collection_id": 1}
    return repo

def test_add_image_to_collection(mock_image_repo):
    service = ImageService(image_repo=mock_image_repo)
    
    result = service.add_image("img.png", "/path/img.png", 1)

    assert result["filename"] == "img.png"
    assert result["collection_id"] == 1
    mock_image_repo.add_image.assert_called_once()
