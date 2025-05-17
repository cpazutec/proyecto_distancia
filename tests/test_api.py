from ciudad.api import CiudadAPI

def test_coordenadas_api():
    api = CiudadAPI()
    coordenadas = api.obtener_coordenadas("Paris", "France")
    assert coordenadas is None or (isinstance(coordenadas[0], float) and isinstance(coordenadas[1], float))
