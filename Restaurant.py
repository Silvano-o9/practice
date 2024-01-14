print("Bienveninos a este Restaurante")
dollar = 0
precioAT = 16
precioC100M = 10
precioC200M = 25
precioC500M = 50
precioC1000M = 100
unidadC = 0
pedido = ""
print("Aqui esta el menú: Arroz. Cafe. Carne. Leche. Jugo. Té. Brocoli. Bacalao. Confles. Pescado. Spaghetti. ")

pedido = input("Que desea llevar ")

if pedido == "Arroz":
	eleccion = input("Genial, ¿Quiere una taza o un plato de arroz? ")
	if eleccion == "taza":
		print(f"Genial, su pedido es de {precioAT} dollars ")
	dollar = int(input("Pague aqui: "))
	if dollar == precioAT:
		print("Muchas gracias")

elif pedido == "Cafe":
 	eleccion = print("Genial, ¿De cuantos mililitros quiere su Cafe?")
 	eleccionMC = int(input(f"De {100} ml, {200} ml, {500} ml, o {1000} ml." ))
 	if eleccionMC == 100:
 		print(f"Muchas gracias por su pedido, el costo del Cafe de {100} ml es de {10} dollars")
 		quieremas = input("¿Solo quiere un cafe? hay 5 cafes de 100 ml " )
 		if quieremas == "Yes":
 			unidad = int(input("¿Cuantos quiere, 2. 3. 4. o 5. ? "))
 			if unidad == 2:
 				print(f"Muchas gracias, el costo de su pedido es de {20} dollars ")
 				dollar = int(input("Por favor, pague aqui "))
 				if dollar == 20:
 					print("Gracias por su compra.")
 					while unidadC < unidad:
 						print("Cafe 100 ml")
 						unidadC += 1
 						
 					print("Have a perfec day!")
 					
 			elif unidad == 3:
 				print("Muchas gracias, el costo de su pedido es de 30 dollars ")
 				dollar = int(input("Por favor, pague aqui "))
 				if dollar >= 30:
 					print("Muchas gracias por su compra")
 					while unidadC < 3:
 						print("Cafe 100 ml")
 						unidadC += 1
 					print("Have a perfec day.")