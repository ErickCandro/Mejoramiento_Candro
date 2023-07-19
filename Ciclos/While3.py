"""El siguiente programa esta diseñado para que le usuario ingrese un numero
cualquiera y el programa debera decirle que numero nesecita para superar el numero
ingresado"""

def num():
    maximo = int(input("Introduce un número máximo: "))
    suma = 0
    n = 1
    while suma <= maximo:
        suma=suma+n
        n+=1
    print("El número natural más pequeño necesario para superar el máximo es:", n-1)
num()