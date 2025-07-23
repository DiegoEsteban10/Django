# numero1 = int (input('Digite su numero: '))
# numero2 = int (input('Digite su numero: '))


# def potencias(numero1,numero2):
#     return numero1**numero2


# print(potencias(numero1,numero2))


# def MixMax (valores):
#     return min(valores), max(valores)

# min,max = MixMax([2,3,4,5,6,7,8,9])
# print (min,max)


x = "global"

def externo():
    x = 'medio'
    def interno():
        x = 'local'
        
        interno()
    externo()
    