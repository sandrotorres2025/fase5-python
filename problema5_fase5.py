# ---------------------------------------------
# Programa: Control de horas trabajadas
# Problema 5 - Evaluación Final
# ---------------------------------------------

# Función para calcular total y clasificación
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz donde se almacenarán los datos
matriz_recursos = []

# Cantidad de recursos
cantidad = 4

print("===================================")
print(" CONTROL DE HORAS SEMANALES ")
print("===================================")

# Ingreso de datos
for i in range(cantidad):

    print(f"\nIngreso de datos del recurso #{i+1}")

    nombre = input("Nombre del recurso: ")

    lunes = float(input("Horas trabajadas el lunes: "))
    martes = float(input("Horas trabajadas el martes: "))
    miercoles = float(input("Horas trabajadas el miércoles: "))
    jueves = float(input("Horas trabajadas el jueves: "))
    viernes = float(input("Horas trabajadas el viernes: "))

    # Guardar en la matriz
    matriz_recursos.append([
        nombre,
        lunes,
        martes,
        miercoles,
        jueves,
        viernes
    ])

# Mostrar resultados
print("\n===================================")
print(" RESULTADOS ")
print("===================================")

for recurso in matriz_recursos:

    nombre = recurso[0]

    # Lista de horas
    horas = recurso[1:]

    # Llamado de la función
    total, clasificacion = calcular_jornada(horas)

    print(f"\nRecurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")