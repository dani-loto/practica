nombre = input ("escribe tu nombre ")
print ( " **** Selecciona una opción **** ")
print (nombre + "presiona 1 para traductor de números del 1-10: ingles a español")
print (nombre + "presiona 2 para traductor de colores del 1-10: español a inglés")
print (nombre + "presiona 3 para traductor de números del 1-10: ingles a italiano")
print (nombre + "presiona 4 para traductor de colores del 1-10: italiano a inglés")
print (nombre + "presiona 5 para traductor de números del 1-10: español a francés")
opcion = int(input(" Escribe la opcion que vas a usar "))

#opcion 1 ingles a español
if opcion == 1:
    print ( "*inglés a español*" )
    opcion_uno = (input ("escribe el número del 1-10 que quieres traducir "))
    if opcion_uno == "one":
        print ("La palabra significa UNO")
    elif opcion_uno == "two":
        print ("la palabra significa DOS")
    elif opcion_uno == "three":
        print ("la palabra significa TRES")
    elif opcion_uno == "four":
        print ("la palabra significa CUATRO")
    elif opcion_uno == "five":
        print ("la palabra significa CINCO")
    elif opcion_uno == "six":
        print ("la palabra significa SEIS")
    elif opcion_uno == "seven":
        print ("la palabra significa SIETE")
    elif opcion_uno == "height":
        print ("la palabra significa OCHO")
    elif opcion_uno == "nine":
        print ("la palabra significa NUEVE")
    elif opcion_uno == "ten":
        print ("la palabra significa DIEZ")
    else:
        print("opcion no válida")

#opcion 2: español a inglés
elif opcion == 2:
    print ( "*español a inglés *")
    opcion_uno = input ("escribe un número del 1-10 que quieres traducir ")
    if opcion_uno == "uno":
        print ("La palabra significa ONE")
    elif opcion_uno == "dos":
        print ("la palabra significa TWO")
    elif opcion_uno == "tres":
        print ("la palabra significa THREE")
    elif opcion_uno == "cuatro":
        print ("la palabra significa FOUR")
    elif opcion_uno == "cinco":
        print ("la palabra significa FIVE")
    elif opcion_uno == "seis":
        print ("la palabra significa SIX")
    elif opcion_uno == "siete":
        print ("la palabra significa SEVEN")
    elif opcion_uno == "ocho":
        print ("la palabra significa EIGHT")
    elif opcion_uno == "nueve":
        print ("la palabra significa NINE")
    elif opcion_uno == "diez":
        print ("la palabra significa TEN")
    else:
        print("opcion no válida")

#opcion 3 inglés a italiano
if opcion == 3:
    print ( "*inglés a italiano*" )
    opcion_uno = input ("escribe el número del 1-10 que quieres traducir ")
    if opcion_uno == "one":
        print ("La palabra significa UNO")
    elif opcion_uno == "two":
        print ("la palabra significa DUE")
    elif opcion_uno == "three":
        print ("la palabra significa TRE")
    elif opcion_uno == "four":
        print ("la palabra significa QUATTRO")
    elif opcion_uno == "five":
        print ("la palabra significa CINQUE")
    elif opcion_uno == "six":
        print ("la palabra significa SEI")
    elif opcion_uno == "seven":
        print ("la palabra significa SETTE")
    elif opcion_uno == "height":
        print ("la palabra significa OTTO")
    elif opcion_uno == "nine":
        print ("la palabra significa NOVE")
    elif opcion_uno == "ten":
        print ("la palabra significa DIECI")
    else:
        print("opcion no válida")

#opcion 4 italiano a inglés
if opcion == 4:
    print ( "*italiano a inglés*" )
    opcion_uno = input ("escribe el número del 1-10 que quieres traducir ")
    if opcion_uno == "uno":
        print ("La palabra significa ONE")
    elif opcion_uno == "due":
        print ("la palabra significa TWO")
    elif opcion_uno == "tre":
        print ("la palabra significa THREE")
    elif opcion_uno == "quattro":
        print ("la palabra significa FOUR")
    elif opcion_uno == "cinque":
        print ("la palabra significa FIVE")
    elif opcion_uno == "sei":
        print ("la palabra significa SIX")
    elif opcion_uno == "sette":
        print ("la palabra significa SEVEN")
    elif opcion_uno == "otto":
        print ("la palabra significa EIGHT")
    elif opcion_uno == "nove":
        print ("la palabra significa NINE")
    elif opcion_uno == "di":
        print ("la palabra significa TEN")
    else:
        print("opcion no válida")

#opcion 5 español a francés
elif opcion == 5:
    print ( "*español a francés *")
    opcion_uno = input ("escribe un número del 1-10 que quieres traducir ")
    if opcion_uno == "uno":
        print ("La palabra significa UN")
    elif opcion_uno == "dos":
        print ("la palabra significa DEUX")
    elif opcion_uno == "tres":
        print ("la palabra significa THROIS")
    elif opcion_uno == "cuatro":
        print ("la palabra significa QUATRE")
    elif opcion_uno == "cinco":
        print ("la palabra significa CINQ")
    elif opcion_uno == "seis":
        print ("la palabra significa SIX")
    elif opcion_uno == "siete":
        print ("la palabra significa SEPT")
    elif opcion_uno == "ocho":
        print ("la palabra significa HUIT")
    elif opcion_uno == "nueve":
        print ("la palabra significa NEUF")
    elif opcion_uno == "diez":
        print ("la palabra significa DIX")
    else:
        print("opcion no válida")