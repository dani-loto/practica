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

    #OPCIÓN 2: LONDES, INGLATERRA
    if destino == 2:
        print (nombre + " escogiste Londres, Inglaterra")

    #OPCIÓN 3: NEW YORK CITY, USA
    if destino == 3:
        print (nombre + " escogiste New York City, USA")

    #OPCIÓN 4: CIUDAD DE MÉXICO, MÉXICO
    if destino == 4:
        print (nombre + " escogiste CDMX, México")

    #OPCIÓN 5: SAO PABLO, BRASIL
    if destino == 5:
        print (nombre + " escogiste Sao Pablo, Brasil")