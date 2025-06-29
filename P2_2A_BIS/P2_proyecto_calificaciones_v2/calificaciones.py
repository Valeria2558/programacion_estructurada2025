def borarpantalla():
    import os
    import platform
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def esperarTecla():
    input("📝 Oprima cualquier tecla para continuar...")

def menu_principal():
    print("..:: 🎓 Sistema de gestión de calificaciones ::..")
    print("1️⃣.- Agregar calificaciones")
    print("2️⃣.- Mostrar calificaciones")
    print("3️⃣.- Calcular promedios")
    print("4️⃣.- 🚪 Salir")

def agregar_calificaciones(lista):
    borarpantalla()
    print("📝 Agregar calificaciones")
    nombre = input("👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"📝 Calificación #{i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else: 
                    print("❌ ¡Error! Ingrese un valor entre 0 y 10")
            except ValueError:
                print("❌ ¡Error! Ingrese un valor numérico")
    lista.append([nombre] + calificaciones)
    print("✅ Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borarpantalla()
    print("🔍 Mostrar Calificaciones")
    if len(lista) > 0:
        print(f"{'👤 Nombre':<15}  {'📝 Calif. 1':<10}  {'📝 Calif. 2':<10}  {'📝 Calif. 3':<10}")
        print("-" * 50)
        for fila in lista:
            print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
            print("-"*50)
        cuantos = len(lista)
        print(f"📊 Total: {cuantos} alumnos")
    else:
        print("⚠ No hay calificaciones registradas")

def calcular_promedios(lista):
    borarpantalla()
    print("📊 Promedio de alumnos")
    if len(lista) > 0:
        print(f"{'👤 Nombre':<15}  {'📊 Promedio':<10}")
        print("-" * 40)
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = (fila[1] + fila[2] + fila[3])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal += promedio
            print("-"*40)
        promedio_grupal = promedio_grupal/len(lista)
        print(f"🎉 Promedio grupal: {promedio_grupal:.2f}")
    else:
        print("⚠ No hay calificaciones para calcular")