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