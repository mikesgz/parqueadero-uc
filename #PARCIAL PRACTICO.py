# PARCIAL PRACTICO
# MIGUEL ANGEL MARTINEZ
# VALENTINA SALAZAR 
N = int(input("Ingrese numero de vehiculos: "))

vehiculos_validos = 0
total_recaudado = 0

estudiantes = 0
docentes = 0
visitantes = 0

total_horas = 0

i = 0

while i < N:

    if vehiculos_validos == 30:
        print("PARQUEADERO LLENO")
        break

    print("\n--- Vehículo", i + 1, "---")

    placa = input("Digite la placa: ")
    tipo = input("Tipo de usuario ESTUDIANTE/DOCENTE/VISITANTE (e/d/v): ").upper()
    hora_entrada = int(input("Hora de entrada (0-23h): "))
    horas = float(input("Horas de permanencia: "))


    if hora_entrada < 0 or hora_entrada > 23:

        print("ERROR: La hora debe estar entre 0 y 23.")
        i = i + 1
        continue


    if horas <= 0:

        print("ERROR: Las horas de permanencia deben ser mayores que 0.")
        i = i + 1
        continue


    if tipo != "E" and tipo != "D" and tipo != "V":

        print("ADVERTENCIA: Tipo inválido. Se registrará como visitante.")
        tipo = "V"


    if horas > 0:

        if tipo == "E":

            estudiantes = estudiantes + 1

            if horas <= 2:
                tarifa = 0
            else:
                tarifa = (horas - 2) * 800

        elif tipo == "D":

            docentes = docentes + 1
            tarifa = horas * 500

        else:

            visitantes = visitantes + 1

            if horas <= 1:
                tarifa = 1500
            else:
                tarifa = 1500 + (horas - 1) * 1200

    if hora_entrada >= 20 or hora_entrada < 6:
        tarifa = tarifa * 0.90

    tarifa = round(tarifa, 2)

    vehiculos_validos = vehiculos_validos + 1
    total_recaudado = total_recaudado + tarifa
    total_horas = total_horas + horas

    print("Placa:", placa)
    print("Tarifa a pagar: $", tarifa)

    i = i + 1

print("\n========== RESUMEN DEL DÍA ==========")

print("Vehículos registrados:", vehiculos_validos)

porcentaje_ocupacion = (vehiculos_validos / 30) * 100
print("Ocupación:", round(porcentaje_ocupacion, 2), "%")

print("Recaudo total: $", round(total_recaudado, 2))

print("Estudiantes:", estudiantes)
print("Docentes:", docentes)
print("Visitantes:", visitantes)

if vehiculos_validos > 0:
    promedio_horas = total_horas / vehiculos_validos
else:
    promedio_horas = 0

print("Promedio de permanencia:", round(promedio_horas, 2), "horas")