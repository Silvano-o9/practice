print("Bienvenidos a Restaurant's")
dollar = 0

wow = ""
unidad = 0
eleccionA = ""
precioAT = 16
precioAP = 28
precioC100M = 10
precioC200M = 25
precioC500M = 50
unidadC = 0
of_in = ""
selection = ""
pedido = ""
error = "support"

def session_buy():
	xc = 1
	dollaR = 0
	print(f"Good buy, el precio de su pedido {TCcarne[0]} es de {35} RES")
	dollaR = int(input("Please,  pague aquí su pedido: "))
	if dollaR >= 35:
		print("Muchas gracias por su compra")
		while xc <= 1:
			print(TCcarne[0])
			print("Have a perfect day")
			xc += 1




def process_tobuy(item, precio, session):
	x = 0
	money = 0
	print(f"Muy buen gusto, su pedido: {item} es de ${precio} RES ")
	print(f"¿Cuantas unidades deseas {UNIDADES}")
	universal = int(input(":"))
	if universal == 1:
		print(f"El precio de su pedido es de ${precio * universal}")
		money = int(input("Please,  page aqui su pedido: "))
		if money == precio * universal:
		    	for x in range(universal):
		    		print(f"Pedido: Unidad: {session}, {item} ${precio}")
	elif universal == 2:
		print(f"El precio de su pedido es de ${precio * universal}")
		money = int(input("Please,  page aqui su pedido: "))
		if money == precio * universal:
		    	for x in range(universal):
		    		print(f"Pedido: Unidad: {session}, {item} ${precio}")
			
	elif universal == 3:
		print(f"El precio de su pedido es de ${precio * universal}")
		money = int(input("Please,  page aqui su pedido: "))
		if money == precio * universal:
		    	for x in range(universal):
		    		print(f"Pedido: Unidad: {session}, {item} ${precio}")


	print("Have a nice day")
		    
					
TCcarne = ["Bleu", "Inglés", "Termino medio", "Tres cuartos", "Bien Cocido"]
Tcarne = ["Cerdo", "Pollo", ]
TPcarne = ["Alas", "Mulo corto", "Mulo largo", "Pechuga",]

Tp_alas = ["Alas picantes", "Alas barbacoa", "Alas teriyaki", "Alas a la parrilla con miel", "Alas estilo bufalo"]


UNIDADES = (1, 2, 3)

## INICIA LA CLASE BUY TIP

class buy_tip:
    money = 0
    unidades = (1, 2, 3, 4, 5, 6, 7)
    selec_unid = 0
    selection = ""
    
    
    def tobuy_tip(self, tip, price, section, sub):
        print(f"Tiene buen gusto, su pedido: {tip} tiene un precio de: {price} ")
        print("¿Cuantas unidades desea?" + str(self.unidades))
        self.selec_unid = int(input(": "))
       
       
        
        if self.selec_unid == 1:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
        
        elif self.selec_unid == 2:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
        elif self.selec_unid == 3:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
        elif self.selec_unid == 4:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
        elif self.selec_unid == 5:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
        elif self.selec_unid == 6:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
        elif self.selec_unid == 7:
            print(f"Espero y le encante el servicio,  su pedido {tip}x{self.selec_unid}, tiene un precio de ${price * self.selec_unid} RES")
            self.money = int(input("Por favor, pague aquí su pedido: "))
            if self.money == price * self.selec_unid:
                print(f"Pedido: Unidad: {section}, Session: {sub}, Part {tip}, Price: ${price * self.selec_unid} RES, Unidades: {self.selec_unid}")
                print("Thanks, have a perfec day")
                
tip_buy = buy_tip()                
                          
                
## FINALIZA CLASE BUY TIP        
                

Menú = ["Cafe", "Arroz", "Carne", "Leche", "Jugo", "Té", "Brocoli", "Bacalao", "Pescado", "Spaghetti"]

print("Aqui esta el menú:")
for wow in Menú:
    print(wow)


pedido = input("Que desea llevar ").capitalize()

if pedido == "Arroz":
	eleccionA = input("Genial, ¿Quiere una Taza o un Plato de arroz? ").capitalize()
	
	if eleccionA == "Taza":
		print(f"Genial, su pedido es de {precioAT} RES ")
		dollar = int(input("Pague aqui: "))
		if dollar == precioAT:
			print("Muchas gracias")
			
			#version plato
			
if eleccionA == "Plato":
			print(f"Genial, su pedido es de {28} RES ")
			dollar = int(input("Pague aqui: "))
			if dollar >= 28:
				print("Gracias")
		
		#Aqui se acaba la orden de la l Arroz he inica la orden del cafe

