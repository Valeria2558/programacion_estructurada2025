peliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Películas ::.")
    nombre = input("Ingresa el nombre de la película: ").upper().strip()
    peliculas.append(nombre)
    print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::") 
    esperarTecla()

def mostrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for i, peli in enumerate(peliculas, start=1):
            print(f"\t{i}. {peli}")
    esperarTecla()

def mostrarUnaPorUna():
    borrarPantalla()
    if not peliculas:
        print("No hay películas para borrar.")
        return

    mostrarPeliculas()
    try:
        idx = int(input("Ingresa el número de la película a borrar: ")) - 1
        if 0 <= idx < len(peliculas):
            borrada = peliculas.pop(idx)
            print(F"{borrada} fue eliminada con exito")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def mostrarDel1Al4():
    borrarPantalla()
    print("\n\t.:: Películas del 1 al 4 ::.\n")
    if len(peliculas) == 0:
        print("\tNo hay películas registradas.")
    else:
        for i in range(min(4, len(peliculas))):
            print(f"\t{i+1}. {peliculas[i]}")
    esperarTecla()

def borrarPeliculas():
    borrarPantalla()
    peliculaBorrar = input("Ingresa el nombre de la película a borrar: ").upper().strip()
    if peliculaBorrar not in peliculas:
        print("\n\t::: Película no encontrada en el sistema :::")
    else:
        peliculas.remove(peliculaBorrar)
        print("\n\t::: Película borrada con éxito! :::")
        print("\n\t::: La película eliminada fue: ", peliculaBorrar)
    esperarTecla()


def buscarPeliculas():
    borrarPantalla()
    print("\n\t.:: Buscar Películas ::.")
    peliculaBuscar = input("Ingresa el nombre de la película a buscar: ").upper().strip()
    if not peliculaBuscar in peliculas:
        print("\n\t::: Película no encontrada en el sistema :::")
    else:
        encontro=0
        for i in range(len(peliculas)):
            if peliculaBuscar == peliculas[i]:
                print(f"\n\t::: Película encontrada: {peliculas[i]} :::")
                encontro+=1
        
        print(f"\n\t::: Tenemos {encontro} coincidencias con ese título :::")
        print("\n\t::: La operación se realizó con éxito! :::")
        esperarTecla()
    
def modificarPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Películas ::.")
    peliculaModificar = input("Ingresa el nombre de la película a modificar: ").upper().strip()
    if peliculaModificar not in peliculas:
        print("\n\t::: Película no encontrada en el sistema :::")
    else:
        nuevoNombre = input("Ingresa el nuevo nombre de la película: ").upper().strip()
        index = peliculas.index(peliculaModificar)
        peliculas[index] = nuevoNombre
        print("\n\t::: Película modificada con éxito! :::")
    esperarTecla()



def menu():
    while True:
        borrarPantalla()
        print("\n\t=== MENÚ DE PELÍCULAS ===")
        print("\t1. Agregar película")
        print("\t2. Mostrar películas (listado)")
        print("\t3. Mostrar películas una por una")
        print("\t4. Mostrar películas del 1 al 4")
        print("\t5. Borrar película del listado")
        print("\t6. Buscar película")
        print("\t7. Modificar película")
        print("\t8. Salir")

        opcion = input("\n\tSelecciona una opción: ")

        if opcion == '1':
            agregarPeliculas()
        elif opcion == '2':
            mostrarPeliculas()
        elif opcion == '3':
            mostrarUnaPorUna()
        elif opcion == '4':
            mostrarDel1Al4()
        elif opcion == '5':
            borrarPeliculas()
        elif opcion == '6':
            buscarPeliculas()
        elif opcion == '7':
            modificarPeliculas()
        elif opcion == '8':
            print("\n\tSaliendo del programa...")
            break
        else:
            print("\n\tOpción no válida.")
            esperarTecla()


menu()