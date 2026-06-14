# Programa para calcular el promedio de 6 edades

edades = []

for i in range(6):
    edad = int(input(f"Ingresa la edad {i+1}: "))
    edades.append(edad)

promedio = sum(edades) / len(edades)

print(f"\nEdades ingresadas: {edades}")
print(f"Promedio de edades: {promedio:.2f}")
