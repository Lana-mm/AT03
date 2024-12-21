import pytest
from main import get_random_cat_image
import requests
from unittest.mock import patch


def test_get_random_cat_image_success():
    # Настраиваем мока для успешного ответа
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

        result = get_random_cat_image()

        assert result == 'https://example.com/cat.jpg'
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")


def test_get_random_cat_image_failure():
    # Настраиваем мока для неуспешного ответа
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None

        result = get_random_cat_image()

        assert result is None
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")
