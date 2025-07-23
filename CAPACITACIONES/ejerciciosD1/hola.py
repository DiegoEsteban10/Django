#Solicite al usuario, mediante input(), los siguientes datos:
# Nombre (cadena de texto)
# Edad en años (entero)
# Altura en metros (número decimal)
# Peso en kilogramos (número decimal)
# Calcule el Índice de Masa Corporal (IMC)
# Clasifique el resultado del IMC según los rangos de la OMS:
# Menor de 18.5: Bajo peso
# 18.5 – 24.9: Normal
# 25.0 – 29.9: Sobrepeso
# 30.0 o más: Obesidad
# Muestre por pantalla un resumen formateado con f-strings que incluya:
# Nombre y edad del usuario
# Altura (con dos decimales) y peso (con un decimal)
# IMC (con dos decimales) y la categoría correspondiente

nombre = input ("Digite su nombre: ")
edad = int (input ("Digite su edad: "))
altura = float (input("digite su altura: "))
peso = float (input("digite su peso: "))

IMC = peso / (altura * altura)

if IMC <= 18.4:
    print (f"{nombre} de edad {edad} tiene una altura de {altura:.2f} con un peso de {peso:.1f} y su IMC {IMC:.2f} esta en la categoria de bajo peso")

elif 18.5 <= IMC < 24.9:
    print (f"{nombre} de edad {edad} tiene una altura de {altura:.2f} con un peso de {peso:.1f} y su IMC {IMC:.2f} esta en la categoria de normal")
    
elif 25.0 <= IMC < 29.9:
    print (f"{nombre} de edad {edad} tiene una altura de {altura:.2f} con un peso de {peso:.1f} y su IMC {IMC:.2f} esta en la categoria de sobrepeso")
    
elif IMC >=30.0:
    print (f"{nombre} de edad {edad} tiene una altura de {altura:.2f} con un peso de {peso:.1f} y su IMC {IMC:.2f} esta en la categoria de obesidad")
    
else :
    print ("los datos ingresados no son correctos")
    