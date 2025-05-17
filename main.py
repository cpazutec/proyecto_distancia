from ciudad.api import CiudadAPI
from ciudad.csv_ciudad import CiudadCSV
from utils.calculadora import CalculadorDistancia

def main():
    print("Elija el método para obtener la información de la ciudad:")
    print("1. Usar API (requiere conexión a internet)")
    print("2. Usar archivo CSV (datos locales)")

    opcion = input("Ingrese el número de la opción elegida: ")

    if opcion == '1':
        metodo_ciudad = CiudadAPI()
    elif opcion == '2':
        metodo_ciudad = CiudadCSV('data/worldcities.csv')
    else:
        print("Opción no válida.")
        return

    ciudad1 = input("Introduce la primera ciudad: ")
    pais1 = input("Introduce el país de la primera ciudad: ")
    ciudad2 = input("Introduce la segunda ciudad: ")
    pais2 = input("Introduce el país de la segunda ciudad: ")

    coordenadas1 = metodo_ciudad.obtener_coordenadas(ciudad1, pais1)
    coordenadas2 = metodo_ciudad.obtener_coordenadas(ciudad2, pais2)

    if coordenadas1 and coordenadas2:
        distancia = CalculadorDistancia.haversine(*coordenadas1, *coordenadas2)
        print(f"La distancia entre {ciudad1}, {pais1} y {ciudad2}, {pais2} es de {distancia:.2f} km.")
    else:
        print("No se pudo obtener la información de una o ambas ciudades.")

if __name__ == "__main__":
    main()
