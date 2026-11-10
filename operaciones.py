
# operaciones.py

def saludar_estudiante(nombre):
    """Función que recibe un nombre e imprime un saludo."""
    print(F"¡Hola {nombre}! Bienvenido al taller de programación.")

def sumar(a, b):
    """Función que retorna la suma de dos números."""
    resultado = a + b
    return resultado

def calcular_promedio(nota1, nota2, nota3):
    """Calcula y retorna el promedio de tres notas."""
    # TU CÓDIGO AQUÍ:
    # 1. Suma las tres notas y divídelas entre 3.
    promedio = (nota1 + nota2 + nota3)/3 

    # 2. Retorna el resultado obtenido.
    return promedio 


def es_par(numero):
    """Retorna True si el número es par, o False si es impar."""
    # TU CÓDIGO AQUÍ:
    

    # Pista: Utiliza el operador módulo (%) -> numero % 2 == 0}
    if numero % 2 == 0 :
        print("true")
        return ("tu resultado es verdadero")
    else:
        print("false")
        return ("tu resultado es falso ")


    