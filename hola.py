opciones = ['piedra', 'papel', 'tijeras']
resultados = [[True, False, False], [False, True, False], [False, False, True]]

def eleccion_ppt():
    eleccion_tuya = input("Escribe tu eleccion: ")
    if eleccion_tuya not in opciones:
        print('Lo siento, % no es una eleccion valida, intentalo de nuevo\n' % eleccion_tuya)
        return eleccion_ppt()
    else:
        print(opcion)