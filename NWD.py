a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))

while b != 0:
    r = a % b
    a = b
    b = r

print(f'NWD wynosi: {a}')
