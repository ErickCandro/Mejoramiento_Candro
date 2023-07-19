"""2. El programa esta dise;ado para que pida tres números y que escriba si son los tres
iguales, si hay dos iguales o si son los tres distintos"""


def NumIguales():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    if num1 == num2 and num1 == num3:
        print("Los tres números son iguales")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Hay dos números iguales")
    else:
        print("Los tres números son distintos")
        
NumIguales()