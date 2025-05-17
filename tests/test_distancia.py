from unittest.mock import MagicMock
from ciudad.api import CiudadAPI
from utils.calculadora import CalculadorDistancia

def test_haversine_distancia_known():
    distancia = CalculadorDistancia.haversine(40.7128, -74.0060, 51.5074, -0.1278)
    assert 5560 < distancia < 5600

def test_distancia_con_mock_api():
    # Creamos una instancia de CiudadAPI pero "mockeamos" el método obtener_coordenadas
    mock_api = CiudadAPI()
    mock_api.obtener_coordenadas = MagicMock(side_effect=[
        (40.7128, -74.0060),  # Nueva York
        (51.5074, -0.1278)    # Londres
    ])

    ciudad1 = "New York"
    pais1 = "USA"
    ciudad2 = "London"
    pais2 = "UK"

    coordenadas1 = mock_api.obtener_coordenadas(ciudad1, pais1)
    coordenadas2 = mock_api.obtener_coordenadas(ciudad2, pais2)

    distancia = CalculadorDistancia.haversine(*coordenadas1, *coordenadas2)

    # Verificamos que se llame correctamente y que el resultado sea el esperado (aprox. 5570 km)
    assert 5560 < distancia < 5600
    mock_api.obtener_coordenadas.assert_any_call("New York", "USA")
    mock_api.obtener_coordenadas.assert_any_call("London", "UK")