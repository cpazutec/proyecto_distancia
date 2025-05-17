from ciudad.geoapify import CiudadGeoapify
from unittest.mock import patch

@patch("ciudad.geoapify.requests.get")
def test_geoapify_mock(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": [{"lat": 40.7128, "lon": -74.0060}]
    }

    geo = CiudadGeoapify("fake_api_key")
    coords = geo.obtener_coordenadas("New York", "USA")
    assert coords == (40.7128, -74.0060)
