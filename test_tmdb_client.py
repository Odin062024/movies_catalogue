import pytest
from unittest.mock import patch, Mock
from tmdb_client import get_movie_details, get_poster_url, get_movie_cast
import pytest
from main import app
from unittest.mock import Mock

@patch('tmdb_client.call_tmdb_api')
def test_get_movie_details(mock_call_tmdb_api):
    mock_response = {"id": 1, "title": "Tytuł Filmu"}
    mock_call_tmdb_api.return_value = mock_response
    
    result = get_movie_details(1)
    mock_call_tmdb_api.assert_called_once_with('movie/1')
    assert result == mock_response

def test_get_poster_url():
    poster_api_path = "path/to/poster.jpg"
    size = "w500"
    expected_url = f"https://image.tmdb.org/t/p/{size}/{poster_api_path}"
    result = get_poster_url(poster_api_path, size)
    assert result == expected_url

@patch('tmdb_client.call_tmdb_api')
def test_get_movie_cast(mock_call_tmdb_api):
    mock_response = {"cast": [{"id": 1, "name": "Imię Aktora"}]}
    mock_call_tmdb_api.return_value = mock_response
    
    result = get_movie_cast(1)
    mock_call_tmdb_api.assert_called_once_with('movie/1/credits')
    assert result == mock_response["cast"]

@pytest.mark.parametrize("list_type,expected_endpoint", [
    ('popular', 'movie/popular'),
    ('top_rated', 'movie/top_rated'),
    ('upcoming', 'movie/upcoming'),
    ('now_playing', 'movie/now_playing'),
])
def test_homepage_with_different_list_types(monkeypatch, list_type, expected_endpoint):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}")
        assert response.status_code == 200
        api_mock.assert_called_once_with(expected_endpoint)

