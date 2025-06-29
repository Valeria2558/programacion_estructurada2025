def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar...")

def menuPrincipal():
    borrarPantalla()
    print("\n\t\t\t .::: GESTIÓN DE CALIFICACIONES :::. \n\n\t 1.-Agregar Calificaciones \n\t 2.-Mostrar Calificaciones \n\t 3.-Calcular Promedios \n\t 4.-Salir")
    opcion = input("\n\tSelecciona una opción: ").upper().strip()
    return opcion

def agregarCalificaciones(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre=input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua = True
        while continua:
            try:
                #calificaciones.append(float(input(f"Calificación #(i):")))
                cal = float(input(f"Calificación #{i}:"))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("Ingresa un valor comprendido entre 0 y 10")
            except ValueError:
                print("Ingresa un valor númerico")

    lista.append([nombre]+calificaciones)
    print("Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar las Calificaciones")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'calif. 1':<10}  {'calif. 2':<10}  {'calif. 3':<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:10}")
            print("-"*60)
            cuantos=len(lista)
            print(f"Son {cuantos} alumnos")
    else:
        print("No hay calificaciones registradas en el sistema")

def calcular_promedios(lista):
    borrarPantalla()
    print("Promedios de los Alumnos")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'Promedio':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            #promedio=(fila[1]+fila[2]+fila[3])/3
            promedio=(fila[1:])/3
            print(f"{'Nombre':<15}  {'Promedio':.2f}")
            promedio_grupal+=promedio
            print("-"*40)
            promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal:.2f}")
    else:
        print("No hay calificaciones registradas en el sistema")

     
                
        
      


