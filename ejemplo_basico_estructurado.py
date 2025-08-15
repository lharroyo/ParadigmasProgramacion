"""
Ejemplo Básico de Programación Estructurada
===========================================

Este programa realiza una operación simple: calcular el área de un rectángulo.
Demuestra los principios básicos de la programación estructurada:
1. Ejecución secuencial
2. Uso de funciones para modularidad
3. Entrada y salida de datos
"""

def obtener_datos():
    """
    Función para obtener la base y la altura del rectángulo desde el usuario.
    """
    print("Cálculo del Área de un Rectángulo")
    print("Ingrese los valores en unidades (por ejemplo, cm, m, etc.)")
    
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    
    return base, altura

def calcular_area(base, altura):
    """
    Función para calcular el área del rectángulo.
    """
    return base * altura

def mostrar_resultado(base, altura, area):
    """
    Función para mostrar el resultado del cálculo.
    """
    print("\nRESULTADO")
    print(f"Base: {base} unidades")
    print(f"Altura: {altura} unidades")
    print(f"Área: {area} unidades cuadradas")

def main():
    """
    Función principal que coordina el flujo del programa.
    """
    # Paso 1: Obtener datos
    base, altura = obtener_datos()
    
    # Paso 2: Calcular el área
    area = calcular_area(base, altura)
    
    # Paso 3: Mostrar el resultado
    mostrar_resultado(base, altura, area)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
