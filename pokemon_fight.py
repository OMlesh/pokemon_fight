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

while pikachu_hp > 0 and chosen_pkmn_hp > 0:
    chosen_attack = input("¿Que ataque quieres realizar, 1 para Impact Trueno, 2 para Bola Voltio?\n")

    while chosen_attack != "1" and chosen_attack != "2":
        chosen_attack = input("Te has equivocado al elegir el ataque, pulsa 1 para Impact Trueno o 2 para Bola Voltio\n")

    if chosen_attack == "1":

        critical = randint(1, 10)

        if critical == 1:
            chosen_pkmn_hp -= (impact_dmg * 2)
            print('El golpe ha sido critico!!')

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print("La vida del rival es " + str(chosen_pkmn_hp))

        else:
            chosen_pkmn_hp -= impact_dmg

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print("La vida del rival es " + str(chosen_pkmn_hp))

    if chosen_attack == "2":

        critical = randint(1, 10)

        if critical == 1:
            chosen_pkmn_hp -= (voltio_dmg * 2)
            print("El golpe ha sido critico!!")

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print("La vida del rival es " + str(chosen_pkmn_hp))

        else:
            chosen_pkmn_hp -= voltio_dmg

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print("La vida del rival es " + str(chosen_pkmn_hp))

    print("El rival va a atacar...")

    critical = randint(1, 10)

    if critical == 1 or critical == 2:
        print("El rival te ha hecho un golpe critico!")
        pikachu_hp -= chosen_pkmn_dmg * 2

        if pikachu_hp <= 0:
            print("Tu Pikachu ha sido debilitado")
        else:
            print("La vida de Pikachu es " + str(pikachu_hp))

    else:
        pikachu_hp -= chosen_pkmn_dmg

        if pikachu_hp <= 0:
            print("Tu Pikachu ha sido debilitado")
        else:
            print("La vida de Pikachu es " + str(pikachu_hp))

if pikachu_hp <= 0:
    print("Has perdido el combate!")
else:
    print("Has ganado el combate!")
