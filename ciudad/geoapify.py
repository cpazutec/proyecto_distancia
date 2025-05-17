import requests
from .interfaz import CiudadInterface

class CiudadGeoapify(CiudadInterface):
    def __init__(self, api_key):
        self.api_key = api_key

    def obtener_coordenadas(self, ciudad, pais):
        url = "https://api.geoapify.com/v1/geocode/search"
        params = {
            "text": f"{ciudad}, {pais}",
            "apiKey": self.api_key,
            "format": "json"
        }

        try:
            respuesta = requests.get(url, params=params)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                resultados = datos.get("results", [])
                if resultados:
                    lat = resultados[0]["lat"]
                    lon = resultados[0]["lon"]
                    return lat, lon
                else:
                    print(f"No se encontraron resultados para {ciudad}, {pais}.")
            else:
                print(f"Error {respuesta.status_code}: {respuesta.text}")
        except Exception as e:
            print("Ocurrió un error al consultar Geoapify:", str(e))

        return None
