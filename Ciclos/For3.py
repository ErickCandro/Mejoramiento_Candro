import random 

def maximo():
    #se crea la primera lista con numeros random
    suma=0
    suma1=0
    lista=[]
    tam= int(random.randint (10,15))
    for x in range (tam):
        num= int(random.randrange(100))
        lista.append(num)
        suma+=num

    #se crea la segunda lista con numeros random
    list=[]
    tamaño= int(random.randint (10,15))
    for i in range (tamaño):
        num= int(random.randrange(100))
        list.append(num)
        suma1+=num

    print("los numeros son ",lista)
    print("los numeros son ",list)
    print("la suma de la primera lista es:",suma)
    print("la suma de la segunda lista es:",suma1)
    
maximo()