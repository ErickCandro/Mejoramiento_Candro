"""1. Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el 
valor del medio es 11. No use operadores lógicos"""

def Medio():
    l1=[]
    n1= int(input("Ingrese el primer numero: "))
    l1.append(n1)
    n2= int (input ("Ingrese el segundo numero: "))
    l1.append(n2)
    n3= int (input (" Ingrese el tercer numero: "))
    l1.append(n3)

    if n1 < n2:
        if n2 < n3:
            medio = n2
        elif n1 < n3:
            medio = n3
        else:
            medio = n1
    else:
        if n1 < n3:
            medio = n1
        elif n2 < n3:
            medio = n3
        else:
            medio = n2
            
    print (l1)      
    print ("El valor del medio es: ", medio)
    
Medio()
