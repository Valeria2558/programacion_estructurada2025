'''
Sistema de gestión de películas
Permite agregar, borrar, modificar, mostrar, buscar y limpiar una lista de películas
'''

import peliculas

opcion = True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::GESTION DE PELICULAS:::.")
    print("\t 1.- Agregar")
    print("\t 2.- Borrar")
    print("\t 3.- Modificar")
    print("\t 4.- Mostrar")
    print("\t 5.- Buscar")
    print("\t 6.- Limpiar lista")
    print("\t 7.- Salir")
    
    opcion = input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")
        case _:
            print("\n\tOpción Inválida vuelva a intentarlo")
            peliculas.esperarTecla()