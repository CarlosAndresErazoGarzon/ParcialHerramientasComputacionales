# 1. Definición y análisis del problema
# Realizar descuentos en la tienda de la universidad a partir del rol del cliente
# 2. Diseño del programa
# - Obtener la cédula y el rol correspondiente
# - Obtener el código del propducto, cantidad y precio
# - Aplicar descuento
# - Preguntar si se desea agregar otro producto
# - Imprimir los productos con el descuento aplicado y el total
# 3. Implementación

# Función para comprobar la cédula
def ingresa_cedula():
    while True:
        entrada = input("Ingrese la cédula del cliente: ")
        if(entrada.isdigit()):
            return entrada
        else:
            print("Ingrese una cédula correcta")

# Función para comprobar los valores entre 0 o 1
def ingresa_bin():
    while True:
        try:
            entrada = int(input())
            if(entrada == 1 or entrada == 0):
                return entrada
            else:
                print("Ingrese un valor que corresponda a 1 o 0")
        
        except ValueError:
            print("No se ingreso un número")

# Función para verificar los números
def es_numero():
    while True:
        try:
            val = int(input())
            return val
        except ValueError:
            print("No se ingreso un número")


print("BIENVENIDO AL SISTEMA DE DESCUENTOS DE LA CAFETERIA\n")
lista = []
cedula = ingresa_cedula() #Valida
print("Ingrese el rol del cliente: (0) estudiante / (1) profesor")
rol = ingresa_bin() #Valida
rol_str = ""

#Ciclo para agregar productos
while True:
    print("Ingrese el código del producto: ")
    codigo = input()
    print("Ingrese la cantidad: ")
    cant = es_numero()  #Valida
    print("Ingrese el precio: ")
    precio = es_numero() #Valida
    #Calcula el total para un producto con su respectiva cantidad
    total = cant*precio
    #Aplica el descuento dependiendo del rol
    if(rol):
        # Descuento de profesor
        lista.append([codigo, total*0.20])
        rol_str = "profesor"
    else:
        # Descuento de estudiante
        lista.append([codigo, cant, precio, float(total*0.50)])
        rol_str = "estudiante"
    #Posibilidad de agregar otro producto
    print("Desea ingresar otro valor: (1) SI / (0) NO: ")
    opc = ingresa_bin()
    #Salida o continuación del ciclo while
    if(opc):
        continue
    else:
        break

#Variable para calcular el valor total
total_final = 0
#Imprimir resultados
print("\nVALOR FINAL\n")
print("El "+rol_str+" con cédula "+cedula+" debe pagar: ")
#Tabla para presentar la información
print("Código del producto | Cantidad | Precio c/u | Precio ")

for n in lista:
    print("\t"+str(n[0])+"\t  \t"+str(n[1])+"  \t  "+str(n[2])+"\t"+str(n[3]))
    total_final += n[1]

print("Precio total: "+str(total_final))
print("\n¡MUCHAS GRACIAS POR SU COMPRA!\n")

# 4. Pruebas y mantenimiento
# - El programa valida las entradas posibles como es el caso de: 
#       - Cédula.
#       - Rol.
#       - Cant.
#       - Precio.
#       - Opc (opción para agregar más productos).
# - El programa permite la posibilidad de agregar varios productos.
# - El programa cuenta con salidas o terminaciones del programa en 
# ciertos casos previstos.
# - Se verifican las operaciones realizadas, el descuento aplicada 
# en un producto es igual que aplicar el descuento al final.