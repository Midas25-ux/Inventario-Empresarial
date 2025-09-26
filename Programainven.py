afirmacion = True
Bienvenida = "Bienvenido a su inventario"
inventario = []

Menu = """
-------------------------------------------------
|                                               |
           Inventario Empresarial               |
|-----------------------------------------------|
|                                               |
|           1. Añada Producto                   |
|           2. Desplegar Inventario             |
|           3. Valor Total del Inventario       |
|           4. Buscar Producto                  |
|           5. Registro Venta                   |
|           6. Salir                            |
|-----------------------------------------------|
"""

print(Bienvenida)

def Inventario_add():
    print("Ha seleccionado la opción 1: Añada Producto")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    valor = float(input("Ingrese el precio del producto: "))
    inventario.append({"Nombre": producto, "Cantidad": cantidad, "precio": valor})
    print("Producto añadido al inventario.")

def precio_sum():
    print("Ha seleccionado la opción 3: Valor Total del Inventario")
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        total = 0
        for item in inventario:
            total += item["Cantidad"] * item["precio"]
        print("El valor total del inventario es:", total)

def Buscar_producto():
    print("Ha seleccionado la opción 4: Buscar Producto")
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False
    for item in inventario:
        if item["Nombre"] == nombre:
            print("Producto encontrado:", item)
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")

def Registro_venta():
    print("Ha seleccionado la opción 5: Registro Venta")
    nombre = input("Ingrese el nombre del producto vendido: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    encontrado = False
    for item in inventario:
        if item["Nombre"] == nombre:
            if item["Cantidad"] >= cantidad_vendida:
                item["Cantidad"] -= cantidad_vendida
                print("Venta registrada. Cantidad restante:", item["Cantidad"])
            else:
                print("No hay suficiente cantidad en inventario.")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")

while afirmacion:
    print(Menu)
    opt = int(input("Seleccione una opción: "))
    
    if opt == 1:
        Inventario_add()
    elif opt == 2:
        print("Ha seleccionado la opción 2: Desplegar Inventario")
        for item in inventario:
            print(item)
    elif opt == 3:
        precio_sum()
    elif opt == 4:
        Buscar_producto()
    elif opt == 5:
        Registro_venta()
    elif opt == 6:
        print("Gracias por usar nuestro sistema de inventario. ¡Hasta pronto!")
        afirmacion = False
    else:
        print("Opción inválida. Intente de nuevo.")

       

           




       

     

      
      



       



      

       

      


       

    





   







       

 


        
        




       



       
      

    


   



    

       
