"""El siguiente programa es un diccionario el cual muestra en pantalla una serie de resultados especificos
tales cuales como una suma,resta,multiplicacion y una division el cual lo hace con numeros random cada vez que se 
ejecute"""
import random 

def s(a, b):
    return a + b

def r(a, b):
    return a - b

def m(a, b):
    return a * b

def d(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: división entre cero")
        return None

# Crear el diccionario con funciones
diccionario = {
    'suma': s,
    'resta': r,
    'multiplicacion': m,
    'division': d
}

# Utilizar las funciones del diccionario
resultado_s = diccionario['suma'](int(random.randint (1,3)), int(random.randrange(100)))
resultado_r = diccionario['resta'](int(random.randint (1,3)), int(random.randrange(100)))
resultado_m = diccionario['multiplicacion'](int(random.randint (1,3)), int(random.randrange(100)))
resultado_d = diccionario['division'](int(random.randint (1,3)), int(random.randrange(100)))

# Imprimir los resultados
print("Resultado suma:", resultado_s)
print("Resultado resta:", resultado_r)
print("Resultado multiplicación:", resultado_m)
print("Resultado división:", resultado_d)