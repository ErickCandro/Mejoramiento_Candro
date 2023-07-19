"""El programa es muy similar al anterior en el sentido que hace lo mismo de buscar si es primo o no
pero en este se le agrega que debe sumar el resultado del proceso anterior y decir si es perfecto o no"""

def mis():
    x=[]
    a= int(input("ingrese un numero por teclado:",))
    contador=0
    suma=0

    for i in range (1, a+1):
        if a % i == 0:
            x.append(i)
            contador=contador+1
            suma=suma+i
    if contador<=2:
        print("Es primo")
    else:
        print("No es primo")
        
    print("Los divisores del numero", a, "Son: ", x)
    print("se puede dividir en:",contador)

    if suma-a == a:
        print("El numero",a, "es perfecto")
    else:
        print("El numero",a, "No es perfecto")
        
mis()