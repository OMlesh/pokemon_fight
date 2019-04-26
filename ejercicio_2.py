
numero = int(input("¿Qué tabla de multiplicar del 5 al 15 quieres consultar?\n"))

for multiplo in range(5, 16):
    print(f"{int(numero)} x {multiplo} = {round(numero * multiplo)}")

print("\n")

for multiplo in range(1, 11):
    resultado = numero * multiplo
    if resultado%2 == 0:
        print(f"{int(numero)} x {multiplo} = {resultado}")

print("\n")

for multiplo in range(1, 11):
    print(f"{int(numero)} x {11 - multiplo} = {resultado}")