"""El siguiente programa esta dise;ado para llenar un arreglo con
datos ingresados por el usuario el cual lo llenara indefinidamente
asta que el usuario ponga un numero negativo arrojando un error o ponga
un cero"""

def max():
    num=[]
    maximo = 0
    n = 1
    while n > 0:
        n = int(input("Introduce un número positivo: "))
        if n > 0:
            num.append(n)
        else:
            print("es un numero negativo")
        if n > maximo:
            maximo = n
    s=len(num)
    for i in range(s-1):
        for j in range (s-i-1):
             if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]

    print("lista ordenada de menor a mayor" ,num)
    print("El máximo número introducido es:", maximo)
    
    
max()