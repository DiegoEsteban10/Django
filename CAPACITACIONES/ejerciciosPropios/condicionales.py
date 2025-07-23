#--------------------------------------------NIVEL BASICO--------------------------------------------#
## Pide un numero al usuario y muestra si es positivo, negatico o cero
numero = int (input("Por favor ingrese un numero que desee (positivo, negativo e incluso 0): "))

if numero > 0:
    print ("El numero que usted escogio es positovo")
    
elif numero < 0:
    print ("El numero que usted escogio es negativo")
    
elif numero == 0:
    print ("El numero que usted escogio es cero")
    
else :
    print ("La opcion es inavalida, intentelo de nuevo")
    