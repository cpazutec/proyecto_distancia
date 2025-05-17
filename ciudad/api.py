import requests
from .interfaz import CiudadInterface

class CiudadAPI(CiudadInterface):
    def obtener_coordenadas(self, ciudad, pais):
        url = f'https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json'
        headers = {'User-Agent': 'MiAplicacion/1.0'}

        try:
            respuesta = requests.get(url, headers=headers)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                if datos:
                    lugar = datos[0]
                    lat = float(lugar.get('lat'))
                    lon = float(lugar.get('lon'))
                    return lat, lon
                else:
                    print(f"No se encontraron resultados para {ciudad}, {pais}.")
            else:
                print("Error en la solicitud:", respuesta.status_code)
        except Exception as e:
            print("Ocurrió un error:", str(e))
        return None
