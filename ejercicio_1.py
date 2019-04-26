
texto = "Hola, me llamo Nate.¿Tu como te llamas?"

n_mayus = 0
lista_vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
n_vocales = 0
vocales = []

for letra in texto:
    if letra.isupper() == 1:
        n_mayus += 1

print(f"La cantidad de mayúsuclas es {n_mayus}")

for letra in texto:
    if letra in lista_vocales:
        vocales.append(letra)
        n_vocales += 1

print(f"La cantidad de vocales es {n_vocales}")
print(vocales)

