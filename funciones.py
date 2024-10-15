from UTN_Heroes_Dataset.utn_pp import (get_original_matrix, mostrar_matriz_texto_tabla, clear_console, color_text)

def validar_opcion(minimo: int, maximo: int) -> int:
    numero = input(f"Ingrese un numero entre {minimo} y {maximo}: ")
    if not numero.isdigit() or minimo > int(numero) or maximo < int(numero):
        return validar_opcion(minimo, maximo)
    return int(numero)

def obtener_existencias():
    matriz_concesionaria = get_original_matrix()
    print("Existencias de vehiculos en cada garage:")

    indice_garage = 1
    for garage in matriz_concesionaria:
        print(f"Garage {indice_garage}: {garage}")
        indice_garage += 1
        if indice_garage > 20:
            break


def cantidad_total_unidades()     