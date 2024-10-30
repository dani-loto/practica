#Cajero
print ("Bienvenido a este tu cajero de confianza")
nombre = input ("¿Cuál es tu nombre?")

print ("*** selecciona una opción ***")
print (nombre + " selecciona 1 para BBVA") 
print (nombre + " selecciona 2 para Santander")
print (nombre + " selecciona 3 para HSBC")
print (nombre + " selecciona 4 para American Express")
print (nombre + " selecciona 5 para Plata")
banco = int (input ("¿Cuál es tu banco?"))

#Opcion 1
if banco == 1:
    print ("Escogiste BBVA")
    ahorro = int (input ("¿Cuál es tu ahorro?"))
    print ("muy bien " + nombre + " ¿qué operación deseas hacer")

    #opciones
    ejecutar = True
    while ejecutar:
        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 2 para hacer tu retiro")
        print (nombre + " selecciona 3 para hacer un abono")

        opcion =int(input("Escribe la opción que deseas usar "))

        #opcion 1: saldo
        if opcion == 1:
            print ("Tu saldo es de ", ahorro, " mxn")
            
            print ("¿Deseas hacer otra operación?")
            print ("*** selecciona una opción ***")
            print (nombre + " selecciona 2 para hacer un retiro") 
            print (nombre + " selecciona 3 para hacer un abono")
            print (nombre + " selecciona 4 para salir")
            opcion_uno = int (input ("¿Deseas hacer otra operación?"))

            if opcion_uno == 2:
                print ("tendrás que regresar al menu principal")
                ejecutar = True
            elif opcion_uno == 3:
                print ("selecciona 3 para hacer un abono")
                ejecutar = False
            elif opcion_uno == 4:
                print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                ejecutar = False 
            else: print ("opción no válida")

        #opción 2: retiro
        if opcion == 2:
            print ("Tu saldo es de ", ahorro, " mxn")
            retiro = int(input("¿Cuánto deseas retirar?"))
            cambio = ahorro - retiro
            if retiro > ahorro:
                print ("Tu retiro supera tus ahorros, prueba con otra cantidad")
                print ("En tu cuenta te queda:", cambio, " mxn" )

                print ("*** selecciona una opción ***")
                print (nombre + " selecciona 1 para consultar tu saldo") 
                print (nombre + " selecciona 3 para hacer un abono")
                print (nombre + " selecciona 4 para salir")
                opcion_uno = int(input ("¿Deseas hacer otra operación?"))

                if opcion_uno == 1:
                    print ("tendrás que regresar al menu principal")
                    ejecutar = True
                elif opcion_uno == 3:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False
                elif opcion_uno == 4:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False 
                else: print ("opción no válida")

        #opción 3:abono
        if opcion == 3:
            print ("Tu saldo es de ", ahorro, " mxn")
            abono = int(input("¿Cuánto deseas retirar?"))
            total = ahorro + abono
            print ("En tu cuenta te queda:", total, " mxn" )

            print ("*** selecciona una opción ***")
            print (nombre + " selecciona 1 para consultar tu saldo") 
            print (nombre + " selecciona 2 para hacer tu retiro")
            print (nombre + " selecciona 4 para salir")
            opcion_uno = int(input ("¿Deseas hacer otra operación?"))

            if opcion_uno == 1:
                print ("Tendrás que regresar al menu principal")
                ejecutar = True
            elif opcion_uno == 2:
                print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                ejecutar = False
            elif opcion_uno == 4:
                print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                ejecutar = False 
            else: 
                print ("opción no válida")

#Opcion 2
if banco == 2:
    print ("Escogiste Santander")
ahorro = int (input ("¿Cuál es tu ahorro?"))
print ("muy bien " + nombre + " ¿qué operación deseas hacer")

