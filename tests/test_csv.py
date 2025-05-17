from ciudad.csv_ciudad import CiudadCSV

def test_coordenadas_csv():
    lector = CiudadCSV("data/worldcities.csv")
    coordenadas = lector.obtener_coordenadas("Lima", "Peru")
    assert coordenadas is not None
    lat, lon = coordenadas
    assert isinstance(lat, float) and isinstance(lon, float)
