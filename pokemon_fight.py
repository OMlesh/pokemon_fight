from random import randint
chosen_pkmn = input("¿Contra que pokemon quieres luchar? Squirtle, Charmander o Bulbasaur\n").lower()
chosen_pkmn_hp = 0
chosen_pkmn_dmg = 0
pikachu_hp = 100
impact_dmg = 10
voltio_dmg = 12

while chosen_pkmn != "squirtle" and chosen_pkmn != "charmander" and chosen_pkmn != "bulbasaur":
    print("Te has equivocado al escribir el nombre, vuelve a escribir el nombre del rival\n")
    chosen_pkmn = input("Squirtle, Charmander o Bulbasaur?\n").lower()

if chosen_pkmn == "squirtle":
    chosen_pkmn_hp = 90
    chosen_pkmn_dmg = 8
    print("Tu rival es Squirtle\n")
elif chosen_pkmn == "charmander":
    chosen_pkmn_hp = 80
    chosen_pkmn_dmg = 7
    print("Tu rival es Charmander\n")
else:
    chosen_pkmn_hp = 100
    chosen_pkmn_dmg = 10
    print("Tu rival es Bulbasaur\n")

print("Estas son sus estadisticas")
print("     Vida de " + str(chosen_pkmn) + ": " + str(chosen_pkmn_hp))
print("     Daño de " + str(chosen_pkmn) + ": " + str(chosen_pkmn_dmg) + "\n")
print("Y estos son las estadisticas de tu pikachu")
print("     Vida de pikachu: " + str(pikachu_hp))
print("     Daño de impact trueno: " + str(impact_dmg))
print("     Daño de bola voltio: " + str(voltio_dmg) + "\n")

print("Vamos a decidir con piedra, papel o tijeras:")
rock_scissor = input("Escribeme tu eleccion").lower()
while rock_scissor != "piedra" and rock_scissor != "papel" and rock_scissor != "tijeras":
    print("Te has equivocado al escribir tu eleccion, vuelve a hacerlo")
    rock_scissor = input("Piedra, papel o tijeras?\n").lower()

#eleccion_tuya =
eleccion_rival = (randint(1,3))

#klajsdkaskjdlaskjldkjlasdjklasd


#while pikachu_hp > 0 and chosen_pkmn_hp > 0