#opciones
ejecutar = True
while ejecutar:
    print ("*** selecciona una opción ***")
    print (nombre + " selecciona 1 para consultar tu saldo") 
    print (nombre + " selecciona 2 para hacer tu retiro")
    print (nombre + " selecciona 3 para hacer un abono")

    opcion =int(input("Escribe la opción que deseas usar "))

    #opcion 1: saldo
    if opcion == 1:
        print ("Tu saldo es de ", ahorro, " mxn")
        
        print ("¿Deseas hacer otra operación?")
        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 2 para hacer un retiro") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int (input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 2:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("selecciona 3 para hacer un abono")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 2: retiro
    if opcion == 2:
        print ("Tu saldo es de ", ahorro, " mxn")
        retiro = int(input("¿Cuánto deseas retirar?"))
        cambio = ahorro - retiro
        print ("En tu cuenta te queda:", cambio, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 3:abono
    if opcion == 3:
        print ("Tu saldo es de ", ahorro, " mxn")
        abono = int(input("¿Cuánto deseas retirar?"))
        total = ahorro + abono
        print ("En tu cuenta te queda:", total, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 2 para hacer tu retiro")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("Tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 2:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: 
            print ("opción no válida")

#Opción 3
if banco == 3:
    print ("Escogiste HSBC")
ahorro = int (input ("¿Cuál es tu ahorro?"))
print ("muy bien " + nombre + " ¿qué operación deseas hacer")

#opciones
ejecutar = True
while ejecutar:
    print ("*** selecciona una opción ***")
    print (nombre + " selecciona 1 para consultar tu saldo") 
    print (nombre + " selecciona 2 para hacer tu retiro")
    print (nombre + " selecciona 3 para hacer un abono")

    opcion =int(input("Escribe la opción que deseas usar "))

    #opcion 1: saldo
    if opcion == 1:
        print ("Tu saldo es de ", ahorro, " mxn")
        
        print ("¿Deseas hacer otra operación?")
        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 2 para hacer un retiro") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int (input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 2:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("selecciona 3 para hacer un abono")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 2: retiro
    if opcion == 2:
        print ("Tu saldo es de ", ahorro, " mxn")
        retiro = int(input("¿Cuánto deseas retirar?"))
        cambio = ahorro - retiro
        print ("En tu cuenta te queda:", cambio, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 3:abono
    if opcion == 3:
        print ("Tu saldo es de ", ahorro, " mxn")
        abono = int(input("¿Cuánto deseas retirar?"))
        total = ahorro + abono
        print ("En tu cuenta te queda:", total, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 2 para hacer tu retiro")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("Tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 2:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: 
            print ("opción no válida")

#Opcion 4
if banco == 4:
    print ("Escogiste Santander")
ahorro = int (input ("¿Cuál es tu ahorro?"))
print ("muy bien " + nombre + " ¿qué operación deseas hacer")

#opciones
ejecutar = True
while ejecutar:
    print ("*** selecciona una opción ***")
    print (nombre + " selecciona 1 para consultar tu saldo") 
    print (nombre + " selecciona 2 para hacer tu retiro")
    print (nombre + " selecciona 3 para hacer un abono")

    opcion =int(input("Escribe la opción que deseas usar "))

    #opcion 1: saldo
    if opcion == 1:
        print ("Tu saldo es de ", ahorro, " mxn")
        
        print ("¿Deseas hacer otra operación?")
        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 2 para hacer un retiro") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int (input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 2:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("selecciona 3 para hacer un abono")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 2: retiro
    if opcion == 2:
        print ("Tu saldo es de ", ahorro, " mxn")
        retiro = int(input("¿Cuánto deseas retirar?"))
        cambio = ahorro - retiro
        print ("En tu cuenta te queda:", cambio, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 3 para hacer un abono")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 3:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: print ("opción no válida")

    #opción 3:abono
    if opcion == 3:
        print ("Tu saldo es de ", ahorro, " mxn")
        abono = int(input("¿Cuánto deseas retirar?"))
        total = ahorro + abono
        print ("En tu cuenta te queda:", total, " mxn" )

        print ("*** selecciona una opción ***")
        print (nombre + " selecciona 1 para consultar tu saldo") 
        print (nombre + " selecciona 2 para hacer tu retiro")
        print (nombre + " selecciona 4 para salir")
        opcion_uno = int(input ("¿Deseas hacer otra operación?"))

        if opcion_uno == 1:
            print ("Tendrás que regresar al menu principal")
            ejecutar = True
        elif opcion_uno == 2:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False
        elif opcion_uno == 4:
            print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
            ejecutar = False 
        else: 
            print ("opción no válida")

#opcion 5
if banco == 5:
    print ("Escogiste Plata")
ahorro = int (input ("¿Cuál es tu ahorro?"))
print ("muy bien " + nombre + " ¿qué operación deseas hacer")

    #opciones
ejecutar = True
while ejecutar:
            print ("*** selecciona una opción ***")
            print (nombre + " selecciona 1 para consultar tu saldo") 
            print (nombre + " selecciona 2 para hacer tu retiro")
            print (nombre + " selecciona 3 para hacer un abono")

            opcion =int(input("Escribe la opción que deseas usar "))

            #opcion 1: saldo
            if opcion == 1:
                print ("Tu saldo es de ", ahorro, " mxn")
                
                print ("¿Deseas hacer otra operación?")
                print ("*** selecciona una opción ***")
                print (nombre + " selecciona 2 para hacer un retiro") 
                print (nombre + " selecciona 3 para hacer un abono")
                print (nombre + " selecciona 4 para salir")
                opcion_uno = int (input ("¿Deseas hacer otra operación?"))

                if opcion_uno == 2:
                    print ("tendrás que regresar al menu principal")
                    ejecutar = True
                elif opcion_uno == 3:
                    print ("selecciona 3 para hacer un abono")
                    ejecutar = False
                elif opcion_uno == 4:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False 
                else: print ("opción no válida")

            #opción 2: retiro
            if opcion == 2:
                print ("Tu saldo es de ", ahorro, " mxn")
                retiro = int(input("¿Cuánto deseas retirar?"))
                cambio = ahorro - retiro
                print ("En tu cuenta te queda:", cambio, " mxn" )

                print ("*** selecciona una opción ***")
                print (nombre + " selecciona 1 para consultar tu saldo") 
                print (nombre + " selecciona 3 para hacer un abono")
                print (nombre + " selecciona 4 para salir")
                opcion_uno = int(input ("¿Deseas hacer otra operación?"))

                if opcion_uno == 1:
                    print ("tendrás que regresar al menu principal")
                    ejecutar = True
                elif opcion_uno == 3:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False
                elif opcion_uno == 4:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False 
                else: print ("opción no válida")

            #opción 3:abono
            if opcion == 3:
                print ("Tu saldo es de ", ahorro, " mxn")
                abono = int(input("¿Cuánto deseas retirar?"))
                total = ahorro + abono
                print ("En tu cuenta te queda:", total, " mxn" )

                print ("*** selecciona una opción ***")
                print (nombre + " selecciona 1 para consultar tu saldo") 
                print (nombre + " selecciona 2 para hacer tu retiro")
                print (nombre + " selecciona 4 para salir")
                opcion_uno = int(input ("¿Deseas hacer otra operación?"))

                if opcion_uno == 1:
                    print ("Tendrás que regresar al menu principal")
                    ejecutar = True
                elif opcion_uno == 2:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False
                elif opcion_uno == 4:
                    print ("Gracias por vitar a tu cajero de confianza, nos vemos luego")
                    ejecutar = False 
                else:
                    print ("opción no válida")