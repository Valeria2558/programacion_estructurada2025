import calificaciones

def main():
    datos = []
    
    while True:
        calificaciones.borarpantalla()
        calificaciones.menu_principal()
        opcion = input("📝 Seleccione una opción (1-4): ")
        
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                print("\n\t 🎉 Terminaste la ejecución del programa. ¡Gracias por usarlo!")
                calificaciones.esperarTecla()
                calificaciones.borarpantalla()
                break
            case _:
                print("\n\t ❌ Opción no válida, por favor selecciona una opción del menú (1-4)")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()