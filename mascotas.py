#Código para conocer datos sobre tu mascota
nombre = input ("escribe tu nombre ")
print ( " **** Selecciona una opción para conocer más datos de tu mascotas **** ")
print (nombre + " presiona 1 para perro")
print (" presiona 2 para conocer datos sobre tu gato")
opcion = int(input(" Escribe la opcion que vas a usar "))

#opción 1: perro
if opcion == 1:
    print ("El perro es la mascota más común, superando al gato y al pez")
    opcion_uno = (input ("Ahora, escribe la raza de tu perro "))

    #LABRADOR
    if opcion_uno == "labrador":
        print ("Esta raza es la más frecuente entre los dueños de perros")

        opcion_uno = (input ("Escribe el nombre de tu perro "))
        if opcion_uno == "Luna":
            print ("El nombre de tu perro es el más usual")
        elif opcion_uno == "Coco":
            print ("El nombre de tu perro es el segundo más usual")
        elif opcion_uno == "Nala":
            print ("El nombre de tu perro es el tercero más usual")
        elif opcion_uno == "Kira":
            print ("El nombre de tu perro es el cuarto más ususal")
        elif opcion_uno == "Thor":
            print ("El nombre de tu perro es el quinto más usual")
        else: 
            print ("Felicidades, el nombre de tu labrador es muy poco común")

        opcion_dos = int(input (nombre + " escribe la edad de tu labrador "))
        if opcion_dos == 0:
            print ("Tu perro en edad humana tiene 2 a 14 años")
        elif opcion_dos == 1:
            print ("Tu perro en edad humana tiene 16 a 29 años")
        elif opcion_dos == 2:
            print ("Tu perro en edad humana tiene 24 años")
        elif opcion_dos == 3:
            print ("Tu perro en edad humana tiene 30 años")
        elif opcion_dos == 4:
            print ("Tu perro en edad humana tiene 36 años")
        elif opcion_dos == 5:
            print ("Tu perro en edad humana tiene 42 años")
        elif opcion_dos == 6:
            print ("Tu perro en edad humana tiene 48 años")
        elif opcion_dos == 7:
            print ("Tu perro en edad humana tiene 54 años")
        elif opcion_dos == 8:
            print ("Tu perro en edad humana tiene 60 años")
        else :
            print ("Tu perro puede tener entre 66 a 96 años humanos si tiene entre 9 a 14 años")

    #BULLDOG
    elif opcion_uno == "bulldog":
        print ("Esta raza es la tercera más frecuente entre los dueños de perros")
        print ("¿Qué color es tu buldog?")
        opcion_uno = (input ("Escribe su color "))
        if opcion_uno == "negro":
            print ("El color de tu bulldog el más común")
        elif opcion_uno == "negro tricolor":
            print ("El color de tu bulldog el segundo más común")
        elif opcion_uno == "rojo":
            print ("El color de tu bulldog el tercero más común")
        else :
            print ("Felicidades, el color de tu bulldog es muy poco común")
        
        print ( " **** Selecciona una opción conforme a la edad de tu bulldog **** ")
        print (nombre + " presiona 1 para cachorro")
        print (" presiona 2 para adulto")
        print (" o presiona 3 para anciano")
        opcion_tres = int(input (nombre + " escribe la opción que vas a usar "))

        if opcion_tres == 1:
            print ("¿Cada cuando paseas a tu cachorro? ")
            opcion_4 = int(input ("Escribe la cantidad "))
            if opcion_4 == 0:
                print ("Muy mal " + nombre +" lo correcto sería de 5 a 6" )
            elif opcion_4 == 1:
                print ("Debes mejorar " + nombre +" lo correcto sería de 5 a 6" )
            elif opcion_4 == 2:
                print ("Debes mejorar " + nombre +" lo correcto sería de 5 a 6" )
            elif opcion_4 == 3:
                print ("Muy bien, pero puede mejorar " + nombre + " lo correcto sería de 5 a 6" )
            elif opcion_4 == 4:
                print ("Muy bien, pero puede mejorar " + nombre + " lo correcto sería de 5 a 6" )
            elif opcion_4 == 5:
                print ("Excelente, tienes un perro feliz " + nombre)
            elif opcion_4 == 6:
                print ("Excelente, tienes un perro feliz " + nombre)
            else:
                print ("¡SUPER! Eres el mejor dueño, tienes un bulldog muy sano")

        elif opcion_tres == 2:
            print ("¿Cada cuando paseas a tu cachorro?")
            opcion_4 = int(input ("Escribe la cantidad "))
            if opcion_4 == 0:
                print ("Muy mal " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 1:
                print ("Debes mejorar " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 2:
                print ("Muy bien, pero puede mejorar " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 3:
                print ("Excelente " + nombre)
            elif opcion_4 == 4:
                print ("Excelente " + nombre )
            else:
                print ("¡SUPER! Eres el mejor dueño, tienes un bulldog muy sano")

        elif opcion_tres == 3:
            print ("¿Cada cuando paseas a tu cachorro?")
            opcion_4 = int(input ("Escribe la cantidad "))
            if opcion_4 == 0:
                print ("Muy mal " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 1:
                print ("Debes mejorar " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 2:
                print ("Muy bien, pero puede mejorar " + nombre +" lo correcto sería de 3 a 4" )
            elif opcion_4 == 3:
                print ("Excelente " + nombre)
            elif opcion_4 == 4:
                print ("Excelente " + nombre )
            else:
                print ("¡SUPER! Eres el mejor dueño, tienes un bulldog muy sano")

    #PASTOR ALEMAN
    elif opcion_uno == "pastor aleman":
        print ("Esta raza es la tercera más frecuente entre los dueños de perros")

        opcion_uno = (input ("Escribe el nombre de tu perro "))
        if opcion_uno == "Luna":
            print ("El nombre de tu perro es el más usual")
        elif opcion_uno == "Coco":
            print ("El nombre de tu perro es el segundo más usual")
        elif opcion_uno == "Nala":
            print ("El nombre de tu perro es el tercero más usual")
        elif opcion_uno == "Kira":
            print ("El nombre de tu perro es el cuarto más ususal")
        elif opcion_uno == "Thor":
            print ("El nombre de tu perro es el quinto más usual")
        else: 
            print ("Felicidades, el nombre de tu labrador es muy poco común")
        
        print ( " **** Selecciona una opción conforme al sexo de tu pastor aleman **** ")
        print (nombre + " presiona 1 para hembra")
        print (" presiona 2 para macho")
        opcion_tres = int(input (nombre + " escribe la opción que vas a usar "))

        if opcion_tres == 1:
            print ("Llena los datos para verificar que la masa corporal")
            PC = int(input(nombre + "¿Cuál es el peso corporal de tu perro:"))
            AH = int(input(nombre + "¿Cuál es la altura del piso al hombro:"))
            DO = int(input(nombre + "¿Cuál es la distancia de la parte inferior de la cabeza a la cola:"))
            IMC = (PC*AH/DO)

            if IMC >= 21:
                print ("Debes mejorar " + nombre +" tu perro esta delgado, tiene un IMC de : ", IMC)
            elif IMC >= 22:
                print ("Debes mejorar " + nombre +" tu perro esta en límite aceptado de : ", IMC)
            elif IMC >= 32:
                print ("Muy bien, pero puede mejorar " + nombre +" aprobaste con un promedio de : ", IMC)
            elif IMC <= 32:
                print ("Muy mal, tu perro puede tener sobre peso " + nombre +" su es promedio de : ", IMC)

        elif opcion_tres == 2:
            print ("Llena los datos para verificar que la masa corporal")
            PC = int(input(nombre + "¿Cuál es el peso corporal de tu perro:"))
            AH = int(input(nombre + "¿Cuál es la altura del piso al hombro:"))
            DO = int(input(nombre + "¿Cuál es la distancia de la parte inferior de la cabeza a la cola:"))
            IMC = (PC*AH/DO)
            if IMC >= 29:
                print ("Debes mejorar " + nombre +" tu perro esta delgado, tiene un IMC de : ", IMC)
            elif IMC >= 30:
                print ("Debes mejorar " + nombre +" tu perro esta en límite aceptado de : ", IMC)
            elif IMC >= 40:
                print ("Muy bien, pero puede mejorar " + nombre +" aprobaste con un promedio de : ", IMC)
            elif IMC <= 41:
                print ("Muy mal, tu perro puede tener sobre peso " + nombre +" su es promedio de : ", IMC)
  
    #NO HAY ESA OPCIÓN
    else:
        print (nombre + " la raza de tu mascota es muy poco común por lo que este programa no cuenta con esa opción, pon el nombre de tu perro para saber que tan común es")
        opcion_uno = (input ("Escribe el nombre de tu perro "))
        if opcion_uno == "Luna":
            print ("El nombre de tu perro es el más usual")
        elif opcion_uno == "Coco":
            print ("El nombre de tu perro es el segundo más usual")
        elif opcion_uno == "Nala":
            print ("El nombre de tu perro es el tercero más usual")
        elif opcion_uno == "Kira":
            print ("El nombre de tu perro es el cuarto más ususal")
        elif opcion_uno == "Thor":
            print ("El nombre de tu perro es el quinto más usual")
        else: 
            print ("Felicidades, el nombre de tu perro es muy poco común")

#opción 2: gato 
if opcion == 2:
    print ("El gato es la segunda mascota más común, por debajo del perro")

    #NEGRO
    opcion_uno = (input (nombre + " ahora, escribe el color de tu gato "))
    if opcion_uno == "negro":
        print ("El color de tu gato el más común")
        opcion_5 = (input ("Escribe el nombre de tu perro "))
        if opcion_5 == "Luna":
            print ("El nombre de tu gato es el más usual")
        elif opcion_5 == "Pelusa":
            print ("El nombre de tu gato es el segundo más usual")
        elif opcion_5 == "Nala":
            print ("El nombre de tu gato es el tercero más usual")
        elif opcion_5 == "Kira":
            print ("El nombre de tu gato es el cuarto más ususal")
        elif opcion_5 == "Kitty":
         print ("El nombre de tu gato es el quinto más usual")
        else: 
         print (nombre + " felicidades, el nombre de tu gato es muy poco común")

    #GRIS
    elif opcion_uno == "gris":
        print ("El color de tu gato el segundo más común")
        opcion_dos = int(input (nombre + " escribe la edad de tu labrador "))
        if opcion_dos == 0:
            print ("Tu gato en edad humana tiene 1 a 14 años")
        elif opcion_dos == 1:
            print ("Tu gato en edad humana tiene 15 a 24 años")
        elif opcion_dos == 2:
            print ("Tu gato en edad humana tiene 24 años")
        elif opcion_dos == 3:
            print ("Tu gato en edad humana tiene 28 años")
        elif opcion_dos == 4:
            print ("Tu gato en edad humana tiene 32 años")
        elif opcion_dos == 5:
            print ("Tu gato en edad humana tiene 36 años")
        elif opcion_dos == 6:
            print ("Tu gato en edad humana tiene 40 años")
        elif opcion_dos == 7:
            print ("Tu gato en edad humana tiene 44 años")
        elif opcion_dos == 8:
            print ("Tu gato en edad humana tiene 48 años")
        else :
            print ("si tu gato tiene entre 9 a 20, puede tener entre 49 a 96 años humanos si tiene entre 9 a 14 años")
    
    #NARANJA
    elif opcion_uno == "naranja":
        print ("El color de tu gato el tercero más común")
        print ("Ahora calcularemos el indice de masa corporal de tu gato")
        CT = int (input (nombre + "¿Cuánto mide la caja torácipa de tu gato?:"))
        MP = int (input (nombre + "¿Cuánto mide de la cabeza a las patas?:"))
        imc = (CT / 0,7062 - MP) / 0.9156

        if imc >= 3:
             print ("Debes mejorar " + nombre +" tu perro esta delgado, tiene un IMC de : ", imc)
        elif imc >= 3.6:
            print ("Debes mejorar " + nombre +" tu perro esta en límite aceptado de : ", imc)
        elif imc >= 4.5:
            print ("Muy bien, pero puede mejorar " + nombre +" aprobaste con un promedio de : ", imc)
        elif imc <= 4.6:
            print ("Muy mal, tu perro puede tener sobre peso " + nombre +" su es promedio de : ", imc)
    
    #NINGUNA DE LAS OPCIONES
    else :
        print ("Felicidades, el color de tu gato es muy poco común")