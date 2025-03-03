arabicsValues = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

substractValues = {
    4: ['IV', 'XL', 'CD'],
    9: ['IX', 'XC', 'CM']
}

def arab_to_rom(arab):
    roman = ''
    if arab < 1 or arab > 3999 or type(arab) != int:
        print('El número ingresado no es válido')
        return
    arab = list(str(arab))
    arab.reverse()
    arabInString=[]

    for i in range(len(arab)):
        arab[i] = int(arab[i]) * (10 ** i)
        arabInString.append(str(arab[i]))

    for i in range(len(arab)):
        print('Iteracion numero: ', i)
        if arab[i] in arabicsValues:
            roman = arabicsValues[arab[i]] + roman
        elif arab[i] in substractValues:
            roman = substractValues[arab[i]][0] + roman
        elif int(arabInString[i][0]) in range(2,4):
            print('Numero en rango 2-3')
            roman = arabicsValues[10 ** i] * int(arabInString[i][0]) + roman
            print(roman)
        elif int(arabInString[i][0]) in range(5,9):
            print('Numero en rango 5-8')
            roman = arabicsValues[5 * (10 ** i)] + arabicsValues[10 ** i] * (int(arabInString[i][0]) - 5) + roman

    
    print(arab)
    print(roman)


arab_to_rom(1234)