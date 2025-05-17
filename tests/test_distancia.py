from utils.calculadora import CalculadorDistancia

def test_haversine_distancia_known():
    distancia = CalculadorDistancia.haversine(40.7128, -74.0060, 51.5074, -0.1278)
    assert 5560 < distancia < 5600
