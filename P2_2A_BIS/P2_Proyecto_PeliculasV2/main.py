#Crear un proyecto que permita administrar peliculas. Colocar un menú de opciones: Agregar, borrar, modificar, mostrar, buscar
#Limpiar una lista de peliculas.
#Notas:
#1 Utilizar funciones y mandar llamar desde otro archivo (módulo)
#2 Utilizar dict para almacenar los atributos (nombre, categoría, clasificación, género, idioma, etc.)


import peliculas
opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .::: GESTIÓN DE PELÍCULAS :::. \n\n\t 1.-Crear \n\t 2.-Borrar \n\t 3.-Mostrar \n\t 4.- Agregar característica \n\t 5.-Modificar característica \n\t 6.-Borrar característica \n\t 7.-Salir")
    opcion = input("\n\tSelecciona una opción: ").upper

    match opcion:
        case '1':
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case '2':
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case '3':
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case '4':
            peliculas.agregarCaracteristica()
            peliculas.esperarTecla()
        case '5':
            peliculas.modificarCaracteristica()
            peliculas.esperarTecla()
        case '6':
            peliculas.borrarCaracteristica()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")
        case _:
            print("\n\tOpción Inválida vuelva a intentarlo")
            peliculas.esperarTecla()

    