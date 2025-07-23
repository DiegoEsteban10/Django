# Desarrolla un programa llamado panaderia.py que permita al dueño llevar un inventario sencillo:
# Diccionario inicial de productosinventario = { "pan":    {"precio": 1200, "stock": 40}, "leche":  {"precio": 4200, "stock": 25}, "huevo":  {"precio": 500,  "stock": 180}, }
# Cada clave es el nombre del producto; el valor es otro diccionario con su precio y la cantidad disponible (stock).
# Menú interactivo en bucle while
# Consultar precio y stock
# Registrar venta
# Agregar nuevo producto
# Mostrar inventario completo
# Salir
# Consultar: pide el nombre, muestra precio y stock o “No disponible”.
# Registrar venta: solicita producto y cantidad; resta al stock si hay suficiente, e imprime el total a pagar.
# Agregar producto: pide nombre, precio y stock inicial; si ya existe, solo actualiza precio y stock.
# Mostrar inventario: recorre inventario.items() y lista cada producto con precio y stock.
# Validaciones
# Evita que el stock quede negativo.
# Asegúrate de convertir los input() numéricos a int.
# Usa get() para manejar claves inexistentes sin crashear.

inventario = {
    "pan": {"precio": 1200, "stock":40},
    "leche": {"precio": 4200, "stock":25},
    "huevo": {"precio": 500, "stock":180}
}

while True:
    print ("Menu de opciones para el inventario de la panderia")
    print ("1. Consultar precio y stock")
    print ("2. Registrar venta")
    print ("3. Agragar nuevo producto")
    print ("4. Mostrar inventario completo")
    print ("0. Salir")
    
    
    opcion = input("Por favor, elige una opcion: ")
    
    if opcion == '1':
        if inventario.get:
            print (inventario.get(input("Ingrese el nombre del producto que desea consultar: ")))
        else:
            print ("No disponible")
            
    elif opcion == '2':
        for stock in inventario:
            if stock == input("Ingrese el nombre del producto que desea registrar: "):
                if inventario[stock]["stock"] >= inventario[stock]["stock"]:
                    inventario[stock]["stock"] -= int(input("Ingrese la cantidad del producto que desea consultar: "))
                    print (f"El total a pagar es: {inventario[stock]['precio'] * int(input('Ingrese la cantidad del producto que desea consultar: '))}")
                else:
                    print ("No hay suficiente stock")
            
        
    elif opcion == '3':
        print (input("Ingrese el nombre del producto que desea agregar: "))
        print (input("Ingrese el precio del producto que desea agregar: "))
        print (input("Ingrese el stock del producto que desea agregar: "))
        
    elif opcion == '4':
        print("Mostrando todos los productos del inventario...")
        for nombre, datos in inventario.items():
            print (f"{nombre}")
            print (f"{datos}")
        
    elif opcion == '0':
        break
        
        
    
    
    