"""El siguiente programa esta diseñado para que el usuario ingrese un numero por teclado y el programa 
lo que debera hacer es buscar cuales son sus multiplos y mostrar en pantalla el total de la cantidad de multiplos que tiene"""

def multiplo():
    y=[]
    z= int(input("ingrese un numero por teclado:",))
    contador=0
    for i in range (1, z+1):
        if z % i == 0:
            y.append(i)
            contador=contador+1
    if contador<=2:
        print("Es primo")
    else:
        print("No es primo")
        
    print("Los divisores del numero", z, "Son: ", y)
    print(contador)

multiplo()