elif pedido == "Cafe":
 	eleccion = print("Genial, ¿De cuantos mililitros quiere su Cafe?")
 	
 	#Aqui pide de cuantos milímetros quiere el cafe
 	
 	eleccionMC = int(input(f"De {100} ml, {200} ml, {500} ml." ))
 	
 	#Aqui le da la opción al usuario para que elija, no tiene que poner "ml",solo con el número basta, o sea, 100. 200. o 500"
 	
 	if eleccionMC == 100:
 		print(f"Muchas gracias por su pedido, el costo del Cafe de {100} ml es de {10} RES")
 		unidad = int(input("¿Cuantos quiere, 2. 3. ? "))

 		
 		if unidad == 2:
 				print(f"Muchas gracias, el costo de su pedido es de {20} RES ")
 				dollar = int(input("Por favor, pague aqui "))
 				if dollar == 20:
 					print("Gracias por su compra.")
 					while unidadC < unidad:
 						print("Cafe 100 ml")
 						unidadC += 1
 						
 					print("Have a perfec day!")
 					#Aqui se acaba el proceso de compra de la unidad 2, en caso de que el usuario elija que quiere 2 cafes.
 					
 		elif unidad == 3:
 				print(f"Muchas gracias, el costo de su pedido es de {30} RES ")
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
 			print(f"Muchas gracias por su pedido, el costo del Cafe de {200} ml es de {25} RES")
 			unidad = int(input("¿Cuantos quiere, 2. 3. ? "))
 			if unidad == 2:
 				print(f"Muchas gracias por su compra, su pedido es de {50} RES")
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
 										print(f"Muchas gracias por su compra, el costo de su pedido es de {75} RES")
 										dollar = int(input("Por favor, pague aquí "))
 			
 	if dollar >= 75:
 				print("Muchas gracias por su compra, su pedido estará en seguida")
 				
 				while unidadC < 3:
 						print("Cafe 200 ml")
 						unidadC += 1
 				print("Have a perfec day.")
 						
 						# Se acaba eleccionMC = 200 he inica eleccionMC = 500
 						
 	elif eleccionMC == 500:
    	 print(f"Gracias por su pedido, el costo del Café de {500} ml es de {50} RES")
    	 unidad = int(input(f"¿Cuantos desea? {2}. {3}. o solo {1}. "))
    	 if unidad == 1:
 							print("Una lástima, 2 o 3 hubiera sido mejor, pero lo comprendemos,")
 							print("El precio de su pedido es de {50} RES")
 							dollar = int(input("Por favor, pague aquí "))
 							if dollar == 50:
 								print("Muchas gracias por su compra de {1} cafe, su pedido se le entregará enseguida")
 								print("1 Café (500ml)")
 							elif dollar > 50:
 								print("Muchas gracias por su compra y su gran gesto al recompensarnos con propina, sin duda le gusto el servicio, le entregaremos su café en seguida")
 								print("1 Café (500ml)")
 							else:
 								print("Hey friend, póngase a trabajar, ande a chambear")
 								
 #FIN UNIDAD 1, STAR UNIDAD 2
 								   
if unidad == 2:
	wow = input("Vamos, uno más ¿si? y/n ")
	if wow == "y":
		print("Esoo, le daremos +1 totalmente gratis por ser un buen cliente")
		print("El precio de su pedido es de 100 RES")
		dollar = int(input("Please, pagué aquí "))
		print("Vayase al diablo entonces")
		if dollar == 100:
			print("Gracias por su pedido, pase un buen día")
			while unidadC <= 3:
				print(f"Café ({500}ml)")
				unidadC += 1
if wow == "n":
					print("Una pena")
					print("El precio de su pedido es de 100 RES")
					dollar = int(input("Please, pague aquí "))
					if dollar == 100:
						print("Gracias por su compra")
						while unidadC <= 2:
							print(f"Café ({500}ml)")
							unidadC += 1
							print("Pase un lindo día ")
							class Unidad3_3:
								
								error
								
if unidad == 3:
									print("Eso es, ni uno ni dos, 3 de una vez,  usted si es un buen bebedor de Café no como esos del 'ay el café le hace daño al corazón' (acto seguido lo ves fumando vape XD")
									print(f"Dejémonos de cuentos, el precio de su café es de {150} RES")
									dollar = int(input(f"Como buen bebedor de Café, le daremos una rebaja de {20} RES,  asi que, puede pagar {130} RES,  pero viniendo de usted, seguro que nos da propina: "))
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
												
#SESION CARNE
 
elif pedido == "Carne":
	print("De maravilla, gracias a dios no eres vegano, podrás disfrutar de lo que es SABROSO")
	selection = input(f"De que le gustaría su carne: {Tcarne[0]} o {Tcarne[1]} ").capitalize()
	if selection == "Cerdo":
		print("Genial, la carne de cerdo está muy rica últimamente, y, ¿Como le gustaría su corte?")
		for wow in TCcarne:	    
		    print(wow)
		of_in = input(": ").capitalize()
		if of_in == "Bleu":
		    session_buy()	
		elif of_in == "Ingles":
		    process_tobuy(TCcarne[1], 75, Menú[2])
		elif of_in == "Termino medio":
		    process_tobuy(TCcarne[2], 125, Menú[2])
		elif of_in == "Tres cuartos":
		    process_tobuy(TCcarne[3], 165, Menú[2])
		elif of_in == "Bien cocido":
		    process_tobuy(TCcarne[4], 185, Menú[2])
#SESION POLLO				
	if selection == "Pollo":    
            print("Lo mejor de lo mejor, la carne de pollo")
            print("¿Que parte le gustaría?")
            for wow in TPcarne:
                print(wow)                
            of_in = input(": ").capitalize()
#PART-ALAS                
            if of_in == "Alas":
                print("¿Como les gustarían sus alas?")
                for wow in Tp_alas:
                    print(wow)
                                    
                selection_tip = input(": ").capitalize()
                
                if selection_tip == "Alas picantes":
                    tip_buy.tobuy_tip(Tp_alas[0], 7, Menú[2], Tcarne[1])
                elif selection_tip == Tp_alas[1]:
                    tip_buy.tobuy_tip(Tp_alas[1], 10, Menú[2], Tcarne[1])
                elif selection_tip == Tp_alas[2]:
                    tip_buy.tobuy_tip(Tp_alas[2], 13, Menú[2], Tcarne[1])
                elif selection_tip == Tp_alas[3]:
                    tip_buy.tobuy_tip(Tp_alas[3], 15, Menú[2], Tcarne[1])
                elif selection_tip == Tp_alas[4]:
                    tip_buy.tobuy_tip(Tp_alas[4], 19, Menú[2], Tcarne[1])
                
                
	                
	            
	            	            