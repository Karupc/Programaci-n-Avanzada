# Simulador de votación con validación cruzada
print(f" BIENVENID@ AL SISTEMA DE VOTACIÓN \nPor favor ingrese los datos datos que se le soliciten:")
nombre_completo = input("Ingrese su nombre completo: ")
if len(nombre_completo) < 5:
    print("Ingrese un nombre válido")
else:
    anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
    edad = 2025 - anio_nacimiento
    if edad == 17:
        departamento = input("Ingrese su departamento: ")
        if departamento.lower() == "petén" or departamento.lower() == "alta verapaz":
            print(f"Bienvenid@ {nombre_completo}, su centro de votación está en {departamento}")
        else:
            print("Usted no puede votar ya que es menor de edad")
    elif edad < 18:
        print("Usted no puede votar ya que es menor de edad")
    elif edad >= 18:
        dpi = input("Ingrese su número de DPI: ")
        if len(dpi) != 13 or not dpi.isdigit():
            print("Ingrese un número de DPI válido")
        else:
            departamento = input("Ingrese su departamento: ")
            print(f"Bienvenid@ {nombre_completo}, su centro de votación está en {departamento}")
# Calculadora de impuestos progresivos + deducciones
print("BIENVENID@")
ingreso = float(input("Ingrese ingreso anual: Q"))
dependientes = int(input("Cantidad de dependientes: "))
deduccion = dependientes * 1000
neto = ingreso - deduccion
if ingreso < 40000 and dependientes > 2:
    print("No paga impuestos.")
if ingreso >= 40000 or dependientes <= 2:
    if neto <= 30000:
        print("Debe pagar Q" + str(neto * 0.05))
    if neto > 30000 and neto <= 60000:
        print("Debe pagar Q" + str(neto * 0.10))
    if neto > 60000 and neto <= 100000:
        print("Debe pagar Q" + str(neto * 0.15))
    if neto > 100000:
        print("Debe pagar Q" + str(neto * 0.20))
# Sistema de autenticación avanzado con penalización
print("BIENVENID@ AL SISTEMA")
usuario = input("Ingrese el suario: ")
contra = input("Ingrese la contraseña: ")
if usuario == "karla" and contra == "1234":
    print("Acceso concedido")
    print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
if usuario == "maria" and contra == "abcd":
    print("Acceso concedido")
    print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
if usuario == "pedro" and contra == "5678":
    print("Acceso concedido")
    print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
if not ((usuario == "karla" and contra == "1234") or (usuario == "maria" and contra == "abcd") or (usuario == "pedro" and contra == "5678")):
    print("Intento 2")
    usuario2 = input("Ingrese el usuario: ")
    contra2 = input("Ingrese la contraseña: ")
    if usuario2 == "karla" and contra2 == "1234":
        print("Acceso concedido")
        print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
    if usuario2 == "maria" and contra2 == "abcd":
        print("Acceso concedido")
        print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
    if usuario2 == "pedro" and contra2 == "5678":
        print("Acceso concedido")
        print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
    if not ((usuario2 == "karla" and contra2 == "1234") or (usuario2 == "maria" and contra2 == "abcd") or (usuario2 == "pedro" and contra2 == "5678")):
        print("Intento 3")
        usuario3 = input("Ingrese el usuario: ")
        contra3 = input("Ingrese la contraseña: ")
        if usuario3 == "karla" and contra3 == "1234":
            print("Acceso concedido")
            print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
        if usuario3 == "maria" and contra3 == "abcd":
            print("Acceso concedido")
            print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
        if usuario3 == "pedro" and contra3 == "pass":
            print("Acceso concedido")
            print("1.- Ver perfil\n2.- Cambiar contraseña\n3.- Cerrar sesión")
        if not ((usuario3 == "karla" and contra3 == "1234") or (usuario3 == "maria" and contra3 == "abcd") or (usuario3 == "pedro" and contra3 == "5678")):
            print("ACCESO BLOQUEADO")
# Simulador de facturación con IVA, descuentos y propina
print("BIENVENID@")
cantidad_productos = int(input("Por favor ingrese la cantidad de productos que lleva: "))
st = 0
for i in range(cantidad_productos):
    precios = float(input(f"Ingresa el precio del producto {i+1}: Q"))
    subtotal = st + precios
    iva = subtotal * 0.12
    propina = 0
    resp_propina = input(f"¿Desea agregar propina? \n1.- Si \n2.- No: ")
    if resp_propina == 1:
        porcentaje = int(input("¿Cuánto porcentaje de propina dará?: "))
        propina = subtotal * (porcentaje / 100)
    descuento = 0
    resp_descuento = input(f"¿Cuenta con una trajeta de cliente frecuente? \n1.Sí \n2.- No")
    if resp_descuento == 1:
        descuento = subtotal * 0.10
    total = (subtotal + iva + propina) - descuento
    print("DETALLES DE LA FACTURA")
    print(f"Subtotal: Q{subtotal}")
    print(f"IVA: Q{iva}")
    print(f"Propina: Q{propina}")
    print(f"Descuento: Q{descuento}")
    print(f"Total: Q{total}")