# #Arreglo/Listas []
# #tuplas con ()
# #diccionarios {}
# agenda = {'Manuel':'1234-5678-9012','Maria':'1234-5678-9013','Pedro':'1234-5678-9014'}
# agenda['Luis'] = '1234-5678-9015'
# agenda['Daniel'] = '1234-5678-9016'
# print (agenda)
# del agenda['Luis']
# print (agenda)
# vacia = dict()
# for nombres,tel in agenda.items():
#     print (f"{nombres} tiene el telefono {tel}")
# # print (agenda.get('Manuel'))
# # print (list (agenda.keys()))
# # print (list (agenda.values()))
# # print (list (agenda.items()))

palabra = input ("Digite una palabra: ").lower()
freq = {}
for i in palabra:
    if i.isalpha():
        freq[i]= freq.get(i,0)+1
print (freq)

