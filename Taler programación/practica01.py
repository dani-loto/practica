#Calcula el pormedio de IMC
nombre = input ("Escribe tu nombre ")

#IMC= Peso actual (kg) ÷ altura (m) x altura (m)= kg/m2.
print (nombre + "ahora comenzaremos a calcular tu Indice de Masa Corporal")

PA = float(input ("¿Cuál es tu peso corporal en kilogramos? "))
altura = float (input ("¿Cuál es tu altura en metros? "))

IMC = PA / altura * altura
print ("Tu IMC es igual a ", IMC)

rango = str(input ("¿Deseas saber qué tal esta tu IMG?"))
if rango == "Si":
    if IMC < 18.4:
        print (nombre + " tienes bajo peso, tu IMC es de ", IMC)

    elif IMC <= 24.9:
        print (nombre + " tienes un peso normal con un IMC de ", IMC)

    elif IMC <= 29.9:
        print (nombre + " tienes un sobrepeso con un IMC de ", IMC)

    elif IMC <= 34.9:
        print (nombre + " tienes obesidad de en grado I con un IMC de ", IMC)

    elif IMC <= 39.9:
        print (nombre + " tienes obesidad de en grado II con un IMC de ", IMC)

    elif IMC >= 40:
        print (nombre + " tienes obesidad de en grado III con un IMC de ", IMC)

elif rango == "No":
    print ("Gracias por usar esta calculadora de IMC")

