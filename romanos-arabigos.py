romanValues = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

romanSubstract = {
    'I': ['V', 'X'],
    'X': ['L', 'C'],
    'C': ['D', 'M']
}

def secuence(rm1, rm2):
    romanNumbers = ["M", "D", "C", "L", "X", "V", "I"]
    for i in range(len(romanNumbers)):
        if rm1 == romanNumbers[i]:
            index1 = i
        if rm2 == romanNumbers[i]:
            index2 = i
    return index1 > index2

def rom_to_arab(num_prueba, rom):

    print('Numero a esperar: ', num_prueba)

    arabic = 0
    rom = rom.upper()
    rom = list(rom)
    rom.reverse()
    was_sub = False
    repeat_count = 1

    for i in range(len(rom)):
        print('Iteracion numero: ', i)

        actual = romanValues[rom[i]]
        previous = romanValues[rom[i - 1]] if i > 0 else 0
        is_consec = secuence(rom[i], rom[i - 1]) if i > 0 else False

        if rom[i] not in romanValues:
            print('El valor ingresado no es un número romano')
            return

        if i > 0 and rom[i] == rom[i - 1]:
            repeat_count += 1
        else:
            repeat_count = 1

        if repeat_count > 3:
            print('El número romano ingresado no es válido porque se repite más de 3 veces el mismo número')
            return

        if i == 0:
            arabic += actual
        elif actual >= previous:
            if was_sub and actual < previous:
                was_sub = False
                print('El número romano ingresado no es válido en suma')
                return
            arabic += actual
        elif actual < previous:
            is_sub = rom[i - 1] in romanSubstract[rom[i]]
            if is_consec and is_sub:
                was_sub = True
                arabic -= actual
            else:
                print('El número romano ingresado no es válido en resta')
                return

    print('Valor del numero romano: ', arabic)
    print(rom)

#Correctos
rom_to_arab(14, 'xiv')
rom_to_arab(62, 'lxii')
rom_to_arab(125, 'cXXv')
rom_to_arab(800, 'dCCC')    
rom_to_arab(2019, 'MMXIX')
rom_to_arab(444, 'CDXLIV')

#Incorrectos
rom_to_arab(99, 'ic')
rom_to_arab(15, 'vx')
rom_to_arab(9, 'iiix')
rom_to_arab(1000, 'dd')
