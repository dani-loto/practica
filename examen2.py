#Sistema de ventascomp

print ("Bienvenido a tiendita de confianza")
nombre = input ("¿Cuál es tu nombre? ")

ejecutar = True
while ejecutar:
    print ("*** selecciona una opción para la categoría de tu compra ***")
    print (nombre + " selecciona 1 para LIMPIEZA") 
    print ("selecciona 2 para COMIDA Y BEBIDAS")
    print ("selecciona 3 para PAGO DE SERVICIO DE LUZ, AGUA O GAS")
    categoria = int (input ("¿Cuál sería la opción que vas a usar? "))


    #Opcion 1 ABARROTES
    if categoria == 1:
        print ("Escogiste LIMPIEZA")
        print ("*** selecciona una opción para el producto que quieres comprar ***")
        print (nombre + " selecciona 1 para JABÓN LÍQUIDO") 
        print ("selecciona 2 para JABÓN EN POLVO")
        print ("selecciona 3 para ESCOBAS")
        categoria2 = int (input ("¿Cuál sería la opción que vas a usar? "))

        #Categoría 1: JABÓN LÍQUIDO
        if categoria2 == 1:
            print ("Escogiste jabón líquido")
            compra_JL = int(input("¿Cuántos litros vas a comprar? "))
            inventario_1 = 100 - compra_JL
            total1= compra_JL * 20
            if inventario_1 < 100:
                print ("Super, el total por ", compra_JL , "litros seria de", total1, "pesos")
                ejecutar = True

            elif inventario_1 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad") 
                ejecutar = True

        #Categoría 2: JABÓN EN POLVO
        if categoria2 == 2:
            print ("Escogiste jabón en polvo")
            compra_JP = int(input("¿Cuántos kilos vas a comprar? "))
            inventario_1 = 100 - compra_JP
            total2 = compra_JL * 18
            if inventario_1 < 100:
                print ("Super, el total por ", compra_JP , "litros seria de", total2, "pesos")
                ejecutar = True

            elif inventario_1 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad")
                ejecutar = True

    #Categoría 3: ESCOBAS
        if categoria2 == 3:
            print ("Escogiste escobas")
            compra_E = int(input("¿Cuántas escobas vas a comprar? "))
            inventario_1 = 100 - compra_E
            compra3 = compra_E * 50
            if inventario_1 < 100:
                print ("Super, el total por ", compra_E , "litros seria de", compra3, "pesos")
                ejecutar = True

            elif inventario_1 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad")
                ejecutar = False

        #Categoría 4: NO HAY ESA OPCIÓN
        else:
            print ("Lo sentimos, no hay esa opción en esta categoría, prueba regresando al menú principal")
            ejecutar = True

    #Opción 2: COMIDA Y BEBIDAS
    elif categoria == 2:
        print ("Escogiste COMIDA Y BEBIDAS")
        print ("*** selecciona una opción para el producto que quieres comprar ***")
        print (nombre + " selecciona 1 para PAPAS FRITAS") 
        print ("selecciona 2 para REFRESCO")
        print ("selecciona 3 para DULCERÍA")
        categoria2 = int (input ("¿Cuál sería la opción que vas a usar? "))

        #Categoría 1: PAPAS FRITAS
        if categoria2 == 1:
            print ("Escogiste papas fritas")

            papas = int (input ("¿Cuántos kilos de papas vas a querer?"))
            inventario_2 = 100 - papas
            compra4 = papas * 15
            if inventario_2 < 100:
                print ("Super, el total por ", papas , "kilos seria de", compra4, "pesos")
                ejecutar = True

            elif inventario_2 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad")
                ejecutar = True

        #Categoría 2: REFRESCO
        elif categoria2 == 2:
            print ("Escogiste refresco")
            refresco = int(input("¿Cuántos litros vas a comprar? "))
            inventario_3 = 100 - refresco
            compra5 = refresco * 23
            if inventario_3 < 100:
                print ("Super, el total por ", refresco , "litros seria de", compra5, "pesos")
                ejecutar = True

            elif inventario_3 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad")
                ejecutar = True

    #Categoría 3: DULCERÍA
        elif categoria2 == 3:
            print ("Escogiste dulcería")
            dulces = int(input("¿Cuántos kilos de dulces vas a querer? "))
            inventario_4 = 100 - dulces
            compra6 = dulces * 16
            if inventario_4 < 100:
                print ("Super, el total por ", dulces , "kilos seria de", compra6, "pesos")
                ejecutar = True

            elif inventario_4 > 100:
                print ("Tu compra supera nuestro inventario, prueba con otra cantidad")
                ejecutar = True

        #Categoría 4: NO HAY ESA OPCIÓN
        else:
            print ("Lo sentimos, no hay esa opción en esta categoría, prueba regresando al menú principal")
            ejecutar = True

    #Opción 3: PAGO DE SERVICIOS DE LUZ, AGUA O GAS
    elif categoria == 3:
        print ("Escogiste el pago de tus servicios de luz, agua y/o gas")
        print ("*** selecciona una opción para la categoría para realizar tu pago ***")
        print ("selecciona 1 para el pago de la LUZ") 
        print ("selecciona 2 para el pago del AGUA")
        print ("selecciona 3 para el pago del GAS")
        categoria_pagos = int (input ("¿Cuál sería la opción que vas a usar? "))

        #Categoría 1: LUZ
        if categoria_pagos == 1:
            print ("Escogiste pagar tu servicio de luz, tienes que pagar $450")
            metodo = input("¿Cuál sería tu método de pago, en efectivo o tarjeta? ")

            if metodo == "efectivo":
                pago = int (input("En este caso solo se aceptan billetes ¿Con qué billete vas a pagar? "))
                cambio = pago - 450

                if cambio < pago:
                    print ("Tu cambio es de ", cambio, "pesos, gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif cambio > pago:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo otro billete")
                    ejecutar = True

            elif metodo == "tarjeta":
                fondos = int (input ("¿Cuál es tu fondo en tu tarjeta?"))
                cambio = fondos - 450

                if fondos < cambio:
                    print ("Muchas gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif fondos > cambio:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo más fondos en tu cuenta")
                    ejecutar = True

        #Categoría 2: AGUA
        if categoria_pagos == 2:
            ("Escogiste pagar tu servicio de agua, tienes que pagar $320")
            metodo2 = input("¿Cuál sería tu método de pago, en efectivo o tarjeta? ")

            if metodo2 == "efectivo":
                pago = int (input("En este caso solo se aceptan billetes ¿Con qué billete vas a pagar? "))
                cambio = pago - 320

                if cambio < pago:
                    print ("Tu cambio es de ", cambio, "pesos, gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif cambio > pago:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo otro billete")
                    ejecutar = True

            elif metodo == "tarjeta":
                fondos = int (input ("¿Cuál es tu fondo en tu tarjeta?"))
                cambio = fondos - 320

                if fondos < cambio:
                    print ("Muchas gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif fondos > cambio:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo más fondos en tu cuenta")
                    ejecutar = False

        #Categoría 3: GAS
        if categoria_pagos == 3:
            ("Escogiste pagar tu servicio de agua, tienes que pagar $320")
            metodo2 = input("¿Cuál sería tu método de pago, en efectivo o tarjeta? ")

            if metodo2 == "efectivo":
                pago = int (input("En este caso solo se aceptan billetes ¿Con qué billete vas a pagar? "))
                cambio = pago - 420

                if cambio < pago:
                    print ("Tu cambio es de ", cambio, "pesos, gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif cambio > pago:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo otro billete")
                    ejecutar = False

            elif metodo == "tarjeta":
                fondos = int (input ("¿Cuál es tu fondo en tu tarjeta?"))
                cambio = fondos - 420

                if fondos < cambio:
                    print ("Muchas gracias por pagar tu servicios en tu tiendita de confianza")
                    ejecutar = True

                elif fondos > cambio:
                    print ("Lo sentimos, tu pago no es suficiente para pagar tu servicio, prueba poniendo más fondos en tu cuenta")
                    ejecutar = False

    else:
        print ("Lo sentimos, esa opción no esta disponible")
        ejecutar = False

total_de_compra =  (" EL total de tu comra es de", total1 + total2 + compra3 + compra4 + compra5 + compra6, "pesos, gracias por tu compra")
