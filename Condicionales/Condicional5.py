"""5.Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 200 pesos y cada minuto adicional 
cuesta 50 pesos. Escriba un programa que permita calcular el costo de una llamada dados los minutos de duración."""

def Telefonia():
    min= int(input ("¿Cuantos minutos duro la llamada? (Numero entero): "))
    if min > 3:
        adicionales= min - 3 
        cobroadicional= adicionales*50
        total= cobroadicional + 200
        print ("Debe pagar ", total, "pesos")
    if min == 3:
        print ("Fue un banderazo, debe pagar 200 pesos ")
        
Telefonia()