#Programa para comprar boletos
nombre = input ("Escribe tu nombre ")
print (nombre + " bienvenido a tu protal de compra de boletos en la mejor aereolínea")
print ("En esta ocación tenemos una selección limitada de destinos, acontinuación escoge cuál será")

ejecutar = True
while ejecutar:
    #Opciones de destinos
    print ( " **** Selecciona una opción para escoger el destino de tu vuelo **** ")
    print ("Destino 1: MADRID, ESP")
    print ("Destino 2: LONDES, ING")
    print ("Destino 3: NYC, USA")
    print ("Destino 4: CDMX, MEX")
    print ("Destino 5: SAO PABLO, BRA")
    destino = int(input("Escribe la opcion que vas a usar "))
   
    #OPCIÓN 1: MADRID, ESPAÑA
    if destino == 1:
        print (nombre + " escogiste Madrid, España")
        clase = input("¿Deseas viajar en clase turista o primera clase? ")

        #Clase turista
        if clase == "clase turista":
            print ("Escogiste viajar en clase turista")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10- boletos
            costo = inventario * 12000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $1500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total1 = Num * 1500 + costo
                    print ("El total de tu compra es de", total1)

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total1 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")
                    ejecutar = False

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

        elif clase == "primera clase":
            print ("Escogiste viajar en primera clase")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10 - boletos
            costo = inventario * 26000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $2500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total2 = Num * 2500 + costo
                    print ("El total de tu compra es de", total2)

                    volver = int(input("¿Deseas volver al menú principal? "))
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total2 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False
                
    #OPCIÓN 2: LONDES, INGLATERRA
    if destino == 2:
        print (nombre + " escogiste Londres, Inglaterra")
        clase = input("¿Deseas viajar en clase turista o primera clase? ")

        #Clase turista
        if clase == "clase turista":
            print ("Escogiste viajar en clase turista")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10- boletos
            costo = inventario * 12000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $1500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total1 = Num * 1500 + costo
                    print ("El total de tu compra es de", total1)

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total1 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")
                    ejecutar = False

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

        elif clase == "primera clase":
            print ("Escogiste viajar en primera clase")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10 - boletos
            costo = inventario * 26000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $2500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total2 = Num * 2500 + costo
                    print ("El total de tu compra es de", total2)

                    volver = int(input("¿Deseas volver al menú principal? "))
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total2 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

    #OPCIÓN 3: NEW YORK CITY, USA
    if destino == 3:
        print (nombre + " escogiste New York City, USA")
        clase = input("¿Deseas viajar en clase turista o primera clase? ")

        #Clase turista
        if clase == "clase turista":
            print ("Escogiste viajar en clase turista")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10- boletos
            costo = inventario * 12000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $1500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total1 = Num * 1500 + costo
                    print ("El total de tu compra es de", total1)

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total1 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")
                    ejecutar = False

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

        elif clase == "primera clase":
            print ("Escogiste viajar en primera clase")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10 - boletos
            costo = inventario * 26000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $2500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total2 = Num * 2500 + costo
                    print ("El total de tu compra es de", total2)

                    volver = int(input("¿Deseas volver al menú principal? "))
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total2 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

    #OPCIÓN 4: CIUDAD DE MÉXICO, MÉXICO
    if destino == 4:
        print (nombre + " escogiste CDMX, México")
        clase = input("¿Deseas viajar en clase turista o primera clase? ")

        #Clase turista
        if clase == "clase turista":
            print ("Escogiste viajar en clase turista")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10- boletos
            costo = inventario * 12000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $1500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total1 = Num * 1500 + costo
                    print ("El total de tu compra es de", total1)

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total1 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")
                    ejecutar = False

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

        elif clase == "primera clase":
            print ("Escogiste viajar en primera clase")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10 - boletos
            costo = inventario * 26000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $2500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total2 = Num * 2500 + costo
                    print ("El total de tu compra es de", total2)

                    volver = int(input("¿Deseas volver al menú principal? "))
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total2 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

    #OPCIÓN 5: SAO PABLO, BRASIL
    if destino == 5:
        print (nombre + " escogiste Sao Pablo, Brasil")
        clase = input("¿Deseas viajar en clase turista o primera clase? ")

        #Clase turista
        if clase == "clase turista":
            print ("Escogiste viajar en clase turista")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10- boletos
            costo = inventario * 12000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $1500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total1 = Num * 1500 + costo
                    print ("El total de tu compra es de", total1)

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total1 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")
                    ejecutar = False

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False

        elif clase == "primera clase":
            print ("Escogiste viajar en primera clase")
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            inventario = 10 - boletos
            costo = inventario * 26000

            if inventario < 10:
                maletas = input("Recuerda que tienes derecho a una maleta de mano y no debe exceder de 56 x 36 x 23 cm (22 x 14 x 9 pulgadas) y debe caber en el medidor de equipaje del aeropuerto ¿Deseas documentar tu equipaje? ")
                
                if maletas == "Si":
                    print ("Cada maleta docuemntada tiene un costo de $2500")
                    Num = int (input("¿Cuántas maletas deseas documentar? "))
                    total2 = Num * 2500 + costo
                    print ("El total de tu compra es de", total2)

                    volver = int(input("¿Deseas volver al menú principal? "))
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Entonces tu total es de ", total2 )
                        ejecutar = False

                elif maletas == "No":
                    print ("Ok, recuerda que aún tienes tu maleta de mano")

            elif inventario > 10:
                print ("Lo sentimos, no te podemos vender esa cantidad de boletos")
                ejecutar = False