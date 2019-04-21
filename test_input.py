from random import randint

opciones = ['piedra', 'papel', 'tijeras']
resultados = [[True, False, False], [False, True, False], [False, False, True]]
ganador = 0
while ganador == 0:
    opcion = input("Escribe tu eleccion: ")
    if opcion not in opciones:
        print('Lo siento, %s no es una eleccion valida, intentalo de nuevo\n' % opcion)

    else:
        opcion_pc = randint(0, 2)
        opcion_us = opciones.index(opcion)
        print('PC: %s vs TU: %s' % (opciones[opcion_pc], opcion))
        if (opcion_pc == opcion_us):
            print('No hay ganador\n')
        else:
            if resultados[opcion_pc][opcion_us]:
                ganador[0] += 1
                if (int(nums) > 1): print('Perdiste la partida\n')
            else:
                ganador[1] += 1
                if (int(nums) > 1): print('Ganaste la partida\n')