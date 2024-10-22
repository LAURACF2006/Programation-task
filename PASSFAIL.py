def evaluar_aprobacion(nota_examen=75, total_clases=40, clases_asistidas=32):
    # Calcular el porcentaje de asistencia
    porcentaje_asistencia = (clases_asistidas / total_clases) * 100
    
    # Determinar si el estudiante aprueba o reprueba
    if nota_examen >= 70 and porcentaje_asistencia >= 80:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"
    
    # Mostrar los resultados
    print("Resultados de la Evaluación")
    print(f"Nota del Examen: {nota_examen}")
    print(f"Total de Clases: {total_clases}")
    print(f"Clases Asistidas: {clases_asistidas}")
    print(f"Porcentaje de Asistencia: {porcentaje_asistencia:.2f}%")
    print(f"Resultado: {resultado}")

# Obtener entradas del usuario o usar valores predeterminados
try:
    nota_examen = input("Ingrese la nota del examen (el valor predeterminado es 75): ")
    total_clases = input("Ingrese el total de clases (el valor predeterminado es 40): ")
    clases_asistidas = input("Ingrese el número de clases asistidas (el valor predeterminado es 32): ")

    # Convertir entradas a enteros si se proporcionan, de lo contrario usar valores predeterminados
    nota_examen = int(nota_examen) if nota_examen else 75
    total_clases = int(total_clases) if total_clases else 40
    clases_asistidas = int(clases_asistidas) if clases_asistidas else 32

    # Evaluar si aprueba o reprueba
    evaluar_aprobacion(nota_examen, total_clases, clases_asistidas)
except ValueError:
    print("Entrada no válida. Por favor, ingrese valores numéricos para la nota del examen, el total de clases y las clases asistidas.")
evaluar_aprobacion()