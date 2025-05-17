import csv
from .interfaz import CiudadInterface

class CiudadCSV(CiudadInterface):
    def __init__(self, ruta_csv):
        self.datos_ciudades = self.cargar_datos_csv(ruta_csv)

    def cargar_datos_csv(self, ruta_csv):
        datos_ciudades = {}
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                clave = (fila['city'].strip(), fila['country'].strip())
                datos_ciudades[clave] = (float(fila['lat']), float(fila['lng']))
                print(f"Ciudad: {fila['city'].strip()}, País: {fila['country'].strip()}, Coordenadas: ({fila['lat']}, {fila['lng']})")
        print(f"Se han cargado {len(datos_ciudades)} ciudades desde el archivo CSV.")
        return datos_ciudades

    def obtener_coordenadas(self, ciudad, pais):
        return self.datos_ciudades.get((ciudad, pais), None)
