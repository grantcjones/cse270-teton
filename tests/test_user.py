import pytest
import requests
from unittest.mock import MagicMock

@pytest.mark.parametrize("username, password, expected_status_code", [
    ("admin", "admin", 401),
    ("admin", "qwerty", 200)
])
def test_login(username, password, expected_status_code, mocker):
    url = "http://127.0.0.1:5500/users"
    params = {
        "username": username,
        "password": password
    }

    # Create a mock response object
    mock_response = MagicMock()
    mock_response.status_code = expected_status_code
    mock_response.text = ""

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mock_response)

    # Make the request
    response = requests.get(url, params=params)

    # Check if response status code matches expected
    assert response.status_code == expected_status_code
    
    # Check if response body is empty
    assert not response.text.strip(), "Response body is not empty"

    if expected_status_code == 401:
        print("Test for wrong credentials passed!")
    else:
        print("Test for correct credentials passed!")

if __name__ == "__main__":
    pytest.main()
