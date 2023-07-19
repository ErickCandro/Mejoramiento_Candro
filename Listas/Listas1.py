"""El siguiente ejercicio llena un arreglo con numeros generados de manera random 
y muestra en pantalla que suma de los numeros es maypr de los dos """

import random 
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

lista1=llenarLista(10,20)
print("La lista 1 es: ",lista1)

lista2=llenarLista(10,20)
print("La lista 2 es: ",lista2)
#funcion para decir cual de los dos numeros de las anteriores listas tiene la suma mayor
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

if lista1>lista2:
    print("la lista uno tiene la suma mayor con un total de:",sumaLista(lista1))
elif lista1==lista2:
    print("la suma de los numeros es igual")
else:
    print("la lista dos tiene la suma mayor con un total de:",sumaLista(lista2))

