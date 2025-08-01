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
usuario = input("Ingrese el usuario: ")
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
resp_propina = input(f"¿Desea agregar propina? \n1.- Si \n2.- No \nEscriba el número de la opción que desea:  ")
if resp_propina == "1":
    porcentaje = int(input("¿Cuánto porcentaje de propina dará?: "))
    propina = subtotal * (porcentaje / 100)
descuento = 0
resp_descuento = input(f"¿Cuenta con una trajeta de cliente frecuente? \n1.- Sí \n2.- No \n Escriba el número de la opción que desea: ")
if resp_descuento == "1":
    descuento = subtotal * 0.10
total = (subtotal + iva + propina) - descuento
print("DETALLES DE LA FACTURA")
print(f"Subtotal: Q{subtotal}")
print(f"IVA: Q{iva}")
print(f"Propina: Q{propina}")
print(f"Descuento: Q{descuento}")
print(f"Total: Q{total}")
# Verificador de fecha válida con día de la semana
print("BIENVENID@ AL VERIFICADOR DE FECHAS VÁLIDAS")
d = int(input("Día: "))
m = int(input("Mes: "))
a = int(input("Año: "))
if m == 1:
    m = 13
    a = a - 1
if m == 2:
    m = 14
    a = a - 1
q = d
k = a % 100
j = a // 100
h = (q + (13*(m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
dias = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
print("La fecha ingresada fue un", dias[h])
# Clasificador de envío con múltiples condiciones
print(f"BIENVENID@ AL SISTEMA DE ENVÍO \n Por favor ingrese los datos que se le solicitan")
peso = float(input("Ingrese el peso del paquete en kg: "))
distancia = float(input("Ingrese la distancia en km: "))
urgente = input(f"¿Su envio es urgente? \n1.- Sí \n2.- No \nEscriba el número de la opcíon que desea: ")
tamaño = input("Ingrese el tamaño del paquete (pequeño/mediano/grande): ")
costo_base = peso * 5 + distancia * 0.1
recargo_urgente = 0
if urgente == "1":
    recargo_urgente = 50
recargo_tamaño = 0
if tamaño.lower() == "grande":
    recargo_tamaño = 30
descuento = 0
if urgente == "2" and peso < 5:
    descuento = 20
total = costo_base + recargo_urgente + recargo_tamaño - descuento
print("DESGLOSE DEL ENVÍO")
print(f"Costo base: Q{round(costo_base, 2)}")
print(f"Recargo por urgencia: Q{recargo_urgente}")
print(f"Recargo por tamaño: Q{recargo_tamaño}")
print(f"Descuento aplicado: Q{descuento}")
print(f"Total a pagar: Q{round(total, 2)}")
# Sistema de calificaciones con curva
nombres = []
notas = []
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nombres.append(nombre)
    notas.append([nota1, nota2, nota3])
todos_bajos = True
for n in notas:
    promedio = (n[0] + n[1] + n[2]) / 3
    if promedio >= 70:
        todos_bajos = False
if todos_bajos:
    for i in range(5):
        for j in range(3):
            if notas[i][j] + 5 > 100:
                notas[i][j] = 100
            else:
                notas[i][j] = notas[i][j] + 5
print("RESULTADOS")
for i in range(5):
    promedio = (notas[i][0] + notas[i][1] + notas[i][2]) / 3
    print(f"{nombres[i]} - Promedio final: {round(promedio, 2)}")
# Calculadora de rumbo entre puntos cardinales
print("BIENVENID@ A LA CALCULADORA DE RUMBO ENTRE PUNTOS CARDINALES")
punto_inicio = input("Ingrese el punto desde el que parte (norte, sur, este, oeste): ")
punto_final = input("Ingrese el punto al que se dirige (norte, sur, este, oeste): ")
if punto_inicio.lower() == "sur" and punto_final.lower() == "norte":
    print("Dirigirse recto hacia el norte")
elif punto_inicio.lower() == "sur" and punto_final.lower() == "este":
    print("Dirigirse hacia el sureste")
elif punto_inicio.lower() == "sur" and punto_final.lower() == "oeste":
    print("Dirigirse hacia el suroeste")
elif punto_inicio.lower() == "norte" and punto_final.lower() == "sur":
    print("Dirigirse recto hacia el sur")
elif punto_inicio.lower() == "norte" and punto_final.lower() == "este":
    print("Dirigirse hacia el noreste")
elif punto_inicio.lower() == "norte" and punto_final.lower() == "oeste":
    print("Dirigirse hacia el noroeste")
elif punto_inicio.lower() == "este" and punto_final.lower() == "sur":
    print("Dirigirse hacia el sureste")
elif punto_inicio.lower() == "este" and punto_final.lower() == "norte":
    print("Dirigirse hacia el noreste")
elif punto_inicio.lower() == "este" and punto_final.lower() == "oeste":
    print("Dirigirse recto hacia el oeste")
elif punto_inicio.lower() == "oeste" and punto_final.lower() == "sur":
    print("Dirigirse hacia el suroeste")
elif punto_inicio.lower() == "oeste" and punto_final.lower() == "norte":
    print("Dirigirse hacia el noroeste")
elif punto_inicio.lower() == "oeste" and punto_final.lower() == "este":
    print("Dirigirse recto hacia el este")
elif punto_inicio == punto_final:
    print("El punto inicial es el mismo al final")
else:
    print("Dirección inválida")
# Simulador de entradas al cine con validación múltiple
print(f"BIENVENID@ AL SISTEMA DE ENTRADAS AL CINE \nPor favor ingrese los datos que se le solicitan")
edad = int(input("Ingrese su edad: "))
dia = input("¿Qué día de la semana es? ").lower()
estudiante = input(f"¿Es estudiante? \n1.- Sí \n2.- No \nIngrese el número de la opción que desea elegie")
clasificacion = int(input("¿Qué clasificación tiene la película? (Ej. 13, 15, 18): "))
if edad < 13 and clasificacion > 13:
    print("No puede ver esta película por su edad.")
else:
    if estudiante == "1":
        precio = 35
    else:
        precio = 50
    if dia.lower() == "miércoles" or dia.lower() == "miercoles":
        print("Hoy es miércoles. ¡Promoción 2x1!")
        print(f"Precio total por 2 personas: Q{precio}")
    else:
        print(f"Precio total: Q{precio}")
# Comparador de fechas (tipo calendario digital)
dia1 = int(input("Ingrese el día de la primera fecha: "))
mes1 = int(input("Ingrese el mes de la primera fecha: "))
año1 = int(input("Ingrese el año de la primera fecha: "))
dia2 = int(input("Ingrese el día de la segunda fecha: "))
mes2 = int(input("Ingrese el mes de la segunda fecha: "))
año2 = int(input("Ingrese el año de la segunda fecha: "))
if año1 > año2:
    print("La primera fecha es mayor.")
elif año2 > año1:
    print("La segunda fecha es mayor.")
else:
    if mes1 > mes2:
        print("La primera fecha es mayor.")
    elif mes2 > mes1:
        print("La segunda fecha es mayor.")
    else:
        if dia1 > dia2:
            print("La primera fecha es mayor.")
        elif dia2 > dia1:
            print("La segunda fecha es mayor.")
        else:
            print("Ambas fechas son iguales.")
if mes1 == mes2 and año1 == año2:
    print("Están en el mismo mes y año.")
else:
    print("No están en el mismo mes y año.")
dias1 = dia1 + mes1 * 30 + año1 * 365
dias2 = dia2 + mes2 * 30 + año2 * 365
diferencia = abs(dias1 - dias2)
print(f"Han pasado {diferencia} días entre ambas fechas aproximadamente")
