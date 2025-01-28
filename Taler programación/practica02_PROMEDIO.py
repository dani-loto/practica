print ("Sistema para calcualar el promedio de un alumno")

nombre = input("Para comenzar ¿cuál es tu nombre? ")
mate = int(input(nombre + " ¿Cuál es tu calificación en matematicas? "))
quimica = int(input(nombre + " ¿Cuál es tu calificación en quimica? "))
espanol = int(input(nombre + " ¿Cuál es tu calificación en espanol? "))
historia = int(input(nombre + " ¿Cuál es tu calificación en historia? "))
ingles = int(input(nombre + " ¿Cuál es tu calificación en inglés? "))

promedio = (mate + quimica + espanol + historia + ingles ) / 5

print ("Tu promedio es de:", promedio)

if promedio >= 70:
    print ("Tu promedio es regular " + nombre +" aprobaste con : ", promedio)

elif promedio >= 80:
    print ("Bien, pero puede mejorar " + nombre +" aprobaste con un promedio de : ", promedio)

elif promedio >= 90:
    print ("Súper bien, sigue así " + nombre +" aprobaste con un promedio de : ", promedio)

elif promedio == 100:
    print ("Excelente, eres muy inteligente " + nombre +" aprobaste con un promedio de : ", promedio)

    print ("FIn.")

else:
    print("Te fue muy mal, reprobaste.")
