"""
Ejemplo de Programación Estructurada en Python
==============================================

Este ejemplo demuestra los principios clave de la programación estructurada:
1. Ejecución secuencial
2. Selección (sentencias condicionales)
3. Iteración (bucles)
4. Diseño modular con funciones
5. Enfoque de arriba hacia abajo
6. Puntos únicos de entrada y salida para las estructuras de control
"""

def obtener_calificaciones():
    """
    Función para recopilar calificaciones de estudiantes desde la entrada del usuario.
    Demuestra ejecución secuencial y validación de entrada.
    """
    calificaciones = []
    print("Ingrese las calificaciones de los estudiantes (ingrese -1 para finalizar):")
    
    while True:  # Estructura de iteración
        try:
            calificacion = float(input("Ingrese calificación (0-100): "))
            
            # Estructura de selección - validación de entrada
            if calificacion == -1:
                break
            elif calificacion < 0 or calificacion > 100:
                print("¡Calificación inválida! Por favor, ingrese un valor entre 0 y 100.")
                continue
            else:
                calificaciones.append(calificacion)
                
        except ValueError:
            print("¡Entrada inválida! Por favor, ingrese un número.")
    
    return calificaciones

def calcular_estadisticas(calificaciones):
    """
    Función para calcular estadísticas básicas a partir de las calificaciones.
    Demuestra ejecución secuencial y diseño modular.
    """
    if not calificaciones:  # Estructura de selección
        return None, None, None
    
    # Ejecución secuencial
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    mayor = max(calificaciones)
    menor = min(calificaciones)
    
    return promedio, mayor, menor

def clasificar_calificacion(calificacion):
    """
    Función para clasificar una calificación en una letra.
    Demuestra estructura de selección con múltiples condiciones.
    """
    # Estructura de selección con múltiples ramas
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80:
        return 'B'
    elif calificacion >= 70:
        return 'C'
    elif calificacion >= 60:
        return 'D'
    else:
        return 'F'

def mostrar_resultados(calificaciones, promedio, mayor, menor):
    """
    Función para mostrar los resultados de manera formateada.
    Demuestra iteración y ejecución secuencial.
    """
    print("\n" + "="*50)
    print("RESULTADOS DEL ANÁLISIS DE CALIFICACIONES")
    print("="*50)
    
    # Ejecución secuencial
    print(f"Total de estudiantes: {len(calificaciones)}")
    print(f"Promedio de calificaciones: {promedio:.2f}")
    print(f"Calificación más alta: {mayor:.1f}")
    print(f"Calificación más baja: {menor:.1f}")
    print(f"Calificación general de la clase: {clasificar_calificacion(promedio)}")
    
    print("\nDistribución de Calificaciones:")
    # Estructura de iteración para contar calificaciones por letra
    conteo_calificaciones = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    for calificacion in calificaciones:  # Iteración
        letra = clasificar_calificacion(calificacion)
        conteo_calificaciones[letra] += 1
    
    # Iteración para mostrar la distribución
    for letra, conteo in conteo_calificaciones.items():
        if conteo > 0:  # Selección
            porcentaje = (conteo / len(calificaciones)) * 100
            print(f"  {letra}: {conteo} estudiantes ({porcentaje:.1f}%)")

def generar_reporte(calificaciones):
    """
    Función para generar un reporte detallado.
    Demuestra estructuras de iteración y selección.
    """
    print("\nREPORTE DETALLADO DE ESTUDIANTES:")
    print("-" * 30)
    
    # Iteración con enumeración
    for i, calificacion in enumerate(calificaciones, 1):
        letra = clasificar_calificacion(calificacion)
        estado = "APROBADO" if calificacion >= 60 else "REPROBADO"  # Selección
        print(f"Estudiante {i}: {calificacion:.1f} ({letra}) - {estado}")

def main():
    """
    Función principal que demuestra el enfoque de programación estructurada de arriba hacia abajo.
    Punto único de entrada con flujo secuencial claro.
    """
    print("Sistema de Análisis de Calificaciones de Estudiantes")
    print("Usando Principios de Programación Estructurada")
    print("-" * 40)
    
    # Ejecución secuencial del flujo principal del programa
    # Paso 1: Recopilar datos
    calificaciones = obtener_calificaciones()
    
    # Paso 2: Validar datos
    if not calificaciones:  # Estructura de selección
        print("No se ingresaron calificaciones. Saliendo del programa.")
        return
    
    # Paso 3: Procesar datos
    promedio, mayor, menor = calcular_estadisticas(calificaciones)
    
    # Paso 4: Mostrar resultados
    mostrar_resultados(calificaciones, promedio, mayor, menor)
    
    # Paso 5: Generar reporte detallado (opcional)
    eleccion_usuario = input("\n¿Generar reporte detallado? (s/n): ").lower()
    if eleccion_usuario == 's':  # Estructura de selección
        generar_reporte(calificaciones)
    
    print("\n¡Programa completado exitosamente!")

# Punto de entrada del programa - demuestra el principio de programación estructurada
# de tener un único punto de entrada principal
if __name__ == "__main__":
    main()
