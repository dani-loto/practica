#Cajero
print ("Bienvenido a tu aplicación de banco")
nombre = input ("¿Cuál es tu nombre? ")
password = int (input ("Escribe tu contraseña para acceder "))

ejecutar = True
while ejecutar:

    if password == 7899:

        ejecutar = True
        while ejecutar:
            print ("Haz accedido a tu cuenta, selecciona tu tipo de tarjeta para hacer movimientos ")
            tarjeta = input ("Escribe TC para tarjeta de crédito, escribe TD par débito: ")

            if tarjeta == "TC":
                print ("*** Selecciona una opción de movimiento ***")
                print (nombre + " selecciona 1 para RETIROS") 
                print (nombre + " selecciona 2 para ABONAR")
                print (nombre + " selecciona 3 para PRÉSTAMO")
                print (nombre + " selecciona 4 para CHECAR SALDO")
                print (nombre + " selecciona 5 para TRANSFERENCIAS")
                movimiento1 = int (input ("¿Cuál es el moviviento que harás? "))

            #RETIRO
                if movimiento1 == 1:
                    print ("Escogiste retiretirar de tu cuenta")
                    retiro = int (input ("¿Cuánto dinero deseas retirar? "))

                    if retiro <= 100000:
                        print ("Perfecto, tu retiro fue aprovado, ahora tu saldo es de ",(100000 - retiro))

                    elif retiro> 100000:
                        print ("Lo sentimos, tu retiro supera el saldo en tu cuenta, regresa para probar con una cantidad menor ")

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Gracias por usar tu aplicación bancaria, vueve pronto" )
                        ejecutar = False

            #ABONO
                elif movimiento1 == 2:
                    print ("Escogiste abonar a tu cuenta")
                    abono = int (input ("¿Cuánto dinero deseas abonar? "))
                    print ("Perfecto, tu abono fue aprovado, ahora tu saldo es de ",(100000 + abono))

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Gracias por usar tu aplicación bancaria, vueve pronto" )
                        ejecutar = False

            #PRÉSTAMO
                elif movimiento1 == 3:
                    print ("Escogiste solicitar un préstamo")
                    prestamo = int (input ("¿Cuánto dinero deseas solicitar para tu préstamo? "))
                    if prestamo <= 50000:
                        print ("Tu prestamo ha sido aprovado")

                    elif prestamo > 50000:
                        print ("Tu préstamo ha sido rechazado, prueba con otra cantidad")

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Gracias por usar tu aplicación bancaria, vueve pronto" )
                        ejecutar = False

            #CHECAR SALDO
                elif movimiento1 == 4:
                    print ("Escogiste consultar tu saldo")
                    print ("Tu saldo es de 100000")

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Gracias por usar tu aplicación bancaria, vueve pronto" )
                        ejecutar = False

            #TRANSFERENCIA
                elif movimiento1 == 5:
                    print ("Escogiste hacer una transferencia")
                    transferencia = int (input ("¿Cuánto dinero deseas transferir?"))
                    print ("El total de tu cuenta a apagar es de ", (transferencia * .10) + transferencia )

                    volver = input("¿Deseas volver al menú principal? ")
                    if volver == "Sí":
                        ejecutar = True
                    elif volver == "No":
                        print ("Gracias por usar tu aplicación bancaria, vueve pronto")
                        ejecutar = False

ejecutar = False 
print ("Lo sentimos, contraseña incorrecta")
            