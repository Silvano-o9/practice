print("Bienveninos a este Restaurante")
dollar = 0
wow = ""
unidad = 0
eleccionA = ""
precioAT = 16
Tcarne = ""
precioAP = 28
precioC100M = 10
precioC200M = 25
precioC500M = 50
unidadC = 0
selection = ""
pedido = ""
error = "soporte"

TCcarne = ["Bleu", "Inglés", "Termino medio", "Tres cuartos", "Bien Cocido"]
Tcarne = ["Cerdo", "Pollo", ]
TPcarne = ["Alas", "Mulo corto", "Mulo largo", "Pechuga",]

print("Aqui esta el menú: Arroz. Cafe. Carne. Leche. Jugo. Té. Brocoli. Bacalao. Confles. Pescado. Spaghetti. ")

pedido = input("Que desea llevar ")

if pedido == "Arroz":
	eleccionA = input("Genial, ¿Quiere una Taza o un Plato de arroz? ").capitalize()
	
	if eleccionA == "Taza":
		print(f"Genial, su pedido es de {precioAT} dollars ")
		dollar = int(input("Pague aqui: "))
		if dollar == precioAT:
			print("Muchas gracias")
			
			#version plato
			
if eleccionA == "Plato":
			print(f"Genial, su pedido es de {28} dollars ")
			dollar = int(input("Pague aqui: "))
			if dollar >= 28:
				print("Gracias")
		
		#Aqui se acaba la orden del Arroz he inica la orden del cafe

elif pedido == "Cafe":
 	eleccion = print("Genial, ¿De cuantos mililitros quiere su Cafe?")
 	#Aqui pide de cuantos milímetros quiere el cafe
 	eleccionMC = int(input(f"De {100} ml, {200} ml, {500} ml." ))
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
 			print("I'm sorry, la opción no es validad, elija otra, please")
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
 				#Aqui finaliza el proceso de compra de la unidad 2 de la eleccionMC 200 ha inicia la unidad 3
 	elif unidad == 3:
 										print(f"Muchas gracias por su compra, el costo de su pedido es de {75} dollars")
 										dollar = int(input("Por favor, pague aquí "))
 			
 	if dollar >= 75:
 				print("Muchas gracias por su compra, su pedido estará en seguida")
 				
 				while unidadC < 3:
 						print("Cafe 200 ml")
 						unidadC += 1
 				print("Have a perfec day.")
 						
 						# Se acaba eleccionMC = 200 he inica eleccionMC = 500
 						
 	elif eleccionMC == 500:
    	 print(f"Gracias por su pedido, el costo del Café de {500} ml es de {50} dollars")
    	 unidad = int(input(f"¿Cuantos desea? {2}. {3}. o solo {1}. "))
    	 if unidad == 1:
 							print("Una lástima, 2 o 3 hubiera sido mejor, pero lo comprendemos,")
 							print("El precio de su pedido es de {50} dollars")
 							dollar = int(input("Por favor, pague aquí "))
 							if dollar == 50:
 								print("Muchas gracias por su compra de {1} cafe, su pedido se le entregará enseguida")
 								print("1 Café (500ml)")
 							elif dollar > 50:
 								print("Muchas gracias por su compra y su gran gesto al recompensarnos con propina, sin duda le gusto el servicio, le entregaremos su café en seguida")
 								print("1 Café (500ml)")
 							else:
 								print("Hey friend, póngase a trabajar, ande a chambear")
 								
 						#fin de la unidad 1, empieza la 2.
 								   
if unidad == 2:
	wow = input("Vamos, uno más ¿si? y/n ")
	if wow == "y":
		print("Esoo, le daremos +1 totalmente gratis por ser un buen cliente")
		print("El precio de su pedido es de 100 dollars")
		dollar = int(input("Please, pagué aquí "))
		print("Vayase al diablo entonces")
		if dollar == 100:
			print("Gracias por su pedido, pase un buen día")
			while unidadC <= 3:
				print(f"Café ({500})ml")
				unidadC += 1
if wow == "n":
					print("Una pena")
					print("El precio de su pedido es de 100 dollars")
					dollar = int(input("Please, pague aquí "))
					if dollar == 100:
						print("Gracias por su compra")
						while unidadC <= 2:
							print(f"Café ({500})ml")
							unidadC += 1
							print("Pase un lindo día ")
							class Unidad3_3:
								
								error
								
if unidad == 3:
									print("Eso es, ni uno ni dos, 3 de una vez,  usted si es un buen bebedor de Café no como esos del 'ay el café le hace daño al corazón' (acto seguido lo ves fumando vape XD")
									print("Dejémonos de cuentos, el precio de su café es de {150} dollars")
									dollar = int(input(f"Como buen bebedor de Café, le daremos una rebaja de {20} dollars,  asi que, puede pagar {130} dollars,  pero viniendo de usted, seguro que nos da propina: "))
									if dollar < 150:
										
										print("Gracias por hacer efectiva su rebaja por ser un buen cliente, se le quiere mucho")
										while unidadC < 3:
											print(f"Café ({500}) ml")
											unidadC += 1
										
										print("Que pase un maravilloso resto del día, le deseo lo mejor")
									elif dollar  >= 150:
												print("Gracias de todas formas, y se le agradece su propina")
												
												while unidadC < 3:
													print(f"Café ({500}) ml")
													unidadC += 1
												
												print("Pase un lindo día, se le quiere")
												
												#session carne
 
elif pedido == "Carne":
	print("De maravilla, gracias a dios no eres vegano, podrás disfrutar de lo que es SABROSO")
	selection = 	input(f"De que le gustaría su carne: {Tcarne[0]} o {Tcarne[1]} ").capitalize()
	if selection == "Cerdo":
		print("Genial, la carne de cerdo está muy rica últimamente, y, ¿Como le gustaría su corte?")
		for wow in TCcarne:
			print(wow)
	input(": ")

#Arrozcomplet, carne en process, in the next coding, 1r session carne