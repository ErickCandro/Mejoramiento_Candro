""" 3. Pedir un número entre 0 y 100 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa"""

def NumCifras():
    numero = float(input("Ingrese un número entre 0 y 100: "))
    if numero < 0 or numero > 1000:
        print("El número ingresado está fuera de los límites requeridos.")
    else:
        cifras = 1
        while numero >= 10:
            cifras += 1
            numero //= 10
        print("El número ingresado tiene", cifras, "cifras.")
        
        
NumCifras()