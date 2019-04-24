
print("Bienvenido al conversor de Celsius a Farenheit")

celsius = (input("Indícame en números los grados celisus:\n"))

#while celsius is not int
#    celsius = (input("Indícame en NÚMEROS los grados celisus:\n"))

farenheit = (int(celsius) * 9 / 5) + 32

print("{} grados Celsius equivalen a {} grados Farenheit".format(celsius, farenheit))