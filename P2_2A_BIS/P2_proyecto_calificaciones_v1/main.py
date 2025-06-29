import calificaciones

def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrar_pantalla()
        opcion=calificaciones.menu_principal()


        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperar_tecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperar_tecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperar_tecla()


if __name__ == "__main__":
    main()

