from random import randint

chosen_pkmn = input("¿Contra que pokemon quieres luchar? Squirtle, Charmander o Bulbasaur\n").capitalize()
chosen_pkmn_hp = 0
chosen_pkmn_dmg = 0
pikachu_hp = 100
impact_dmg = 10
voltio_dmg = 12

while chosen_pkmn != "Squirtle" and chosen_pkmn != "Charmander" and chosen_pkmn != "Bulbasaur":
    print("Te has equivocado al escribir el nombre, vuelve a escribir el nombre del rival\n")
    chosen_pkmn = input("Squirtle, Charmander o Bulbasaur?\n").capitalize()

if chosen_pkmn == "Squirtle":
    chosen_pkmn_hp = 90
    chosen_pkmn_dmg = 8
    print("Tu rival es Squirtle\n")
elif chosen_pkmn == "Charmander":
    chosen_pkmn_hp = 80
    chosen_pkmn_dmg = 7
    print("Tu rival es Charmander\n")
else:
    chosen_pkmn_hp = 100
    chosen_pkmn_dmg = 10
    print("Tu rival es Bulbasaur\n")

print("Estas son sus estadisticas")
print(f"     Vida de {chosen_pkmn} : {chosen_pkmn_hp}")
print(f"     Daño de {chosen_pkmn} : {chosen_pkmn_dmg}\n")
print("Y estos son las estadisticas de tu pikachu")
print(f"     Vida de Pikachu: {pikachu_hp}")
print(f"     Daño de Impact Trueno: {impact_dmg}")
print(f"     Daño de Bola Voltio: {voltio_dmg}\n")

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
                print(f"La vida del {chosen_pkmn} es {chosen_pkmn_hp}")

        else:
            chosen_pkmn_hp -= impact_dmg

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print(f"La vida del {chosen_pkmn} es {chosen_pkmn_hp}")

    if chosen_attack == "2":

        critical = randint(1, 10)

        if critical == 1:
            chosen_pkmn_hp -= (voltio_dmg * 2)
            print("El golpe ha sido critico!!")

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print(f"La vida del {chosen_pkmn} es {chosen_pkmn_hp}")

        else:
            chosen_pkmn_hp -= voltio_dmg

            if chosen_pkmn_hp <= 0:
                print("El rival ha sido debilitado")
            else:
                print(f"La vida del {chosen_pkmn} es {chosen_pkmn_hp}")

    print("El rival va a atacar...")

    critical = randint(1, 10)

    if critical == 1 or critical == 2:
        print("El rival te ha hecho un golpe critico!")
        pikachu_hp -= chosen_pkmn_dmg * 2

        if pikachu_hp <= 0:
            print("Tu Pikachu ha sido debilitado")
        else:
            print(f"La vida de Pikachu es: {pikachu_hp}")

    else:
        pikachu_hp -= chosen_pkmn_dmg

        if pikachu_hp <= 0:
            print("Tu Pikachu ha sido debilitado")
        else:
            print(f"La vida de Pikachu es: {pikachu_hp}")

if pikachu_hp <= 0:
    print("Has perdido el combate!")
else:
    print("Has ganado el combate!")
