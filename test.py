import pytest
from main import get_weather


def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    api_key = '01d50d241915f5d850574139c275f457'
    city = 'London'
    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }




