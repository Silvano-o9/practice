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
		
		#Aqui se acaba la orden del Arroz he inica la orden del cafe

elif pedido == "Cafe":
 	eleccion = print("Genial, ¿De cuantos mililitros quiere su Cafe?")
 	#Aqui pide de cuantos milímetros quiere el cafe
 	eleccionMC = int(input(f"De {100} ml, {200} ml, {500} ml, o {1000} ml." ))
 	#Aqui le da la opción al usuario para que elija, no tiene que poner "ml",solo con el número basta, o sea, 100. 200. o 500"
 	if eleccionMC == 100:
 		print(f"Muchas gracias por su pedido, el costo del Cafe de {100} ml es de {10} dollars")
 		#Aqui le esta diciendo cuanto cuesta el cafe
 		unidad = int(input("¿Cuantos quiere, 2. 3. ? "))
 		#Aqui pide cuantos quiere, si es que quiere más de uno, si no es así, solo debe de poner 1.
 		
 		if unidad == 2:
 				print(f"Muchas gracias, el costo de su pedido es de {20} dollars ")
 				dollar = int(input("Por favor, pague aqui "))
 				if dollar == 20:
 					print("Gracias por su compra.")
 					while unidadC < unidad:
 						print("Cafe 100 ml")
 						unidadC += 1
 						
 					print("Have a perfec day!")
 					#Aqui se acaba el proceso de compra de la unidad 2, en caso de que el usuario elija que quiere 2 cafes.
 					
 		elif unidad == 3:
 				print(f"Muchas gracias, el costo de su pedido es de {30} dollars ")
 				dollar = int(input("Por favor, pague aqui "))
 				if dollar >= 30:
 					print("Muchas gracias por su compra")
 					while unidadC < 3:
 						print("Cafe 100 ml")
 						unidadC += 1
 					print("Have a perfec day.")
 		else:
 			print("Ok, solo se le dará 1 unidad")
 			#Aqui se acaba eleccionMC == 100 (O café de 100 milímetros, he inicia eleccionMC 200 o (Café de 100 milímetros)
 			
 	elif eleccionMC == 200:
 			print(f"Muchas gracias por su pedido, el costo del Cafe de {200} ml es de {25} dollars")
 			unidad = int(input("¿Cuantos quiere, 2. 3. ? "))
 			if unidad == 2:
 				print(f"Muchas gracias por su compra, su pedido es de {50} dollars")
 				dollar = int(input("Por favor, pague aquí "))
 			if dollar >= 50:
 				print("Muchas gracias por su compra")
 				if dollar != 50:
 					print("Ponte a chambear")
 					
 				while unidadC < 2:
 						print("Cafe 100 ml")
 						unidadC += 1
 						print("Have a perfec day.")
 				#Aqui finaliza el proceso de compra de la unidad 2 de la eleccionMC 200 he inicia la unidad 3
 	elif unidad == 3:
 										print(f"Muchas gracias por su compra, el costo de su pedido es de {75} dollars")
 										dollar = int(input("Por favor, pague aquí "))
 			
 	if dollar >= 75:
 				print("Muchas gracias por su compra, su pedido estará en seguida")
 				
 				while unidadC < 3:
 						print("Cafe 200 ml")
 						unidadC += 1
 				print("Have a perfec day.")
 						

 					