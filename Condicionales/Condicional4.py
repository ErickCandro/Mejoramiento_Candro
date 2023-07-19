"""4. Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, 
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores"""

def Notas():
    nota = float(input("Ingrese la nota entre 0 y 10: "))

    if nota < 5:
        print("Bajo")
    elif nota < 6.5:
        print("Basico")
    elif nota < 8.5:
        print("Bien")
    elif nota < 9.5:
        print("Alto")
    else:
        print("Excelente")
        
        
Notas()