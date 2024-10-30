print ("Sistema para calcualar tus compras semanales")
nombre = input("Para comenzar, ¿ cuál es tu nombre?:")
papas = int(input(nombre + "¿Cuánto cuestan las papas fritas?:"))
huevo = int(input(nombre + "¿Cuánto cuesta el kilo de huevo?:"))
jamon = int(input(nombre + "¿Cuánto es de 1/4 de jamon?:"))
galletas = int(input(nombre + "¿Cuánto seria de estas galletas?:"))
refresco = int(input(nombre + "¿Cuánto cuesta este refrsco de un litro?:"))
compra = (papas + huevo + jamon + galletas + refresco)

pago = int(input ("es hora de pagar, el cajero pregunta con qué billete vas a pagar"))
regreso = (pago - compra)
billete = int(input(nombre + "mi billegte sería de:"))
if compra >= billete:
    print ("no te alcanza " + nombre +" intenta con otro billete : ")
elif compra <= billete: 
    print ("perfecto, tu cambio es de" + cambio + nombre)
print ("gracias por tu compra, vuelva pronto")