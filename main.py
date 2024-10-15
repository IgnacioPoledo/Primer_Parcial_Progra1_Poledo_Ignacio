from salida_consola import *
from funciones import *

def garages(matriz: list[list]) -> None:

    while True:

        mostrar_menu()
        opcion = validar_opcion(1, 9)

        match opcion:
            case 1:
                obtener_existencias()
            case 2:
                cantidad_total_unidades()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("Salir")
                break
            case _:
                print("Opcion no valida")    

garages(get_original_matrix)