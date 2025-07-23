from math import isqrt, pi  

def qurybuilder(baseurl: str, **params) -> str:
    print (type (params))
    from urllib.parse import urlencode
    return f"{baseurl}?{urlencode(params)}"

print (qurybuilder("https://www.youtube.com/?app=desktop&hl=es",id=65, formato='json'))

def eventlogger (evento,*args, **kwargs):
    print (f"[{evento}] args = {args} kwargs = {kwargs}")
    

eventlogger ('login','Fabian', ip = '172.36.231.13', exito = False)