x = 'increible'
def myfuncion():
    x = 'fabuloso'
myfuncion()
print ('Python es ' + x)

z = 'increible'
def mifuncion():
    global z
    z = 'fabuloso'
mifuncion()
print ('Python es ' + z)