#condicionales
x = int(input("escribe un número menor a 200000"))
while x < 200000:
    print ("Este número", x , "y es menor a 200000 le voy a sumar uno hasta llegar al número")
    x += 1

if x == 200000:
    print ("Felicidades, no sabes seguir instrucciones :(")

else:
    print ("No se hizo nada ya que escvribist un número mayor, pon más atención")