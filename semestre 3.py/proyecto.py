#programa para calcular los gastos personales
print ("Sistema para calcular el promedio de tus gastos mensualmente, recuerda que máximo a +promediar es $5680")
nombre = input("Para comenzar, ¿ cuál es tu nombre?: ")
casa = int(input(nombre + " ¿Cuánto gastas para mantener tu casa mensualmente: "))
comida = int(input(nombre + " ¿Cuánto gastas en el supermercado?: "))
salidas = int(input(nombre + " ¿Cuánto gastas cuando sales con tus amigos?: "))
mascotas = int(input(nombre + " ¿Cuánto dinero gastas para tu mascota?: "))
escuela = int(input(nombre + "¿ Qué tanto gastas para lo materiales que te piden en la escuela: "))
emergencias = int(input(nombre + " ¿Cuánto dinero apartas para alguna emergencia?: "))
promedio = (casa + comida + salidas + mascotas + escuela + emergencias) / 6
if promedio >= 3800:
    print ("¡Muy bien, te sobró bastante dinero que puedes ahorrar para el próximo mes! " + nombre +" tus gastos promedian : ", promedio)
elif promedio >= 4000:
    print ("Super, incluso te sobró dinero " + nombre +" con estos gastos tienes un promedio de : ", promedio)
elif promedio >= 5500:
    print ("Casi te sales del presupuesto, intenta gastar menos cuando sales con tus amigos " + nombre +" promediaste : ", promedio)
elif promedio >= 5680:
    print ("Te pasaste de presupuesto, ahora debes dinero en tu tarjeta, te recomiendo no gastar en salidas o en la escuela para ahorrar algo de dinero y que no tengas una gran deuda " + nombre +" en promedio gastaste : ", promedio)
    print ("FIn.")

else:
    print("Te fue muy mal, no organizaste bien tus gastos.")