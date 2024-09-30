'''
Menú principal:
• Mostrar las siguientes opciones:
o Agregar producto al inventario.
o Realizar una venta.
o Mostrar productos disponibles.
o Salir del sistema.

'''
inventario = [
    ["Chupetin Sable De Luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 990],
    ["Barrita De Cereal Wookiee", 48, 2500],
    ["Galletitas R2D2", 20, 15800],

]

def mostrar_menu():
    '''
    funcion que sirve para mostrar el menu 
    dependiendo la opcion llama distintas funciones
    si se elige una opcion incorrecta repite el bucle
    
    no recibe parametros ni retorna valores
    '''
    opcion = ""

    while opcion != "4":   
        print('''
        1. Agregar producto al inventario.
        2. Realizar una venta.
        3. Mostrar productos disponibles.
        4. Salir del sistema.
        ''')
            

        opcion = input("Ingrese la opcion deseada: ")

        match opcion:

            case "1":
                agregar_producto()
        

            case "2":
                realizar_venta()

            case "3":
                mostrar_inventario()

            case "4":
                    
                print("Gracias por utilizar nuestro servicio")
                return

            case _:
                print("Opcion erronea, ingrese nuevamente")
                
                


'''2. Agregar producto al inventario:
• Permitir al usuario agregar productos al inventario. Cada producto debe tener
un nombre, una cantidad disponible y un precio unitario.
• Los productos deben almacenarse en una lista.
• Ver la estructura del inventario al final de la consigna'''

def agregar_producto():
    
    respuesta = "s"
    while respuesta.lower() == "s":
    
        nombre_producto = input("Ingrese el nombre del producto que añade: ")        
        stock_producto = -1
                    
        while stock_producto < 1:
            
            stock_producto = input("Ingrese el stock del producto que añade: ")

            if stock_producto.isdigit():
                
                stock_producto = int(stock_producto)
                        
            else:
                stock_producto = -1 

        precio_producto = -1
                    
        while precio_producto < 1:
            
            precio_producto = input("Ingrese el precio del producto: ")

            if precio_producto.isdigit():

                precio_producto = float(precio_producto)

            else:
                precio_producto = -1

                        
                    
                    
                    

        inventario.append([nombre_producto, stock_producto, precio_producto])
        
        print("Producto añadido con exito")
        
        respuesta = input("¿Desea añadir más productos (s/n)?: ").lower()
        
        while respuesta not in ["s", "n"]:
            
            respuesta = input("Respuesta no valida. Ingrese 's' para continuar o 'n' para salir: ").lower()

def mostrar_inventario():
    
    for i in range(len(inventario)):
        
        nombre = inventario[i][0]
        stock = inventario[i][1]
        precio = inventario[i][2]
        
        print(f"producto: {nombre}, stock: {stock} y precio: {precio}  ")





'''3. Realizar una venta:
• Mostrar una lista de productos disponibles (nombre, precio y cantidad).
• El usuario podrá seleccionar un producto y la cantidad que desea comprar.
• Verificar que haya suficiente stock del producto seleccionado.
• Restar la cantidad comprada del inventario.
• Mostrar el total a pagar al cliente por la venta.
• Si no hay suficiente stock, mostrar un mensaje que indique que no se puede
realizar la venta.'''


def realizar_venta():
    mostrar_inventario()
    
    producto_compra = input(f"¿Cual producto desea comprar?: ")
    
    cantidad_compra = input(f"¿Cuanta cantidad de {producto_compra} desea comprar?: ")

    if cantidad_compra.isdigit() and int(cantidad_compra) > 0:
        
        cantidad_compra = int(cantidad_compra)
    
        for i in range(len(inventario)):
            
            if inventario[i][0].lower() == producto_compra.lower():
                
                stock_disponible = inventario[i][1]
                precio_producto = inventario[i][2]
                
                if cantidad_compra <= stock_disponible:
                    
                    total_a_pagar = cantidad_compra * precio_producto
                    
                    inventario[i][1] -= cantidad_compra
                    
                    print(f"El total a pagar por {producto_compra} es de : {total_a_pagar}")
                    
                    print(f"Compra realizada con exito, quedan {inventario[i][1]} en stock.")
                
                else:
                    
                    print(f"No hay suficiente stock para realizar la venta, hay {stock_disponible} unidades .")
                
                return
            
        print("El producto no se encuentra en el inventario.")
    
    else:

        print("El stock debe ser un numero entero y positivo")
    
   




mostrar_menu()






    

