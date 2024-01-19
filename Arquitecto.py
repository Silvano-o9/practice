area = 0
base = 0
altura = 0
costo = 0

base = int(input("Dame el valor de la base "))
altura = int(input("Dame el valor de la altura "))

class Rectangulo:
	 global area
	 area = base * altura
	 print(f"El area del terreno es de: {area} metros cuadrados")

	
class Costo:
 costo = area * 2500
 print("El costo a pagar por el terreno es de $" + str(costo))